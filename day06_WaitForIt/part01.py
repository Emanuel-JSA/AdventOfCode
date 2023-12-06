from functools import reduce

input_data = """Time:        51     69     98     78
Distance:   377   1171   1224   1505"""

split_data = input_data.splitlines()
clean_data = [line.split(":")[1] for line in split_data]
races = [line.split() for line in clean_data]

def ways_to_win(time_limit, distance):
    ways = 0
    print(f"Time: {time_limit}, Distance: {distance}")
    for i in range(time_limit):
        vel = i
        if vel * (time_limit - i) > distance:
            ways += 1
    return ways
        

def time_x_distance(races):
    win = []
    for time, distance in zip(races[0], races[1]):
        win.append(ways_to_win(int(time), int(distance)))    
    return win

print(reduce(lambda x, y: x*y, time_x_distance(races)))
