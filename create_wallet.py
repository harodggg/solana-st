from mnemonic import Mnemonic
from solders.keypair import Keypair
import base58
import csv

mnemo = Mnemonic("english")
words = mnemo.generate(strength=128)
print(words)
for i in range(300):
    path = f"m/44'/501'/{i}'/0'"
    keypair = Keypair().from_seed_and_derivation_path(mnemo.to_seed(words),path)
    rawPk = bytes(keypair)
    pk = base58.b58encode(rawPk).decode()
    with open('data.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([keypair.pubkey(),pk])


