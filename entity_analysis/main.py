# f = open("datasets/SmartOffer_new/entity_analysis/entities.tsv","r")
# lines = f.readlines()
# words = []
# for l in lines:
#     l = l.strip()
#     words.append(l)

# wordcount = {}
# for word in words:
#     wordcount[word] = wordcount.get(word, 0)+1
# print(sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:100])
# /apdcephfs/share_1157269/ziheliu/TencentPretrain/datasets/SmartOffer/prediction.tsv


count_dict = {}

f = open("datasets/SmartOffer/entity_analysis/entities_ood_1_1.tsv","r")
lines = f.readlines()
words = []
for l in lines:
    l = l.strip().split("\t")
    if len(l) == 2:
        if l[1] not in count_dict.keys():
            count_dict[l[1]] = []
            count_dict[l[1]].append(l[0])
            # count_dict[l[1]] = list(set(count_dict[l[1]]))
        else:
            count_dict[l[1]].append(l[0])
            # count_dict[l[1]] = list(set(count_dict[l[1]]))
        words.append(l[0])


import json
string = json.dumps(count_dict,ensure_ascii=False,indent=4)
with open("datasets/SmartOffer/entity_analysis/ood_dict_1_1.json", "w", encoding="utf-8") as f:
    f.write(string)

keys = count_dict.keys()
sums = 0
each_num = {}
for k in keys:
    sums += len(count_dict[k])

for k in keys:
    each_num[k] = len(count_dict[k]) / sums
    print(k + "占比：{:.2f}%".format(each_num[k]*100))


# print("团队协作能力")
# print(count_dict["团队协作能力"])
# print("人际交往能力")
# print(count_dict["人际交往能力"])
# print("分析能力")
# print(count_dict["分析能力"])
# print("工程职业道德")
# print(count_dict["工程职业道德"])
# print("情绪管理能力")
# print(count_dict["情绪管理能力"])

# 统计排序算法
wordcount = {}
for word in words:
    wordcount[word] = wordcount.get(word, 0)+1
print(sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:100])