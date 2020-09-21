def findPrimeNumbers(limit):


    for potensialPrime in range(2, int(limit)):

        prime = True

        for x in range(2, potensialPrime//2+1):

            if potensialPrime % x == 0:
                prime = False

        if prime:
            print(potensialPrime)


if __name__ == '__main__':
    limit = input("Find all prime numbers under: ")

    findPrimeNumbers(limit)