def back_to_sender(number_of_successful_delivery):
  wages, base_pay = 0, 5000
  if(number_of_successful_delivery == 0): print("No bonus for the rider today, pay him/her only ", base_pay, " for base pay, And give him/her a warning letter" )
  
  amount_per_parcel_for_less_than_fifty_percent, amount_per_parcel_in_range_fifty_to_fifty_nine,amount_per_parcel_in_range_sixty_to_sixty_nine, amount_per_parcel_in_range_seventy_to_hundred = 160, 200, 250, 500
 
 
  if(number_of_successful_delivery < 50):
     wages = number_of_successful_delivery * amount_per_parcel_for_less_than_fifty_percent + base_pay
     
     
  elif(number_of_successful_delivery <= 59):  
      wages = number_of_successful_delivery * amount_per_parcel_in_range_fifty_to_fifty_nine + base_pay
      
      
  elif(number_of_successful_delivery <= 69):  
      wages = number_of_successful_delivery * amount_per_parcel_in_range_sixty_to_sixty_nine + base_pay
      

  elif(number_of_successful_delivery >= 70):  
      wages = number_of_successful_delivery * amount_per_parcel_in_range_seventy_to_hundred + base_pay      
            

  return wages
  
  
rider_total_delivery = int(input("Enter rider total delivery for the day: "))
  
print(back_to_sender(rider_total_delivery))