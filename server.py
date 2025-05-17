import hashlib

SECRET_KEY = b'supersecretkey'  # Hidden from attacker

def generate_mac(message: bytes) -> str:
    return hashlib.md5(SECRET_KEY + message).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return generate_mac(message) == mac

if __name__ == "__main__":
    msg = b"amount=100&to=alice"
    mac = generate_mac(msg)
    print("Original Message:", msg.decode())
    print("Original MAC:", mac)

