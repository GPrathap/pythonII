#!/usr/bin/env python3

# lists all jpg files in pics/ and resize them to 500x500 and write to resized/

from PIL import Image
import os

def resize_image(input_filename, output_filename):
    img = Image.open(input_filename)
    new_img = img.resize((500,500))
    new_img.save(output_filename)

file_list = os.listdir('pics/')
file_list_n = len(file_list)
for i in range(0,file_list_n,1):
    file_name = file_list[i]
    input_file_path = os.path.join('pics', file_name)
    output_file_path = os.path.join('resized', file_name)
    if file_name.endswith(".jpg"):
        print(input_file_path)
        resize_image(input_file_path, output_file_path)
