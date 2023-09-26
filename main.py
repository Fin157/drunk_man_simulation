import pos_helpers as position
import random
from typing import List, Tuple
from endpoint import *

def go_home(pub_x: int, pub_y: int, max_step_size: int, max_steps: int) -> None:
    # Initialization
    home_point = Endpoint2D("The drunk man was able to get home safely.", 'H', 0, 0)
    pub_point = Endpoint2D("Oh no! Ended in the pub again!", 'P', pub_x - 1, pub_y - 1)
    endpoints = (home_point, pub_point)
    pos = position.get_middle(home_point.position, pub_point.position)
    steps = 0

    # Walk until any ending point (either home or pub) is hit or until the max steps limit is reached
    while steps < max_steps and not position.compare(pos, home_point.position) and not position.compare(pos, pub_point.position):
        pos = take_step(pos, home_point.position, pub_point.position, max_step_size)
        print_progress(pos, endpoints)
        steps += 1

    # Inform the user of the result of this simulation run
    print_end(pos, endpoints, "The drunk man got nowhere and fell asleep.")
    
def take_step(pos: List[int], home_pos: Endpoint, pub_pos: Endpoint, max_step_size) -> List[int]:
    directions_relative = ((0, max_step_size), (0, -max_step_size), (max_step_size, 0), (-max_step_size, 0))
    directions_absolute = list()

    for dir_rel in directions_relative:
        dir_abs = position.offset_clamped(pos, dir_rel, home_pos, pub_pos)
        if not position.is_on_edge(dir_abs, home_pos, pub_pos):
            directions_absolute.append(dir_abs)

    return random.choice(directions_absolute)

def print_progress(pos: List[int], endpoints: Tuple[Endpoint], iteration_num: int) -> None:
    print(f"\nIteration number {iteration_num}:")

    walk_area = position.offset_pos(endpoints[1].position, position.scalar_multiply(endpoints[0].position, -1))
    # We need to add 1 to the walk area size to compensate for us saving it as a zero-based integer
    line = ["."] * (walk_area[0] + 1)
    screen = line * (walk_area[1] + 1)
    screen[pos[0]][pos[1]] = "*"
    for endpoint in endpoints:
        screen[endpoint.position[0]][endpoint.position[1]] = endpoint.char

    for row in screen:
        for char in row:
            print(char, end=" ")
        print()

def print_end(pos: List[int], endpoints: Tuple[Endpoint], no_endpoint_mess: str) -> None:
    # For each endpoint in the endpoints list
    for endpoint in endpoints:
        # Compare the drunk man's position with the current endpoint's position
        if position.compare(pos, endpoint.position):
            # If the positions match, print this endpoint's end message and return out of the function
            print(endpoint.end_message)
            return
    
    # If the drunk man is standing at no endpoint, print a message for that special case
    print(no_endpoint_mess)

go_home(5, 5, 2, 20)