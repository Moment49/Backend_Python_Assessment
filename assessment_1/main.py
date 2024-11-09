from .even_num_func import even_list
def main():
    """This is the main program file that will be excuted and 
    serves as the entry point to the application script
    """
    program_prompt = "\nWelcome to The Even Number List Splicer\n"
    program_prompt += "1 - Enter any list of integer numbers and I will return only the even numbers to you\n"
    program_prompt += "Enter 'Q' or 'exit' to quit the program\n"
    program_prompt += "Select an action to perform (1 or quit program): "
    user_input = input(program_prompt)

    isStart = False
    while not isStart:   
        if user_input == "1":
            # Get all user inputs
            user_nums = input("Enter a list of numbers: ").split()

            # Convert the split string to a list of numbers
            nums_list = [int(num) for num in user_nums]
            
            # Check if ist is not empty
            if nums_list:
                # Call the even_list function to return the even numbers
                even_nums = even_list(nums_list)
                # Check if the num_list is zero
                if len(even_nums) == 0:
                    print("No even number found")
                else:
                    print(f"These are the even numbers within the list of numbers you entered is: {even_nums}")

            # Ask the user for more numbers if they need to
            user_response = input("Do you want to enter more numbers? (yes or no): ")

            # Check if user response if 'NO' return the even numbers found
            if user_response.title() == 'No':
               # Check and return the numbers if they are even or not
                even_nums = even_list(nums_list)
                # Check if the num_list is zero
                if len(even_nums) == 0:
                    print("No even number found")
                else:
                    print(f"Even numbers within the list of numbers you entered is: {even_nums}")
                
                # break out of loop
                isStart = True
                break
                  
         
        if user_input.title() == 'q' or user_input.title() == 'Q' or user_input.title() == 'Exit':
            isStart = True

      
        






if __name__ == "__main__":
    main()