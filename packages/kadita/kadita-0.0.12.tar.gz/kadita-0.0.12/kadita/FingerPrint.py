from kadita.fingerprintmatcher.fingerprint_matcher import FingerprintMatcher
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fingerprint Matching")
    parser.add_argument("sample_image_path", help="Path ke gambar sampel sift.")
    parser.add_argument("dataset_folder", help="Folder tempat gambar dataset sift berada.")
    args = parser.parse_args()

    matcher = FingerprintMatcher(args.sample_image_path)
    matcher.match(args.dataset_folder)
