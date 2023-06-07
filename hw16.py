def first_word(sentence: str) -> str:
    sentence = sentence.replace('.', ' ')
    sentence = sentence.replace(',', ' ')
    words = sentence.split()
    for word in words:
        return words[0]
