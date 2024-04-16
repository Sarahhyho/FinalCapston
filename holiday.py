#Define options for the different city destinations
def destinations():
    print("Destination options: \n 1 = Paris \n 2 = Tokyo \n 3 = California")


#Request user input and set flight price based on chosen destination
destinations()
#city_flight = int()
city_flight = int(input("Please enter the number representing your travel destination: "))
num_nights = int(input("Please enter number of nights of hotel stay: "))
rental_days = int(input("Please enter number of days of car hire: "))



#Create function to calculate hotel cost
def hotel_cost(num_nights):
    return (num_nights * 200)   # assuming nightly stay costs $200

print("\nCost breakdown: \nHotel costs: " + str(hotel_cost(num_nights)))



#Create function to calculate plane cost
def plane_cost(city_flight):
     if city_flight == 1:
        return 500
     elif city_flight == 2:
        return 400
     elif city_flight == 3:
        return 300
     else:
        print("\nError. Invalid choice. Please restart & select one of the 3 destination options. \n")
        return 0   # return 0 if invalid choice
     
print("Flight costs: " + str(plane_cost(city_flight)))



#Create function to calculate cost for car rental
def car_rental(rental_days):
    return (rental_days * 10)   # assuming daily rental costs $10

print ("Car rental costs: " + str(car_rental(rental_days)))



#Create function to calculate total holiday cost base of the 3 costs elements
def holiday_cost(hotel_cost, plane_cost, car_rental):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    rental = car_rental(rental_days)
    return hotel + plane + rental


# Print grand total of holiday cost
print (f"TOTAL COST FOR THE HOLIDAY: " + str(holiday_cost(hotel_cost,plane_cost, car_rental)))


