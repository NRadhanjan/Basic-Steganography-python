from PIL import Image
import numpy as np
def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])


def extract_data(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    binary_data = ''
    for row in data:
        for pixel in row:
            for n in range(3):
                binary_data += str(pixel[n] & 1)
                if binary_data.endswith('1111111111111110'):
                    return bin_to_text(binary_data[:-16])
    return "No message found."


if __name__ == "__main__":
    message = extract_data('output.png')
    print("🔍 Extracted message:", message)
