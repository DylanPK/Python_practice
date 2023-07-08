weight = 4.8
cost = 0
cost_ground_premium = 125

#Ground Shipping
if weight <= 2:
    cost = (weight*1.50)+20
elif weight <= 6:
    cost = (weight*3)+20
elif weight <= 10:
    cost = (weight*4)+20
elif weight > 10:
    cost = (weight*4.75)+20
else:
    print("Error. Weight is not defined")
print(cost)

#Ground Shipping Premium
print("Ground Shipping Premium $", cost_ground_premium)

#Drone Shipping
#Ground Shipping
if weight <= 2:
    cost = (weight*4.50)
elif weight <= 6:
    cost = (weight*9)
elif weight <= 10:
    cost = (weight*12)
elif weight > 10:
    cost = (weight*14.25)
else:
    print("Error. Weight is not defined")
print(cost)