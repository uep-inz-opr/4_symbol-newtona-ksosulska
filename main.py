

def new(n,k):
	if k==0 or k==n:
		return 1
	else:
		return new(n-1,k)+new(n-1,k-1)

n=int(input())
k=int(input())

print (int(new(n,k)))