import os
import random
import pathlib
import subprocess

training_text_file = 'words.txt'

lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/soi-ground-truth'
fonts_directory = 'C:\\Windows\\Fonts'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 100

lines = lines[:count]

line_count = 0
for line in lines:
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'eng_{line_count}.gt.txt')
    with open(line_training_text, 'w') as output_file:
        output_file.writelines([line])

    file_base_name = f'eng_{line_count}'

    subprocess.run([
        'text2image',
        f'--fonts_dir={fonts_directory}',
        '--font=Monospac821 BT',
        f'--text={line_training_text}',
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=12',
        '--xsize=1000',
        '--ysize=250',
        '--char_spacing=0.0',
        '--exposure=0',
        '--unicharset_file=langdata/eng.unicharset'
    ])

    line_count += 1