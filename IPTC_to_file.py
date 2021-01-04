import sys
import os

from iptcinfo3 import IPTCInfo


def delete_without_keywords(filepath):
    info = IPTCInfo(filepath, inp_charset='utf_8')
    if len(info['keywords']) == 0:
        os.remove(filepath)
        return True
    return False

if __name__ == '__main__':
    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        raise ValueError("Input directory path is not correct")
    if len(sys.argv) == 3:
        output_filename = sys.argv[2]
    else:
        output_filename = "keywords"

    f = open(output_filename, "w")

    for filename in os.listdir(input_dir):
        if not delete_without_keywords(str(input_dir) + "/" + str(filename)):
            # Throws warning but works fine
            info = IPTCInfo(str(input_dir) + "/" + str(filename), inp_charset='utf_8')
            stringBuilder = filename + ":"
            for keyword in info['keywords']:
                stringBuilder += keyword + ";"
            stringBuilder += "\n"
            f.write(stringBuilder)
    f.close()

