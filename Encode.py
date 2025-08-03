from PIL import Image
import numpy as np

def text_to_bin(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_data(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    binary_message = text_to_bin(message) + '1111111111111110'  
    msg_index = 0

    for row in data:
        for pixel in row:
            for n in range(3): 
                if msg_index < len(binary_message):
                    pixel[n] = (pixel[n] & 254) | int(binary_message[msg_index])
                    msg_index += 1

    encoded_img = Image.fromarray(data)
    encoded_img.save(output_path)
    print("Message hidden! Saved as:", output_path)

if __name__ == "__main__":
    message = input("Enter the message to hide: ")
    hide_data('input.png', message, 'output.png')
