from sys import argv

file_name = argv[1]
def count_words(file_name):
    """Take name of text file, returns None.
        Counts occurence of each word.
    """
    # each word is the key, value is the count of that word
    word_count = {}
    # open a text file
    with open(file_name) as in_file:
        for line in in_file:
            words = line.split()
            for word in words:
                word = word.lower()
                word = word.replace('.', '').replace(',', '').replace('?', '')
                # make sure the word isn't already in the word_count dict
                if word not in word_count:
                    word_count[word] = 1
                # word is already in the word_count dict, so increment value by one
                else:
                    word_count[word] += 1

    #print word_count
    for word, count in word_count.items():
        print word, count

count_words(file_name)