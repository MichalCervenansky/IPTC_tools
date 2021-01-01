import os
import sys

from keyword_intersect import build_dic, write_dic

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
    result_dic = dict()
    for key in first_dic.keys():
        result_dic[key] = len(first_dic[key])

    write_dic(result_dic, output_filename + "_counts")
