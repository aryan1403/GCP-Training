from google.cloud import firestore

db = firestore.Client(database="meowdb")

# Create
doc_ref = db.collection('users').add({
    'name': 'John Doe',
    'email': 'john@example.com',
    'role': 'Developer',
    'exp': 5
})

# Read
print("Users exp >= 10")
for doc in db.collection('users').where('exp', '>=', 10).stream():
    print(f'{doc.id} => {doc.to_dict()}')

# Update
db.collection('users').document(doc_ref[1].id).update({
    'exp': 6
})
print(f"Updated user {doc_ref[1].id} exp to 6")

# Delete
query = db.collection('users').where('name', '==', 'Meow')


for doc in query.stream():
    db.collection('users').document(doc.id).delete()
    print(f"Deleted user with name {doc.id}")