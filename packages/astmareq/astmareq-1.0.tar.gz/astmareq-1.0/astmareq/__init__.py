def Create_Bag_of_words_py():
    s="""import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
text = ["I love writing code in Python. I love Python code",
 "I hate writing code in Java. I hate Java code"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
cv = CountVectorizer(stop_words='english')
cv_matrix = cv.fit_transform(df['text'])
df_dtm = pd.DataFrame(cv_matrix.toarray(),
 index=df['review'].values,
 columns=cv.get_feature_names())
df_dtm"""
    return s
def chunking():
    s="""import nltk
sentence = [
 ("the", "DT"),
 ("book", "NN"),
 ("has","VBZ"),
 ("many","JJ"),
 ("chapters","NNS")
]
chunker = nltk.RegexpParser(
 r'''
 NP:{<DT><NN.*><.*>*<NN.*>}
 }<VB.*>{
 '''
)
chunker.parse(sentence)
Output = chunker.parse(sentence)
print(Output)"""
    return s
def Named_Entity_Recognition():
    s="""! pip install spacy
! pip install nltk
! python -m spacy download en_core_web_sm
import spacy
from spacy import displacy
NER = spacy.load("en_core_web_sm")
raw_text="The Indian Space Research Organisation or is the national space agency of India,
headquartered in Bengaluru. It operates under Department of Space which is directly overseen by
the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
text1= NER(raw_text)
for word in text1.ents:
 print(word.text,word.label_)"""
    return s
def POS_tagging():
    s="""import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
txt = "Sukanya, Rajib and Naba are my good friends. " \
 "Sukanya is getting married next year. " \
 "Marriage is a big step in one’s life." \
 "It is both exciting and frightening. " \
 "But friendship is a sacred bond between people." \
 "It is a special kind of love between us. " \
 "Many of you must have tried searching for a friend "\
 "but never found the right one."

# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module
tokenized = sent_tokenize(txt)
for i in tokenized:

 # Word tokenizers is used to find the words
 # and punctuation in a string
 wordsList = nltk.word_tokenize(i)
 # removing stop words from wordList
 wordsList = [w for w in wordsList if not w in stop_words]
 # Using a Tagger. Which is part-of-speech
 # tagger or POS-tagger.
 tagged = nltk.pos_tag(wordsList)
 print(tagged)"""
    return s
def stemming_lemmatization():
    s="""import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
print("Stemming for {} is {}".format(w,porter_stemmer.stem(w)))"""
    return s
def td_idf():
    s="""import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
text = ["I love writing code in Python. I love Python code",
 "I hate writing code in Java. I hate Java code"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
tfidf = TfidfVectorizer(stop_words='english', norm=None)
tfidf_matrix = tfidf.fit_transform(df['text'])
df_dtm = pd.DataFrame(tfidf_matrix.toarray(),
 index=df['review'].values,
 columns=tfidf.get_feature_names())
df_dtm"""
    return s
def sentiment():
    s="""import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# reading and wragling data
df_avatar = pd.read_csv('avatar.csv', engine='python')
df_avatar_lines = df_avatar.groupby('character').count()
df_avatar_lines = df_avatar_lines.sort_values(by=['character_words'], ascending=False)[:10]
top_character_names = df_avatar_lines.index.values
# filtering out non-top characters
df_character_sentiment = df_avatar[df_avatar['character'].isin(top_character_names)]
df_character_sentiment = df_character_sentiment[['character', 'character_words']]
# calculating sentiment score
sid = SentimentIntensityAnalyzer()
df_character_sentiment.reset_index(inplace=True, drop=True)
df_character_sentiment[['neg', 'neu', 'pos', 'compound']] =
df_character_sentiment['character_words'].apply(sid.polarity_scores).apply(pd.Series)
df_character_sentimen"""
    return s
def wordcloud():
    s="""from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = "wordcloud implementation example text"
wordcloud = WordCloud(width=800, height=400, background_color='white')
wordcloud.generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()"""
    return s
def stopwords():
    s="""import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
print(sw_nltk)
print(len(sw_nltk))
text = "When I first met her she was very quiet. She remained quiet during the entire two hour long
journey from Stony Brook to New York."
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)
print("Old length: ", len(text))
print("New length: ", len(new_text))"""
    return s
def wordnet():
    s="""import nltk
from nltk.corpus import wordnet
synonyms = []
antonyms = []
for synset in wordnet.synsets("evil"):
 for l in synset.lemmas():
 synonyms.append(l.name())
 if l.antonyms():
 antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))"""
    return s

