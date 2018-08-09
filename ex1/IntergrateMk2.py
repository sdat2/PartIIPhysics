import numpy as np
import operator
import matplotlib.pyplot as plt
def function(coordinate):
	return np.sin(coordinate)

def Monte_Gradual_integrate(Lower_Limit=0,Upper_Limit=np.pi/8,Dimensions=8,N=10):
	count_in=0; square_count_in=0;Results=[];Error=[] 
	Volume = (Upper_Limit-Lower_Limit)**Dimensions
	
	for i in range(1,int(N)+1):
		coordinate = 0
		for j in range(int(Dimensions)):
			coordinate += np.random.rand()*(Upper_Limit-Lower_Limit) + Lower_Limit
		count_in+=float(function(coordinate)); square_count_in += float((function(coordinate))**2)
		#print(count_in, square_count_in)
		Results.append(Volume*count_in/i)
		Error.append(Volume*(np.power(((-np.power(((count_in)/i),2)+(square_count_in/i))/i),0.5)))
	return [x*10**6 for x in Results], [x*(10**6) for x in Error]
N=1000
Results, Error = Monte_Gradual_integrate(N=N)


plt.plot(range(1,len(Results)+1),Results,color='black')
plt.plot(range(1,len(Results)+1),list(map(operator.sub, Results, Error)),color='blue')
NError = [-x for x in Error]
plt.plot(range(1,len(Results)+1),list(map(operator.sub,Results,NError)),color='blue')
plt.xlabel('Number of Random Numbers (N)')
plt.title('Monte Carlo Integration Test')
plt.savefig('New_Plot.pdf')
plt.clf()

plt.plot(range(1,len(Results)+1),[x-537.1873411 for x in Results],color='black')
plt.plot(range(1,len(Results)+1),[x-537.1873411 for x in list(map(operator.sub, Results, Error))],color='blue')
NError = [-x for x in Error]
plt.plot(range(1,len(Results)+1),[x-537.1873411 for x in list(map(operator.sub,Results,NError))],color='blue')
plt.xlabel('Number of Random Numbers (N)')
plt.ylabel('Result-537.183411')
plt.title('Monte Carlo Integration Test')
plt.savefig('Comparative_Plot.pdf')
u = [537.183411/x for x in range(10,1000)]
l = [-537.183411/x for x in range(10,1000)]
plt.plot(range(10,1000),u,color='green')
plt.plot(range(10,1000),l,color='green')
plt.savefig('Compartative_Plot_Add_Lines.png')
