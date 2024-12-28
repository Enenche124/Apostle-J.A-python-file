print("Welcome to Iya moses pizza joint Ajegunle")
number_of_guest = int(input("Enter number of your guest: "))
print("Below is our pizza menu")

print("""
     1.  Sapa size          4                2,500
	
     2.  Small money        6                2,900

     3.  Big boys           8                4,000
	
     4. odogwu             12               5,200


 """)
 
sapa_price, small_money_price, big_boys_price,odogwu_price  = 2500, 2900, 4000, 5200 

sapa_slice, small_money_slice, big_boys_slice, odogwu_slice = 4, 6, 8, 12


boxes_of_pizza_to_buy = number_of_guest // sapa_slice
if(number_of_guest % sapa_slice != 0): boxes_of_pizza_to_buy+=1


boxes_of_pizza_to_buy2 = number_of_guest // small_money_slice
if(number_of_guest % small_money_slice != 0): boxes_of_pizza_to_buy2+=1


boxes_of_pizza_to_buy3 = number_of_guest // big_boys_slice
if(number_of_guest % big_boys_slice != 0): boxes_of_pizza_to_buy3+=1


boxes_of_pizza_to_buy4 = number_of_guest // odogwu_slice
if(number_of_guest % odogwu_slice != 0): boxes_of_pizza_to_buy4+=1

 

after_serving = boxes_of_pizza_to_buy * sapa_slice
left_over = after_serving - number_of_guest

after_serving2 = boxes_of_pizza_to_buy2 * small_money_slice
left_over2 = after_serving2 - number_of_guest

after_serving3 = boxes_of_pizza_to_buy3 * big_boys_slice
left_over3 = after_serving3 - number_of_guest

after_serving4 = boxes_of_pizza_to_buy4 * odogwu_slice
left_over4 = after_serving4 - number_of_guest
 
while (True):
  type_of_pizza = int(input("Select between (1-4) the type of pizza you want: "))
  if (type_of_pizza == 1):
     print("Number of boxes to buy is ", boxes_of_pizza_to_buy, "Left over after serving is ", left_over, "Amount to pay is ",  boxes_of_pizza_to_buy*sapa_price)
  elif (type_of_pizza == 2):
     print("Number of boxes to buy is ", boxes_of_pizza_to_buy2, "Left over after serving is ", left_over2, "Amount to pay is ",  boxes_of_pizza_to_buy2*small_money_price)
  elif (type_of_pizza == 3):
     print("Number of boxes to buy is ", boxes_of_pizza_to_buy3, "Left over after serving is ", left_over3, "Amount to pay is ",  boxes_of_pizza_to_buy3*big_boys_price)
  elif (type_of_pizza == 4):
     print("Number of boxes to buy is ", boxes_of_pizza_to_buy4, "Left over after serving is ", left_over4, "Amount to pay is ",  boxes_of_pizza_to_buy4*odogwu_price)
  break