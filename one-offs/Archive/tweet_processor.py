from stop_words import get_stop_words
import re
from collections import defaultdict
import snowballstemmer

class TweetProcessor:

    def __init__(self):

        self.stops = get_stop_words('en')
        self.stemmer = snowballstemmer.EnglishStemmer()
        self.hashtag_pattern = re.compile(r'(#[a-zA-Z_]+)')
        self.processed_hashtags = {}



    def clean_text(self, text):
        text = str(text)
        text = self.split_hashtags(text)

        #repeat splitting hashtags to go back and check for any non-camelcase hashtags that missed out on camelcase processed version
        text = self.split_hashtags(text)

        text = re.sub('(https?://)?(www\.)?[a-zA-Z\d]+\.((com?)|(gov?)|(org)|(net)|(co\.uk))((/[a-zA-Z0-9_\-]+)+)?', ' ', text)
        text = re.sub('&[a-zA-Z]+;', ' ', text)
        text = re.sub('\\n', ' ', text)
        text = re.sub('@[a-zA-Z0-9_]+', " ", text)
        text = re.sub(r'\s[a-zA-Z]\s', ' ', text)
        text = re.sub(r'\d', ' ', text)
        text = re.sub(r'[^A-Za-z]|[;:\"\']', ' ', text)
        text = re.sub('_', ' ', text)
        text = text.lower()
        text = re.sub('^rt', ' ', text)
        text = re.sub('&amp;',' ', text)
        text = [word for word in str(text).lower().split() if word not in self.stops]

        return text



    def make_sparse(self, texts, threshold = 1):

        frequency = defaultdict(int)
        for i in range(len(texts)):
            for token in texts[i]:
                frequency[token] += 1

        texts = [[token for token in text if frequency[token] > threshold] for text in texts]
        return texts

    def stem_text(self, word_list):

        stemmed_text = self.stemmer.stemWords(words=word_list)
        return stemmed_text

    def re_string(self, text_list):
        string = ''
        for word in text_list:
            string += ' ' + word

        return string

    def split_hashtags(self, text):
        hashtags = self.hashtag_pattern.findall(text)
        final_text = str(text)

        for hashtag in hashtags:

            #remove '#'
            hashtag = hashtag[1:]

            #check if hashtag was already processed before
            #this accounts for non camelcase versions of hashtags previously labelled
            if hashtag.lower() in self.processed_hashtags.keys():
                string = self.processed_hashtags[hashtag.lower()]
                final_text = re.sub('#' + hashtag, string, final_text)
                continue

            #if separated by _ then just split on _ and make spaces
            elif '_' in hashtag:
                split_hash = hashtag.split('_')
                string = ''
                for token in split_hash:
                    string += ' ' + token
                    final_text = re.sub(hashtag, string, final_text)

            #if no camel case then we move on
            elif hashtag.islower() or hashtag.isupper():
                continue

            else:
                tokens = []
                current_token = ''

                #iterate thru letters
                for index in range(len(hashtag)):

                    if re.match(r'[0-9]', hashtag[index]):
                        pass

                    #if current string empty just get it started or if current letter lowercase just add
                    elif current_token == '' or hashtag[index].islower():
                        current_token += hashtag[index]

                    #if current letter capital letter
                    elif hashtag[index].isupper():

                        # and if last letter was capital as well assume acronym and keep moving
                        if hashtag[index-1].isupper():

                            #unless its the last capital letter before lowercases then assume its start of new word after acronym
                            if index < len(hashtag) - 1 and hashtag[index + 1].islower():

                                #that is unless the next couple lowercase letters are 'of' because then its just lowercase on purpose
                                if index < len(hashtag) - 3 and (hashtag[index+1:index+3] == 'of' or hashtag[index+1:index+3] == 'in'):
                                    current_token += hashtag[index]
                                    tokens.append(current_token)
                                    current_token = ''

                                else:
                                    tokens.append(current_token)
                                    current_token = hashtag[index]

                            else:
                                current_token += hashtag[index]

                        #otherwise start new token
                        else:
                            tokens.append(current_token)
                            current_token = hashtag[index]

                    else:
                        tokens.append(current_token)

                tokens.append(current_token)
                string = ''
                for token in tokens:
                    string += ' ' + token

                final_text = re.sub('#' + hashtag, string, final_text)
                self.processed_hashtags[hashtag.lower()] = string

        return final_text
