pred_path = "datasets/SmartOffer/OOD/prediction_ood.tsv"
text = "datasets/SmartOffer/OOD/test_nolabel.tsv"

f = open(text, "r")
texts = f.readlines()
fb = open(pred_path, "r")
preds = fb.readlines()

with open("datasets/SmartOffer/v3_RDAS/train.tsv", "w") as fs:
    fs.write("text_a\tlabel\n")
    for i in range(0, len(preds)):
        t = texts[i].strip()
        l = preds[i].strip()
        if t == "text_a":
            continue
        else:
            fs.write(t + "\t" + l + "\n")
