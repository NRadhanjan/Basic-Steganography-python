# Basic-Steganography-python
A simple image steganography tool using Python


# 🕵️‍♂️ Basic Steganography Tool in Python

This is a simple image steganography tool built with Python. It allows you to **hide** and **extract** secret messages inside images using the **Least Significant Bit (LSB)** technique.

---

## 📁 Files

- `encode.py` – Hides a secret message inside an image.
- `decode.py` – Extracts a hidden message from a stego image.
- `input.png` – Input image file (must be placed in the same folder as the scripts).

---

## 🚀 Getting Started

### 🔐 To Hide a Message:

1. Place your cover image in the same directory and rename it to `input.png`.
2. Run the encoding script:

    ```bash
    python encode.py
    ```

3. Enter your message when prompted.
4. The stego image will be saved as `output.png`.

---

### 🔓 To Reveal a Message:

1. Make sure the stego image (`output.png` or any `.png` file with hidden data) is in the same folder.
2. Run the decoding script:

    ```bash
    python decode.py
    ```

3. The script will extract and print the hidden message.

---

## 💡 How It Works

- Each character of your secret message is converted into **8-bit binary**.
- A **16-bit delimiter** `1111111111111110` is added to mark the end of the message.
- The binary data is hidden inside the **Least Significant Bits (LSB)** of the RGB pixels in the input image.
- This slightly changes the pixel values, but the human eye can’t detect it.
- The decoding script reverses the process by reading those LSBs and extracting the hidden binary string.

---

## 📌 Notes

- This tool is for educational use and basic steganography demonstration.
- Works best with `.png` images (avoid `.jpg` as it introduces compression artifacts).
- No encryption is used — the message is only hidden, not protected.
- Make sure your input image is large enough to hold the message.

---

## 🧪 Example

```bash
Enter the message to hide: The password is 1234
Message hidden! Saved as: output.png
