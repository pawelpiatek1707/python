import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Paweł\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def read_text_from_img(img_path: str) -> str:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    converted_img = cv2.threshold(cv2.GaussianBlur(gray, (5, 5), 0), 0, 255, cv2.THRESH_BINARY
                                  + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(converted_img)
    return text


print(read_text_from_img('img/img1.png'))
# print(read_text_from_img('img/img2.png'))
# print(read_text_from_img('img/img3.png'))
# print(read_text_from_img('img/img4.png'))
# print(read_text_from_img('img/img5.png'))
