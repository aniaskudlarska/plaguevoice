import markovify


filename = input("Type the name of the file as base")
with open ('path2EnglishParsed.txt', encoding="utf8") as f:
    text = f.read()

model = markovify.Text(text)

for i in range(50):
    print(model.make_sentence())


#TODO: Make this modular, open different files, and print them
#TODO: Format text, replace \n\

