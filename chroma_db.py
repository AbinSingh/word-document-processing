import chromadb
from sentence_transformers import SentenceTransformer
import json

# Initialize Chroma client # no storage
# chroma_client = chromadb.Client()

# Initialize Chroma client with persistent storage settings
client = chromadb.PersistentClient(path="chroma_storage")

# Check if collection already exists, if not create it
if "insurance_policies" in [coll.name for coll in client.list_collections()]:
    collection = client.get_collection("insurance_policies")
else:
    collection = client.create_collection("insurance_policies")

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample policy document
policy_doc = {
    "policy_id": "001",
    "policy_type": "Home Guard",
    "country": "Hong Kong",
    "coverage_details": [
        "Accidental Death and Disablement",
        "Public Conveyance Double Cover",
        "Overseas Medical Expenses",
        "Medical Treatment after Return to Singapore"
    ],
    "general_exclusions": "Financial circumstances...",
    "target_market_determination": {
        "product": "Home Guard Insurance...",
        "target_customer": "Ideal for homeowners, renters..."
    }
}

# Convert relevant fields to embeddings
product_embedding = model.encode(policy_doc["target_market_determination"]["product"])
target_customer_embedding = model.encode(policy_doc["target_market_determination"]["target_customer"])

# Flatten or serialize coverage details and general exclusions
coverage_details_str = json.dumps(policy_doc["coverage_details"])  # Convert list to JSON string
general_exclusions_str = policy_doc["general_exclusions"]  # Keep as-is if it's already a string


# Add to Chroma DB
collection.add(ids=[policy_doc["policy_id"]],
    documents = [f"Coverage: {coverage_details_str}, Exclusions: {general_exclusions_str}"],

    metadatas = [{
        "policy_type": policy_doc["policy_type"],
        "country": policy_doc["country"]
    }],
    embeddings=[product_embedding])

# Similarity Search for Customer Profile
customer_profile = "Looking for insurance for a homeowner in Hong Kong with coverage for accidental damage and natural disasters."
customer_profile_embedding = model.encode(customer_profile)

# Retrieve similar policies
results = collection.query(
    query_embeddings=[customer_profile_embedding],
    n_results=1,
    where = {"$and": [
            {"policy_type": {"$eq": "Home Guard"}},
            {"country": {"$eq": "Hong Kong"}}]
    }
)

# Print relevant details of retrieved policies
for result in results["documents"]:
    if len(result)>0:
        print(result)
        # print("Policy ID:", result["policy_id"])
        # print("Coverage Details:", result["coverage_details"])
        # print("Exclusions:", result["general_exclusions"])
