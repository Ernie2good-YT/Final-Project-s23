from manager import Manager
PIN="0000"
def login():
    while True:
        p=input("enter PIN: ")
        if p==PIN:
            break
def menu():
    print("pick an option:")
    print("1. generate password")
    print("2. update password")
    print("3. delete password")
    print("4. get password")
    print("5. quit")
    choice=input("enter option:")
    return choice
 
def generate_pass(m):
    site=input("enter site name: ")
    usr=input("enter username")
    length=input("password length: ")
    print("password: "+m.generate_password(site,usr,length))
 
def get_pass(m):
    site=input("enter site: ")
    usr=input("enter username: ")
    print("username:",usr)
    print("password: ",m.get_password(site,usr))
 
def delete(m):
    site=input("enter site: ")
    usr=input("enter username: ")
    m.delete(site, usr)
 
def main():
    login()
 
main()