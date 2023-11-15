import pandas as pd
import seaborn as sns
from nltk.probability import FreqDist
from nltk import pos_tag
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

class TextAnalysis:
    def __init__(self, comments:str):
        self.comments = comments

    def prepare_nouns(self):
        all_words = []
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('averaged_perceptron_tagger')
        for comment in self.comments:
            tokens = word_tokenize(comment)
            all_words.extend(tokens)
        stop_words = set(stopwords.words('english'))
        filtered_words = [word.lower() for word in all_words if
                          word.isalnum() and word.lower() not in stop_words]
        nouns = [word for (word, tag) in pos_tag(filtered_words) if tag.startswith('N')]
        return nouns
    
    def prepare_word_freq(self, nouns) -> pd.DataFrame:
        noun_counts = FreqDist(nouns)
        df_word_freq = pd.DataFrame(list(noun_counts.items()), columns=['Nouns', 'Frequency'])
        df_word_freq = df_word_freq.sort_values(by='Frequency', ascending=False)
        return df_word_freq

    def plot_freq(self, df_word_freq, num_dis: int = 10):
        sns.set(style="white")
        top_words = df_word_freq.head(num_dis)
        plt.figure(figsize=(10, 4))
        sns.barplot(x='Nouns', y='Frequency', data=top_words)
        plt.title("Top 10 Words Frequency")
        plt.xticks(rotation=45)
        sns.despine()
        plt.show()

    def plot_wordcloud(self, nouns):
        sns.set(style="white")
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(nouns))
        plt.figure(figsize=(10, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()