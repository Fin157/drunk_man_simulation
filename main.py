from helpers import *
import random

def go_home(home_pub_distance, max_steps, step_size):
    pub_pos = home_pub_distance - 1
    pos = get_starting_pos(pub_pos)
    steps = 0
    result = is_end(pos, pub_pos, steps, max_steps)

    while result == Ending.Walking:
        pos = take_step(pos, step_size, pub_pos)
        render(pos, pub_pos)
        result = is_end(pos, pub_pos, steps, max_steps)
        steps += 1

    render_end(result)

def take_step(pos, step_size, pub_pos) -> int:
    return random.choice((clamp(pos - step_size, 0, pos),
                        clamp(pos + step_size, pos, pub_pos)))

def get_starting_pos(pub_pos):
    return round(pub_pos / 2)

def is_end(pos, pub_pos, steps, max_steps) -> Ending:
    if pos == 0:
        return Ending.Home
    elif pos == pub_pos:
        return Ending.Pub
    elif steps >= max_steps:
        return Ending.Asleep
    return Ending.Walking

def render(pos, pub_pos):
    line = ["."] * (pub_pos + 1)
    line[0] = "home"
    line[pos] = "*"
    line[pub_pos] = "pub"
    print(*line)

def render_end(result):
    if result == Ending.Walking:
        return
    elif result == Ending.Asleep:
        print("Oh no! The drunk man fell asleep right on the pavement!")
    elif result == Ending.Home:
        print("Luckily, the drunk man was able to get home safely.")
    elif result == Ending.Pub:
        print("Sheesh! The drunk man ended in the pub again!")

go_home(20, 20, 2)