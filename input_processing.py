# input_processing.py
# Ashim Orko, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        # Initializes default sensor statuses
        self.light = 'green'
        self.pedestrian = 'no'
        self.vehicle = 'no'
                
    # The function updates the sensor status based on user input
    # It continuously prompts user for updates until the user enters a 0 to terminate the program
    # It takes 'self', an instance of the Sensor class, as an argument and updates the instance's attributes based on user input
    def update_status(self): 

        # Starts and infinite loop to continuously prompt for input          
        while True:

            try:
                print("Are changes detected in the vision input?")
                
                # Display menu options and receives user input
                menu_option = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

                # If user selects 0, ends the loop and stops the program
                if menu_option == '0':
                    break
                
                # Handles the option for changing the light status 
                if menu_option == '1':
                    prompt = input('What change has been identified?: ')
                    # Validates input and updates the light status
                    if prompt == 'green' or prompt == 'yellow' or prompt == 'red':
                        self.light = prompt
                    else:
                        # Prints this message if status input is invalid  
                        print('Invalid vision change.')
                              
                # Handles the option for changing the pedestrian status 
                elif menu_option == '2':
                    prompt = input('What change has been identified?: ')
                    # Validates input and updates the pedestrian status
                    if prompt == 'yes' or prompt == 'no':
                        self.pedestrian = prompt
                    
                    else:
                        # Prints this message if status input is invalid  
                        print('Invalid vision change.')
                                 
                # Handles the option for changing the vehicle status 
                elif menu_option == '3':
                    prompt = input('What change has been identified?: ')
                     # Validates input and updates 1
                     # the vehicle status
                    if prompt == 'yes' or prompt == 'no':
                        self.vehicle = prompt
                    else:
                        # Prints this message if status input is invalid  
                        print('Invalid vision change.')
                    
                else:
                    # Raises an error if the menu option input is invalid
                    raise ValueError('You must select either 1, 2, 3 or 0.\n')
                            
             

            except ValueError as err:
                # Prints the error message and restarts the loop
                print(err)
                continue

            

            # Calls the print_message function which is defined below  
            print_message(self)   

# Function to print the action message and current status.
# It takes the 'sensor' object as an argument and prints its statuses.
def print_message(sensor):
    
    # Validates sensor status and prints action message
    if sensor.light == 'green' and sensor.pedestrian == 'no' and sensor.vehicle == 'no':
        print('\nProceed\n')
    elif sensor.light == 'yellow' and sensor.pedestrian == 'no' and sensor.vehicle == 'no':
        print('\nCaution\n')
    else:
        print('\nSTOP\n')
    # Prints the current status of the sensors as a string
    print('Light =', sensor.light, ', Pedestrian =', sensor.pedestrian, ', Vehicle =', sensor.vehicle,'\n' )     



# Defines the main function
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Creates a new sensor object and starts the update status loop
    sensor = Sensor()
    sensor.update_status()
        


# Runs the main function
if __name__ == '__main__':
    main()

