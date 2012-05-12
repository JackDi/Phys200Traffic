class Car(object):
	"""does car things"""
	#initializes the car
	def __init__(self,pos=0, array=[], v=0, vmax = 0, p=0, cruise_control=True):
		self.pos = pos
		self.array = array
		self.v = v
		self.vmax = vmax
		self.p = p
		self.g = 0
		self.cruise_control = True
	#checks how many spaces are in front	
	def check_front():
		i=1
		while pos+i <= len(self.array):
			#checks if the car leaves the array
			if pos+i >= len(array):
				if self.array[0] = empty:
					self.pos=0
					check_front()
				else:
					g = i-1
					return len(self.array)
			#+1 to empty space count
			elif array[pos+1] == empty:
				i = i+1
			#returns number of empty spaces ahead of it
			else:
				g = i-1
				return pos+i-1
	#makes v
	def check_velocity():
		#sets v = to g
		if self.v > self.g or self.v < self.g:
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
	def set_velocity():
		self.v = check_velocity()
	#I think you might need to reset each car's internal array each loop to match the actual visible array so here's this method though I think you could just do array[i].array = array or something
	def set_array(array=[]):
		self.array = array
			