def square_numbers(start, end):
    squares = []
    odd = []
    even = []

    for i in range(start, end + 1):
        squares.append(i ** 2)

    for num in squares:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print("Squares:", squares)
    print("Odd squares:", odd)
    print("Even squares:", even)

square_numbers(1, 5)