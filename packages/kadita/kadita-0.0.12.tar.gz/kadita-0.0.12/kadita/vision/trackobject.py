import math
import cvzone
import numpy as np
import cv2


class Tracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0

    def update(self, objects_rect):
        # Objects and ids
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 35:
                    self.center_points[id] = (cx, cy)
                    #                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        return objects_bbs_ids


class Count:

    def __init__(self, video_path, lower_range, upper_range):
        self.cap = cv2.VideoCapture(video_path)
        self.lower_range = lower_range
        self.upper_range = upper_range
        self.tracker = Tracker()
        self.area = [(391, 244), (370, 443), (391, 438), (410, 237)]
        self.counter = []
        self.manual_poly_points = []
        cv2.namedWindow('RGB')
        cv2.setMouseCallback('RGB', self.draw_manual_poly)

    def RGB(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            point = [x, y]
            print(point)

    def draw_manual_poly(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.manual_poly_points.append((x, y))
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.manual_poly_points = []

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (640, 480))
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower_range, self.upper_range)
            _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
            cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            bbox_list = []
            for c in cnts:
                x = 500
                if cv2.contourArea(c) > x:
                    x, y, w, h = cv2.boundingRect(c)
                    bbox_list.append([x, y, w, h])
            bbox_idx = self.tracker.update(bbox_list)
            for bbox in bbox_idx:
                x1, y1, w1, h1, _id = bbox
                cx = int(x1 + x1 + w1) // 2
                cy = int(y1 + y1 + h1) // 2

                results = cv2.pointPolygonTest(np.array(self.area, np.int32), (cx, cy), False)
                if results >= 0:
                    cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                    cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
                    cvzone.putTextRect(frame, f"{_id}", (x1, y1), 2, 2)
                    if self.counter.count(_id) == 0:
                        self.counter.append(_id)
            # cv2.polylines(frame, [np.array(self.area, np.int32)], True, (255, 255, 255), 2)
            c1 = len(self.counter)
            cvzone.putTextRect(frame, f"{c1}", (50, 60), 2, 2)

            # Draw manually created polylines
            if len(self.manual_poly_points) > 1:
                cv2.polylines(frame, [np.array(self.manual_poly_points, np.int32)], True, (0, 255, 255), 2)

            cv2.imshow("RGB", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

