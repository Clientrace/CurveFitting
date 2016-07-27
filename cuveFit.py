import math

#fits exponential curve that scipy can't offer to ordinary individual.
def curve_fit(x,y):
	sumLnY = 0
	sumX2 = 0
	sumX = 0
	sumXLnY = 0
	N = len(x)

	for i in range(0,len(x)):
		sumLnY = sumLnY + math.log(float(y[i]))
		sumX2 = sumX2 + float(x[i])*float(x[i])
		sumX = sumX + float(x[i])
		sumXLnY = sumXLnY + float(x[i]) * math.log(float(y[i]))
		
	a = ((sumLnY * sumX2) - (sumX*sumXLnY))/((N*sumX2)-(sumX*sumX))
	b = ((N * sumXLnY)-(sumX * sumLnY))/((N*sumX2)-(sumX*sumX))
	
	
	A = math.exp(a)
	B = b
	
	return A,B
	
	
def main():
	#read sets of x and y
	print("Enter filename: ")
	fn = input()
	file = open(fn+".txt",'r')
	
	x = []
	y = []
	
	for line in file:
		data = line.split('\t')
		if(data[0]!='#'):
			x.append(data[0])
			y.append(data[1])
				
	A,B = curve_fit(x,y)
	
	
	print("A: "+str(A))
	print("B: "+str(B))
	
main()



















