from PIL import Image
import numpy as np

# ------------------------------
# Load image
# ------------------------------
def load_image(path):
    img = Image.open(path)
    img_array = np.array(img)
    return img, img_array

# ------------------------------
# Encryption / Decryption (Math Operation)
# ------------------------------
def encrypt_image_math(img_array, key=50):
    encrypted = (img_array.astype(np.int16) + key) % 256
    return encrypted.astype(np.uint8)

def decrypt_image_math(img_array, key=50):
    decrypted = (img_array.astype(np.int16) - key) % 256
    return decrypted.astype(np.uint8)

# ------------------------------
# Encryption / Decryption (Pixel Swap)
# ------------------------------
def encrypt_image_swap(img_array):
    encrypted = np.flipud(np.fliplr(img_array))  # flip both vertically & horizontally
    return encrypted

def decrypt_image_swap(img_array):
    decrypted = np.fliplr(np.flipud(img_array))  # reverse the flips
    return decrypted

# ------------------------------
# Save image
# ------------------------------
def save_image(img_array, output_path):
    encrypted_img = Image.fromarray(img_array.astype(np.uint8))
    encrypted_img.save(output_path)

# ------------------------------
# Main function
# ------------------------------
if __name__ == "__main__":
    # Load the original image
    img, img_array = load_image("input.png")

    # --- Method 1: Math Encryption ---
    encrypted_math = encrypt_image_math(img_array, key=50)
    save_image(encrypted_math, "encrypted_math.png")
    print("✅ Encrypted (Math) saved as encrypted_math.png")

    decrypted_math = decrypt_image_math(encrypted_math, key=50)
    save_image(decrypted_math, "decrypted_math.png")
    print("✅ Decrypted (Math) saved as decrypted_math.png")

    # --- Method 2: Pixel Swap Encryption ---
    encrypted_swap = encrypt_image_swap(img_array)
    save_image(encrypted_swap, "encrypted_swap.png")
    print("✅ Encrypted (Swap) saved as encrypted_swap.png")

    decrypted_swap = decrypt_image_swap(encrypted_swap)
    save_image(decrypted_swap, "decrypted_swap.png")
    print("✅ Decrypted (Swap) saved as decrypted_swap.png")
