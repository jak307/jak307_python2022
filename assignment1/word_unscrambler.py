#open the text file, read the text fie, and store the data in a variable
words = open('words.txt', 'r')

#create an array from the words in the file
wordlist = words.readlines()

#remove the newline character and convert each word to lowercase
wordclean = [word.strip().lower() for word in wordlist]

#remove duplicates
wordunique = list(set(wordclean))

#sort the word list in lexiographic order
wordunique.sort()

#this function sorts a string into lexiographic order
def signature(word):
    return ''.join(sorted(word))

sortedWords = []

#takes in a string and searches through the wordlist to find anagrams
def anagram(myword):
    for word in wordunique:
        if(signature(word) == signature(myword)):
            sortedWords.append(word)

#makes sure user input is neither blank nor null
def validate_input(user_input):
    if user_input != "" and user_input != None:
        return True
    else:
        return False

#takes user input
user_input = input("Please enter a word or a phrase: ")

if validate_input(user_input):
    #sorts user input into lexiographic order
    sortedLetters = sorted(user_input)
    #finds every unique combination of elements from a list
    from itertools import combinations
    #counts letters in word
    counter = 6
    while (counter > 2):
        print(counter, " letters:")
        theList = []
        sortedWords = []
        #creates list of all possible combinations of a word's letters
        for i in combinations(sortedLetters, counter):
            s = ""
            s = s.join(i)
            theList.append(s)
            #removes duplicates from list
        uniqueList = list(set(theList))
        #sorts the list in alphabetical order
        uniqueList.sort()
        #looks for anagrams in list
        for i in uniqueList:
            anagram(i)
        #sorts list of anagrams in lexiographic order
        sortedWords.sort()
        #prints list of angrams
        print(sortedWords)
        counter = counter - 1
