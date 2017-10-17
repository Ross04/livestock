#!/usr/bin/python

print ("Some input is required.  Please enter your method of recieveing money (hd. lbs., hd. cwt., hd., lbs., cwt., sale)")
method = raw_input("Please enter your method: ");
if method == 'hd. lbs.':
   print ("Please enter the price per lb.")
   price = int(raw_input())
   print ("Please enter the weight per head.")
   lbs = int(raw_input())
   print ("Please enter the head count.")
   head = int(raw_input())
   sale = lbs * price * head
elif method == 'hd. cwt.':
   print ("Please enter the price per cwt.")
   price = int(raw_input())
   print ("Please enter the weight per head.")
   lbs = int(raw_input())
   print ("Please enter the head count.")
   head = int(raw_input())
   sale = lbs / 100 * price * head
elif method == 'hd.':
   print ("Please enter the price per head.")
   price = int(raw_input())
   print ("Please enter the head count.")
   head = int(raw_input())
   sale = price * head
elif method == 'lbs.':
   print ("Please enter the total pounds.")
   lbs = int(raw_input())
   print ("Please enter the price per lb.")
   price = int(raw_input())
   sale = lbs * price
elif method == 'cwt.':
   print ("Please enter the total weight.")
   lbs = int(raw_input())
   print ("Please enter the price per cwt.")
   price = int(raw_input())
   sale = price / 100 * lbs
elif method == 'sale':
   print ("Please enter total sale reciepts")
   sale = int(raw_input())
print ("Please enter the total of other revenues")
other = int(raw_input())
print ("Please enter the total rent cost.")
rent = int(raw_input())
print ("Please enter the total labor cost.")
labor = int(raw_input())
print ("Please enter the total feed cost.")
feed = int(raw_input())
print ("Please enter the total mineral cost.")
mineral = int(raw_input())
print ("Please enter the total medicine cost.")
medicine = int(raw_input())
print ("Please enter total losses to deathes.")
death = int(raw_input())
profit = sale + other - rent - labor - feed - mineral - medicine - death
print ("Total profit is: "), profit
print ("Press c to close.")
close = str(raw_input())
print ("Thanks for using this!")


