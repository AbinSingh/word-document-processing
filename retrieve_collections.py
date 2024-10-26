import chromadb

# Initiating a persistent Chroma client
client = chromadb.PersistentClient(path="chroma_storage")

# Check if collection already exists, if not create it
if "insurance_policies" in [coll.name for coll in client.list_collections()]:
    collection = client.get_collection("insurance_policies")
else:
    collection = client.create_collection("insurance_policies")

# Retrieve all documents from a collection
all_docs = collection.get()

print(all_docs)