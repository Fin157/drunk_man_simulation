import random
from helpers import *

def go_home(home_pub_distance: int, max_steps: int, step_size: int, verbose: bool) -> Ending:
    # Convert the input pub position to a 0-based number
    pub_pos = home_pub_distance - 1
    steps = 0
    pos = get_starting_pos(pub_pos)
    # Calculate the initial state of the simulation
    state = is_end(pos, pub_pos, steps, max_steps)

    # Make the drunk man walk until the state changes
    # to anything other than 'Walking'
    while state == Ending.Walking:
        # Calculate the drunk man's new position
        pos = take_step(pos, step_size, pub_pos)

        # Render the changes
        if verbose:
            render(pos, pub_pos)

        # Update the simulation state variables
        state = is_end(pos, pub_pos, steps, max_steps)
        steps += 1

    # Inform the user of the simulation's end result
    if verbose:
        render_end(state)

    # Return the result of the simulation run
    return state

def take_step(pos: int, step_size: int, pub_pos: int) -> int:
    '''
    This function makes the drunk man walk a single step.

    The input step size gets randomly added to or subtracted
    from the input position. The result of this operation is
    clamped between 0 and the position of the pub.
    '''

    # Choose a random item from a tuple of two items.
    # The tuple's items are the drunk man's movement options
    # turned into absolute positions (they determine where
    # the drunk man would end up being if he chose that
    # movement option). These positions are then clamped to ensure
    # that they don't 'overflow' into negative or
    # bigger-than-pub-position values.
    return random.choice((clamp(pos - step_size, 0, pos),
                        clamp(pos + step_size, pos, pub_pos)))

def get_starting_pos(pub_pos: int) -> int:
    '''
    Calculates the drunk man's starting position based on the pub's position.

    The drunk man starts between his home and the pub. To calculate the middle
    position between those two points, we use the formula for arithmetical
    average. As the home's position is equal to 0, we can omit it from the
    calculation and just divide the pub's position by 2 and round it.
    '''

    return round(pub_pos / 2)

def is_end(pos: int, pub_pos: int, steps: int, max_steps: int) -> Ending:
    if pos == 0:
        # The drunk man got home
        return Ending.Home
    elif pos == pub_pos:
        # The drunk man got to the pub
        return Ending.Pub
    elif steps >= max_steps:
        # Max simulation steps reached
        return Ending.Asleep
    return Ending.Walking

def render(pos: int, pub_pos: int) -> None:
    # Create the line as a list of dot characters with each dot
    # representing one square the drunk man can be on
    line = ['.'] * (pub_pos + 1)
    # Make the first square say 'home' instead of the dot to indicate
    # where the man's home is
    line[0] = 'home'
    # Visualise the man's position as an asterisk
    line[pos] = '*'
    # Visualise the pub's position
    line[pub_pos] = 'pub'
    print(*line)

def render_end(result: Ending) -> None:
    '''Writes a message into the console based on the specified result.'''

    if result == Ending.Walking:
        return
    elif result == Ending.Asleep:
        print('Oh no! The drunk man fell asleep right on the pavement!')
    elif result == Ending.Home:
        print('Luckily, the drunk man was able to get home safely.')
    elif result == Ending.Pub:
        print('Sheesh! The drunk man ended in the pub again!')