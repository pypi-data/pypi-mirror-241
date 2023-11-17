import setuptools

setuptools.setup(
    name="packagenlp",
    packages=['packagenlp'],
    version="0.0.50",
    author="Business & Decision",
    description="A package for NLP",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["NLP", "Français", "Langues", "Traitements"],
    download_url="https://gitlab.com/business-decision-data-science/packagenlp/-/package_files/82622627/download",
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'nltk',
        'spacy',
        'unidecode',
        'treetaggerwrapper',
        'streamlit',
        'plotly',
        'wordcloud'
    ],
    include_package_data=True,
    package_data={'packagenlp': ['data/stopWords_spacy_en.csv', 'data/stopWords_spacy_fr.csv', 'data/image.jpg', 'data/Logo_B_D.png', 'resources/TreeTagger.zip']},
)

# Code pour décompresser le fichier après l'installation
import os
import shutil
import zipfile

treetagger_zip = os.path.join(os.path.dirname(__file__), 'packagenlp', 'resources', 'TreeTagger.zip')
target_dir = 'C:\\TreeTagger'  # Répertoire d'installation cible

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    with zipfile.ZipFile(treetagger_zip, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

