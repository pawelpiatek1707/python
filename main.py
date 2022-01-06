import argparse
import os.path
from helpers.detectPeople import detect_people

parser = argparse.ArgumentParser(description='File name')

parser.add_argument('File', metavar='file', type=str)

args = parser.parse_args()

file_name = args.File

img_path = f'img/{file_name}.jpg'

if os.path.exists(img_path):
    print(img_path)

    detect_people(f'img/{file_name}.jpg', (4, 4), (4, 4), 1.05, 1)
else:
    print('Wrong file name')
