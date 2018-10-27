import hashlib
import json
import datetime

# Genesis node - The first node of the chain
genesis_block = {
    'index': 0,
    'datetime': datetime.datetime.now().__str__(),
    'prev_hash': None,
    'data': "First block"
}
genesis_block_serial = json.dumps(genesis_block, sort_keys=True).encode('utf-8')
genesis_block_hash = hashlib.sha256(genesis_block_serial).hexdigest()
print(genesis_block)
print(genesis_block_hash)


