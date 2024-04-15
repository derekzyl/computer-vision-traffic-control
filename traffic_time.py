

def calculate_light_time(max_in_x, max_in_y, type, max_cars_in_lane=20, base_green_light_time=60)->float:
    cars_in_lane =0 
    # Calculate the number of cars in the lane

    match type:
        case "x":
            if max_in_x ==0 and max_in_y==0:
                cars_in_lane = 1   
            else:
                cars_in_lane = max_in_x
        case "y":
            if max_in_x ==0 and max_in_y==0:
                cars_in_lane = 1
            else:
                cars_in_lane = max_in_y

    


    
    # Calculate green light time based on the number of cars in the lane
    green_light_time = base_green_light_time *   (cars_in_lane / max_cars_in_lane) 
    green_light_time = min(green_light_time, 90)
    return  green_light_time
    


