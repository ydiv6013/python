
raw1 =["😀","😁","😊"]
raw2 =["😇","😉","😌"]
raw3 =["🥰","😘","😍"]
print(raw1,raw2,raw3)
#nested list

fruites = "Lemon,Lime,Loganberry,Longan,Loquat,Blood Orange,Papaya,Passion,Fruit,Peach,Pear"
vegitables = "lettuce, spinach, cabbage, cauliflower, Brussels sprouts, pumpkin, cucumber, potato, sweet potato"

fruites_list = fruites.split(',')
print("\n",fruites_list)

#split from comma with space , 
vegitables_list =vegitables.split(', ')
print("\n",vegitables_list)

veg = [ fruites_list , vegitables_list]
print("\n",veg)