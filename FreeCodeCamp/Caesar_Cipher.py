def caesar(text, shift, encrypt=True):
    """
    Perform Caesar cipher encryption or decryption on a given text.

    Args:
        text (str): The input text to encrypt or decrypt.
        shift (int): Number of positions to shift (1–25).
        encrypt (bool): True for encryption, False for decryption.

    Returns:
        str: The transformed text or an error message if input is invalid.
    """
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


def encrypt(text, shift):
    """
    Encrypt text using the Caesar cipher.

    Args:
        text (str): Plain text to encrypt.
        shift (int): Shift value (1–25).

    Returns:
        str: Encrypted text.
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypt text using the Caesar cipher.

    Args:
        text (str): Encrypted text to decrypt.
        shift (int): Shift value (1–25).

    Returns:
        str: Decrypted text.
    """
    return caesar(text, shift, encrypt=False)


encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)

decrypted_text = decrypt(encrypted_text, 3)
print(decrypted_text)
