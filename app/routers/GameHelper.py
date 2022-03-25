import wordle




def getRandomWord():

    word = wordle.Wordle(word = wordle.random_answer(), real_words = True).word
    return word


if __name__ == "__main__":
    print(getRandomWord())
