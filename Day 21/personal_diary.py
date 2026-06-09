# creating personal diary
from datetime import datetime

while True:
    print("\n ==== Persona lDiary ====")
    print("1. write new entry.")
    print("2. Read all entries.")
    print("3. Exit.")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
       current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       txt_entry = input("Enter your diary entry: ")
       file_path = "C:/Users/paras/OneDrive/Desktop"
       with open(file_path + "/personal_diary.txt", "a") as file:
        file.write(f"[{current_date}] {txt_entry}\n")
        print(f"Diary entry added to successfully.")
    elif choice == "2":
        try:
         file_path = "C:/Users/paras/OneDrive/desktop"
         with open(file_path + "/personal_diary.txt", "r") as file:
            entries = file.read()
            print("\n ==== Your Diary Entries====")
            print(entries)
        except FileNotFoundError:
            print("No diaries found. Start writing your first entry!")
    elif choice == "3":
        print("Exiting Personal Diary. Sayonara!")
        break
    else:
        print("Enter the valid choice. Try again.")