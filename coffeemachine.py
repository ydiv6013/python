print("""
+-++-++-++-++-++-+ +-++-++-++-++-++-++-+
|C||o||f||f||e||e| |m||a||c||h||i||n||e|
+-++-++-++-++-++-+ +-++-++-++-++-++-++-+

"""
)
flavours = ["Espresso","Latte","Cappuccino"]
recipe = [
    {
        "flavour" : 'Espresso',
        "water" : 50,
        "milk" : 0,
        "cofee" : 18,
        "price" : 1.50,
    },
    {
        "flavour" : 'Latte',
        "water" : 200,
        "milk" : 150,
        "cofee" : 24,
        "price" : 2.50
    },
     {
        "flavour" : 'Cappuccino',
        "water" : 250,
        "milk" : 100,
        "cofee" : 24,
        "price" : 3.00
    },
]

water_qty = 0
milk_qty = 0
cofee_qty = 0
#Coffee is in Grms,milk is in ml,water is in ml
resources ={
  "coffee" : 3000,
  "milk" : 5000,
  "water" : 7500
}

def availableresoucres(water,milk,cofee):

    print("asdxc")
    
print(flavours)
option =input("Welcome to the python coffee.please enter coffee flavour as above : ")
qty =int(input("Please enter number of qty : "))

if flavours[0] == option :
    print("1.5")
    print(recipe[0]["flavour"])
elif flavours[1] == option :
    print("2.5")
    print(recipe[1]["flavour"])
elif flavours[2] == option :
    print("3")
    print(recipe[2]["flavour"])
else :
    print("thanks for the coffee")
print(f"you have selected {option}")