first= int(input())

second = int(input())

if second < first:
    print("Second integer can't be less than the first.")
else:
    for f in range(first, second + 1, 5):
        print(f, end=" ")
        
    print()
