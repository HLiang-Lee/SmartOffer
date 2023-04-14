file = "datasets/SmartOffer/v1_SKILL/train.tsv"
with open(file, "r") as f:
    lines = f.readlines()
    number_of_words = 0
    number_of_entities = {}
    for l in lines:
        l = l.strip().split("\t")
        if l[0] == 'text_a':
            continue
        else:
            sents = l[0].split()
            tags = l[1].split()
            number_of_words += len(sents)
            for i in range(0, len(sents)):
                if tags[i].startswith("B"):
                    name = tags[i].split("-")[1]
                    if name not in number_of_entities.keys():
                        number_of_entities[name] = [0,0]
                    number_of_entities[name][0] += 1
                if tags[i].startswith("B") or tags[i].startswith("I"):
                    number_of_entities[name][1] += 1


print("当前数据集为：", file)
print("数据集总共字符数：", number_of_words)
print("不同实体类型对应 实体数-字符数：")
for name in sorted(number_of_entities):
    print("{}：{}-{}".format(name, number_of_entities[name][0], number_of_entities[name][1]))
