def encrypt_block(raw_text, shift_key):
    encrypted = ""
    for char in raw_text:
        if char.isalpha():
            encrypted += chr(ord(char) + shift_key)
        else:
            encrypted += char
    return encrypted

if __name__ == "__main__":
    print(encrypt_block("EECS_2026", 4))

