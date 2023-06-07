from cryptography.fernet import Fernet
import hashlib
import base64

# An encryption function that on input secret key and plaintext, it returns a ciphertext
def encrypt(key, ptext):
    ctext = Fernet(key).encrypt(ptext)
    return ctext


# A decryption function that on input secret key and ciphertext, it returns a plaintext
def decrypt(key, ctext):
    ptext = Fernet(key).decrypt(ctext)
    return ptext


# A function that on input PIN, it returns its SHA256 in Hex format
def hash_to_key(pin):
    PIN = str(pin)
    hash_pin = hashlib.sha256(PIN.encode()).hexdigest()
    return hash_pin


# A function that on input Hex value, it returns string in Base64 format
# Note that this Base64 format is necessary as the input for encryption function
def b64_encode(hex_input):
    b64 = base64.b64encode(bytes.fromhex(hex_input)).decode()
    return b64


print("==================== Welcome to Xuan\'s program ====================")
# ===================== Start your answer here ==================================
# read ciphertext in the file.
PWDCiphertext="gAAAAABkUfln3QT2qvF4Kxoj2xJCkPxLh4HgD6Mf8grf0GvPxpAjotrjpXe3O_w8bhLMHuhJWMwZdaso7e1NRVBgqMrHY_g2XWq2fUuKXtntTY6vfq9q5X8NID6CBhyGb68rzV3HgY8lpad41ewsSqrwFnCixZsuOMkh5AcPnzoX5Wv-iF4VxdliJXVUaRLYkgrX6Ic1x_19eSAWqCpkXGFtdZxFtgA0PDVV9Y5uLYE8GoSuinN84hCL-WED_DOe7AnrA9KAX1kE__tibqIBxaUBtcRF0drkLQ=="
# with open('PWDCiphertext.txt', 'r') as f:
#     pwd_ctext = f.read()
# print("In PWDCiphertext.txt, ciphertext is: ", pwd_ctext)
# the potential values of PIN
PINs = [str(t).zfill(4) for t in range(10000)]
# crack password
for pin in PINs:
    hash_pin = hash_to_key(pin)
    hash_pin_b64 = b64_encode(hash_pin)
    try:
        plaintext = decrypt(hash_pin_b64.encode(), PWDCiphertext)
        print("The key PIN of this password is: ", pin)
        print("Password for the protected file is : ", plaintext.decode())
        break
    except:
        print("this key is invalid")

# ===================== Stop your answer here ==================================
print("=========================== END ===========================")
