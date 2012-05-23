class Car(object):
	"""does car things"""
	#initializes the car
	def __init__(self,pos=0, array=[], v=0, vmax = 0, p=0, cruise_control=True):
		self.pos = pos
		self.array = array
		self.v = v
		self.vmax = vmax
		self.p = p
		self.cruise_control = True
	#checks how many spaces are in front	
	def check_front():
		i=1
		while pos+i <= len(self.array):
			#checks if the car leaves the array
			if pos+i >= len(array):
				if self.array[0] = empty:
					self.pos=0
					return i + check_front()
				else:
					return len(self.array)
			#+1 to empty space count
			elif array[pos+1] == empty:
				i = i+1
			#returns number of empty spaces ahead of it
			else:
				return pos+i-1
	#makes v
	def check_velocity():
		#sets v = to g
		if self.v > check_front() or self.v < check_front():
			self.v = self.g
			#random chance of reducing speed
			if self.p > random() and self.v != self.vmax and cruise_control==True:
				self.v = self.v - 1
				return v
			else:
				return v
		else:
			if self.p > random() and self.v != self.vmax and cruise_control==True:
				self.v = self.v - 1
					return v
			else:
				return v
	def move_car():
		x = self.pos + check_velocity()
		#checks is the new position is greater than the length of the array and loops the car through
		if x >= len(self.array)
			return x - len(self.array)
		else
			return x
	def set_velocity():
		self.v = check_velocity()
	#I think you might need to reset each car's internal array each loop to match the actual visible array so here's this method though I think you could just do array[i].array = array or something
	def set_array(array=[]):
		self.array = array
			