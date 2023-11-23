def fizz_buzz():
    # ✅↓ Write your code here. ↓✅
    for valor in range(1,101):
        if valor % 3 == 0 and valor % 5 == 0:
            print("FizzBuzz")
        elif valor % 3 == 0:
            print("Fizz")
        elif valor % 5 ==0:
            print("Buzz")
        else: print(valor)        


# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()