import pandas as pd

offer_name = ['a', 'b', 'c', 'd', 'e', 'h', 'i', 'j', 'k']

texts = []

for i in range(0, len(offer_name)):
    file_path = "datasets/SmartOffer/OOD/{}-offer.xlsx".format(offer_name[i])
    cur_data = pd.read_excel(file_path)
    print(cur_data.keys())
    if '岗位要求' in cur_data.keys():
        offers = cur_data.loc[:, ['岗位要求']].values.tolist()
    elif '岗位描述和要求' in cur_data.keys():
        offers = cur_data.loc[:, ['岗位描述和要求']].values.tolist()
    for o in offers:
        try:
            texts += o[0].split("\n")
        except:
            continue
with open("datasets/SmartOffer/OOD/test_nolabel.tsv", "w") as f:
    f.write("text_a\n")
    for t in texts:
        if t != "" and len(t) >=8 :
            t = list(t)
            t = " ".join(t)
            t = t.replace("\n", "")
            f.write(t+"\n")
