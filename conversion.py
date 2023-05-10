# Conversion of epsilon-NFA to DFA and visualization using Graphviz
# this code developed by Kirollos George
from graphviz import Digraph

class NFA:
	def __init__(self, no_state, states, no_alphabet, alphabets, start,
				no_final, finals, no_transition, transitions):
		self.no_state = no_state
		self.states = states
		self.no_alphabet = no_alphabet
		self.alphabets = alphabets
		
		# Adding epsilon alphabet to the list
		# and incrementing the alphabet count
		self.alphabets.append('e')
		self.no_alphabet += 1
		self.start = start
		self.no_final = no_final
		self.finals = finals
		self.no_transition = no_transition
		self.transitions = transitions
		self.graph = Digraph()

		# Dictionaries to get index of states or alphabets
		self.states_dict = dict()
		for i in range(self.no_state):
			self.states_dict[self.states[i]] = i
		self.alphabets_dict = dict()
		for i in range(self.no_alphabet):
			self.alphabets_dict[self.alphabets[i]] = i
			
		# transition table is of the form
		# [From State + Alphabet pair] -> [Set of To States]
		self.transition_table = dict()
		for i in range(self.no_state):
			for j in range(self.no_alphabet):
				self.transition_table[str(i)+str(j)] = []
		for i in range(self.no_transition):
			self.transition_table[str(self.states_dict[self.transitions[i][0]])
								+ str(self.alphabets_dict[
									self.transitions[i][1]])].append(
										self.states_dict[self.transitions[i][2]])

	# Method to get input from User
	@classmethod
	def fromUser(cls):
		no_state = int(input("Number of States : "))
		states = list(input("States : ").split())
		no_alphabet = int(input("Number of Alphabets : "))
		alphabets = list(input("Alphabets : ").split())
		start = input("Start State : ")
		no_final = int(input("Number of Final States : "))
		finals = list(input("Final States : ").split())
		no_transition = int(input("Number of Transitions : "))
		transitions = list()
		print("Enter Transitions (from alphabet to) (e for epsilon): ")
		for i in range(no_transition):
			transitions.append(input("-> ").split())
		return cls(no_state, states, no_alphabet, alphabets, start,
				no_final, finals, no_transition, transitions)

	# Method to represent quintuple
	def __repr__(self):
		return "Q : " + str(self.states)+"\nΣ : "
		+ str(self.alphabets)+"\nq0 : "
		+ str(self.start)+"\nF : "+str(self.finals) + \
			"\nδ : \n" + str(self.transition_table)

	def getEpsilonClosure(self, state):
	
		# Method to get Epsilon Closure of a state of NFA
		# Make a dictionary to track if the state has been visited before
		# And a array that will act as a stack to get the state to visit next
		closure = dict()
		closure[self.states_dict[state]] = 0
		closure_stack = [self.states_dict[state]]

		# While stack is not empty the loop will run
		while (len(closure_stack) > 0):
		
			# Get the top of stack that will be evaluated now
			cur = closure_stack.pop(0)
			
			# For the epsilon transition of that state,
			# if not present in closure array then add to dict and push to stack
			for x in self.transition_table[
					str(cur)+str(self.alphabets_dict['e'])]:
				if x not in closure.keys():
					closure[x] = 0
					closure_stack.append(x)
			closure[cur] = 1
		return closure.keys()

	def getStateName(self, state_list):
	
		# Get name from set of states to display in the final DFA diagram
		name = ''
		for x in state_list:
			name += self.states[x]
		return name

	def isFinalDFA(self, state_list):
	
		# Method to check if the set of state is final state in DFA
		# by checking if any of the set is a final state in NFA
		for x in state_list:
			for y in self.finals:
				if (x == self.states_dict[y]):
					return True
		return False


