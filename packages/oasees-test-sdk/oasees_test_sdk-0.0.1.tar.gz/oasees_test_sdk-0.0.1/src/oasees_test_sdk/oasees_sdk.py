from web3 import Web3
import ipfshttpclient
import json
import requests

IPFS_HOST = "172.19.215.220"



web3 = Web3(Web3.HTTPProvider("http://172.19.215.220:8545"))
account_addr = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
wallet_address = Web3.to_checksum_address(account_addr)

balance = web3.eth.get_balance(wallet_address)
#print(web3.from_wei(balance,"ether"))

response = requests.get('http://172.19.215.220:6002/get_marketplace_ipfs_hash')
data = response.json()
ipfs_hash = data['ipfs_hash']

client = ipfshttpclient.connect("/ip4/{}/tcp/5001".format(IPFS_HOST))
ipfs_json = client.cat(ipfs_hash)
ipfs_json = ipfs_json.decode("UTF-8")
ipfs_json = json.loads(ipfs_json)

marketplace_abi = ipfs_json['marketplace_abi']['abi']
marketplace_address = ipfs_json['marketplace_address']

nft_abi = ipfs_json['nft_abi']['abi']

nft_marketplace = web3.eth.contract(address=marketplace_address, abi=marketplace_abi)


def getPurchases():
    _filter=nft_marketplace.events.Bought.create_filter(fromBlock="0x0", argument_filters={"buyer":account_addr})
    results=_filter.get_new_entries()

    purchases=[]

    for r in results:
        nft_address = r['args']['nft']
        token_id = r['args']['tokenId']

        #print(token_id)
        ntf = web3.eth.contract(address=nft_address, abi=nft_abi)
        token_uri=ntf.functions.tokenURI(token_id).call()

        nft_ipfs_json = client.cat(token_uri)
        nft_ipfs_json = nft_ipfs_json.decode("UTF-8")
        nft_ipfs_json = json.loads(json.loads(nft_ipfs_json))
        # _hash=token_uri.split("?filename=")[1].strip(".")
        # print(type(nft_ipfs_json))

        purchases.append(nft_ipfs_json)
        
        # algo = client.cat(nft_ipfs_json['contentURI'])

        # #print(algo)

        # with open(nft_ipfs_json['title'] + ".py", "wb") as binary_file:

        #     binary_file.write(algo)
    
    return purchases

def list():
    purchases = getPurchases()
    for purchase in purchases:
        print (purchase['title'])

def deploy():
    purchases = getPurchases()
    for purchase in purchases:
        algo = client.cat(purchase['contentURI'])

        with open(purchase['title'] + ".py", "wb") as binary_file:
            binary_file.write(algo)