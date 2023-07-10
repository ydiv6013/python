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
  "coffee" : 10000,
  "milk" : 10000,
  "water" : 10000
}

def availableresoucres(water,milk,coffee):

    water_qty = resources["water"] - water
    milk_qty = resources["milk"] - milk
    cofee_qty = resources["coffee"] - coffee
    print(water_qty,milk_qty,cofee_qty)
    print(resources)

    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    print(resources)

print(flavours)
option =input("Welcome to the python coffee.please enter coffee flavour as above : ")
qty =int(input("Please enter number of qty : "))

if flavours[0] == option :
    print("1.5")
    print(recipe[0]["flavour"])
    req_water_resource = qty * recipe[0]["water"]
    req_milk_resource = qty * recipe[0]["milk"]
    req_coffee_resource = qty * recipe[0]["cofee"]
    availableresoucres(req_water_resource,req_milk_resource,req_coffee_resource)
elif flavours[1] == option :
    print("2.5")
    print(recipe[1]["flavour"])
elif flavours[2] == option :
    print("3")
    print(recipe[2]["flavour"])
else :
    print("thanks for the coffee")
print(f"you have selected {option}")