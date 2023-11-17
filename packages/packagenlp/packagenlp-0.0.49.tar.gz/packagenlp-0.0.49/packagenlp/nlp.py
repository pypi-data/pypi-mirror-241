import pandas as pd
import re


import logging


import treetaggerwrapper
from unidecode import unidecode
from importlib.resources import files

from packagenlp import logging_config




class NLP:

    def __init__(self):
        logging_config.setup_logging()
        logging.info("Initialisation de la classe NLP.")
        
        resource_container = files("packagenlp")
        
        try:
            with resource_container.joinpath("data/stopWords_spacy_fr.csv").open('r', encoding='utf-8') as file:
                self.stopwords_fr = pd.read_csv(file, sep=';', encoding='utf-8')['word'].tolist()
                logging.info("Stopwords français chargés avec succès.")
        except (FileNotFoundError, PermissionError) as e:
            logging.error(f"Erreur lors du chargement du fichier des stopwords français: {e}")
            self.stopwords_fr = []
    
        try:
            with resource_container.joinpath("data/stopWords_spacy_en.csv").open('r', encoding='utf-8') as file:
                self.stopwords_en = pd.read_csv(file, sep=';', encoding='utf-8')['word'].tolist()
                logging.info("Stopwords anglais chargés avec succès.")
        except (FileNotFoundError, PermissionError) as e:
            logging.error(f"Erreur lors du chargement du fichier des stops words anglais: {e}")
            self.stopwords_en = []

 
        
    def cleanStopWord(self, text, langue='', add_stopwords=[], remove_stopwords=[]):
        logging.info(f"Nettoyage des mots d'arrêt pour la langue : {langue}")
        try:
            
            
            if langue == 'fr':             
                stopwords = [word for word in self.stopwords_fr if word not in remove_stopwords]
            elif langue == 'en': 
                stopwords = [word for word in self.stopwords_en if word not in remove_stopwords]
            else:
                raise ValueError("Invalid language for text.")

            stopwords.extend(add_stopwords)
            logging.debug(f"Stopwords supplémentaires ajoutés : {add_stopwords}")
            logging.debug(f"Stopwords supprimés : {remove_stopwords}")
            
            tokens = text.split(' ')
            cleaned_text = ' '.join([token for token in tokens if token.lower() not in stopwords])
            logging.info("Nettoyage des mots d'arrêt terminé.")
            return cleaned_text

        except Exception as e:
            logging.error(f"Erreur lors du nettoyage des stopwords: {e}")
            return text

    def cleanText(self, text, keep_numbers=True, exception='', remove_accent=True, lowercase=True):
        logging.info("Nettoyage du texte commencé.")
        try:
            

            if remove_accent:
                text = unidecode(text)
                logging.debug("Accents retirés du texte.")

            if lowercase:
                text = text.lower()
                logging.debug("Texte converti en minuscules.")

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
            logging.debug(f"Expression régulière utilisée pour le nettoyage: {regex_pattern}")

            cleaned_text = pattern.sub(' ', text)
            cleaned_text = cleaned_text.strip()

            logging.info("Nettoyage du texte terminé.")
            return cleaned_text
   
        except Exception as e:
            logging.error(f"Erreur lors du nettoyage du texte: {e}")
            return text


    def lemmatisation(self, text, lemma_exclu, langue='', keep_numbers=True, keep_type_word=[]):
        logging.info(f"Début de la lemmatisation pour la langue : {langue}")
        try:
            
        

            try:
                if langue == 'fr':
                    tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGDIR='C:\\TreeTagger\\TreeTagger')
                elif langue == 'en':
                    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGDIR='C:\\TreeTagger\\TreeTagger')
                else:
                    raise ValueError("Invalid language for text.")
            except treetaggerwrapper.TreeTaggerError as e:
                logging.error(f"Erreur lors de l'initialisation de TreeTagger pour la langue {langue}: {e}")
                return ""

            tokenisation_majuscule = list()
            majuscule_tokenised = ''
            tags = tagger.tag_text(str(text), nosgmlsplit=True)
            for tag in tags:
                word, mottag, lemma = tag.split()
                if len(lemma.split('|')) > 1:
                    lemma = lemma.split('|')[0]
                if word in lemma_exclu.keys():
                    lemma = lemma_exclu[word]
                if keep_numbers and mottag == 'NUM':
                    lemma = word
                    pos = mottag.split(':')[0]
                if keep_type_word == [] or pos in keep_type_word:
                    majuscule_tokenised = majuscule_tokenised + ' ' + lemma

            tokenisation_majuscule.append(majuscule_tokenised)
            
            lemmatized_text = ' '.join(tokenisation_majuscule)
            logging.info("Lemmatisation terminée.")
            return lemmatized_text.strip()

        except Exception as e:
            logging.error(f"Erreur lors de la lemmatisation: {e}")
            return text

