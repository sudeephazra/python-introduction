import Block
import json
import datetime

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    genesis_block = Block.Block(0, datetime.datetime.now().__str__(), "Genesis Block", "0")
    return genesis_block

def next_block(last_block):
    this_index = last_block.index + 1
    this_data = "Block " + str(this_index)
    this_hash = last_block.hash
    next_block_chain = Block.Block(this_index, datetime.datetime.now().__str__(), this_data, this_hash)
    return next_block_chain

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 5

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

# Prints the entire blockchain in JSON form
for i in range(0, blockchain.__len__()):
    print(json.dumps(blockchain[i].__dict__))

print("########################################")
# Printing the original block
print(json.dumps(blockchain[2].__dict__))
# Tampering with the block data
blockchain[2].data = "Modified"
# Re-hashing the block
blockchain[2].hash = Block.Block.hash_block(blockchain[2])
# Printing the tampered block
print(json.dumps(blockchain[2].__dict__))