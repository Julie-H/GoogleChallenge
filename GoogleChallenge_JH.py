# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:21:25 2016

@author: Julie
"""

import string

string.split('I am in London', " ")
tup = ['a']

def listOptimise(positions, termsList):
    while len(positions[termsList[0]])>1:
        #Remove the position of the 1st item of the list
        positions[termsList[0]] = positions[termsList[0]][1:]
        #Remove the 1st item from the list
        termsList = termsList[1:]
    #and again

def answer(document, searchTerms):
    textList = string.split(document)
    start = -1
    textLength = len(textList)
    #k will be the current position all along the document
    k = 0
    positions = {}
    termsNumber = len(searchTerms)
    termsList = []
    #Find the 1st instance of a search term in the document
    while start == -1:
        for i in range(termsNumber):
            if textList[k] == searchTerms[i]:
                start = k
                #Start filling in the positions dictionnary and building the list of search terms:
                positions[textList[k]] = [k]
                termsList.append(textList[k])
        k+=1
        lengthPos = 1
    #Find the remaining search terms in the document to build an initial list
    #and record positions as they are encountered:   
    while k < textLength and lengthPos < termsNumber:
        for i in range(termsNumber):
            if textList[k] == searchTerms[i]:
                if textList[k] in positions.keys():
                    positions[textList[k]].append(k)
                    termsList.append(textList[k])
                else:
                     positions[textList[k]] = [k]
                     termsList.append(textList[k])
                lengthPos +=1
        k+=1
    #Now optimise the initial list:
    listOptimise(positions, termsList)
    #We have an initial optimised list. Now record length and start:
    length = k - positions[termsList[0]][0]
    start = positions[termsList[0]][0]
    while k < textLength:
        #Look for next appearance of 1st item in the current optimised list.
        #Along the way, record the search terms appearing:
        while (k < textLength and textList[k]<>termsList[0]):
            for i in range(termsNumber):
                if textList[k] == searchTerms[i]:
                    positions[textList[k]].append(k)
                    termsList.append(textList[k])
            k+=1
        #If not reached end of list, means that we found another instance of 1st item
        #so record position and add to list of occurences
        if k < textLength:
            positions[textList[k]].append(k)
            termsList.append(k)
            #Now we have found a candidate list with everything in. Time to optimise:
            listOptimise(positions, termsList)
            #Check if current optimised list is shorter than shortest so far.
            #If so, record start and length:
            if (k - positions[termsList[1]][0])<length:
                length = k - positions[termsList[1]][0] + 1
                start = positions[termsList[1]][0]
        #and again:
        k+=1
    return string.join(textList[start:(start+length)])
    
text = "a b c d e f g h"
terms = ["b", "e"]   

terms[1:]

answer(text, terms) 

test1 = "many google employees can program"
search1 = ["google", "program"]

answer(test1, search1)

test2 = "a b c d a"
search2 = ["a", "c", "d"]
        

dico = {'a':[1, 3], 'b':[0, 2, 5], 'c':[8]}
mylist = ['b', 'a', 'b', 'a', 'b', 'c']

mylist[1:1+3]

listOptimise(dico, mylist)