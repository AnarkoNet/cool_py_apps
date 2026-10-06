import hashlib
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from math import log, log2, ceil, e
from zxcvbn import zxcvbn
import base64

def check(x):
    return zxcvbn(str(x))

def hsh(x):
    if type(x) != bytes:
        x=str(x).encode("utf-8")
    return hashlib.sha256(x).digest()
def encrypt(x,k):
    if type(x) != bytes:
        x=str(x).encode("utf-8")
    if type(k) != bytes:
        k=str(k).encode("utf-8")
    k=hashlib.sha256(k).digest()
    aes=AESGCM(k)
    iv=os.urandom(12)
    result=iv+aes.encrypt(iv,x,None)
    return result
def decrypt(x,k):
    if type(x) != bytes:
        x=str(x).encode("utf-8")
    if type(k) != bytes:
        k=str(k).encode("utf-8")
    k=hashlib.sha256(k).digest()
    iv=x[:12]
    result=x[12:]
    aes=AESGCM(k)
    result=aes.decrypt(iv,result,None)
    return result

def b64(x):
    if type(x) == str:
        return base64.b64decode(x.encode("utf-8"))
    else:
        return base64.b64encode(x).decode("utf-8")