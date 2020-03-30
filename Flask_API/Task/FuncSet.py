def fibonacci(n, fib=[0,1]):
	if type(n) is not int:
		n = int(n)
	if n >= len(fib):
		for i in range(len(fib), n+1):
			fib.append(fib[i-1]+fib[i-2])
	return str(fib[n])
	
def ackermann(m,n):
	if m==0:
		return n+1
	elif m>0 and n==0:
		return ackermann(m-1,1)
	elif m>0 and n>0:
		return ackermann(m-1,ackermann(m,n-1)) 

def factorial(n):
	answer = 1
	for i in range( 1, n+1):
		answer *= i
	return str(answer)