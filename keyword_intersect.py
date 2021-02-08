import os
import sys

from tools import build_dic, write_dic

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Input parameter is missing")
    first = sys.argv[1]
    sec = sys.argv[2]
    if not os.path.isfile(first):
        raise ValueError("Input file path is not correct")
    if not os.path.isfile(sec):
        raise ValueError("Input file path is not correct")
    if len(sys.argv) > 3:
        output_filename = sys.argv[3]
    else:
        output_filename = "keywords"

    first_dic = build_dic(first)
    second_dic = build_dic(sec)
    intersection_dic = dict()
    result_dic = dict()
    for key in first_dic.keys():
        intersection_dic[key] = first_dic[key].intersection(second_dic[key])
        result_dic[key] = len(intersection_dic[key])

    write_dic(intersection_dic, output_filename + "_intersection")
    write_dic(result_dic, output_filename + "_results")
