#! /usr/bin/python
# Filename: interface2.py -----> calculate the distance between the atoms and pick up the one within the vander Waal distance + 0.5 cut - off.

import sys
import math # for the round off purpose

# the dictionary defines the values used for cryo_EM/homology models

ab = {'C':2.5, 'N':2.5, 'O':2.5, 'S':2.5, 'P':2.5}  # Creating a dictionary(it has both the identifier and the value) 
Q = 0  # Q is the cut - off

n1 = sys.argv[1]
list = []

for i1 in open(sys.argv[1]): 

	if i1.startswith ("ATOM"):
		
     		u1 = float(i1[29:38]) # the x - coordinate
     		v1 = float(i1[38:46]) # the y - coordinate
     		w1 = float(i1[46:54]) # the z - coordinate
		
     		a1 = i1[13:14] # the symbol of the atom involved.
		c1 = i1[21:22] # the chain id

		list.append(c1)

     		for j1 in open(sys.argv[1]):

	   			if j1.startswith ("ATOM"):

					u2 = float(j1[29:38]) # the x - coordinate
					v2 = float(j1[38:46]) # the y - coordinate
					w2 = float(j1[46:54]) # the z - coordinate

					a2 = j1[13:14] # the symbol of the atom
					c2 = j1[21:22] # the chain id

					if c2 not in list:

						d1 = (((u1 -u2 )**2) +((v1-v2)**2)+((w1-w2)**2))**0.5

						for atom1, distance1 in ab.iteritems(): #iterating over the key and value

		     					if atom1 == a1:

								l1 = float(distance1)

								for atom1, distance1 in ab.iteritems():

			    						if atom1 == a2:

			    							k1 = float(distance1)

										if d1<= (l1 + k1 + Q):

				    							g1 = open(n1[:4] + '_' + i1[21:22] + j1[21:22] +'_int.txt', 'a')                                                               
											g1.write(i1[17:20]+ '\t' + i1[21:22]+ '\t' + i1[22:27]+ '\t'+ j1[17:20]+ '\t' + j1[21:22]+'\t' +j1[22:27]+ '\t'+ str(round(d1,2)) + '\n') # round is to round off the no.
											g1.close()
					else:
					
						continue	 	
