import os
import re


class WordAndNumber:
    '''
    Object that contains a word and the frequency of that word

    Constructor takes:
    word: string: the saved word
    frequency: int: the frequency of the saved word
    '''

    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __repr__(self):
        str = "{}: {}"
        return str.format(self.word, self.frequency)


def findFile(filename):

    '''
    Function that finds a file in the subdirectory tree beneath the python file

    takes:
    :param filename: string: the name of the file to be found
    :return: string: the relative path to the file
    '''

    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        if filename in files:
            return os.path.join(root, filename)
    raise Exception("File not found")


def getWordFreqs(filename):

    '''
    Function that creates a dictionary with the frequency of words in a file.
    Before the words are counted, each line in the file has any special characters removed with Regex, all letters are
    set to lowercase, and line breaks are removed. Finally the line is split by word into a list and the words
    are counted.

    :param filename: string: the name of the file
    :return: List: list of WordAndNumber objects. The list is sorted by frequency, decreasing
    '''

    returnList = []

    filename = findFile(filename)

    reader = open(filename, "r", encoding='utf-8')
    currentLine = ""

    while True:

        currentLine = reader.readline()

        if currentLine == '':
            break

        currentLine = re.sub('[^A-Za-z0-9]+', " ", currentLine).lower().replace("\n", "").split(' ')

        found = False

        # This loop loops through each word in the 'currentLine' list and checks if a word of that type
        # has been registered before. If such a word has already been registered, the frequency is incremented.
        # if not, the word is registered in the returnList as a WordAndNumber object.

        for word in currentLine:
            for element in returnList:
                if element.word == word:
                    element.frequency += 1
                    found = True
                    break
            if not found:
                returnList.append(WordAndNumber(word, 1))
            found = False

    return sorted(returnList, key=lambda element: element.frequency, reverse=True)


def getWordsLine(filename, checkWord):

    '''
    Function that creates a list of line numbers where a check word is present
    The function loops through the file line-by-line.

    :param filename: string: name of the file to be checked
    :param checkWord: string: the keyword that is used  when checking each line in the file
    :return:
    '''

    returnList = []

    filename = findFile(filename)

    if not checkWord.startswith(" "):
        checkWord = " " + checkWord

    if not checkWord.endswith(" "):
        checkWord = checkWord + " "

    reader = open(filename, "r", encoding='utf-8')
    currentLine = ""
    lineNumber = 1

    while True:
        currentLine = reader.readline()

        if currentLine == '':
            break

        if checkWord in currentLine:

            returnList.append(lineNumber)

        lineNumber += 1

    return returnList


if __name__ == "__main__":
    print(getWordsLine("test.txt", "hi"))
    print(getWordFreqs("11-0.txt"))