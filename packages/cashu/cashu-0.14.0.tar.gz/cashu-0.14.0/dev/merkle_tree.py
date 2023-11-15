import hashlib
from os import path

from pymerkle import InmemoryTree as MerkleTree

from cashu.core.crypto.aes import AESCipher

data: bytes = b""
BLOCK_SIZE = 1024
preimage = b"4f27f3189dcf41891daaf43ee77210b64cc4e67da9232a37d58ee68d8293be9a"


# def pad_block(block: bytes):
#     while len(block) % BLOCK_SIZE != 0:
#         block += b"\x00" * (BLOCK_SIZE - len(block) % BLOCK_SIZE)
#     return block


plaintext_tree = MerkleTree()
encrypted_tree = MerkleTree()

plaintext_hashes = []
encrypted_chunks = []

with open(path.join("data", "wallet", "wallet.sqlite3"), "rb") as f:
    block_nr = 0
    while True:
        chunk = f.read(BLOCK_SIZE)
        if not chunk:
            break
        chunk_hash = hashlib.sha256(chunk).digest()
        # print(f"Chunk {block_nr}: {chunk_hash.hex()}")

        encrypted_chunk = AESCipher(preimage.hex()).encrypt(chunk_hash)

        # this will be sent to the client
        plaintext_hashes.append(chunk_hash.hex())
        encrypted_chunks.append(encrypted_chunk)

        encrypted_tree.append_entry(chunk_hash)
        encrypted_tree.append_entry(encrypted_chunk.encode())

        # add data to merkle tree
        index = plaintext_tree.append_entry(chunk_hash)  # leaf index
        value = plaintext_tree.get_leaf(index)  # leaf hash
        assert isinstance(value, bytes)
        size = plaintext_tree.get_size()  # current tree size: number of leaves

        # print(
        #     f"Current tree size: {size}, index: {index}, value: {value.hex()},"
        #     f" len(chunk): {len(chunk)}"
        # )
        block_nr += 1


plaintext_state = plaintext_tree.get_state()
print(f"File ID merkle root: {plaintext_state.hex()}")

encrypted_state = encrypted_tree.get_state()
print(f"Encrypted ID merkle root: {encrypted_state.hex()}")

# client side

# print(f"Encrypted chunks: {encrypted_chunks}")
# print(f"Plaintext hashes: {plaintext_hashes}")

# print(hashlib.sha256(data).hexdigest())
# tree = MerkleTree()
# tree.append_entry()
