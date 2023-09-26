import math
import random
from endpoint import Endpoint

def go_home(pub_x, pub_y, step_size, max_steps):
    # Set the drunk man's initial position
    man_pos = get_starting_pos(home_pub_distance)
    steps = 0
    current_endpoint = get_reached_endpoint(man_pos, 0, home_pub_distance)

    # Take steps until an endpoint is reached or until max steps reached
    while steps < max_steps and current_endpoint == Endpoint.NONE:
        man_pos = take_step(man_pos, step_size)

        draw_progress(man_pos, home_pub_distance)

        current_endpoint = get_reached_endpoint(man_pos, home_pub_distance)

    draw_end(current_endpoint)

def get_starting_pos(pub_x, pub_y):
    return math.ceil(home_pub_distance / 2)

def take_step(current_pos, step_size):
    direction = random.choice([-1, 1])
    pos_delta = step_size * direction

    return current_pos + pos_delta

def get_reached_endpoint(current_pos, home_pub_distance):
    if current_pos == 0:
        return Endpoint.HOME
    elif current_pos == home_pub_distance:
        return Endpoint.PUB
    else:
        return Endpoint.NONE

def draw_progress(current_pos, home_pub_distance):
    distance_home = current_pos - 1
    distance_pub = home_pub_distance - current_pos

    print("home ")
    print(". " * distance_home)
    print("* ")
    print(". " * distance_pub)
    print("pub")

def draw_end(endpoint):
    if endpoint == Endpoint.NONE:
        print()