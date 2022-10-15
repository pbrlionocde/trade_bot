import os
from secrets import Secrets
from typing import Final

from web3 import Web3

BINANCE_DEFAULT_NETWORK_PROVIDER: Final = os.environ['BSC_RPC']

# Web3.HTTPProvider('http://127.0.0.1:8545')

class Web3_Wrapped:

    def __init__(self):
        self.web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri='http://127.0.0.1:8545'))     # TODO: use the real provider as `BINANCE_DEFAULT_NETWORK_PROVIDER`
        self.secrets = Secrets()

    def is_connected(self):
        return self.web3.isConnected()

    def get_latest_block_info(self):
        latest_info = self.web3.eth.get_block('latest')
        return latest_info

    @property
    def accounts(self):
        return self.web3.eth.accounts

    def convert_to_ether(self, balance: int):
        return self.web3.fromWei(balance, 'ether')


    def get_balance(self, converted: bool = False):
        balance = self.web3.eth.get_balance(self.accounts[0])
        if converted:
            return self.convert_to_ether(balance)
        return balance


if __name__ == '__main__':
    web3_instance = Web3_Wrapped()
    print(f'connected status: {web3_instance.is_connected()}')
    print(web3_instance.get_latest_block_info())

    a = web3_instance.accounts
    print(f'balance {web3_instance.get_balance()}')
    print(f'converted balance {web3_instance.get_balance(converted=True)}')
