# Start a while loop to continuously ask for user input
while True:
    user_input = input("What you gotta say? : ")
    
    # Check if the user input is "STOP"
    if user_input == "STOP":
        break  # Exit the loop when user enters "STOP"
    
    # Provide a response to the user input
    print("I got that! Anything else? : " , end="")