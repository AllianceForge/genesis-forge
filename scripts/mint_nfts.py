from web3 import Web3
import json

NFT_CONTRACT_ADDRESS = "0xTuContrato"
PRIVATE_KEY = "TU_PRIVATE_KEY"
RPC_URL = "https://cronos-node-url"
ACCOUNT = "0xTuWallet"
with open("contract_abi.json") as f:
    abi = json.load(f)

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=abi)

def mint_nft(token_uri):
    nonce = w3.eth.get_transaction_count(ACCOUNT)
    txn = contract.functions.mint(ACCOUNT, token_uri).build_transaction({
        "from": ACCOUNT,
        "nonce": nonce,
        "gas": 250000,
        "gasPrice": w3.to_wei("5", "gwei")
    })
    signed = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print("Minted:", tx_hash.hex())

def main():
    with open("./output/metadata_uris.txt") as f:
        uris = f.read().splitlines()
    for uri in uris:
        mint_nft(uri)

if __name__ == "__main__":
    main()
