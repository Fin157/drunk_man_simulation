from io import TextIOWrapper
from drunk_man import go_home

input_file_path = 'C:\\Users\\444St\\OneDrive\\Plocha\\test_input.txt'
output_file_path = 'C:\\Users\\444St\\OneDrive\\Plocha\\test_output.txt'

def simulate() -> None:
    '''
    This is the master function of the system. It gathers everything needed
    for the simulation to run and then runs it multiple times to see what
    the most frequent result of the current setup is.

    The input values are taken from a file and the outputs are written into
    another one.
    '''

    # Take the input and output file paths from the user
    # input_file_path = input('Input file path: ')
    # output_file_path = input('Output file path: ')

    # Construct the input dictionary from the input file
    inputs = get_input(input_file_path)
    results = dict()

    for _ in range(inputs['sim_count']):
        result = go_home(inputs['home_pub_dist'], inputs['max_steps'], inputs['step_size'], inputs['verbose'])
        # Increase the corresponding result's value
        if not results.__contains__(result.name):
            results[result.name] = 0
        results[result.name] += 1

    write_output(output_file_path, inputs, results)

def get_input(path: str) -> dict:
    '''
    Constructs a dictionary of inputs for the simulation from the specified file.

    Returns
    -------
    The newly obtained inputs.
    '''

    # Read everything in the specified file
    lines = open(path).readlines()

    # Make sure the file has 5 lines (1 input on each line)
    if not len(lines) == 5:
        raise Exception('Invalid input file.')

    # Map the input values from the file to their target type and save them
    # into a dictionary so that they can be accessed through names
    return dict(
        sim_count = int(lines[0]),
        home_pub_dist = int(lines[1]),
        max_steps = int(lines[2]),
        step_size = int(lines[3]),
        verbose = bool(int(lines[4]))
    )

def write_output(path: str, inputs: dict, results: dict) -> None:
    '''
    Writes a complete simulation output into the specified file.

    Writes a header for the whole file, then adds information about the inputs
    used in this simulation and also the results and how many times each of
    them happened.
    '''

    # Open the file
    output_file = open(path, 'w')

    # Write the file header
    output_file.write('Drunk man simulation summary\n----------------------------')

    output_file.write('Inputs\n')
    for key in inputs.keys():
        output_file.write(f'{key}: {inputs[key]}\n')
    
    output_file.write('Results\n')
    for key in results.keys():
        output_file.write(f'{key}: {results[key]} ({100 * results[key] / inputs["sim_count"]}%)\n')

    # Close the file
    output_file.close()

def write_dictionary(file: TextIOWrapper, header: str, d: dict) -> None:
    '''
    Writes a dictionary of data into the specified file in key: value format
    and with an arbitrary header preceding all data.
    '''

    # Make sure we avoid any errors caused by the file not being in the correct format
    if not file.writable():
        raise Exception('The specified file cannot be written into.')

    # Write the header
    file.write(header + '\n')

    # Write the dictionary itself
    for key in d.keys():
        file.write(f'{key}: {d[key]}\n')

simulate()