import os
import sys

from nltk.corpus import wordnet
import nltk

from keyword_intersect import build_dic, write_dic

nltk.download('wordnet')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Input parameter is missing")
    first = sys.argv[1]
    if not os.path.isfile(first):
        raise ValueError("Input file path is not correct")
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
    else:
        output_filename = "keywords"

    first_dic = build_dic(first)
    syn_dic = dict()
    for key in first_dic.keys():
        synonyms = set()
        for word in first_dic[key]:
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.add(l.name())
        syn_dic[key] = synonyms

    print()

    write_dic(syn_dic, output_filename + "_synonyms")
