# Swap-and-Step-Cipher
Encryption algorithm designed to securely encrypt text by performing character swaps and position-based shifts.

Similar to how Ramanujan's mathematical theorems were revealed to him in a dream, the idea for this cipher popped into my head during the dreary heat of a cryptography class. I have attempted to explain it as simply as possible:-

The encryption algorithm involves two main steps:
Character Swapping: The input text is divided into pairs of characters. Each pair is swapped, meaning the second character takes the first position and vice versa.
Position-Based Shifting: After swapping, each character is shifted based on its position:
Even positions are incremented by one letter.
Odd positions are decremented by one letter.
This encryption is reversible, allowing the encrypted message to be decrypted back to the original text using the same logic in reverse.

Consider the text "abcd":
Forming Pairs and Swapping: The pairs are ("ab", "cd"), which swap to become ("ba", "dc").
Position-Based Shifting:
For 'b' (position 0, even): Incremented to 'c'.
For 'a' (position 1, odd): Decremented to 'z'.
For 'd' (position 2, even): Incremented to 'e'.
For 'c' (position 3, odd): Decremented to 'b'.
The resulting encrypted text would be "czeb"

When the plaintext has an odd number of letters:
The algorithm processes all characters in pairs except for the last single character (since it has no pair).
For this last character:
It is shifted according to its position (even, so increment).

Spaces b/w words are managed by:
Recording the positions of spaces in the original text before encryption.
Removing all spaces from the text during the encryption process to only encrypt letters.
Restoring spaces to their original positions in the decrypted text after decryption.

GUI Features
The GUI, built with tkinter, provides an intuitive, three-page flow:
Welcome Page: A start page with a button to initiate the encryption process.
Encryption Page: Users input plaintext, which is encrypted upon pressing "Tap to Encrypt." The encrypted text is then displayed.
Decryption Page: Shows the encrypted text with a button to decrypt it back to the original message.

This project is still a WIP. Feel free to modify and do get back with your changes.
