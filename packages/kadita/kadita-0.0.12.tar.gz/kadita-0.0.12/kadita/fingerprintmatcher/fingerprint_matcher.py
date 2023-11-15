import os
import cv2
import time

class FingerprintMatcher:
    def __init__(self, sample_image_path):
        self.sample = cv2.imread(sample_image_path)
        if self.sample is None:
            raise ValueError("Gambar sample tidak valid.")

    def match(self, dataset_folder):
        start_time = time.time()
        best_score = 0
        filename = None
        image = None
        kp1, kp2, mp = None, None, None

        for file in [file for file in os.listdir(dataset_folder)][:1000]:
            fingerprint_image = cv2.imread(os.path.join(dataset_folder, file))
            sift = cv2.SIFT_create()

            keypoints_1, descriptor_1 = sift.detectAndCompute(self.sample, None)
            keypoints_2, descriptor_2 = sift.detectAndCompute(fingerprint_image, None)

            bf = cv2.BFMatcher(cv2.NORM_L2)
            matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)
            match_points = []

            for p, q in matches:
                if p.distance < 0.3 * q.distance:  # maks 0.3
                    match_points.append(p)

            keypoints = min(len(keypoints_1), len(keypoints_2))
            print(keypoints)
            if keypoints > 0 and len(match_points) / keypoints * 100 > best_score:
                best_score = len(match_points) / keypoints * 100
                filename = file
                image = fingerprint_image
                kp1, kp2, mp = keypoints_1, keypoints_2, match_points

        if filename is not None:
            print("BEST MATCH: " + filename)
        else:
            print("Tidak Ditemukan")

        print("HASIL DETEKSI: " + str(best_score))
        print("TIME DELAY: ", time.time() - start_time)

        if self.sample is not None and image is not None:
            result = cv2.drawMatches(self.sample, kp1, image, kp2, mp, None)
            result = cv2.resize(result, (result.shape[1] * 2, result.shape[0] * 2))
            cv2.imshow("Hasil", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Gambar sample atau image tidak valid.")
