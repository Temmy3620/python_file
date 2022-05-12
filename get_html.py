"""
HTMLからデータの取得と集計を行う
URLの数
ASCII文字の数（上位10個）

"""

from inspect import indentsize
from bs4 import BeautifulSoup #HTMLやXMLからデータを抽出するためのpythonのライブラリ

import urllib.request as req #urllibとはurlを扱うためのライブラリreqと（別名）をつける


def is_ascii(string):
    """
    ASCII文字判定
    """
    if string:
        return max([ord(char) for char in string]) < 128
    return True


url = "https://news.yahoo.co.jp/" #URL
res = req.urlopen(url).read()#URLを読み込む
soup = BeautifulSoup(res,"lxml")
links = soup.find_all("a")

b = [x.get("href") for x in links]#URLの数

print("URL数:" + str(len(b)))



text = soup.get_text()#テキストを取得
lines= [line.strip() for line in text.splitlines()]
text = "\n".join(line for line in lines if line)#テキストを取得

text_list = list(text)
char_lists = [i for i in text_list if i != "\n" and i !=" "]
ascii_list = [s for s in char_lists if is_ascii(s)]

d = dict() #辞書を作る
for i in ascii_list:
    d[i] = d[i] + 1 if i in d else 1


dict2 = sorted(d.items(), key=lambda x:x[1], reverse=True)


for t,w in dict2[:10]:
    print(str(t) + ":" + str(w))
    
"""
グラフの表示
"""

import numpy as np
import matplotlib.pyplot as plt

word = []
FY = []

e = dict2[:50]

for i in range(len(e)):
    word.append(e[i][0])
    FY.append(e[i][1])

indices = np.arange(len(e))
plt.bar(indices, FY, color="r")
plt.xticks(indices, word, rotation = "vertical")
plt.tight_layout()
plt.show()