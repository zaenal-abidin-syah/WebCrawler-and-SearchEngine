import sys
import json
import pickle
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Argumen check
if len(sys.argv) != 4:
    print("\n\nPenggunaan\n\tquery.py [index] [n] [query]..\n")
    sys.exit(1)

query = sys.argv[3].split(" ")
n = int(sys.argv[2])
factory = StemmerFactory()
stemmer = factory.create_stemmer()
query = [stemmer.stem(q)  for q in query]

# Load index file
with open(sys.argv[1], 'rb') as indexdb:
    indexFile = pickle.load(indexdb)

# Query
list_doc = {}
for q in query:
    try:
        for doc in indexFile.get(q, []):
            if doc['url'] in list_doc:
                list_doc[doc['url']]['score'] += doc['score']
            else:
                list_doc[doc['url']] = doc
    except Exception as e:
        print(f"Error while processing query: {e}")

# Convert to list
list_data = list(list_doc.values())

# Sorting list descending by score
sorted_list_data = sorted(list_data, key=lambda k: k['score'], reverse=True)

# Print top n results
for i, data in enumerate(sorted_list_data):
    print(json.dumps(data))
    if i + 1 == n:
        break
