import cv2
import pytesseract

# Tesseract ocr Executable file location
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def img_load():
    img = cv2.imread('img/no029.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# Image to String
# print(pytesseract.image_to_string(img))

# Detecting Characters
def detect_chr():
    img = img_load()
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)


# Detecting Words

def detect_words():
    img = img_load()
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)
    for a, b in enumerate(boxes.splitlines()):
        if a != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)
                cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)


# Detecting ONLY Digits

def detect_digits():
    img = img_load()
    hImg, wImg, _ = img.shape
    conf = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_boxes(img, config=conf)
    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow("Result", img)
    cv2.waitKey(0)


# Webcam and Screen Capture
def detect_from_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        timer = cv2.getTickCount()
        _, img = cap.read()
        # DETECTING CHARACTERS
        hImg, wImg, _ = img.shape
        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            # print(b)
            b = b.split(' ')
            # print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
            cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 230, 20), 2)
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    choice = input("Enter your choice : \n 1.detect character \n 2.detect words \n 3.detect digits \n 4.detect "
                   "character using webcam\n")
    if choice == "1":
        detect_chr()
    elif choice == "2":
        detect_words()
    elif choice == "3":
        detect_digits()
    elif choice == "4":
        detect_from_webcam()
    else:
        print("Invalid Choice")
