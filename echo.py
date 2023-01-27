

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from itertools import chain
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter














#input      


def moodJudgement():







    input_array = []
    very_common_words = []
    positive_sentiments = []
    negative_sentiments = []

    for i in range(1):
        input_array.append(input("tell me about your day:       "))

    
    tokens = [word_tokenize(i) for i in input_array]#tokens
    more_tokens = [sent_tokenize(i) for i in input_array] #seperate variable for tokens
    flattened_tokens = list(chain.from_iterable(tokens))#flattened tokens
    tagged_tokens = pos_tag(flattened_tokens)#pos tagged tokens
    tag_count = Counter([tag for token, tag in tagged_tokens])#count for pos tags
    print(tag_count) #count of which occur most frequently

    
    text = " ".join(flattened_tokens)#flattened tokens turned back into text
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(sentiment) #judges sentiment vaguely, the 1 is positive, and -1 is negative


    #asume that 'flattened_tokens' is a list of tokenized words
    word_count = Counter(flattened_tokens)
    #print the 10 most common words and their frequency
    for word, count in word_count.most_common(10):
        print(f'{word}: {count}')

    
    # Iterate over the word count dictionary
    for word, count in word_count.most_common(5):
    # Add the word to the very_common_words list
        very_common_words.append(word)
    print(very_common_words)

    
    if sentiment['compound'] > 0:
        positive_sentiments.append("good mood")
    print(positive_sentiments)


    if sentiment['compound'] < 0:
        negative_sentiments.append("bad mood")
    print(negative_sentiments)


    #try to identify sadness

    #try to indentify nervousnesss















moodJudgement()
#improve what we have ?
