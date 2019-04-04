# Name: Arti Jain         
# Course: CPE 202
# Instructor: Hatalsky 
# Assignment: Lab 0 
# Term: Spring 2019

def weight_on_planets():
	weight_on_earth = input("What do you weigh on earth? ")
	weight = int(weight_on_earth)
	mars = weight * 0.38
	jupiter = weight * 2.34
	print ("\nOn Mars you would weigh", mars, "pounds.\nOn Jupiter you would weigh", jupiter, "pounds.")

   
if __name__ == '__main__':
   weight_on_planets()

