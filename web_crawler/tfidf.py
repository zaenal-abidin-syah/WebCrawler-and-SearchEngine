import re
import sys
import pickle
import math
import csv


# Argumen check
if len(sys.argv) != 3:
    print ("\n\\Use python \n\t tf-idf.py [hasil_scrap.csv] [output]\n")
    sys.exit(1)

# Data arguments
input_data = sys.argv[1]
output_data = sys.argv[2]

# Load data from CSV
content = []
with open(input_data, 'r', encoding='latin1') as file:
    reader = csv.DictReader(file)
    for row in reader:
        content.append(row)

# Clean string function
def clean_str(text):
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\s+', ' ', text)      # Replace multiple spaces with single space
    text = text.lower()                   # Convert text to lowercase
    return text

# Calculate TF and IDF
df_data = {}
tf_data = {}
idf_data = {}

for data in content:
    tf = {}
    clean_content = clean_str(data['Konten'])
    list_word = clean_content.split()

    for word in list_word:
        # TF term frequency
        if word not in tf:
            tf[word] = 0
        tf[word] += 1

    for word in set(list_word):  # Use set to count DF
        if word in df_data:
            df_data[word] += 1
        else:
            df_data[word] = 1

    tf_data[data['URL']] = tf

# Calculate IDF
total_docs = len(content)
idf_data = {word: 1 + math.log10(total_docs / df_data[word]) for word in df_data}

# Calculate TF-IDF
tf_idf = {}
for word in df_data:
    list_doc = []
    for data in content:
        url = data['URL']
        tf_value = tf_data[url].get(word, 0)
        weight = tf_value * idf_data[word]

        doc = {
            'url': url,
            'judul': data['Judul'],
            'kelas': data['Kelas'],
            'waktu': data['Waktu'],
            'score': weight
        }

        if doc['score'] != 0:
            list_doc.append(doc)

    tf_idf[word] = list_doc

# Write dictionary to file
with open(output_data, 'wb') as file:
     pickle.dump(tf_idf, file)
