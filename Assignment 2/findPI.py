def findPI(repetitions):
    pi = 1.0

    flipFlop = True

    counter = 0
    divider = 3

    while counter <= int(repetitions):
        if flipFlop == True:
            pi -= 1/divider
            flipFlop = False
        else:
            pi += 1/divider
            flipFlop = True

        divider += 2
        counter = counter + 1

    print("Your pi is: ")
    print(4 * pi)

if __name__ == '__main__':
    repetitions = input("Enter the amount of repetitions (Higher = more precision): ")
    findPI(repetitions)
