#verifing the player status
player_status1 = "Alive".title()
player_status2 = "Dead".title()
health_status1 = "good"
health_status2 = "low"
health_status3 = "critical"

player = input("Enter the player status: ").title()
if player == player_status1:
    health = input("Enter the health status: ")
    if health == health_status1:
        weapon =  input("Do you weapon?: ")
        if weapon == "yes" or weapon == "Yes":
            print("Attack")
        else:
            print("Run")
    elif health == health_status2:
        print("Find health pack.")
    elif health == health_status3:
        print("Game Over soon.")
else:
    print("GAME OVER")