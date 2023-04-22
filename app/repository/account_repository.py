from tinydb import TinyDB, Query

# Open the JSON file for reading and writing
db = TinyDB('resources/account_database.json')


# Insert data into the database
def create_account(account):
    db.insert(account)
    return True


def get_account_by_id(account_id):
    acc = db.search(Query().accountId == str(account_id))
    if acc is not None:
        return acc[0]
    else:
        return None
