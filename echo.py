import nltk
nltk.download('words')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import word_tokenize, pos_tag, ne_chunk
from itertools import chain
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet









class MoodJudgement:
    def __init__(self):
        self.input_array = []
        self.very_common_words = []
        self.positive_sentiments = []
        self.negative_sentiments = []
        self.medium_sentiments = []
        self.sad_sentiments = []
        self.mad_sentiments = []

    def get_input(self):
        for i in range(1):
            self.input_array.append(input("Tell me about your day: "))

    def ner(self):
        for text in self.input_array:
            tokens = nltk.word_tokenize(text)
            pos_tags = nltk.pos_tag(tokens)
            named_entities = nltk.ne_chunk(pos_tags)
            print(named_entities)

    def tokenize_input(self):
        self.tokens = [word_tokenize(i) for i in self.input_array]
        self.more_tokens = [sent_tokenize(i) for i in self.input_array]
        self.flattened_tokens = list(chain.from_iterable(self.tokens))
        self.tagged_tokens = pos_tag(self.flattened_tokens)

    def sentiment_analysis(self):
        text = " ".join(self.flattened_tokens)
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        print(sentiment)
        if sentiment['compound'] > 0.7:
            self.positive_sentiments.append("good mood")
        elif sentiment['compound'] < -0.7:
            self.negative_sentiments.append("bad mood")
        elif sentiment['compound'] >= -0.7 and sentiment['compound'] <= 0.7:
            self.medium_sentiments.append("medium mood")
        print(self.positive_sentiments)
        print(self.negative_sentiments)
        print(self.medium_sentiments)

    def get_common_words(self):
        word_count = Counter(self.flattened_tokens)
        for word, count in word_count.most_common(10):
            print(f'{word}: {count}')

        for word, count in word_count.most_common(5):
            self.very_common_words.append(word)
        print(self.very_common_words)

    def talkative(self):
        if len(self.flattened_tokens) > 10:
            print('Talkative')
        elif len(self.flattened_tokens) < 10:
            print('Not Talkative')

    
            
    def pos_tag_count(self):
        tag_count = Counter([tag for token, tag in self.tagged_tokens])
        print(tag_count)









#run
mood_judgement = MoodJudgement()
mood_judgement.get_input()
mood_judgement.tokenize_input()
mood_judgement.pos_tag_count()
mood_judgement.sentiment_analysis()
mood_judgement.get_common_words()
mood_judgement.talkative()
#mood_judgement.sad_analysis()
mood_judgement.ner()
