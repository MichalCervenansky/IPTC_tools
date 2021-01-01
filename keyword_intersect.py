import os
import sys


def build_dic(file):
    with open(file) as f:
        dictionary = dict()
        first_file = [line.rstrip() for line in f]
        for line in first_file:
            name_keywords = line.split(":")
            keyword_set = set(name_keywords[1].split(";"))
            keyword_set.remove('')
            dictionary[name_keywords[0]] = keyword_set
    return dictionary


def write_dic(dic, output_filename):
    with open(output_filename, "w") as f:
        for key in dic.keys():
            stringBuilder = key + ":"
            if isinstance(dic[key], set):
                for keyword in dic[key]:
                    stringBuilder += keyword + ";"
            elif isinstance(dic[key], int):
                stringBuilder += str(dic[key])
            else:
                raise ValueError("Unknown value of dic")
            stringBuilder += "\n"
            f.write(stringBuilder)


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
