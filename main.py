
def caesar_cipher(text, shift, mode):
    result = ""
    
    # If mode is decrypt, reverse the shift
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine starting ASCII value (65 for uppercase, 97 for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # The Formula: (Position + Shift) % 26
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # If it's a space or symbol, keep it unchanged
            result += char
            
    return result

# --- User Input Section ---
print("--- Caesar Cipher Tool ---")
user_message = input("Enter your message: ")
user_shift = int(input("Enter shift value (e.g., 3): "))
user_mode = input("Action (encrypt/decrypt): ").lower()

# Generate and display result
output = caesar_cipher(user_message, user_shift, user_mode)
print(f"\nFinal Result: {output}")