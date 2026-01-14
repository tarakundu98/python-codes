numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)