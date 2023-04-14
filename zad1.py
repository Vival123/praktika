for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # если число i делится на 3 и на 5
        print("FizzBuzz")
    elif i % 3 == 0:   # если число i делится на 3
        print("Fizz")
    elif i % 5 == 0:   # если число i делится на 5
        print("Buzz")
    else:
        print(i)