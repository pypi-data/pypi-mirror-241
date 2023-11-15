import cv2
import dlib
import time
import os
import pygame
from scipy.spatial import distance
from kadita.vision.MouthAR import MouthDetector


class DrowsinessDetector:
    def __init__(self, dat_file_path_):
        self.cap = cv2.VideoCapture(0)
        self.face_detector = dlib.get_frontal_face_detector()
        self.dlib_facelandmark = dlib.shape_predictor(dat_file_path_)
        self.start_time = time.time()
        self.frame_count = 0
        self.current_second = 0
        self.mouth_detector = MouthDetector()
        self.left_eye_blink_count = 0
        self.right_eye_blink_count = 0
        self.last_left_eye_state = False
        self.last_right_eye_state = False
        self.last_drowsiness_detected_time = None
        self.sound_detected = False
        pygame.mixer.init()

    @staticmethod
    def calculate_eye_aspect_ratio(eye):
        poi_A = distance.euclidean(eye[1], eye[5])
        poi_B = distance.euclidean(eye[2], eye[4])
        poi_C = distance.euclidean(eye[0], eye[3])
        aspect_ratio_Eye = (poi_A + poi_B) / (2 * poi_C)
        return aspect_ratio_Eye

    def play_drowsiness_sound(self):
        if not self.sound_detected:
            pygame.mixer.music.load('dataset/sound.wav')  # Load the audio file
            pygame.mixer.music.play(-1)  # Play the audio
            self.sound_detected = True

    def stop_drowsiness_sound(self):
        if self.sound_detected:
            pygame.mixer.music.stop()
            self.sound_detected = False

    def writeImg(self, frame, filename):
        path = os.path.join("out", filename)
        cv2.imwrite(path, frame)
        with open(filename, 'ab') as f:
            f.flush()
            os.fsync(f.fileno())

    def detect_drowsiness(self):
        while True:
            ret, frame = self.cap.read()
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector(gray_scale)
            self.frame_count += 1
            elapsed_time = time.time() - self.start_time
            self.current_second = int(elapsed_time % 60)

            # Jumlah FPS
            fps = self.frame_count / elapsed_time
            cv2.putText(frame, f"FPS: {round(fps, 2)}", (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 1)

            # Time 1 Minute dan Reset
            blink_reset_time = time.time() + 60
            self.current_second = int(elapsed_time % 60)
            cv2.putText(frame, f"Waktu: {self.current_second}", (480, 70), cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 2)

            for face in faces:
                face_landmarks = self.dlib_facelandmark(gray_scale, face)
                leftEye = []
                rightEye = []
                mouth = []

                # LEFT EYES IN .DAT FILE THAT ARE FROM 42 TO 47
                for n in range(42, 48):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    rightEye.append((x, y))
                    next_point = n + 1
                    if n == 47:
                        next_point = 42
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

                # RIGHT EYES IN .DAT FILE THAT ARE FROM 36 TO 41
                for n in range(36, 42):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    leftEye.append((x, y))
                    next_point = n + 1
                    if n == 41:
                        next_point = 36
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

                # Kalo ini untuk ini perhitungan file .DAT Mouth
                for n in range(48, 68):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    mouth.append((x, y))
                    next_point = n + 1
                    if n == 67:
                        next_point = 48
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

                    # Hitung Mata Kiri EAR(Eye Aspect Ratio)
                    left_eye_aspect_ratio = self.calculate_eye_aspect_ratio(leftEye)
                    if left_eye_aspect_ratio < 0.22:
                        if not self.last_left_eye_state:
                            self.left_eye_blink_count += 1
                            self.last_left_eye_state = True
                    else:
                        self.last_left_eye_state = False

                    # Hitung Mata Kanan(Eye Aspect Ratio)
                    right_eye_aspect_ratio = self.calculate_eye_aspect_ratio(rightEye)
                    if right_eye_aspect_ratio < 0.22:
                        if not self.last_right_eye_state:
                            self.right_eye_blink_count += 1
                            self.last_right_eye_state = True
                    else:
                        self.last_right_eye_state = False

                # Hitungan Kedipan Mata Dari 0 Mata Kanan Kiri
                blink_text = f"Berkedip: Kiri {self.left_eye_blink_count} | Kanan {self.right_eye_blink_count}"
                cv2.putText(frame, blink_text, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (21, 56, 210), 2)

                # Hitung Mata Kiri, Kanan, dan Mulut EAR
                right_Eye = self.calculate_eye_aspect_ratio(rightEye)
                left_Eye = self.calculate_eye_aspect_ratio(leftEye)
                Eye_Rat = (left_Eye + right_Eye) / 2
                mar = self.mouth_detector.calculate_mouth_aspect_ratio(mouth)

                # Nilai Rata Rata kedua Mata
                Eye_Rat = round(Eye_Rat, 2)
                eye_rat_text = f"EAR: {Eye_Rat:.2f}"
                cv2.putText(frame, eye_rat_text, (480, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (21, 56, 210), 2)

                # Reset blink counts after one minute
                if time.time() >= blink_reset_time:
                    blink_reset_time = time.time() + 60
                    self.left_eye_blink_count = 0
                    self.right_eye_blink_count = 0
                if elapsed_time >= 60:
                    self.start_time = time.time()
                    self.frame_count = 0
                    self.left_eye_blink_count = 0
                    self.right_eye_blink_count = 0

                # Nilainya Bisa Dirubah(Menyesuaikan) Logikanya
                if self.left_eye_blink_count + self.right_eye_blink_count <= 10 or self.left_eye_blink_count + self.right_eye_blink_count >= 50:
                    # Drowsiness detected
                    cv2.putText(frame, "KANTUK TERDETEKSI", (10, 30),
                                cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
                    self.play_drowsiness_sound()
                    if self.last_drowsiness_detected_time is None:
                        self.last_drowsiness_detected_time = time.time()
                else:
                    cv2.putText(frame, "TIDAK KANTUK", (10, 30),
                                cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
                    self.stop_drowsiness_sound()
                    if self.last_drowsiness_detected_time is not None:
                        elapsed_since_detection = time.time() - self.last_drowsiness_detected_time
                        if elapsed_since_detection >= 60:
                            self.last_drowsiness_detected_time = None
                if mar > 0.3:
                    cv2.putText(frame, "MENGANTUK BERAT!", (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (21, 56, 210), 2)
                self.writeImg(frame, f"HOG-0-output.png")

            cv2.imshow("HOG Detection", frame)
            if cv2.waitKey(1) == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
