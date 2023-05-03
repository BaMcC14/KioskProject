import os #imporint os to delete txt file if needed.
import sys #importing sys to close program. 

#mainMenu function - Starts the program - Gives the user options to close the program or order
def mainMenu():
  print("---Welcome to our Pizza Shop---\n")
  menuOption = input('Please enter: \n\"order\" to order food \n\"exit\" to exit the program:\n')
  menuOptionLower = menuOption.lower()
  if menuOptionLower == "exit":
    sys.exit("Program is closed")
    
  elif menuOptionLower == "order":
    orderMenu()
  else:
    mainMenu()


#orderMenu function - From here the user selects food and drink and is sent to confirm the order.
def orderMenu():
  print("\nPlease Order Food or Drinks and type finish when done.\n")
  orderLength = len(customerOrder)
  customerSelection = input('Please enter:\n\'food\', \'drink\', or \'finish\'\n')
  customerSelectionLower = customerSelection.lower()
  if customerSelectionLower == "food":
    foodMenu()
  elif customerSelectionLower == "drink":
    drinkMenu()
  elif customerSelectionLower == "finish" and orderLength > 0:
    confirmingTransaction()
  else:
    print("Order can not be empty.")
    orderMenu()


#foodMenu function - This function calls for user to select thier food choice
def foodMenu():
  print("\nThese are the Pizza options.")
  customerFoodChoice = input('Please enter one item at a time and press enter:\n\"pepperoni\"  for Pepperoni Pizza - 10.99 \n\"cheese\"     for Cheese Pizza - 9.99\n\"veggie\"     for Veggie Pizza - 11.99\n\"meat\"       for Meat Pizza - 13.99\n')
  global customerTotal 
  if customerFoodChoice == "pepperoni":
    customerOrder.append("Pepperoni Pizza - 10.99")
    customerTotal += pepperoniePizza
    print("\nPepperoni Pizza added to order. \n")
    orderMenu()
  elif customerFoodChoice == "cheese":
    customerOrder.append("Cheese Pizza - 9.99")
    customerTotal += cheesePizza
    print("\nCheese Pizza added to order. \n")
    orderMenu()
  elif customerFoodChoice == "veggie":
    customerOrder.append("Veggie Pizza - 11.99")
    customerTotal += veggiePizza
    print("\nVeggie Pizza added to order. \n")
    orderMenu()
  elif customerFoodChoice == "meat":
    customerOrder.append("Meat Pizza - 13.99")
    customerTotal += meatPizza
    print("\nMeat Pizza added to order. \n")
    orderMenu()
  else:
    foodMenu()


#drinkMenu function - This function calls for user to select thier drink choice
def drinkMenu():
  customerDrinkChoice = input('Please enter one item at a time and press enter: \n\"cola\"     for cola - 2.00 \n\"dietcola\" for Dietcola - 2.00  \n\"water\"    for water - 1.50\n')
  global customerTotal
  if customerDrinkChoice == "cola":
    customerOrder.append("Cola - 2.00")
    customerTotal += colaDrink
    print("\nCola added to order. \n")
    orderMenu()
  elif customerDrinkChoice == "dietcola":
    customerOrder.append("Dietcola - 2.00")
    customerTotal += dietcolaDrink
    print("\nDietcola added to order. \n")
    orderMenu()
  elif customerDrinkChoice == "water":
    customerOrder.append("Water - 1.50")
    customerTotal += waterDrink
    print("\nWater added to order. \n")
    orderMenu()
  else:
    drinkMenu()


#confirmingTransaction function - The user is shown the order summery and confirms or cancels the order. If confirmed the order is appended to a txt file. The file is created if it does not exist.
def confirmingTransaction():
  global ticketNumber
  global customerTotal
  customerOrder.append('\nCustomer Total: ' + str(customerTotal))
  customerOrder.append('Ticket Number: ' + str(ticketNumber) + "\n")
  print('\n')
  for i in customerOrder:
    print(i)
  customerConfirmation = input("\nIf your order is correct type \'confirm\' if order is incorrect type \'cancel\'\n")
  if customerConfirmation == "confirm":
    #This code will try to open/append the customerOrder to the txt file.
    try:
      fout = open('customerOrders.txt', 'a')
      for i in customerOrder:
        fout.write("\n"+ i )
      fout.close()
      print('\nYour order will be ready soon.\n')
    except: 
      print('\nAn error writing to the file has accured\n')
      mainMenu()
    customerTotal = 0.00
    customerOrder.clear()
    ticketNumber += 1
    mainMenu()
  elif customerConfirmation == "cancel":
    print("Order has been canceled")
    customerOrder.clear()
    customerTotal = 0.00
    mainMenu()
  else:
    confirmingTransaction()

#Main Program 
#Variables to track 
ticketNumber = 1
customerOrder = []
customerTotal = 0.00

#menu item prices
pepperoniePizza = 10.99
cheesePizza = 9.99
veggiePizza = 11.99
meatPizza = 13.99
colaDrink = 2.00
dietcolaDrink = 2.00
waterDrink = 1.50

#This is the start of the main menu. 
mainMenu()

#Uncommiting this will delete the txt file when ran!!!
#This will remove the customerOrder.txt file!!! 
#os.remove("customerOrders.txt")









