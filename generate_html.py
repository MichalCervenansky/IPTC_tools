from tools import build_dic

if __name__ == '__main__':
    f = open('my_keywords.html', 'w')
    dic = build_dic("/home/mcervenansky/PycharmProjects/IPTC_tools/keywords")
    message = """<html>
    <head></head>
    <body><table style="width:100%">"""

    for i in range(1, 10):
        message += """<tr><td>{number}</td>
    <td><img src="http://michal.cervenansky.eu/dt_dataset/img_{number}.jpg" width="256" height="256"></td>
    <td>{keywords}</td></tr>
        """.format(number="0" + str(i), keywords=dic["img_" + "0" + str(i) + ".jpg"])

    for i in range(11, 1001):
        message += """<tr><td>{number}</td>
    <td><img src="http://michal.cervenansky.eu/dt_dataset/img_{number}.jpg" width="256" height="256"></td>
    <td>{keywords}</td></tr>
        """.format(number=str(i), keywords=dic["img_" + str(i) + ".jpg"])

    message += """</table></body>
    </html>"""

    f.write(message)
    f.close()
