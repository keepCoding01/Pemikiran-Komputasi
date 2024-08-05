n = int(input())

customers = []
for i in range(n):
    order, prep = map(int, input().split())
    customers.append((i+1, order+prep))

customers.sort(key=lambda x: (x[1], x[0]))

for customer in customers:
    print(customer[0], end=" ")
