#goal is to create a library that will aid in nlp

#``````````````

#this library will create a way for the program to memorize relevant things about the user
#based on input and create a sense of friendship

#``````````````

#input then send to box
#how to create memory
#long term or short term memory
#input must then be understood as it grows and then correct response
#response will come from somewhere
#input will trigger response and response will be related to input, friendly relationship
#will listen and respond
#will listen and learn about user from inputs and respond and become their friend





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


#input

input_array = []

for i in range(10):
    input_array.append(input("Enter a value: "))
    
tokens = [word_tokenize(i) for i in input_array]
tokens2 = [sent_tokenize(i) for i in input_array]
flattened_tokens = list(chain.from_iterable(tokens))
tagged_tokens = pos_tag(flattened_tokens)
tag_count = Counter([tag for token, tag in tagged_tokens])
print(tag_count) #count of pos tags and which occur most frequently

text = " ".join(flattened_tokens)
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(text)
print(sentiment) #judges sentiment vaguely


#goal is to create a friendship, regardless of if the input is good or bad i think
#goal is to now use the their mood and tempo to respond better.
