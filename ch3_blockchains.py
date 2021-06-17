
# What does a block look like?
# ---> A Python Dictionary?
# Each block contains the hash of th previous block.  IMUTABLE
# If a single bit in an earlier block were tampered with
# The entire subsequent blockchain would be invalid.
# Everyone on the blockchain network would immediately 
# notice and ignore the change.

block_1038 = {
    'index': 1038,
    'timestamp': "2020-02-25T08:07:42.170675",
    'data': [
        {
            'sender': "bob",
            'recipient': "alice",
            'amount': "$5",
        }
    ],
    'hash': "83b2ac5b",
    'previous_hash': "2cf24ba5f"
}



