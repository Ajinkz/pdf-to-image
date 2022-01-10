# pdf-to-image


from pdf2image import convert_from_path
from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

poppler_path = r"C:\Program Files\poppler-0.68.0\bin"
filename = "2020_Delta_ESG_Report_EN.pdf"
pg_num = 196

pages = convert_from_path(filename, pg_num, poppler_path = poppler_path)

data_dct = {}

for i in range(len(pages)):
    #page.save('imgs/out.jpg', 'JPEG')
    #pages[i].save('imgs/'+ str(i) +'.jpg', 'JPEG')
    # This function will extract the text from the image
    
    text = pytesseract.image_to_string(pages[i])
    data_dct[i] = text
