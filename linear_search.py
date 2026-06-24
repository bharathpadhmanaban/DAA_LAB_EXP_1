numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

key = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")