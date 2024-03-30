# Парсинг транзакций хеш и txid

import requests
import time

def get_unconfirmed_transactions():
    url = "https://blockchain.info/unconfirmed-transactions?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        transactions = data['txs']
        return transactions
    else:
        print("Error:", response.status_code)
        return None

def main():
    while True:
        unconfirmed_transactions = get_unconfirmed_transactions()
        if unconfirmed_transactions:
            print("Транзакции:")
            for tx in unconfirmed_transactions:
                print("ID транзакции (txid) Хэш транзакции:", tx['tx_index'], tx['hash'])
        else:
            print("Транзакций не обнаружено")
        time.sleep(10)

if __name__ == "__main__":
    main()
