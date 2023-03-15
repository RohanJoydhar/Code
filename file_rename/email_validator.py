import re
def io():
    print("io")
    email = input("email: ")
    password = input("password: ")
    userid = input("userid: ")
    return email, password, userid

def check_io(email, password, userid):
    print("check_io")
    print("checking all entities")

    if re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
        print("email is ok 🥳")
    else:
        print("email is not ok 🧐")
    if re.match(r'^[a-zA-Z0-9@#!&?_-]+$', password):
        if len(password) >= 14:
            print("password is ok 🥳")
        else:
            print("password is not long enough 🧐")
    else:
        print("password is not ok 🧐")
    if re.match(r'^[a-zA-Z0-9_-]+$', userid):
        if len(userid) >= 6:
            print("userid is ok 🥳")
        else:
            print("userid is not long enough 🧐")
    else:
        print("userid is not ok 🧐")
    
def main():
    print("hellow world")
    email, password, userid = io()
    check_io(email, password, userid)

if __name__ == "__main__":
    main()