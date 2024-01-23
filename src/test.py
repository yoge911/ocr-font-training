import subprocess
import os

import pytesseract

#testimage_dir = 'tesstrain/data/soi-test-data'
#imagename = f'{testimage_dir}/testpage.tif'
#outputfile = f'{testimage_dir}/ocr.txt'
#trained_model = 'tesstrain/data/soi'

# Set the path to the tessdata directory
# tessdata_directory = '/opt/homebrew/Cellar/tesseract/5.3.3/share/tessdata'

# Set the TESSDATA_PREFIX environment variable
# os.environ['TESSDATA_PREFIX'] = tessdata_directory

# subprocess.run([
#     'tesseract',
#     imagename,
#     outputfile,
#     '--tessdata-dir', trained_model,
#     '-l', "soi",
#     '--oem', '0'
# ])

#trained_data = "/opt/homebrew/Cellar/tesseract/5.3.3/share/tessdata/soi.traineddata"
# Set the path to the Tesseract executable (change this to your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.3/bin/'

# Specify the OCR Engine Mode (OEM) and Language
custom_config = r'--oem 1 --psm 6 -l soi'

imagename = "testdata/SOI_test1.png"

text = pytesseract.image_to_string(imagename, config=custom_config)

print(text)
