command = " "
started = False

while True:
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("the car is already started...")
        else:
           started = True    
           print("the car is started..")
           
           
    elif command == "stop":
        if not started:
            print("the car is already stopped..")
        else:     
           started = False
           print("the car is stopped..")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to end the game
    """)
    
    
    elif command == "quit":
        break
    else:
        print("sry,i dont understand!...")
