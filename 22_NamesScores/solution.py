with open("input.txt") as file:
    fileContents = file.read()
    fileContents = fileContents.replace('"', '')
    wordList = fileContents.split(',')

wordList.sort()

sum = 0
iterator = 0
for word in wordList:
    wordSum = 0
    for letter in word:
        wordSum += ord(letter.lower())-96
    iterator += 1
    sum += wordSum*iterator

print(sum)
