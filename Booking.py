import random

# To run Main loop program Again and Again 
while True:
    print("\n--- CAB BOOKING CHATBOT ---")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        # Step 1: select Cab 
        print("\nSelect Cab Type:")
        print("1. Auto (Rs 10/km)")
        print("2. Sedan (Rs 12/km)")
        print("3. SUV (Rs 15/km)")

        cab_choice = input("Enter cab choice (1-3): ")

        if cab_choice == "1":
            cab_name = "Auto"
            rate = 10
        elif cab_choice == "2":
            cab_name = "Sedan"
            rate = 12
        elif cab_choice == "3":
            cab_name = "SUV"
            rate = 15
        else:
            print("Invalid choice! Return to Main menu ")
            continue

        # Step 2: select Route 
        print("\nSelect Route:")
        print("1. Pune Station to Shivajinagar (5 km)")
        print("2. Swargate to Hadapsar (8 km)")
        print("3. Hinjawadi to Wakad (10 km)")

        route_choice = input("Enter route choice (1-3): ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Hadapsar"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid choice! Return to Main menu ")
            continue

        # Step 3: calculation
        total_fare = distance * rate

        # Display Summary 
        print("\n--- BOOKING DETAILS ---")
        print("Cab Type:", cab_name)
        print("Route:", source, "to", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs", rate, "/km")
        print("Total Fare: Rs", total_fare)

        # Step 4: Confirm Or Cancel ride
        print("\nOptions:")
        print("1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm_choice = input("Enter choice (1 or 2): ")

        if confirm_choice == "2":
            print("Ride cancel ")
        elif confirm_choice == "1":
            otp = random.randint(1000, 9999)
            print("\nBooking Confirmed! Your 4 digit OTP is :", otp)
            print("Note: The ride cannot be cancelled once the OTP has been shared.")
        else:
            print("Invalid choice!")

    elif choice == "2":
        print("Thankyou! Goodbye!")
        break
    else:
        print("Wrong option! Please select 1 Or 2 option .")