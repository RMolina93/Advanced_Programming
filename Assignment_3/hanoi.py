#Towers of Hanoi

from collections import deque


def hanoi_recursive(n,srcPeg,dstPeg,tmpPeg):
	"""
	Added a tmp variable in the hanoi algorithm only for nomenclature. 
	It could be computed by making (6-src-dst), but this only would be valid when src and dest are called 1 and 2. 
	I prefered to add a variableonly for adding the name you want, this way you can call the Pegs by strings.
	"""
	if n <= 0:
		return
	else:
		hanoi_recursive(n-1,srcPeg,tmpPeg,dstPeg)
		print ("Moved from:",srcPeg,"to",dstPeg)
		hanoi_recursive(n-1,tmpPeg,dstPeg,srcPeg)


def hanoi_iterative(n, src, tmp, dst):

	#Starting the system

	srcPeg = deque()
	dstPeg = deque()
	tmpPeg = deque()
	for disk in reversed(range(1,n+1)):
		srcPeg.append(disk)

	#Defining the permitted movement between two Pegs
	def legal_movement(Peg1,Peg2, Peg1name, Peg2name):

		if len(Peg1)==0:
			disk = Peg2.pop()
			Peg1.append(disk)
			print ("Moved from:",Peg2name,"to",Peg1name)
			return

		if len(Peg2)==0:
			disk = Peg1.pop()
			Peg2.append(disk)
			print ("Moved from:",Peg1name,"to",Peg2name)
			return

		if Peg1[-1] > Peg2[-1]:
			disk = Peg2.pop()
			Peg1.append(disk)
			print ("Moved from:",Peg2name,"to",Peg1name)
			return

		if Peg1[-1] < Peg2[-1]:
			disk = Peg1.pop()
			Peg2.append(disk)
			print ("Moved from:",Peg1name,"to",Peg2name)
			return

	if n%2 == 0:
		try:
			while True:

				legal_movement(srcPeg,dstPeg, src, dst)
				legal_movement(srcPeg,tmpPeg, src, tmp)
				legal_movement(tmpPeg,dstPeg, tmp, dst)
		except:
			print ("The algorithm has finished")

	if n%2 != 0:
		try:
			while True:

				legal_movement(srcPeg,tmpPeg, src, tmp)
				legal_movement(srcPeg,dstPeg, src, dst)
				legal_movement(tmpPeg,dstPeg, tmp, dst)
		except:
			print ("The algorithm has finished")
