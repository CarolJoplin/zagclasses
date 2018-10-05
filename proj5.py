"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 5: This project accepts two words as command line input and displays
the minimum edit distance and the alignment from the minimum edit distance
computation.
Due: 5 October 2018
Usage: python proj5.py <source> <target>
# should be Python 2.7
"""

import re
import sys

INS_COST = 1
DEL_COST = 1

def sub_cost(sourceChar, targetChar):
    if sourceChar == targetChar:
        return 0
    return 2

# TO DO
def minEditDistance(source, target):
    n = len(target)
    m = len(source)
    distance = []
    distance.append([0])
    for i in range(1,n+1):
        distance.append([distance[i - 1][0] + INS_COST])
    for j in range(1,m+1):
        distance[0].append(distance[0][j - 1] + DEL_COST)
    for i in range(1,n+1):
        for j in range(1,m+1):

	    # this takes the minimum always
	    # what about the cases where we want diagonal because its the same letter?
            distance[i].append(min(
                distance[i-1][j] + INS_COST,
                distance[i-1][j-1] + sub_cost(source[j-1], target[i-1]),
                distance[i][j-1] + DEL_COST
            ))
    return distance[n][m], distance

# TO DO
def computeAlignment(source, target, graph):
    changes = ""
    # i = row, j  column
    i = len(graph) - 1
    print i
    j = len(graph[0]) - 1
    print j
    #print "Value: ",graph[i][j]
    #print "\n"
    # while not at bottom left corner of matrix
    while i > 0 and j > 0:
	# DEBUG CODE
        print "Changes: ",changes
	
	# value is set at top righthand corner
	# value = minimum edit distance
		# minimum of diagonal, down, left
	# determines what value is
	#if graph[i][j] == graph[i-1][j-1]:
		#if source[j-1] == target[i-1]:
			#value = graph[i-1][j-1]
		#else:
			
	#else:
        	#value = min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j])

	value = min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j])
	#value = computeValue(graph[i][j], graph[i-1][j-1], graph[i][j-1], graph[i-1][j])
	
	#DEBUG CODE
        print "Value:",value

	# MISSING CASE:	
		# if minimum value of all three cells is NOT what you want
		# because one of the higher values is the same letter

	# if minimum edit distance is equal to down diagonal:
	# Substitution = 2
        if value == graph[i-1][j-1]:
	    # if current element equal to downward diagonal
            if graph[i][j] == graph[i-1][j-1]:
                changes = " " + changes

	    else:
                changes = "s" + changes

            i -= 1
            j -= 1

	# if we don't want the min, but we want a larger number
		# because its the same letter as current

	# if minimum edit distance is equal to cell below
	# Down = 1
        elif value == graph[i][j-1]:
	    
	   changes = "d" + changes
           j -= 1
            
	# if minimum edit distance is equal to lefthand cell
	# Left = 1
        elif value == graph[i-1][j]:
	   # if we don't want the min, but we want a larger number
		# because its the same letter as current
	   #if graph[i][j] == graph[i-1][j-1]:
                #changes = " " + changes
		#i -= 1
	    #else:
		#changes = "i" + changes
		#i -= 1
	   changes = "i" + changes
	   i -= 1
            
    # now in a 0 row or column, or both
    while j > 0:
	j -= 1
	changes = "d" + changes
    
    while i > 0:
	i -= 1
	changes = "i" + changes

    print "Changes: ",changes
    printAlignment(source, target, changes)

'''
Computes the value 

My attempt at getting the diagonal value to be chosen
instead of minimum value, if identical value is the same letter
Currently just takes diagonal every time
'''
def computeValue( graphCell, graphDiagonal, graphDown, graphLeft ):
	# value is set at top righthand corner
	# value = minimum edit distance
		# minimum of diagonal, down, left

	# determines what value is
	if graphCell == graphDiagonal:
		value = graphDiagonal
	else:
        	value = min(graphDiagonal, graphDown, graphLeft)

	return value

'''
Print the alignment 
according to book formatting
'''
def printAlignment(source, target, changes):
	#print "Changes: ",changes
	print "Source: ",source
	print "Target: ",target
	
	for i in range(len(changes)):
		print changes[i],
	print ""

	# when an i is present in changes,
		# add * to source
	for i in range(len(changes)):
		if changes[i] == 'i':
			source = source[:i] + '*' + source[i:]

	# DEBUG CODE
	print "Source: ",source

	# when a d is present in changes,
		# add a * to the start of target
	for i in range(len(changes)):
		if changes[i] == "d":
    			#print "Changes in target: ",changes
			#target = '*' + target
			target =target[:i] + '*' + target[i:]
			#target = target.replace(target[i], "*",)
	# DEBUG CODE
	print "Target: ",target

	# print source in upper case
	for i in range(len(source)):
		print source[i].upper(),
		#print source[i], 
	print ""

	# matches formatting in book
	for i in range(len(changes)):
		print "|", 
	print ""

	# print target in uppercase
	for i in range(len(target)):
		print target[i].upper(),
		#print target[i], 
	print ""

	# below, display changes
	for i in range(len(changes)):
		# alignment string
		print changes[i],

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Incorrect.\nUsage: python proj5.py <source> <target>"
        exit()
    print "Source:", sys.argv[1], "\nTarget:", sys.argv[2]
    distance, graph = minEditDistance(sys.argv[1], sys.argv[2])
    print "Min Edit Distance:", distance
    print graph
    computeAlignment(sys.argv[1], sys.argv[2], graph)
  
