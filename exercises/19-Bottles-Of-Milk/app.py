# ✅↓ Write your code here. ↓✅
def number_of_bottles():
    for x in range(99,0,-1):
        if x==1:
                
            print(f"{x} bottle of milk on the wall, {x} bottle of milk. Take one down and pass it around, no more bottles of milk on the wall. No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"{x} bottles of milk on the wall, {x} bottles of milk. Take one down and pass it around, {x-1} bottles of milk on the wall.")
            

           

number_of_bottles()            