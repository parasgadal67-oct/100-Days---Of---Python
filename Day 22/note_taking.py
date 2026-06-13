# creating note taking app
while True:
 print("1. Add note.")
 print("2. View all notes.")
 print("3. Delete note.")
 print("4. Search note.")
 print("5. Exit.")
 choice = input("Enter your choice(1/2/3/4/5): ")
 if  choice == '1':  
      note = input("Enter the note you gonna save: ")
      file_path = "C:/Users/paras/OneDrive/Desktop/notes.txt"
      with open(file_path, 'a') as file:
        file.write(note + "\n")
      print("Note added successfully.")
 elif choice == '2':
    try:
        file_path = "C:/Users/paras/OneDrive/Desktop/notes.txt"
        with open(file_path, 'r') as file:
            notes = file.readlines()
            print("Your notes:")
            for note in notes:
                print(note.strip())
    except FileNotFoundError:
        print("No such files found.")
 elif choice == '3':
     
     try:
         file_path = "C:/Users/paras/OneDrive/Desktop/notes.txt"
         with open(file_path, 'r')as file:
                notes = file.readlines()
                if not notes:
                  print("No notes found.")
                else:
                    for i, note in enumerate(notes, start=1):
                        print(f"{i}.{note.strip()}")  
                    note_number = int(input("Enter the note number to delete: "))
                    if 1 <= note_number <= len(notes):
                            deleted_note = notes.pop(note_number - 1)  
                            with open(file_path, 'w') as file:
                                file.writelines(notes)
                                print(f"Note '{deleted_note.strip()}' deleted successfully.")
                    else:
                            print("Invalid number.")
     except ValueError:
                        print("Please enter a valid number.")
 elif choice == '4':
         
         try:
                file_path = "C:/Users/paras/OneDrive/Desktop/notes.txt"
                with open(file_path, 'r') as file:
                    notes = file.readlines()
                    search_note = input("Enter the Keyword to search: ")
                    found_notes = [note for note in notes if search_note.lower() in note.lower()]
                    if found_notes:
                        print("Foundnotes: ")
                        for note in found_notes:
                            print(note.strip())
                    else:
                            print("No notes found with given keyword.")
         except FileNotFoundError:
                        print("No files found.")
 elif choice == '5':
              print("Exiting the program, Thankyou for using the app,")
              break