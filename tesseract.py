import pytesseract
from PIL import Image




img = Image.open('book.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r"--oem 2 --psm 36"

text = pytesseract.image_to_string(img, lang='rus')
print(text)
