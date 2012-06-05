import random
class Car(object):
	"""does car things"""
	#initializes the car
	def __init__(self,pos=0, vmax = 0, p=0, cruise_control=False):
		self.pos = pos
		self.vmax = vmax
		self.v = random.randint(1, self.vmax)
		self.p = p
		self.cruise_control = cruise_control
	#checks how many spaces are in front    
	def check_front(self,array=[]):
		arr = array
		i=1
		while self.pos+i <= len(arr):
			#checks if the car leaves the array
			if self.pos+i >= len(arr):
				if arr[0] == 0:
					self.pos = 0
					return i + self.check_front(arr)
				else:
					return len(arr)
			#+1 to empty space count
			elif arr[self.pos+1] == 0:
				i = i+1
			#returns number of empty spaces ahead of it
			else:
				return self.pos+i-1
	#makes v
	def check_velocity(self,array=[]):
		arr = array
		#sets v = to check_front
		if self.v >= self.vmax:
			self.v = self.vmax
		else:
			self.v = self.v+1
		if self.v > self.check_front(arr):
			self.v=self.check_front(arr)
		if self.p > random.random() and self.v != self.vmax and self.cruise_control==True:
			self.v = self.v - 1
			return self.v
		else:
			return self.v
	#returns the new position
	def move_car(self,array=[]):
		arr = array
		x = self.pos + self.check_velocity(arr)
		#checks if the new position is greater than the length of the array and loops the car through
		if x >= len(arr):
			return x - len(arr)
		else:
			return x
