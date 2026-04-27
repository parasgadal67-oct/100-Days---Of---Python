#find spaces and remove them from email address
#turn uppercase in lower case
#clean it using string method
email = "  PARASGADAL18@GMAIL.COM  "
print(email.strip())
print(email.lower())
print(email.replace(" ","").lower())