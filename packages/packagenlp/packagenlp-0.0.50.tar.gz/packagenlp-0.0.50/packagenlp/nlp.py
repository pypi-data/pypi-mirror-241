import pandas as pd
import re
import treetaggerwrapper
from unidecode import unidecode
from importlib.resources import files

class NLP:

    def __init__(self):
        resource_container = files("packagenlp")
        

        try:
            with resource_container.joinpath("data/stopWords_spacy_fr.csv").open('r', encoding='utf-8') as file:
                self.stopwords_fr = pd.read_csv(file, sep=';', encoding='utf-8')['word'].tolist()
        except (FileNotFoundError, PermissionError) as e:
            self.stopwords_fr = []
            print(f"Erreur lors du chargement du fichier des stopwords français: {e}")
        

        try:
            with resource_container.joinpath("data/stopWords_spacy_en.csv").open('r', encoding='utf-8') as file:
                self.stopwords_en = pd.read_csv(file, sep=';', encoding='utf-8')['word'].tolist()
        except (FileNotFoundError, PermissionError) as e:
            self.stopwords_en = []
            print(f"Erreur lors du chargement du fichier des stops words anglais: {e}")

    def cleanStopWord(self, text, langue='', add_stopwords=[], remove_stopwords=[]):
        try:
            if langue == 'fr':             
                stopwords = [word for word in self.stopwords_fr if word not in remove_stopwords]
            elif langue == 'en': 
                stopwords = [word for word in self.stopwords_en if word not in remove_stopwords]
            else:
                raise ValueError("Langue invalide pour le texte.")

            stopwords.extend(add_stopwords)
            tokens = text.split(' ')
            cleaned_text = ' '.join([token for token in tokens if token.lower() not in stopwords])
            return cleaned_text

        except Exception as e:
            print(f"Erreur lors du nettoyage des stopwords: {e}")
            return text

    def cleanText(self, text, keep_numbers=True, exception='', remove_accent=True, lowercase=True):
        try:
            if remove_accent:
                text = unidecode(text)

            if lowercase:
                text = text.lower()

            regex_pattern = ''
            if keep_numbers and exception:
                regex_pattern = '[^A-Za-z0-9\xe0-\xff '+exception+']'
            elif keep_numbers:
                regex_pattern = '[^A-Za-z0-9\xe0-\xff]'
            elif exception:
                regex_pattern = '[^A-Za-z\xe0-\xff '+exception+']'
            else:
                regex_pattern = '[^A-Za-z\xe0-\xff]'

            pattern = re.compile(regex_pattern)
            cleaned_text = pattern.sub(' ', text)
            cleaned_text = cleaned_text.strip()
            return cleaned_text
   
        except Exception as e:
            print(f"Erreur lors du nettoyage du texte: {e}")
            return text

    def lemmatisation(self, text, lemma_exclu, langue='', keep_numbers=True, keep_type_word=[]):
        try:
            if langue == 'fr' : 
                tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR='C:\TreeTagger')
            elif langue == 'en' : 
                tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGDIR='C:\TreeTagger')
            else : 
                raise ValueError("Invalid langue for text.")
            tokenisation_majuscule = list()
            majuscule_tokenised = ''
            tags = tagger.tag_text(str(text), nosgmlsplit=True)
            for tag in tags:
                word, mottag, lemma = tag.split()
                if len(lemma.split('|')) > 1:
                    lemma = lemma.split('|')[0]
                if word in lemma_exclu.keys():
                    lemma = lemma_exclu[word]
                if keep_numbers:
                    if mottag == 'NUM':
                        lemma = word
                pos = mottag.split(':')[0]
                if keep_type_word == [] : 
                    majuscule_tokenised = majuscule_tokenised + ' ' + lemma
                else : 
                    if pos in keep_type_word:
                        majuscule_tokenised = majuscule_tokenised + ' ' + lemma


            tokenisation_majuscule.append(majuscule_tokenised)

            lemmatized_text = ' '.join(tokenisation_majuscule)
            return lemmatized_text.strip()  

        except Exception as e:
            print(f"Erreur lors de la lemmatisation: {e}")
            return text

