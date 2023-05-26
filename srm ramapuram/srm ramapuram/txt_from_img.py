from PIL import Image
from pytesseract import pytesseract
path_to_tesseract = r'C:\Users\raman\AppData\Local\Tesseract-OCR\tesseract.exe'


def txt(path):
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(path)

    text = pytesseract.image_to_string(img)
    if text:
        return(text)
    else:
        return("No text found")