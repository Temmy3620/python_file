with open('data.csv',"r") as f:
    
    tyu = []
    for i in f:
        ty = i.strip()
        tu = ty.split(",")
        tyu.append(tu)
    
    dict_list = []
    day_list = []
    persons_list = []
    parts_list = []
    for n in range(1,len(tyu) - 1):
        data = dict(zip(tyu[0],tyu[n]))   
        
        data["費用"] = int(data["費用"])
        dict_list.append(data)
        day_list.append(data["日付"][:2])
        persons_list.append(data["担当"])
        parts_list.append(data["区分"])
        
    months = list(set(day_list))
    persons = list(set(persons_list))
    parts = list(set(parts_list))
     
   
    print(" 月別集計　")
    print("月 費用合計")
    for i in range(len(months)):
        m_total = sum([x["費用"] for x in dict_list if x["日付"][:2] == months[i]])
        print("{} {}".format(months[i],m_total))
    print(" 担当別集計 ")
    print("担当者 費用合計")
    for a in range(len(persons)):
        p_total = sum([x["費用"] for x in dict_list if x["担当"] == persons[a]])
        print("{} {}".format(persons[a],p_total))
    print("　区分別集計 ")
    print("区分 費用合計")
    for s in range(len(parts)):
        s_total = sum([x["費用"] for x in dict_list if x["区分"] == parts[s]])
        print("{} {}".format(parts[s],s_total))



#グラフ作画

import numpy as np
import matplotlib.pyplot as plt

m_list = []
p_list = []
s_list = []

for i in range(len(months)):
        m_total = sum([x["費用"] for x in dict_list if x["日付"][:2] == months[i]])
        m_list.append(m_total)
for a in range(len(persons)):
        p_total = sum([x["費用"] for x in dict_list if x["担当"] == persons[a]])
        p_list.append(p_total)
for s in range(len(parts)):
        s_total = sum([x["費用"] for x in dict_list if x["区分"] == parts[s]])
        s_list.append(s_total)
total = sum([x["費用"] for x in dict_list])

# 円グラフを描画

label1 = months
x = np.array([x/total  for x in m_list])

label2 = ["tanaka","satou","suzuki"]
y = np.array([x/total  for x in p_list])

label3 = ["syokuhi","kousai","syoseki"]
z = np.array([x/total for x in s_list])


plt.figure(figsize=(11, 12))


plt.subplot(2,2,1)
plt.pie(x,labels=label1)
plt.subplot(2,2,2)
plt.pie(y,labels=label2)
plt.subplot(2,2,3)
plt.pie(z,labels=label3)
        
plt.show()        
                