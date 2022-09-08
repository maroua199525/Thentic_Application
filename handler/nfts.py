import requests
import json

def create_nft():
    """
    create new NFT contract using THENTIC API"""
    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3',
            'name': 'Artwork by Maroua', 
            'short_name': 'Arts'}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return (response.json()['transaction_url'])

    except requests.exceptions.ConnectionError:
        return "Error creating"


def mint_nft(nft_id, address, data):
    
    """mint a NFT using THENTIC API"""
    url = 'https://thentic.tech/api/nfts/mint'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3',
            'nft_id': nft_id,
            'tot': address,
            'contract': str(get_contract_address()),
            'nft_data': data}

    #mint NFT 
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return (response.json()['transaction_url'])
    else:
        return 'Error minting NFT'




def transfer_nft(nft_id, address_transfer, address_receive):
    """
    transfer NFT using THENTIC API"""
    
    url = 'https://thentic.tech/api/nfts/transfer'
    headers = {'Content-Type': 'application/json'}
    nft_data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3',
            'nft_id': nft_id,
            'contract': get_contract_address(),
            'from': address_transfer,
            'to': address_receive}

    # Transfer NFT to new adress
    try:
        response = requests.post(url, json=nft_data, headers=headers)
        if response.status_code == 200:
            return (response.json()['transaction_url'])

    except requests.exceptions.ConnectionError:
        return "Error transfering NFT"


def get_contract_address():
    """
    get NFT contract address using THENTIC API"""
    url = 'https://thentic.tech/api/contracts'
    headers = {'Content-Type': 'application/json'}
    nft_data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3'}
    # getting the adress of the contract
    try:
        response = requests.get(url, json=nft_data, headers=headers)
        if response.status_code == 200:
            return response.json()['contracts'][0]['contract']

    except requests.exceptions.ConnectionError:
        return "Error getting the adress of the contract "


def get_nfts():
    """
    get NFTs using THENTIC API"""
    url = 'https://thentic.tech/api/nfts'
    headers = {'Content-Type': 'application/json'}
    nft_data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3'}
    # get NFT

    response = requests.get(url, json=nft_data, headers=headers)
    print(response.content)
    if response.status_code == 200:
        return response.json()

    else:
        return 'Error getting The NFT'



def create_invoice(amount, address):
    """
    create invoice for NFT using THENTIC API"""
    url = 'https://thentic.tech/api/invoices/new'
    headers = {'Content-Type': 'application/json'}
    nft_data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3',
            'amount': amount,
            'to': address
    }

    try:
        response = requests.post(url, json=nft_data, headers=headers)
        if response.status_code == 200:
            id = response.json()['request_id']
            return response.json(), id
    except requests.exceptions.ConnectionError:
        return 'Error creating invoice'



def get_invoices():
    """
    get invoice for NFT using THENTIC API"""
    url = 'https://thentic.tech/api/invoices/all'
    headers = {'Content-Type': 'application/json'}
    nft_data = {'key': 'yRVOe6x3p7k1lvqYYJxhvYAL0DNZ9rrs',
            'chain_id': '3'
    }    
    try:
        r = requests.get(url, json=nft_data, headers=headers)
        if r.status_code == 200:
            return r.json()

    except requests.exceptions.ConnectionError:
        return 'Error getting invoice'



# Function helper to retrieve data from the user(input)

def get_form_to_dict(form): 
    """ make from html post form """
    dic = {}
    for key, value in form.items():
        dic[key] = value
    return dic
