import math

def main():
    cans = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]
    
    can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    can_radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    highest_storage_efficiency = 0
    highest_cost_efficiency = 0

    for i in range(len(can_names)):
        radius = can_radii[i]
        height = can_heights[i]
        cost = can_costs[i]

        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        if storage_efficiency > highest_storage_efficiency:
            highest_storage_efficiency = storage_efficiency
            highest_storage_efficiency_index = i
            
        if cost_efficiency > highest_cost_efficiency:
            highest_cost_efficiency = cost_efficiency
            highest_cost_efficiency_index = i

        print(f"{can_names[i]} {storage_efficiency:.2f} {cost_efficiency:.2f}")
        
    print()
    print(f"Highest storage efficiency: {can_names[highest_storage_efficiency_index]} with an efficiency of {highest_storage_efficiency:.2f}")    
    print(f"Highest cost efficiency: {can_names[highest_cost_efficiency_index]} with an efficiency of {highest_cost_efficiency:.2f}")
    return 0


def compute_cost_efficiency(radius, height, cost):
    return compute_volume(radius, height) / cost


def compute_storage_efficiency(radius, height):
    """Computes storage efficiency of a can based on radius and height."""
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area


def compute_volume(radius, height):
    """Computes volume of a can based on radius and height."""
    return math.pi * radius ** 2 * height


def compute_surface_area(radius, height):
    """Computes surface area of a can based on radius and height."""
    return 2 * math.pi * radius * (radius + height)


main()