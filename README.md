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

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ImageEncryptionTool.git
cd ImageEncryptionTool
2.Install dependencies:
pip install pillow numpy
⚡ Usage

Place the image you want to encrypt in the project folder (e.g., input.png).

Run the main script:
python main.py
Outputs:

encrypted_math.png → Image encrypted using mathematical method

decrypted_math.png → Decrypted back

encrypted_swap.png → Image encrypted using pixel swap

decrypted_swap.png → Decrypted back
📌 Author

Himagnya (GitHub: himagnya5)

Email: sshimagnya@gmail.com
🎯 Notes

Make sure your Python environment has all dependencies installed.

Avoid committing large images or unnecessary files; use .gitignore for venv/ and *.pyc.

---

### 🔹 Next Steps

1. Save this as **`README.md`** in your project root (`ImageEncryptionTool/`).  
2. Add it to Git:

```bash
git add README.md
git commit -m "Add README.md"
git push
