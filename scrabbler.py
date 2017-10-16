words = open("scrabble_words.txt")
userInput = ""
while len(userInput) not in range(1,8):
    userInput = input("Input up to 7 tiles: ")      
userInput = userInput.upper()
userInputChars = list(userInput)
print(userInputChars)
matchingWords = []
extraLetter = []
wordScore = []
extraScore = []
finalWord = []
finalScore = []
finalExtra = []
finalExtraScore = []
for line in words:
    line = line.strip("\n")
    temp = list(userInputChars)
    toAdd = True
    count = 0
    for char in line:                
        if char in temp:
            temp.remove(char)            
        elif '_' in temp:
            temp.remove('_')           
        else:
            count += 1
            toAdd = False                                             
    if toAdd == True:
        score = 0
        if len(line) == 7:
            score += 50
        for char in line:
            if char in "AEIOULNSTR":
                score += 1
            elif char in "DG":
                score += 2
            elif char in "BCMP":
                score += 3
            elif char in "FHVWY":
                score += 4
            elif char in "K":
                score += 5
            elif char in "JX":
                score += 8
            elif char in "QZ":
                score += 10
        matchingWords.append(line)
        wordScore.append(score)
    elif count == 1:
        score = 0
        if len(line) == 8:
            score += 50
        for char in line:
            if char in "AEIOULNSTR":
                score += 1
            elif char in "DG":
                score += 2
            elif char in "BCMP":
                score += 3
            elif char in "FHVWY":
                score += 4
            elif char in "K":
                score += 5
            elif char in "JX":
                score += 8
            elif char in "QZ":
                score += 10        
        extraLetter.append(line)
        extraScore.append(score)

while sum(wordScore) > 0:
    maxValue = wordScore.index(max(wordScore))
    finalWord.append(matchingWords[maxValue])
    finalScore.append(wordScore[maxValue])
    wordScore[maxValue] = 0
while sum(extraScore) > 0:
    maxValue = extraScore.index(max(extraScore))
    finalExtra.append(extraLetter[maxValue])
    finalExtraScore.append(extraScore[maxValue])
    extraScore[maxValue] = 0
print("Words you can spell with the given tiles: ")
(len(finalWord))
n=0
for line in finalWord:
    print (line, "\t\t", finalScore[n])
    n+=1
print("Words you can spell with one extra tile: ")
n=0
for line in finalExtra:
    print(line, "\t\t", finalExtraScore[n])
    n+=1