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