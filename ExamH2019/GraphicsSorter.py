import os
import shutil

filenames = []
graphicFilesNames = []


def findFiles(startingFolder, fileList, graphicsNameList):

    """
    Method that finds all media files and lists them in graphicsNameList
    :param startingFolder:
    :param fileList:
    :param graphicsList:
    :param graphicsNameList:
    :return:
    """

    for root, dirs, files in os.walk(startingFolder, topdown=False):
        for file in files:
            fileList.append(root + "/" + file)

            if file.endswith(('.eps', '.tif', '.png', '.jpg', '.JPG')): # This could, admitently be imported as a list argument instead
                graphicsNameList.append(file)

                fileExtension = os.path.splitext(file)[1][1:]

                if not os.path.exists(root + "/" + fileExtension):
                    os.mkdir(root + "/" + fileExtension)


def cleanMainFolder(root):

    """
    Method that cleans up the root folder. It moves all unused files, exept .tex and .bib to a dump folder
    :param: String: root: root folder
    :return: no return
    """
    mainFolderFiles = os.listdir(root)

    for file in mainFolderFiles:
        if not (os.path.splitext(file)[1][1:] == "tex" or os.path.splitext(file)[1][1:] == "bib"):

            # Skips directories, so that they are not put in the dump folder
            if os.path.isdir(root + "/" + file):
                continue

            if not os.path.exists(root + "/dump"):
                os.mkdir(root + "/dump")
            shutil.move(root + "/" + file, root + "/dump/" + file)



def processTex(root, texFile, graphicsNameList):

    """
    Method that opens a .tex files and searches for media file usage.
    if media usage is found ("includegraphics"), the method will check if the file is in our list of files and move it to the relevant subdirectory
    if the subdir does not exist, it will be created.
    :param root:
    :param texFile:
    :param graphicsNameList:
    :return:
    """

    reader = open(texFile, "r")

    currentLine = reader.readline()

    while currentLine != "":
        currentLine = reader.readline()

        if not currentLine.startswith('%'):
            if "includegraphics" in currentLine:
                for file in graphicsNameList:
                    if file in currentLine:
                        fileExtension = os.path.splitext(file)[1][1:]
                        shutil.move(root + "/" + file, root + "/" + fileExtension + "/" + file)


if __name__ == "__main__":
    root = "./files" # here you decide the name of your root folder
    findFiles(root, filenames, graphicFilesNames)

    for file in filenames:
        if file.endswith('.tex'):
            processTex(root, file, graphicFilesNames)

    cleanMainFolder(root)
    print("Graphics files found: " + str(graphicFilesNames.__len__()))

