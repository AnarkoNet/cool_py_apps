import secrets
import math
import base64, os

if os.path.isfile("words.txt"):
  words = open("words.txt").read().split("\n")[:-1]
else:
  words = None

def sentence(n):
  if words:
    try:
      n = int(n)
    except:
      return False
    lords = len(words)
    result = []
    n += 1
    while n > 0:
      n -= 1
      result.append(words[n % lords])
      n //= lords
    return result[::-1]
  else:
    return []

def passphrase(l):
  return " ".join(sentence(secrets.randbits(256))[-int(l):])

def randc(i):
  o=""
  a=""
  u=""
  s=""
  for i in range(i):
    o+=secrets.choice("0123456789ABCDEF")
    a+=secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    u+=chr(secrets.randbits(10))
    s+=secrets.choice('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
  p=passphrase(i//8)
  b=base64.b64encode(os.urandom(math.ceil(3*i/4))).decode("ascii")
  return "HEX: "o+"\nABC: "+a+"\nUNI: "+u+"\nB64: "+b+"\nASC: "+s+"\nPsP: "+p
print(randc(33))