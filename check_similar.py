# given two lists of strings, return a list of most similar strings
# from the second list to the first list

import difflib
import nltk
from nltk.corpus import wordnet as wn

def similar_within_list(tag_list):
    # use difflib to get the most similar words in the list
    most_similar = []
    for i in range(len(tag_list)):
        for j in range(i+1, len(tag_list)):
            if difflib.SequenceMatcher(None, tag_list[i], tag_list[j]).ratio() > 0.8:
                print(tag_list[i], tag_list[j])

    return most_similar

def find_root(tag_list):
    # use nltk to get the root of the words in the list
    root_list = []
    for tag in tag_list:
        root_list.append(nltk.stem.WordNetLemmatizer().lemmatize(tag, 'v'))
    return root_list

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
    f = open("tags-processed-final.txt", "r")
    lines = f.readlines()
    f.close()

    list1 = lines[0].split(',')
    # list2 = ['hi', 'earth', 'vibrant']
    print(similar_within_list(list1))