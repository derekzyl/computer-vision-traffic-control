

def calculate_light_time(max_in_x, max_in_y, type, max_cars_in_lane=20, base_green_light_time=60):


    match type:
        case "x":
            if max_in_x ==0 and max_in_y==0:
                cars_in_lane = 0   
            else:
                cars_in_lane = max_in_x
        case "y":
            if max_in_x ==0 and max_in_y==0:
                cars_in_lane = 0   
            else:
                cars_in_lane = max_in_y

    


    
    # Calculate green light time based on the number of cars in the lane
    green_light_time = base_green_light_time *   (1 if cars_in_lane == 0 else cars_in_lane / max_cars_in_lane) 
    return  green_light_time
    


