# usage: python3 solve.py [salt_hex nonce_hex ciphertext_hex]   (defaults: values from the challenge page)
import sys, json, hashlib, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
args = sys.argv[1:] or ["a3845b1a904c5ee73abe7329b5d735d7", "ca98cff993b27fd3bb352436", "3fa8b9049b01fb8d12df130b404352f9c678c272cccb7e6c034554c902f1ca4d574fc04db8892fead1ad394735e021"]
evidence = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evidence.json')))
E = json.dumps(evidence, ensure_ascii=True, separators=(",", ":")).encode("ascii")
key = hashlib.scrypt(b"isfcr-forensics\x00" + E, salt=bytes.fromhex(args[0]), n=131072, r=8, p=1, maxmem=2**28, dklen=32)
print(AESGCM(key).decrypt(bytes.fromhex(args[1]), bytes.fromhex(args[2]), b"the-last-committed-message").decode())
