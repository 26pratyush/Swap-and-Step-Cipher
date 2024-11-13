import tkinter as tk
from tkinter import messagebox

# Encryption and Decryption fns
def shift_char(c, shift):
    if 'a' <= c <= 'z':  # Handle lowercase letters
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':  # Handle uppercase letters
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c  

def custom_encrypt(text):
    space_positions = [i for i, char in enumerate(text) if char == ' ']
    text = text.replace(" ", "")
    result = []
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    
    for i, pair in enumerate(pairs):
        if len(pair) == 2:
            swapped = pair[1] + pair[0]
            for j, char in enumerate(swapped):
                new_position = 2 * i + j
                if new_position % 2 == 0:
                    result.append(shift_char(char, 1))
                else:
                    result.append(shift_char(char, -1))
        else:
            last_char = pair[0]
            new_position = 2 * i
            if new_position % 2 == 0:
                result.append(shift_char(last_char, 1))
            else:
                result.append(shift_char(last_char, -1))

    encrypted_text = ''.join(result)
    return encrypted_text, space_positions

def custom_decrypt(encrypted_text, space_positions):
    result = []
    pairs = [encrypted_text[i:i+2] for i in range(0, len(encrypted_text), 2)]
    
    for i, pair in enumerate(pairs):
        if len(pair) == 2:
            adjusted_pair = ""
            for j, char in enumerate(pair):
                new_position = 2 * i + j
                if new_position % 2 == 0:
                    adjusted_pair += shift_char(char, -1)
                else:
                    adjusted_pair += shift_char(char, 1)
            result.append(adjusted_pair[1] + adjusted_pair[0])
        else:
            last_char = pair[0]
            new_position = 2 * i
            if new_position % 2 == 0:
                result.append(shift_char(last_char, -1))
            else:
                result.append(shift_char(last_char, 1))

    decrypted_text = ''.join(result)
    for pos in space_positions:
        decrypted_text = decrypted_text[:pos] + ' ' + decrypted_text[pos:]

    return decrypted_text

# GUI 
class EncryptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Swap & Step Encryption")
        self.geometry("400x300")
        self.current_frame = None
        self.encrypted_text = ""
        self.space_positions = []
        
        self.show_welcome_page()

    def show_welcome_page(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True)
        
        tk.Label(self.current_frame, text="Welcome to Swap & Step Encryption", font=("Arial", 16)).pack(pady=30)
        enter_button = tk.Button(self.current_frame, text="Enter", command=self.show_encryption_page)
        enter_button.pack(pady=10)

    def show_encryption_page(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True)
        
        tk.Label(self.current_frame, text="Enter Plaintext:", font=("Arial", 14)).pack(pady=10)
        self.plaintext_entry = tk.Entry(self.current_frame, font=("Arial", 12), width=30)
        self.plaintext_entry.pack(pady=5)
        
        encrypt_button = tk.Button(self.current_frame, text="Tap to Encrypt", command=self.encrypt_text)
        encrypt_button.pack(pady=5)
        
        self.encrypted_label = tk.Label(self.current_frame, text="", font=("Arial", 12))
        self.encrypted_label.pack(pady=10)
        
        send_button = tk.Button(self.current_frame, text="Tap to Send Message", command=self.show_decryption_page)
        send_button.pack(pady=10)

    def show_decryption_page(self):
        if not self.encrypted_text:
            messagebox.showwarning("Warning", "No encrypted text to send.")
            return

        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self)
        self.current_frame.pack(expand=True)
        
        tk.Label(self.current_frame, text="Encrypted Text:", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.current_frame, text=self.encrypted_text, font=("Arial", 12), wraplength=350).pack(pady=5)
        
        decrypt_button = tk.Button(self.current_frame, text="Tap to Decrypt", command=self.decrypt_text)
        decrypt_button.pack(pady=10)
        
        self.decrypted_label = tk.Label(self.current_frame, text="", font=("Arial", 12))
        self.decrypted_label.pack(pady=10)

    def encrypt_text(self):
        plaintext = self.plaintext_entry.get()
        if not plaintext:
            messagebox.showwarning("Warning", "Please enter some text to encrypt.")
            return
        
        self.encrypted_text, self.space_positions = custom_encrypt(plaintext)
        self.encrypted_label.config(text=f"Encrypted Text: {self.encrypted_text}")

    def decrypt_text(self):
        decrypted_text = custom_decrypt(self.encrypted_text, self.space_positions)
        self.decrypted_label.config(text=f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    app = EncryptionApp()
    app.mainloop()
