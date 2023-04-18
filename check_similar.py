# given two lists of strings, return a list of most similar strings
# from the second list to the first list

# import difflib
# import nltk
from nltk.corpus import wordnet as wn

def most_similar(list1, list2):
    # use wordnet to get the synsets of the words in the lists
    synsets1 = [wn.synsets(word) for word in list1]
    synsets2 = [wn.synsets(word) for word in list2]
    # compare the synsets of the words in the lists
    # and return the most similar words from list2
    most_similar = []
    for synset1 in synsets1:
        for synset2 in synsets2:
            if synset1 and synset2:
                if synset1[0].wup_similarity(synset2[0]) > 0.5:
                    most_similar.append(synset2[0].name().split('.')[0])
    return most_similar

if __name__ == '__main__':
    list1 = ['hello', 'laptop', 'colorful']
    list2 = ['hi', 'earth', 'vibrant']
    print(most_similar(list1, list2))