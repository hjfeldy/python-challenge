import os
import re
print(os.listdir())


file = open('paragraph_1.txt', 'r')
txt = file.read()
file.close()


#wordpattern
wpat  = re.compile(r'\S+')


#generate list of words
wordList = wpat.findall(txt)


#find avg world length 
lenTot = 0
lenCount = 0
for word in wordList:
    lenTot += len(word)
    lenCount += 1

wordCount = len(wordList)
avgLen = round((lenTot / lenCount), 2) #avg word length = sum of letters / number of words


#find number of sentences
sentences = 0
for char in txt:
    if char == '.' or char == '!' or char == '!':
        sentences += 1

senLen = round((wordCount / sentences), 2)

print(f'Paragraph Analysis:\n-----------------\nApproximate Word Count: {wordCount}\nApproximate Sentence Count: {sentences}\nAverage Letter Count: {avgLen}\nAverage Sentence Length: {senLen}')



