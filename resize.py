import os, cv2


def run():
    original = "original"
    target = "output"
    img_pathes = []
    img_names = os.listdir(original)
    print(img_names)
    for img_name in img_names:
        print(1)
        img_path = os.path.join(original, img_name)

        if (
            ".png" in img_path.lower()
            or ".jpg" in img_path.lower()
            or ".jpeg" in img_path.lower()
        ):
            img_pathes.append(img_path)

    for i, img_path in enumerate(img_pathes):
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        resized_image = cv2.resize(img, (640, 640))

        target_path = os.path.join(target, img_names[i])

        cv2.imwrite(target_path, resized_image)


if __name__ == "__main__":
    run()
