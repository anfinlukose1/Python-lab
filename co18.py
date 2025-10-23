s = input("Enter a sentence: ")
wordsList = s.split()
uniqueWords = set(wordsList)

for word in uniqueWords:
    print(f"{word} occurs {wordsList.count(word)} times")
