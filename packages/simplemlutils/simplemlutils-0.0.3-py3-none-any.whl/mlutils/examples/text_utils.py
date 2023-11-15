from mlutils.utils.textutils import BagOfWords


if __name__ == '__main__':
    tokens = ['It', 'has', 'also', 'arisen', 'in', 'criminal', 'justice', ',',
              'healthcare', ',', 'and', 'hiring', ',', 'compounding', 'existing',
              'racial', ',', 'economic', ',', 'and', 'gender', 'biases', '.']

    bow = BagOfWords()
    bow.add_tokens(tokens)
    print(bow.most_common(3))