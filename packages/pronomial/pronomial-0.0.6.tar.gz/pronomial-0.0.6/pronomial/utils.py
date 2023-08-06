from os.path import join, dirname, isfile
import csv
import nltk
import pickle

from pronomial.lang.pt import pos_tag_pt
from pronomial.lang.en import pos_tag_en, is_plural_en
from pronomial.lang.es import pos_tag_es
from pronomial.lang.ca import pos_tag_ca

from nltk.tokenize import word_tokenize as _wt


def word_tokenize(text, lang="en"):
    try:
        return _wt(text)
    except LookupError:
        nltk.download("punkt")
        return _wt(text)


def pos_tag(text, lang="en"):
    if lang.startswith("en"):
        return pos_tag_en(text)
    if lang.startswith("pt"):
        return pos_tag_pt(text)
    if lang.startswith("es"):
        return pos_tag_es(text)
    if lang.startswith("pt"):
        return pos_tag_ca(text)
    raise NotImplementedError


def _get_features(name):
    return {
        'suffix1': name[-1],
        'suffix2': name[-2:],
        'suffix3': name[-3:],
        'suffix4': name[-4:],
        'suffix5': name[-5:]
    }


def train_gender_classifier(path):
    dataset = join(dirname(__file__), "res", "names.csv")
    with open(dataset) as f:
        names = [tuple(line) for line in csv.reader(f)]
    train_data = [(_get_features(n), g) for (n, g) in names]
    clf = nltk.NaiveBayesClassifier.train(train_data)
    path = path or join(dirname(__file__), "res", "name_gender.pkl")
    with open(path, "wb") as f:
        pickle.dump(clf, f)
    return clf


def load_gender_classifier(path=None):
    path = path or join(dirname(__file__), "res", "name_gender.pkl")
    if not isfile(path):
        train_gender_classifier(path)
    with open(path, "rb") as f:
        tagger = pickle.load(f)
    return tagger


GENDER = load_gender_classifier()


def predict_gender(word, text="", lang="en"):
    gender = None
    if lang.startswith("en"):
        from pronomial.lang.en import GENDERED_WORDS_EN
        for k, v in GENDERED_WORDS_EN.items():
            if word.lower() in v:
                gender = k
                break
    if lang.startswith("pt"):
        from pronomial.lang.pt import predict_gender_pt
        gender = predict_gender_pt(word, text)
    if lang.startswith("es"):
        from pronomial.lang.es import predict_gender_es
        gender = predict_gender_es(word, text)
    if lang.startswith("ca"):
        from pronomial.lang.ca import predict_gender_ca
        gender = predict_gender_ca(word, text)

    return gender or GENDER.classify(_get_features(word))


def is_plural(text, lang="en"):
    if lang.startswith("en"):
        return is_plural_en(text)
    return text.endswith("s")
