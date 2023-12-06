from functools import reduce

input_data = """Time:        51     69     98     78
Distance:   377   1171   1224   1505"""

split_data = input_data.splitlines()
clean_data = [line.split(":")[1] for line in split_data]
races = [line.replace(" ", "") for line in clean_data]

def ways_to_win(time_limit, distance):
    ways = 0
    for i in range(time_limit):
        vel = i
        if vel * (time_limit - i) > distance:
            ways += 1
    return ways
        

def time_x_distance(races):
    win = 0
    win = ways_to_win(int(races[0]), int(races[1]))    
    return win

print(time_x_distance(races))
