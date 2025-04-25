def block_cipher_encrypt(plaintext, shift=3, block_size=4):
    while len(plaintext) % block_size != 0:
        plaintext += ' '

    ciphertext = ''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        encrypted_block = ''.join(chr((ord(char) + shift) % 256) for char in block)
        ciphertext += encrypted_block

    return ciphertext

def block_cipher_decrypt(ciphertext, shift=3, block_size=4):
    plaintext = ''
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted_block = ''.join(chr((ord(char) - shift) % 256) for char in block)
        plaintext += decrypted_block

    return plaintext

message = "HELLO"
encrypted = block_cipher_encrypt(message)
decrypted = block_cipher_decrypt(encrypted)
print(f"Message : {message}")
print(f"Chiffré : {encrypted}")
print(f"Déchiffré: {decrypted}")