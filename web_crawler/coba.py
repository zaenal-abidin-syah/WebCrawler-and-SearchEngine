content = []
input_data = 'news.csv'
with open(input_data, 'r', encoding='latin1') as file:
    reader = csv.DictReader(file)
    for row in reader:
        content.append(row)

data = pd.DataFrame(content)
data = data.dropna()
data['Konten'] = data['Konten'].str.lower()
data['Konten'] = data['Konten'].str.replace('[^\w\s]', '')
data['Kelas'].value_counts()

result = data.groupby(['Kelas']).size()
sns.barplot(x = result.index, y = result.values)

data['Situs'] = data['URL'].apply(lambda x: x.split('/')[2] if len(x.split('/')) == 2 else '.'.join(x.split('/')[2].split('.')[1:]))
result = data.groupby(['Situs']).size()
sns.barplot(x = result.index, y = result.values)

data['Konten'] = data['Konten'].str.replace("[^\w\s]", ' ', case=False)

# Mengimpor word_tokenize dari modul nltk
from nltk.tokenize import word_tokenize

# Mengimpor RegexpTokenizer dari nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Membuat instance RegexpTokenizer untuk hanya mempertahankan kata (alphanumeric)
regexp = RegexpTokenizer('\w+')

# Menerapkan tokenisasi pada kolom 'content'
data['Konten_token'] = data['Konten'].apply(regexp.tokenize)

nltk.download('stopwords')
# Make a list of Indonesian stopwords
stopwords = stopwords.words("indonesian")

my_stopwords = ['kompas', 'detik', 'okezone']
stopwords.extend(my_stopwords)
data['Konten_token'] = data['Konten_token'].apply(lambda x: [item for item in x if item not in stopwords])

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemmed
def stemmed_wrapper(term):
    return stemmer.stem(term)

term_dict = {}

for document in data['Konten_token']:
    for term in document:
        if term not in term_dict:
            term_dict[term] = ' '

for term in term_dict:
    term_dict[term] = stemmed_wrapper(term)

# apply stemmed term to dataframe
def get_stemmed_term(document):
    return [term_dict[term] for term in document]

data['Konten_stemm'] = data['Konten_token'].swifter.apply(get_stemmed_term)

data['Konten'] = data['Konten_stemm']

clean_data = data[['Judul', 'Waktu', 'URL', 'Kelas', 'Konten']]

clean_data['Konten'] = clean_data['Konten'].apply(lambda x: ' '.join(map(str, x)))

clean_data.to_csv('clean_news.csv', index=False)
