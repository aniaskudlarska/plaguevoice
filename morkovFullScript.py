import markovify
with open ('path2EnglishParsed.txt', encoding="utf8") as f:
    text = f.read()

model = markovify.Text(text)

for i in range(50):
    print(model.make_sentence())