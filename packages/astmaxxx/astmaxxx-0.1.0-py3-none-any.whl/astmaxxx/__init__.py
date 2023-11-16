def sentiment():
    s="""
import pandas as pd
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
df_avatar = pd.read_csv('/content/avatar.csv',  encoding= 'unicode_escape')
df_avatar_lines = df_avatar.groupby('character').count()
df_avatar_lines = df_avatar_lines.sort_values(by=['character_words'], ascending=False)[:10]
top_character_names = df_avatar_lines.index.values
df_character_sentiment = df_avatar[df_avatar['character'].isin(top_character_names)]
df_character_sentiment = df_character_sentiment[['character', 'character_words']]
sid = SentimentIntensityAnalyzer()
df_character_sentiment.reset_index(inplace=True, drop=True)
df_character_sentiment[['neg', 'neu', 'pos', 'compound']] = df_character_sentiment['character_words'].apply(sid.polarity_scores).apply(pd.Series)
df_character_sentiment
"""
    return s

def ner():
    s="""
import spacy
from spacy import displacy
NER = spacy.load("en_core_web_sm")
raw_text="The Indian Space Research Organisation is the national space agency of India,headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
text1= NER(raw_text)
for word in text1.ents:
 print(word.text,word.label_)
"""
    return s

def stemlem():
    s="""
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
print("STEMMING RESULTS")
for w in tokenization:
  print("Stem Word for {} is {}".format(w,stemmer.stem(w)))

print("\nLEMMATIZATION RESULTS")
for w in tokenization:
  print("Lemma for {} is {}".format(w, lemmatizer.lemmatize(w)))
"""
    return s


def bag():
    s="""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
text = ["I love writing code in Python. I love Python code",
        "I hate writing code in Java. I hate Java code"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
cv = CountVectorizer(stop_words='english')
cv_matrix = cv.fit_transform(df['text'])
df_dtm = pd.DataFrame(cv_matrix.toarray(),
                      index=df['review'].values,
                      columns=cv.get_feature_names_out())
df_dtm
"""

    return s

def tfidf():
    s="""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
text = ["I love writing code in Python. I love Python code",
 "I hate writing code in Java. I hate Java code"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
tfidf = TfidfVectorizer(stop_words='english', norm=None)
tfidf_matrix = tfidf.fit_transform(df['text'])
df_dtm = pd.DataFrame(tfidf_matrix.toarray(),
 index=df['review'].values,
 columns=tfidf.get_feature_names_out())
df_dtm
"""

    return s

def stop():
    s="""
import nltk
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
print(sw_nltk)
print(len(sw_nltk))
text = "When I first met her she was very quiet. She remained quiet during the entire two hour long journey from Stony Brook to New York."
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)
print("Old length: ", len(text))
print("New length: ", len(new_text))
"""
    return s

def pos():
    s="""
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
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
tokenized = sent_tokenize(txt)

for i in tokenized:

 wordsList = nltk.word_tokenize(i)
 # removing stop words from wordList
 wordsList = [w for w in wordsList if not w in stop_words]
 # Using a Tagger. Which is part-of-speech
 # tagger or POS-tagger.
 tagged = nltk.pos_tag(wordsList)
 print(tagged)
"""
    return s

def chunk():
    s="""
import nltk
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
print(Output)
"""
    return s

def wordnet():
    s="""
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
synonyms = []
antonyms = []
for synset in wordnet.synsets("bad"):
 for l in synset.lemmas():
  synonyms.append(l.name())
  if l.antonyms():
    antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))
"""
    return s

def cloud():
    s="""
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
class WordCloudGeneration:
  def preprocessing(self, data):
# convert all words to lowercase
    data = [item.lower() for item in data]
# load the stop_words of english
    stop_words = set(stopwords.words('english'))
 # concatenate all the data with spaces.
    paragraph = ' '.join(data)
 # tokenize the paragraph using the inbuilt tokenizer
    word_tokens = word_tokenize(paragraph)
 # filter words present in stopwords list
    preprocessed_data = ' '.join([word for word in word_tokens if not word in stop_words])
    print("\n Preprocessed Data: " ,preprocessed_data)
    return preprocessed_data
  def create_word_cloud(self, final_data):
 # initiate WordCloud object with parameters width, height, maximum font size and background color
 # call the generate method of WordCloud class to generate an image
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200,
    background_color="black").generate(final_data)
 # plt the image generated by WordCloud class
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
wordcloud_generator = WordCloudGeneration()
# you may uncomment the following line to use custom input
# input_text = input("Enter the text here: ")
input_text ='''
Lionel Messi is one of the greatest football players of all time. He has achieved many remarkable feats in his career, both with his clubs and his national team. Here is a paragraph on some of his achievements:
Lionel Messi has won a record seven Ballon d'Or awards, the most prestigious individual honor in football. He has also won six Golden Shoes, awarded to the top scorer in Europe's top leagues. He is the all-time top scorer in La Liga, with over 450 goals, and in the UEFA Champions League, with over 120 goals. He has won 34 trophies with FC Barcelona, including four Champions League titles and 10 La Liga titles. He has also won three FIFA Club World Cups and three UEFA Super Cups with Barcelona. In 2023, he joined Inter Miami CF in the Major League Soccer, where he won the Leagues Cup in his first season. With Argentina, he has won the Copa América in 2021 and the FIFA World Cup in 2022, where he was also awarded the Golden Ball as the best player of the tournament. He is Argentina's most capped player and top scorer, with over 170 appearances and over 100 goals¹²³⁴.
'''
input_text = input_text.split('.')
clean_data = wordcloud_generator.preprocessing(input_text)
wordcloud_generator.create_word_cloud(clean_data)

"""
    return s