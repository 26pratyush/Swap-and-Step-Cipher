# Swap-and-Step-Cipher
Encryption algorithm designed to securely encrypt text by performing character swaps and position-based shifts.

Similar to how Ramanujan's mathematical theorems were revealed to him in a dream, the idea for this cipher popped into my head during the dreary heat of a cryptography class. I have attempted to explain it as simply as possible:-

The encryption algorithm involves two main steps:<br>
Character Swapping: The input text is divided into pairs of characters. Each pair is swapped, meaning the second character takes the first position and vice versa.<br>
Position-Based Shifting: After swapping, each character is shifted based on its position:<br>
Even positions are incremented by one letter.<br>
Odd positions are decremented by one letter.<br>
This encryption is reversible, allowing the encrypted message to be decrypted back to the original text using the same logic in reverse.<br>

Consider the text "abcd":<br>
Forming Pairs and Swapping: The pairs are ("ab", "cd"), which swap to become ("ba", "dc").<br>
Position-Based Shifting:<br>
For 'b' (position 0, even): Incremented to 'c'.<br>
For 'a' (position 1, odd): Decremented to 'z'.<br>
For 'd' (position 2, even): Incremented to 'e'.<br>
For 'c' (position 3, odd): Decremented to 'b'.<br>
The resulting encrypted text would be "czeb"<br>

When the plaintext has an odd number of letters:<br>
The algorithm processes all characters in pairs except for the last single character (since it has no pair).<br>
For this last character:<br>
It is shifted according to its position (even, so increment).<br>

Spaces b/w words are managed by:<br>
Recording the positions of spaces in the original text before encryption.<br>
Removing all spaces from the text during the encryption process to only encrypt letters.<br>
Restoring spaces to their original positions in the decrypted text after decryption.<br>

GUI Features<br>
The GUI, built with tkinter, provides an intuitive, three-page flow:<br>
Welcome Page: A start page with a button to initiate the encryption process.<br>
Encryption Page: Users input plaintext, which is encrypted upon pressing "Tap to Encrypt." The encrypted text is then displayed.<br>
Decryption Page: Shows the encrypted text with a button to decrypt it back to the original message.<br>

This project is still a WIP. Feel free to modify and do get back with your changes.

![Screenshot (136)](https://github.com/user-attachments/assets/67c2916a-175c-4d97-b184-af712379b29b)
![Screenshot (135)](https://github.com/user-attachments/assets/3a51ea62-712d-4c4f-825a-1e1f743d6d0c)
![Screenshot (134)](https://github.com/user-attachments/assets/b29cdee7-3d60-4b84-9dd1-4ec65761eb3e)

