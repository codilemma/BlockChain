import hashlib  # Shipped with Python
from hashlib import sha256

#**********************************
# Hashing a String
#**********************************

# Hash functions expect bytes as input: the encode() method 
# turns strings to bytes
input_bytes = b"backpack"

output = sha256(input_bytes)

# we use hexdigest() to convert bytes to hex because it's 
# # easier to read print(output.hexdigest())
print(output.hexdigest())

# Avalanche effect:
# The smallest change in input should yield a hash
# so different that the new hash appears unreleated to the new hash.

# All hash functions provide predictable output for a given input.

#************************************
# Hashing a Photo
#************************************
#file = open("chpter2.png", "rb") # "rb" = read-only,byte-mode
#hash = sha256(file.read()).hexdigest()
#file.close()

#print(f"The hash of my file is: {hash}")

#************************************
# Sending Untamperable Emails
#************************************
# How to verify and email
# Bob is given this hash
from hashlib import sha256

secret_phrase = "bolognese"

def get_hash_with_secret_phase(input_data,secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()

email_body = "Hey Bob, I think you should learn about Blockchains! "\
             "I've been investing in Bitcoin and currently have exactly" \
             "12.03 BTC in my account."

print(get_hash_with_secret_phase(email_body,secret_phrase))
# The resulting hash should match the has given in the email body.