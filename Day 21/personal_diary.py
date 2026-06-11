# creating personal diary
from datetime import datetime

while True:
    print("\n ==== Persona lDiary ====")
    print("1. write new entry.")
    print("2. Read all entries.")
    print("3. Delete Entry.")
    print("4. Exit.")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
       current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       txt_entry = input("Enter your diary entry: ")
       file_path = "C:/Users/paras/OneDrive/Desktop"
       with open(file_path + "/personal_diary.txt", "a") as file:
        file.write(f"[{current_date}] {txt_entry}\n")
        print(f"Diary entry added to successfully.")
    elif choice == "2":
        try:
         file_path = "C:/Users/paras/OneDrive/Desktop"
         with open(file_path + "/personal_diary.txt", "r") as file:
            entries = file.readlines()
            print("\n ==== Your Diary Entries====")
            for i, entry in enumerate(entries):
                print(f"{i+1}.{entry.strip()}")
        except FileNotFoundError:
            print("No diaries found. Start writing your first entry!")
    elif choice == "3":
        try:
            file_path = "C:/Users/paras/OneDrive/Desktop"
            with open(file_path + "/personal_diary.txt", "r") as file:
                entries = file.readlines()
            if not entries:
                print("No entries to delete.")
            else:
                print("\n ==== Your Diary Entries====")
                for i, entry in enumerate(entries):
                    print(f"{i+1}. {entry.strip()}")
                try:
                    entry_index = int(input("Enter the number of the entry to delete: ")) - 1
                    if 0 <= entry_index < len(entries):
                        del entries[entry_index]
                        with open(file_path + "/personal_diary.txt", "w") as file:
                            file.writelines(entries)
                        print("Entry deleted successfully.")
                    else:
                        print("Invalid entry number.")
                except ValueError:
                    print("Please enter a valid number.")
        except FileNotFoundError:
            print("No diaries found. Start writing your first entry!")
    elif choice == "4":
        print("Exiting Personal Diary. Sayonara!")
        break
    else:
        print("Enter the valid choice. Try again.")