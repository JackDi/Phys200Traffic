class Car(object):
	"""does car things"""
	#initializes the car
	def __init__(self,pos=0, vmax = 0, p=0, cruise_control=False):
		self.pos = pos
		self.vmax = vmax
		self.v = random.randint(0, self.vmax)
		self.p = p
		self.cruise_control = cruise_control
	#checks how many spaces are in front	
	def check_front(array=[]):
		arr = array
		i=1
		while pos+i <= len(arr):
			#checks if the car leaves the array
			if pos+i >= len(arr):
				if arr[0] == 0:
					self.pos = 0
					return i + check_front()
				else:
					return len(arr)
			#+1 to empty space count
			elif arr[pos+1] == 0:
				i = i+1
			#returns number of empty spaces ahead of it
			else:
				return pos+i-1
	#makes v
	def check_velocity(array=[]):
		arr = array
		#sets v = to g
		if self.v > check_front(arr) or self.v < check_front(arr):
			self.v = self.g
			#random chance of reducing speed
			if self.p > random() and self.v != self.vmax and cruise_control==True:
				self.v = self.v - 1
				return self.v
			else:
				return self.v
		else:
			if self.p > random() and self.v != self.vmax and cruise_control==True:
				self.v = self.v - 1
				return self.v
			else:
				return self.v
	#returns the new position
	def move_car(array=[]):
		arr = array
		x = self.pos + check_velocity(arr)
		#checks is the new position is greater than the length of the array and loops the car through
		if x >= len(arr):
			return x - len(arr)
		else:
			return x
	def set_velocity(array=[]):
		arr = array
		self.v = check_velocity(arr)
			