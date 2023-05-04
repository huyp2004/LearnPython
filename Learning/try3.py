n, k = map(int, input().split())
books = list(map(int, input().split()))

combinations = []
for i in range(n+k):
    combination = list(map(int, input().split()))
    combinations.append(combination)

valid_combinations = []
for combination in combinations:
    total = sum(books[i-1] for i in combination)
    if total == n:
        valid_combinations.append(combination)

valid_combinations.sort()
for combination in valid_combinations:
    print(*combination)
