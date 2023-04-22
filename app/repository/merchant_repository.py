from tinydb import TinyDB, Query

# Open the JSON file for reading and writing
db = TinyDB('resources/merchant_database.json')


# Insert data into the database
def create_merchant(merchant):
    db.insert(merchant)
    return True


def get_merchant_by_id(merchant_id):
    merchant = db.search(Query().merchantId == str(merchant_id))
    if merchant is not None:
        return merchant[0]
    else:
        return None
