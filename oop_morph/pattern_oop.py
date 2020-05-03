class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self, path_to_corpus):
        pass


class Sentence:
    def __init__(self, wordforms):
        self._wordforms = wordforms


class Wordform:

    def __init__(self, grammems):
        self._grammems = grammems

