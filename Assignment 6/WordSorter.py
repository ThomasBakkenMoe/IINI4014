import os

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


def wordSort(filename):

    '''
    Function that sorts all the words from a file in lexicographical and increasing length order.
    Returns a sorted list
    The sorting algorithm does not care about capitalization.

    :param filename: string: the name of the file to be sorted
    :return: string list: sorted list of strings
    '''

    wordArray = []

    filename = findFile(filename)

    with open(filename, "r", encoding='utf-8') as f:
        lineArray = f.readlines()

        # reads and splits the words from the file into 'wordArray'
        for line in lineArray:
            currentLine = line.split(" ")
            for word in currentLine:
                wordArray.append(word.replace("\n", ""))

    # Control variables
    unsorted = True
    hit = False
    x = 0

    # Prints the unsorted array for comparisons sake
    print("Unsorted Array: \n",wordArray)

    while unsorted:

        if len(wordArray[x]) > len(wordArray[x + 1]):
            wordArray[x], wordArray[x + 1] = wordArray[x + 1], wordArray[x]
            hit = True

        if (wordArray[x].lower() > wordArray[x + 1].lower()) and (len(wordArray[x]) == len(wordArray[x + 1])):
            wordArray[x], wordArray[x + 1] = wordArray[x + 1], wordArray[x]
            hit = True

        x += 1
        if x + 2 > len(wordArray):
            x = 0
            if hit == False:
                unsorted = False

            hit = False

    return wordArray


if __name__ == '__main__':
    # print(wordSort("UnsortedFile.txt"))
    print('{0:08b}'.format(6))

