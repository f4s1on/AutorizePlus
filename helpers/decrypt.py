from javax.crypto import Cipher
from javax.crypto.spec import IvParameterSpec
from javax.crypto.spec import SecretKeySpec

from java.util import Base64



def decryptJython(payload, key ,mode, iv):
    decoded = Base64.getDecoder().decode(payload)
    aesKey = SecretKeySpec(key, "AES")
    aesIV = IvParameterSpec(iv)
    cipher = Cipher.getInstance(mode)
    if(mode.find("ECB") != -1):
        cipher.init(Cipher.DECRYPT_MODE, aesKey)
    else:
        cipher.init(Cipher.DECRYPT_MODE, aesKey, aesIV)
    return cipher.doFinal(decoded)

def encryptJython(payload, key ,mode, iv):
    aesKey = SecretKeySpec(key, "AES")
    aesIV = IvParameterSpec(iv)
    cipher = Cipher.getInstance(mode)
    if(mode.find("ECB") != -1):
        cipher.init(Cipher.ENCRYPT_MODE, aesKey)
    else:
        cipher.init(Cipher.ENCRYPT_MODE, aesKey, aesIV)
    encrypted = cipher.doFinal(payload)
    return Base64.getEncoder().encode(encrypted)