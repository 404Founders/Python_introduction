print("You are standing at the cross section of Imperial Avenue and LaHarr Boulevard on the city planet Coruscant.")
print("On your right side is an elevator leading to the lower levels.")
choice = input("""Do you want to:  
        1.) Use the elevator to go to the lower levels
        2.) Go up north following Imperial Avenue, or
        3.) Follow LaHarr Boulevard going west? \n""")
#print(choice)
if choice == 1:
    print("""The Elevator takes you to the lower levels of Coruscant. 
    No sunlight comes here. Only artifical light sources illuminate the Bars, Shops and Businesses around you.""")
elif choice ==2:
    print("""You are walking north entering the Administration district. You pass the Kashyyk Embassy,
    a big building in a living tree and the Mon Calamari Embassy a floating bubble of water held together
    by artificial gravity fields.""")
else:
    print("""LaHarr Boulevard takes you the Museums district. You see the Alderaanian Musuem of contemporary Arts.""")