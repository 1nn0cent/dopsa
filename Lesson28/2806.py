class MinMaxWordFinder:
    def __init__(self):
        self.sentences = []
        self.words = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)
        self.words.extend(sentence.split())

    def shortest_words(self):
        if not self.words:
            return []
        min_length = min(len(word) for word in self.words)
        shortest = [word for word in self.words if len(word) == min_length]
        return sorted(shortest)

    def longest_words(self):
        if not self.words:
            return []
        max_length = max(len(word) for word in self.words)
        longest = {word for word in self.words if len(word) == max_length}  
        return sorted(longest)
    
if __name__ == "__main__":      
    finder = MinMaxWordFinder()
    finder.add_sentence('hello')
    finder.add_sentence(' abc def ')
    finder.add_sentence('world')
    finder.add_sentence(' abc ')
    finder.add_sentence('asdf')
    finder.add_sentence('qwert')
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))