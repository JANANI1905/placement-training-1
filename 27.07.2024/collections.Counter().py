from collections import Counter
num_shoes = int(input())

shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

num_customers = int(input())
total_earned = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
    
        total_earned += price
        inventory[size] -= 1

print(total_earned)
