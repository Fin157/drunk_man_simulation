# drunk_man_simulation

This is a simple program made for my programming lessons at school. It simulates movement of a drunk man trying to get home. He starts on the pavement between the pub and his home and goes either to the left or right each step of the simluation. Our goal as the researchers is to find the program's settings that make the drunk man go home in the highest number of cases.

## A Little Disclaimer

This program likely isn't fully idiot-proof. I am sure there are some (read many) ways to break this program by giving it unexpected inputs. I must ask you not to complain about situations when something alike happens as it solves nothing and induces the likelihood of me gifting your machine a tiny malware friend. Thank you :)

## How to use this program

The program accepts a set of parameters in the form of a file with one parameter on each line (see the "Inputs" section for further information) and outputs the results of the simulation into a separate file. To alter paths to the input or output file, please do the following:
1. Find and open a file named "main.py" in the project.
2. Somewhere at the top of the file are two lines beginning with "input_file_path" and "output_file_path".
3. Change these parameters to a new path you'd like to use instead. (A great way of copying a file path in Windows 11 is right-clicking on it and selecting the "Copy as path" option)

### Inputs

The input file contains precisely as many lines as there are inputs with each input on a separate line and with no empty lines in between. The exact order of the parameters is as follows:
1. sim_count - Controls how many times the simulation should be ran with the specified parameters. Accepts non-negative integers.
2. home_pub_dist - Controls the distance between the drunk man's home and the pub. Accepts non-negative integers.
3. max_steps - Determines AT MOST how many steps it takes before the drunk man falls asleep in a SINGLE run (one iteration of the simulation). Accepts non-negative integers.
4. step_size - Dictates the largest possible size of the drunk man's steps. Note that the drunk man will do as large steps as he can and that the only time he does a smaller step than this value is when the resulting position would be out of the pub-to-home bounds. Accepts non-negative integers.
5. verbose - Makes the program inform its user about the progress of the simulation through the console window. Accepts non-negative integers. Zero results in the verbose mode being turned off, any other accepted value means it will be enabled.

### Run program run

After you've set everything up as suggested, it is finally time to do the most fun part of the process: let the drunk man walk! To do this, simply open the project in your favourite code editor, go into the root folder of the program and type `python .\main.py`. If all former steps were a success, you'll see no error jumpscaring you in the terminal window. After the simulation has finished, simply open the output file in any text editor and inspect the results of the simulation. If you're not happy with what you got, tweak the input numbers and do it again! And with that, I wish y'all happy simulating!
