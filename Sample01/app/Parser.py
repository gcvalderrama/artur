class Parser:

    def __get_words(self, target):
        return target.split(" ")

    def __get_representation(self, words):
        state = dict()
        for word in words:
            if word not in state:
                state[word] = 1
            else:
                state[word] += 1
        return state

    def get_most_reapeated_word(self, target):
        words = self.__get_words(target)
        state = self.__get_representation(words)

        state_sorted = sorted(state.items(), key=lambda tuple: tuple[1], reverse=True)

        return state_sorted[0][0]

    def get_unique_words(self, target: str):
        words = self.__get_words(target)
        state = self.__get_representation(words)
        return len(state.keys())
