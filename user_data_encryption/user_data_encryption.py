import os
from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from locker import Locker


KEY_SIZE = 16
BLOCK_SIZE = 16

client = Locker(
    access_key_id=os.getenv("YOUR_ACCESS_KEY_ID"),
    secret_access_key=os.getenv("YOUR_SECRET_ACCESS_KEY")
)

def generate_encryption_key() -> str:
    key = os.urandom(KEY_SIZE)
    return b64encode(key).decode('utf-8')


def generate_iv() -> str:
    iv = os.urandom(BLOCK_SIZE)
    return iv


def save_encryption_key(user_id, encryption_key):
    client.create(key=user_id, value=encryption_key)


def get_encryption_key(user_id):
    return client.get(key=user_id)


def test_user_data_encryption():
    user_id = "user_id_0001"
    # The sensitive data is like address, identity card, bank account, etc...
    sensitive_user_data = "IDENTITY_CARD_NUMBER"
    # Generate an encryption key to encrypt sensitive data
    encryption_key = generate_encryption_key()
    # Save this key with Locker Secrets
    save_encryption_key(user_id=user_id, encryption_key=encryption_key)

    # Encrypt sensitive data by encryption key
    iv = generate_iv()
    cipher = AES.new(b64decode(encryption_key.encode('utf-8')), AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(sensitive_user_data.encode(), BLOCK_SIZE))
    # Now, you can save the encrypted data in your database,...
    print("Encrypted data: ", cipher_text)

    # When you want to decrypt the data from your database, retrieve the encryption from Locker Secrets and decrypt data
    decryption_key = get_encryption_key(user_id=user_id)
    decrypt_cipher = AES.new(b64decode(decryption_key.encode('utf-8')), AES.MODE_CBC, iv)
    plain_data = unpad(decrypt_cipher.decrypt(cipher_text), BLOCK_SIZE)
    print("Decrypted data:", plain_data)


if __name__ == '__main__':
    test_user_data_encryption()
