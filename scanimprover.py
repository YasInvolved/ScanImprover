"""
Copyright 2025 Jakub Bączyk

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject 
to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from PIL import Image
import sys
import os

TOLLERANCE_MIN = int(2.5 * 255)
TOLLERANCE_MAX = 3*255

path = os.path

def make_out_path(input_path: str) -> str:
    split = path.splitext(input_path)
    return f"{split[0]}_improved{split[1]}"

def main():
    file_path = sys.argv[1]
    output_path = make_out_path(file_path)

    input_scan_data = Image.open(file_path, "r").convert("RGB")

    for y in range(input_scan_data.height):
        for x in range(input_scan_data.width):
            r, g, b = input_scan_data.getpixel([x, y])
            
            if r + g + b in range(TOLLERANCE_MIN, TOLLERANCE_MAX):
                input_scan_data.putpixel([x, y], 0xffffff)

    input_scan_data.save(output_path)

if __name__ == "__main__":
    main()