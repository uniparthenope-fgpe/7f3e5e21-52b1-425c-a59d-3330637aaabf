def calculate_travel_cost(distance, fuel_efficiency, fuel_price):
    cost = distance / fuel_efficiency * fuel_price
    return cost

print(calculate_travel_cost(1000, 5, 2))