class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    skip_initial = []

    def __init__(self, path):
        """ Creates an instance of WordFinder which takes the words
            from the path
        """
        self.list_of_words = self.read_words(path)

    def read_words(self, path):
        """ Reads the words from the file from the path and returns 
            a list of words
        """
        file = open(path)

        words = [
                word.strip()
                for word in file
                if self.not_starts_with(word.strip())
            ]

        # for word in file:
        #     if self.not_starts_with(word):
        #         words.append(word.strip())

        file.close()

        print(f"{len(words)} words read")

        return words

    def not_starts_with(self, word):
        """ Check whether the word starts with any of the values
            in the skip_initial list or is empty
        """
        if not word:
            return False
        
        for value in self.skip_initial:
            if word.startswith(value):
                return False

        return True

    def random(self):
        """ Returns a random word from the list_of_words
            property of the instance
        """

        from random import choice

        return choice(self.list_of_words)


class SpecialWordFinder(WordFinder):
    """ Works like a WordFinder instance but ignores blank lines and
        hash symbols (comment lines)
    """
    skip_initial = ['#']

    # def __init__(self, path):
    #     """ Creates an instance of SpecialWordFinder which takes the words
    #         from the path, ignores new lines and comment lines
    #     """
    #     self.list_of_words = super().read_words(path, ['#', '\n'])
