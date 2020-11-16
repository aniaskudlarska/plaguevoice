with open('Path2english.txt', encoding="utf8") as script:
    scriptText = script.read()

strList = []
for line in scriptText:
    #strList.append(filter(lambda x: x.isalpha(), line)) get this working later
    strList.append(line)


scrublist = []
nums = set(map(int,range(10)))
for f in strList:
    ''.join(i for i in f if i not in nums)
    scrublist.append(f)

for item in scrublist:
    print(item)



