def stream_cipher_encrypt(plaintext, streamkey):
    ciphertext=[]
    for i,char in enumerate(plaintext):
        ciphertext.append(chr(ord(char) ^ streamkey[i]))
    return ''.join(ciphertext)

def stream_cipher_decrypt(ciphertext, streamkey):
    plaintext=[]
    for i,char in enumerate(ciphertext):
        plaintext.append(chr(ord(char) ^ streamkey[i]))
    return ''.join(plaintext)


message = "HELLO"
key_stream = [7, 3, 5, 2, 6]
encrypted = stream_cipher_encrypt(message, key_stream)
decrypted = stream_cipher_decrypt(encrypted, key_stream)
print(f"Message : {message}")
print(f"Chiffré : {''.join([str(ord(c)) for c in encrypted])} (en bytes)")
print(f"Déchiffré: {decrypted}")
