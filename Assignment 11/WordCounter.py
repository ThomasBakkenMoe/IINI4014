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


def getAverageScentenceLength(filename):

    '''
    Function that finds the average sentence length from a file.
    It uses Regex to first split the file by ., !, or ? before counting the number of sentences.

    :param filename: string: the name of the file
    :return: double: the file's word count divided på the sentence count
    '''

    reader = open(filename, "r", encoding='utf-8')

    while True:

        s = reader.read().replace("\n", "")

        contentSplitBySentence = re.split('[.!?][\s]{1,2}', s)


        #Remove all special characters

        for x in range(0, contentSplitBySentence.__len__()):
            contentSplitBySentence[x] = re.sub(r'[^a-zA-Z0-9]+', ' ', contentSplitBySentence[x])  # Removes any special characters

        sentenceCount = contentSplitBySentence.__len__()
        wordCount = 0

        for x in range(0, contentSplitBySentence.__len__()):
            wordCount += re.split(r'\s', contentSplitBySentence[x]).__len__()

        return wordCount/sentenceCount


def getUniqueWordPercentage(filename):

    '''
    Function that finds the percentage of unique words from a file.
    uses the getWordFreqs() method to find the number of words in the file, and each unique words frequency.

    :param filename: string: the name of the file
    :return: double: the number of unique words divided by the total amount of words
    '''

    wordsFreqTable = getWordFreqs(filename)
    wordsFreqTable.remove(wordsFreqTable[0])  # I am removing the first element in the table, as my WordFreqs Method annoyingly counts some blank character (not whitespace)
    words = 0

    for word in wordsFreqTable:

        words += word.frequency

    return wordsFreqTable.__len__()/words


def getWordTypePercentage(filename, threshold, greater):

    '''
    Function that finds the percentage of a type of word based on a threshold percentage from a file.
    uses the getWordFreqs() method to find the number of words in the file, and each unique words frequency.


    :param filename: string: the name of the file
    :param threshold: double: percentage to trigger whether or not a word should be counted
    :param greater: boolean: whether or not a words needs to have a frequency greater or lesser than the threshold
    :return: double: the percentage of a type of word that passes greater or lower than the threshold percentage.
    '''

    wordsFreqTable = getWordFreqs(filename)
    wordsFreqTable.remove(wordsFreqTable[0])  # I am removing the first element in the table, as my WordFreqs Method annoyingly counts some blank character (not whitespace)
    words = 0
    wordsOfType = 0

    for word in wordsFreqTable:

        words += word.frequency

    for word in wordsFreqTable:

        if greater:
            if (word.frequency / words) > threshold:
                wordsOfType += word.frequency
        else:
            if (word.frequency / words) < threshold:
                wordsOfType += word.frequency
    return wordsOfType/words


def getSentencesPerParagraph(filename):

    '''
    Function that finds the amount of sentences per paragraph from a file.
    The file first gets split into paragraphs with Regex before each paragraph get split
    into sentences. The sentences get counted.


    :param filename: string: the name of the file
    :return: list: Amount of sentences per paragraph.
    '''

    returnList = []

    reader = open(filename, "r", encoding='utf-8')

    s = reader.read()

    contentSplitByParagraph = re.split('\n\n', s)

    for paragraph in contentSplitByParagraph:
        paragraphSplitBySentence = re.split('[.!?][\s]{1,2}', re.sub('\n', ' ', paragraph))

        returnList.append(paragraphSplitBySentence.__len__())

    return returnList


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

    filename = "1342-0.txt"
    filename = findFile(filename)

    easyWordThreshold = 0.01
    difficultWordThreshold = 0.005


    print("Average words per sentence: \n", getAverageScentenceLength(filename), "\n")  # I choose to do 1. as an average, as the list would be quite long otherwise. I could also do this task as I have 5.
    print("Percentage of easy words (Greater than ", easyWordThreshold, " percent freq.): \n", getWordTypePercentage(filename, easyWordThreshold, True), "\n")
    print("Percentage of difficult words (Less than ", difficultWordThreshold, " percent freq.): \n", getWordTypePercentage(filename, difficultWordThreshold, False), "\n")
    print("Percentage of different words: \n", getUniqueWordPercentage(filename), "\n")
    print("Sentences per paragraph (list): \n", getSentencesPerParagraph(filename), "\n")
