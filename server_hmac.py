import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    return generate_mac(message) == mac

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)
    print("Original message:", message.decode())
    print("MAC:", mac)

    forged_message = message + b"&admin=true"
    if verify(forged_message, mac):
        print(" Insecure: Forged MAC accepted")
    else:
        print(" Secure: Forged MAC rejected")

if __name__ == "__main__":
    main()
