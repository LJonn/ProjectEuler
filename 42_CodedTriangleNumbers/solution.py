def letterValue(letter):
    return ord(letter.lower())-96

def triangleNumber(word):
    value=0
    for letter in word:
        value+=letterValue(letter)
    tn=0
    n=0
    while (tn<value):
        n+=1
        tn=1/2*n*(n+1)
    if tn==value:
        return n
    return 0


with open('42_CodedTriangleNumbers/words.txt') as f:
    words = f.read()
words=words.split(',')

triangleSum=0
for word in words:
    word=word.strip('"')
    if (triangleNumber(word)>0):
        triangleSum+=1

print(triangleSum)

