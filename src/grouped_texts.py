import os
import random
import pathlib
import subprocess

training_text_file = 'words.txt'

lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/soi-test-data'


if not os.path.exists(output_directory):
    os.mkdir(output_directory)

count = 3
lines = lines[:count]
line_test = "\n".join(lines)

l_text_file = f'{output_directory}/sample.gt.txt'
with open(l_text_file, 'w') as output_file:
    output_file.writelines([line_test])


subprocess.run([
    'text2image',
    '--font=Monospac821 BT',
    '--fonts_dir=/Users/yogesh/Library/Fonts',
    f'--text={l_text_file}',
    f'--outputbase={output_directory}/testpage',
    '--max_pages=1',
    '--strip_unrenderable_words',
    '--leading=12',
    '--xsize=1000',
    '--ysize=400',
    '--char_spacing=0.0',
    '--exposure=0',
    '--unicharset_file=langdata/eng.unicharset'
])

# line_count = 0
# for line in lines:
#     if line_count % 4 == 0:
#         lines = lines[line_count:line_count + 4]
#         line_test = "\n".join(lines)
#         file_base_name = f'eng_{line_count}'
#         subprocess.run([
#             'text2image',
#             '--font=Monospac821 BT',
#             f'--text={line_test}',
#             f'--outputbase={output_directory}/{file_base_name}',
#             '--max_pages=1',
#             '--strip_unrenderable_words',
#             '--leading=12',
#             '--xsize=1000',
#             '--ysize=2000',
#             '--char_spacing=0.0',
#             '--exposure=0',
#             '--unicharset_file=langdata/eng.unicharset'
#         ])
#     line_count += 1
#

# TESSDATA_PREFIX=../tesseract/tessdata make training MODEL_NAME=soi START_MODEL=eng TESSDATA=../tesseract/tessdata MAX_ITERATIONS=1000
# TESSDATA_PREFIX=../tesseract/tessdata TESSDATA=../tesseract/tessdata make training MODEL_NAME=soi