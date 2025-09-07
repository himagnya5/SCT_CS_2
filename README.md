# 🖼️ Image Encryption Tool

A Python project to **encrypt and decrypt images** using two methods:  
1. **Mathematical key-based encryption** (pixel value shifts)  
2. **Pixel swapping** (flip transformations)  

This tool demonstrates how images can be securely encrypted and then decrypted back to the original.

---

## 🚀 Features

- Encrypt an image using a **numerical key**  
- Decrypt the image back to original  
- Supports multiple methods of encryption  
- Outputs separate files for each encryption/decryption method

---

## 🛠️ Technologies Used

- Python 3.x  
- [Pillow](https://pypi.org/project/Pillow/) – for image processing  
- [NumPy](https://numpy.org/) – for array manipulation  

---

💻 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ImageEncryptionTool.git
cd ImageEncryptionTool

2️⃣ Install Dependencies
pip install pillow numpy

3️⃣ Usage

Place the image you want to encrypt in the project folder (e.g., input.png).

Run the script:

python main.py

4️⃣ Outputs

After running, you’ll get the following files in your project folder:

🧮 encrypted_math.png → Image encrypted using mathematical method

🔓 decrypted_math.png → Image decrypted back

🔀 encrypted_swap.png → Image encrypted using pixel swap

🔓 decrypted_swap.png → Image decrypted back

