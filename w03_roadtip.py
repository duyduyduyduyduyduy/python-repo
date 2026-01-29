trip_name = input("What's the trip name? ")
driver_name = input("Who's the driver? ")
car_model = input("What's the car model? ")
first_stop = input("Where's the first stop? ")
last_stop = input("Where'sn the last stop? ")
items_packed = int(input("How many items are you packing? "))
items_list = []

total_miles = float(input("What's the total milage? "))
miles_per_gallon = float(input("What's the milage per gallon? "))
price_per_gallon = float(input("What's the price per gallon? "))

for i in range(items_packed):
    items_list.append(input("item:"))

destination = [first_stop, last_stop]
distances = [total_miles, miles_per_gallon, price_per_gallon]

gas_cost = (distances[0] / distances[1]) * distances[2]

print("Trip:", trip_name)
print("Driver:", driver_name)
print("First stop:", distances[0])
print("Last stop:", distances[len(destination) - 1])
print(f"Total distance:, {total_miles:.1f} miles")
print(f"Estimated gas cost: $ {gas_cost:.2f}")
print("Items to pack:", items_list)