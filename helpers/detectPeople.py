from typing import Tuple
import cv2
import imutils


def detect_people(img: str, winStride: Tuple[int, int], padding: Tuple[int, int], scale: float, useMeanshiftGrouping: int) -> None:
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = cv2.imread(img)
    t1 = cv2.getTickCount()
    image = imutils.resize(image,
                           width=min(400, image.shape[1]))

    (regions, _) = hog.detectMultiScale(image,
                                        winStride=winStride,
                                        padding=padding,
                                        scale=scale,
                                        useMeanshiftGrouping=useMeanshiftGrouping)

    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)

    t2 = cv2.getTickCount()

    print(f"number of people detected on image {img}: {len(regions)}")
    print(f"detection time: {(t2 - t1)/cv2.getTickFrequency()}[s]")

    cv2.imshow("Image", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
