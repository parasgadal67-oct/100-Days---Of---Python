# creating profile card for player
player_name = "M.S.Dhoni"
date_of_birth = "7-July-1981"
player_age = 42
nationality = "Indian"
matches_played = 350
runs_scored = 10000
is_retired = True
retirement_status = "Yes, retired" if is_retired else "No, still playing"


print("======= PLAYER PROFILE CARD =======")

print(f"Player Name:{player_name}")
print(f"Date of Birth:{date_of_birth}")
print(f"Age:{player_age}")
print(f"Nationality:{nationality}")
print(f"Matches Played:{matches_played}")
print(f"Runs Scored:{runs_scored}")
print(f"Retired:{retirement_status}")

print("===================================")