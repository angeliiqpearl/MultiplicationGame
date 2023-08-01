# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:42:07 2023

@author: Angel
"""
import random, time
import math

print("Let us practise multiplication tables.")

loopnum = int(input("How many probems do you want?\n"))
num_1 = random.randint(1,10)
num_2 = random.randint(1,10)

starttime=time.time()

def main(loopnum):

    count = 0
    correct = 0
    while count < loopnum:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        guess = int(input("What is " + str(num_1) + "x" + str(num_2) + "?"))
        answer = num_1*num_2
        count += 1

        if guess == answer:
            correct += 1
            print("Correct!")
        else :
            print("Sorry, the answer is", answer, ".")

    if loopnum > 1:
        result = correct * 100./loopnum  

    print("You got ", "%.1f"%result, "% of the problems.")
    
    endtime=time.time()
    totaltime=round(endtime-starttime,1)
    print("The total time it took you to answer the session questions",totaltime,"seconds")

main(loopnum)