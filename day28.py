A = [7,4,8,2,9]
count = 0 

for i in range(len(A)-1):
	if(i==0):
		count += 1 
	else:
		if(A[i-1] > A[i]):
			count += 1 

print(count)

