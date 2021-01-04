import os
import sys

from iptcinfo3 import IPTCInfo


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def write_keywords(keywords, output_file):
    info = IPTCInfo(output_file, force=True, inp_charset='utf8')
    info['keywords'] = list(keywords)
    info.save_as(output_file)


if __name__ == '__main__':
    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        raise ValueError("Input directory path is not correct")
    for filename in os.listdir(input_dir):
        info = IPTCInfo(input_dir + "/" + filename, force=True, inp_charset='utf_8')
        new_keywords = set()
        for each in info['keywords']:
            new_keywords.add(remove_prefix(each, " ").lower())
        info['keywords'] = list(new_keywords)
        info.save_as(input_dir + "2/" + filename)
    print()
