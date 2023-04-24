from tinydb import TinyDB, where

# Open the JSON file for reading and writing
db = TinyDB('resources/account_database.json')


# Insert data into the database
def create_account(account):
    db.insert(account)
    return True


def get_account_by_id(account_id):
    acc = db.search(where("accountId") == str(account_id))
    if acc is not None and len(acc) > 0:
        return acc[0]
    else:
        return None


def update_account_balance(account_id, amount):
    db.update({'balance': amount}, where("accountId") == str(account_id))


def get_all_account():
    return db.all()
