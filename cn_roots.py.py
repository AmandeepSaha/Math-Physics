import numpy as np
import cmath as cm
import matplotlib.pyplot as plt


class Solution:
	def __init__(self):
		self.x = int(input("Real: "))
		self.y = int(input("Imaginary: "))
		self.powr = int(input("Power: "))
		self.r,self.theta = cm.polar(complex(self.x,self.y))[0],cm.polar(complex(self.x,self.y))[1]

	def __str__(self):
		return f"{self.roots()}"

	def roots(self):
		self.roots_lst = []
		for i in range(self.powr):
			self.arg = np.exp((self.theta+2*i*np.pi)/self.powr)
			self.root = cm.rect(self.r,self.arg)
			self.roots_lst.append(self.root)
		return np.array(self.roots_lst)


	def position(self):
		plt.title(f"z = {complex(self.x,self.y)}")
		plt.grid(True)
		plt.xlabel(r"$Re\longrightarrow$")
		plt.ylabel(r"$Im\longrightarrow$")
		plt.plot(self.roots(),".")
		plt.show()