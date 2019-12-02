#Import zone
import sys 
import re
import math

file_data = sys.argv[1]
k = float(sys.argv[2])

#Classes and functions zone

def dist(x,y):   
	distance = float(math.sqrt((float(x.position[0])-float(y.position[0]))**2+(float(x.position[1])-float(y.position[1]))**2))
	return distance

class Sequence:

	def __init__(self, loci, position, name):
		self.loci = loci
		self.position = position.strip("(").strip(")").split(",")
		self.name = name
		self.next = None
		self.prev = None

	def float_to_loci(self):
		if str(self.loci).split(".")[1] == "75":
			self.loci = str(self.loci).replace(".75","q")
		else:
			self.loci = str(self.loci).replace(".25","p")

class LinkedList: 

	def __init__(self):
		self.start_node = None
  
	def sortedInsert(self, new_node):

		# Empty linked list case 
		if self.start_node is None: 
			new_node.next = self.start_node 
			self.start_node = new_node 

		elif self.start_node.loci >= new_node.loci: 
			new_node.next = self.start_node 
			self.start_node = new_node 
  
		else: 
			current = self.start_node 
			while(current.next is not None and current.next.loci < new_node.loci): 
				current = current.next
			new_node.next = current.next
			current.next = new_node
  
	#This method was added for debugging purposes
	def print_list(self):

		node = self.start_node
		linked_list_print = ""
		while node:
			linked_list_print =  linked_list_print + " -> " + node.name + " " + str(node.loci)
			node = node.next
		print (linked_list_print)

	def check_near_nodes(self):
		n_act = self.start_node
		count = 0

		f = open('out.txt', 'w')
		while n_act.next:
			last_location = n_act.loci
			next_location = n_act.next.loci
			#dist =  distance.euclidean(next_location, last_location)
			distance = dist(n_act, n_act.next)

			if (n_act.loci == n_act.next.loci) and (distance <= k):
					if next_location == last_location:
						count += 1

			else:
				n_act.float_to_loci()
				f.write('{0} {1}\n'.format(n_act.loci, count))
				count = 0
						
			n_act = n_act.next

		if n_act.next == None:
			n_act.float_to_loci()
			f.write('{0} {1}\n'.format(n_act.loci, count))


# Main zone

if __name__ == "__main__":

	linked_list = LinkedList()

	#Lets read the file
	with open(file_data) as data:

		for line in data:
			sequence = line.strip().split("\t")
			seq_id = sequence[0]
			coords = sequence[2]

			chromosome = (re.split(r"[p,q]+", sequence[1])[0])
			arm = (re.sub(r'\d+', '', sequence[1]))[:-1]

			if arm == "p": #Let's presume arm P is considerated 0.25 and Q is 0.75 for the insertion sort,
				 			#since its easier to compare by arithmetic functions
				loci = float(chromosome) + 0.25
			elif arm == "q":
				loci = float(chromosome) + 0.75

			new_node = Sequence(loci, coords, seq_id)
			linked_list.sortedInsert(new_node)
			

		linked_list.print_list()
		linked_list.check_near_nodes()









