def my_name():
    print("my name is bader")
    my_name()
    def my_meal(food, drink):
        print(f"i like to eat {food} while drinking {drink}")
        my_meal("pizza", "oj")

def cube(number):
    return number **3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
    
print(cube(2))
print(by_three(3))