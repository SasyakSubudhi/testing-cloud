# usage: python3 solve.py <salt_hex> <nonce_hex> <ciphertext_hex>   (paste the full hex strings from the challenge page)
import sys, json, hashlib, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
evidence = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evidence.json')))
E = json.dumps(evidence, ensure_ascii=True, separators=(",", ":")).encode("ascii")
key = hashlib.scrypt(b"isfcr-forensics\x00" + E, salt=bytes.fromhex(sys.argv[1]), n=131072, r=8, p=1, maxmem=2**28, dklen=32)
print(AESGCM(key).decrypt(bytes.fromhex(sys.argv[2]), bytes.fromhex(sys.argv[3]), None).decode())
