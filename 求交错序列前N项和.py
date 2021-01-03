N = int(input())
print('{:.3f}'.format(sum([i/(i*2-1) if i%2==1 else -i/(i*2-1)  for i in range(1,N+1)])))
