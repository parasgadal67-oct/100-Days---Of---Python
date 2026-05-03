# creating dictionary contact book
contact = {"Paras":"9876543210",
           "Anand":"8765432109",
           "Rahul":"7890123456"}
print(contact.get("Paras"))
contact.update({"Ayush":"7896543217"})
contact.pop("Anand")
print(contact)
 