import markovify

#Create list of plague lines as strings
with open("plaguevoice.txt") as f:
    text = f.read()


strNone = 'None'
sentList = []
#Test markovify on things
textbase = markovify.Text(text)
for i in range(5):
    sentList.append(textbase.make_sentence())

#the plague text isnt long enough to markov, and sometimes returns none. I'll fix this later with a longer corpus of text
composite = str
filtlist = []
for x in sentList:
        if x is not None:
            filtlist.append(x)
composite = ' '.join(filtlist)
print(composite)