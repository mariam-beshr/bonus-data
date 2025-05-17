import hashpumpy
from server import verify

def perform_attack():
    original_message = "amount=100&to=alice"
    original_mac = "614d28d808af46d3702fe35fae67267c"  # Replace with actual MAC from server
    data_to_append = "&admin=true"
    guessed_key_length = 14  # Length of the secret key

    forged_mac, forged_message = hashpumpy.hashpump(
        original_mac,
        original_message,
        data_to_append,
        guessed_key_length
    )

    print("Forged message:", forged_message)
    print("Forged MAC:", forged_mac)

    if verify(forged_message, forged_mac):
        print("Server accepted forged MAC.")
    else:
        print("Server rejected forged MAC.")

if __name__ == "__main__":
    perform_attack()
