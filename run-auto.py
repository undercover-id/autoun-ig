import hashlib
from nacl.secret import SecretBox
pw = input("Masukkan password: ")
key = hashlib.sha256(pw.encode()).digest()[:32]
box = SecretBox(key)
with open("vick.bin","rb") as f:
    data = f.read()
code = box.decrypt(data)
exec(code.decode())
