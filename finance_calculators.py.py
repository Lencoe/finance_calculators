import math
import os

#first line give the user an opportunity to choose the they want to calculate their investment bond repayment
print("\nchoose either *investment* or *bond* from the menu below to proceed:\n")

print("investment    -to calculate the amount of interest you will earn on interest")

print("bond          -to calculate the amount you will have to pay on a home loan\n")

#below code will take the input from user and turn it into a lower cases

choice =input()
choice_made = choice.lower()

#if they decide to calculate the investment the program will give the option to choose if the want simple or compound investment

if choice_made == "investment" :
  deposit = int(input("Enter the amount you want to deposit : "))
  interest_rate = int(input("Enter the interest rate without the % simbol : "))
  number_of_years =int(input("Enter the the number of years you are investing : "))


#code below asks the user if the want a *Simple* or *compound* interest and converts the input into lowercases

  interest = input("DO you want a *Simple* or *compound* interest : ")
  interest1 = interest.lower()
  
#the choice is *simple* the program calculates and display the total the user will get after the interest is applied
  
  if interest1 == "simple" :
    interest_entered = interest_rate/100
    total_amount = deposit*(1+interest_entered*number_of_years)
    print("The total amount after the interest is being applied is : "+str(total_amount))

#the choice is *compound* the program calculates and display the total the user will get after the interest is applied
    
  elif interest1 == "compound" :
    interest_entered = interest_rate/100
    total_amount = deposit*math.pow((1+interest_entered),number_of_years)
    print("The total amount after the interest is being applied is : "+str(total_amount))
  
       
##if they decide to calculate the bond the program will ask for all neccesary inputs and calculated the amount need to be repayed monthly

elif choice_made == "bond" :
  present_value = int(input("\nEnter the present value of the house : "))
  interest_rate = int(input("Enter your enterest : "))
  number_months = int(input("Enter number of months you plan to take to repay the bond : "))
  monthly_interest = interest_rate/12
  repayment = (monthly_interest*present_value)/(1-math.pow((1+monthly_interest),(-number_months)))
  print("\nthe amount that you need to repay monthly is : "+str(repayment))
  print("\n")
# we use os.system("pause")  code to prevent the auto consol close
os.system("pause") 
  
