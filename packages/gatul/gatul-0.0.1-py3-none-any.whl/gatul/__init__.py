def ner():
    s = '''
import spacy
from spacy import displacy
NER = spacy.load("en_core_web_sm")
raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
text1= NER(raw_text)
for word in text1.ents:
    print(word.text,word.label_)'''
    return s

def stem():
    s = '''
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Stemming for {} is {}".format(w,porter_stemmer.stem(w)))'''
    return s

def lem():
    s = '''
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
text = "learning the language python"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))'''
    return s

def bag():
    s = '''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
text = ["I love having fun. I love eating","I hate coming class. I hate love"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
cv = CountVectorizer(stop_words='english')
cv_matrix = cv.fit_transform(df['text'])
df_dtm = pd.DataFrame(cv_matrix.toarray(),
                      index=df['review'].values,
                      columns=cv.get_feature_names())
df_dtm'''
    return s

def tfdf():
    s = '''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
text = ["I love to drinking milkshake. I love chocolate shake","I hate vegetable juice. I hate drinking juice"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
tfidf = TfidfVectorizer(stop_words='english', norm=None)
tfidf_matrix = tfidf.fit_transform(df['text'])
df_dtm = pd.DataFrame(tfidf_matrix.toarray(),
                      index=df['review'].values,
                      columns=tfidf.get_feature_names())
df_dtm'''
    return s

def stopwords():
    s = '''
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
print(sw_nltk)
print(len(sw_nltk))
text = "The traveler is initially hesitant to give the twelfth beggar anything, but he then decides to give him the lair of his clothes. The beggar is overjoyed by this gift, and he immediately begins to put on the traveler's clothes."
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)
print("Old length: ", len(text))
print("New length: ", len(new_text))'''
    return s

def chuncking():
    s = """
import nltk
sentence = [("the", "DT"),("book", "NN"),("has","VBZ"),("many","JJ"),("chapters","NNS")]
chunker = nltk.RegexpParser(r'''NP:
{<DT><NN.*><.*>*<NN.*>}
}<VB.*>{ 
''')
chunker.parse(sentence)
Output = chunker.parse(sentence)
print(Output)"""
    return s

def pos():
    s = '''
import nltk
from nltk import word_tokenize
s="hi ,i am going to school"
print (nltk.pos_tag(word_tokenize(s)))'''
    return s

def wordnet():
    s = '''
import nltk
from nltk.corpus import wordnet
synonyms = []
antonyms = []
for synset in wordnet.synsets("standard"):
    for l in synset.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))'''
    return s

def wordcloud():
    s = '''
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python is a high-level programming language that is versatile and easy to learn. It is widely used for web development, data analysis, artificial intelligence, and more."

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()
'''
    return s

def sentiment():
    s = '''
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(review):
    nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)

    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

review = "Overall experience of the movie was neutral"
result = analyze_sentiment(review)
print(f"Sentiment: {result}")
'''
    return s



