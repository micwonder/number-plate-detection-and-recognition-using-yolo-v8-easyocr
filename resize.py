import os, cv2
from tqdm import tqdm


def run():
    original = "original"
    target = "output"
    img_paths = []
    img_names = os.listdir(original)
    # print(img_names)
    for img_name in img_names:
        img_path = os.path.join(original, img_name)

        if (
            ".png" in img_path.lower()
            or ".jpg" in img_path.lower()
            or ".jpeg" in img_path.lower()
        ):
            img_paths.append(img_path)

    
    
    for i, img_path in tqdm(enumerate(img_paths), total=len(img_paths), desc="Processing Images"):
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        resized_image = cv2.resize(img, (640, 640))

        target_path = os.path.join(
            target, os.path.join(os.path.splitext(img_names[i])[0], ".jpg")
        )

        cv2.imwrite(target_path, resized_image)


if __name__ == "__main__":
    run()
