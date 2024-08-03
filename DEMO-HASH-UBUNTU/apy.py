import hashlib
import bcrypt
import time
from argon2 import PasswordHasher

password = "securepassword123"

# MD5
start_time = time.time()
md5_hash = hashlib.md5(password.encode()).hexdigest()
md5_time = time.time() - start_time
print(f"MD5: {md5_hash} - Temps: {md5_time:.6f} secondes")

# Bcrypt
start_time = time.time()
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt_time = time.time() - start_time
print(f"Bcrypt: {bcrypt_hash} - Temps: {bcrypt_time:.6f} secondes")

# Argon2
ph = PasswordHasher()
start_time = time.time()
argon2_hash = ph.hash(password)
argon2_time = time.time() - start_time
print(f"Argon2: {argon2_hash} - Temps: {argon2_time:.6f} secondes")