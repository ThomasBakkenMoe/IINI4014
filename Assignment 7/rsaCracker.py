import rsa
import random
import numpy as np
from random import randint
import sys


def generatePossiblePublicKey(publicKey, possiblePhi):

    possibleD = rsa.multiplicative_inverse(publicKey[0], possiblePhi)

    return (possibleD, publicKey[1])


def generatePossiblePhi(possibleP, possibleQ):

    possiblePhi = (possibleP-1) * (possibleQ-1);

    return possiblePhi


if __name__ == "__main__":
    encrypted_msg = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186,
                     85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932,
                     70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926,
                     66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174,
                     21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327,
                     5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]

    publicKey = (29815, 100127)

    primes = rsa.PrimeGen(100)
    p = q = 2
    possiblePublicKey = (0, 0)
    firstLetter = encrypted_msg[0]
    foundResults = []
    possiblePQ = []

    print(primes.__len__())

    found = False

    for x in range(0, primes.__len__()):
        p = primes[x]
        for y in range()

    for x in range(0, primes.__len__()):
        p = primes[x]
        for y in range(0, primes.__len__()):
            q = primes[y]

            possiblePublicKey = generatePossiblePublicKey(publicKey, generatePossiblePhi(p, q))
            try:
                if rsa.decrypt(possiblePublicKey, [encrypted_msg[0]]) == "h":
                    decrypted_msg = rsa.decrypt(possiblePublicKey, encrypted_msg)
                    print(decrypted_msg)
                    print(possiblePublicKey)
                    break
            except:
                pass
