def decor(func):
    def wrapper():
        print("Sprinkles Added")
        func()
    return wrapper

def drinks(func):
    def wrapper():
        print("Drinks Added")
        func()
    return wrapper

@decor
@drinks
def get_ice_cream():
    print("Here is your ice cream")
   

get_ice_cream() 
