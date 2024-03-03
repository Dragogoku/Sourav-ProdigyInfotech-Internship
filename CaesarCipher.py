def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            # Determine whether to shift forward or backward based on the direction
            if direction == "encode":
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
            elif direction == "decode":
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
            result += shifted_char

        else:
            result += char
    return result

def main():
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Enter your message:\n").lower()
        shift = int(input("Enter the shift number:\n"))

        shift %= 26  # Ensure the shift value is within the range of 0-25

        encrypted_text = caesar_cipher(text, shift, direction)
        print(f"Here's the {direction}d result: {encrypted_text}")

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart != "yes":
            should_continue = False
            print("Goodbye!")

if __name__ == "__main__":
    main()