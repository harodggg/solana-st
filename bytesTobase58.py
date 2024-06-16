import base58
import solana

from solders.keypair import Keypair



key_array =  []
# 
# 
# secret_key = key_array[0:32]
# public_key = key_array[32:64]
# 
# print(bytes(secret_key))
# 
# sk = base58.b58encode(bytes(secret_key))
# pk = base58.b58encode(bytes(public_key))
# 
# print(sk)

k = Keypair.from_bytes(key_array)
print(k)
# bk = bytes(k.pubkey())
# bs = k.secret()
# 
# 
# ek = bk + bs  
# print(ek)
# 
# pk = base58.b58encode(ek).decode()
# print(pk)
rawPk = bytes(k)
print(rawPk)
pk = base58.b58encode(rawPk).decode()

print(pk)
