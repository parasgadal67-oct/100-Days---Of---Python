def greet_user(name):
    def make_message():
        return f"Hello, {name}! welcome to the world of python!"
    message = make_message()
    print(message)
    
greet_user("Paras")    