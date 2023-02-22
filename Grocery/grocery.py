def momGrocery():
	Grocery = ["eggs","milk","bread","yogurt","tomato","lettuce","green onion",
	           "cooking oil","olives","juice","flour","rice","mayonnaise","ketchup",
	           "hot sauce", "butter", "cream cheese","yellow cheese", "garlic",
	           "onion","spinach","garbage bag","kitchen bag", "apple","cucumber","bannana",
                   "red pepper", "green pepper", "potatoes", "grapes", "other fruit/vegetable"]

	counter = 0
	groceryDict = {}
	for elem in Grocery:
	    groceryDict[counter] = elem
	    counter += 1

	for key,val in groceryDict.items():
	    print("{0}: {1}".format(key,val))

	needLst = []
	print("\nEnter number needed and type {0} when finished".format("DONE"))
	while True:
	    strNum = input("Number: ")
	    if strNum.lower() == "done":
	        break
	    needLst.append(int(strNum))
	    
	print("\nThese are the items you need to buy:")
	for key in needLst:
	    print(groceryDict[key])

momGrocery()
    
    
 
