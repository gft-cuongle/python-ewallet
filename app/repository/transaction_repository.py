from tinydb import TinyDB, Query

# Open the JSON file for reading and writing
db = TinyDB('../resources/transaction_database.json')

# Insert data into the database
db.insert({'id': '112313-121321231', 'name': 'John', 'age': 25})
# db.insert({'name': 'Jane', 'age': 30})

# Query the database
User = Query()
result = db.search(User.name == 'John')

# Print the result
print(result)

# Update data in the database
# db.update({'age': 26}, User.name == 'John')

# Remove data from the database
# db.remove(User.name == 'Jane')
