import cv2 as cv


def main():
    img = cv.imread("data/hedgehog.jpeg")

    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    print(k)


def is_testable(s: str) -> str:
    return f"{s}_was_the_string"


if __name__ == "__main__":
    main()
