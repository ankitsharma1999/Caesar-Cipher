from res import caesar_gen, final_msg

class message(str):    # class message has all the attributes of string class

    def __init__(self,msg):
        self.msg = msg
    

    def encrypt(self, key):
        new_m = caesar_gen(msg,key)
        return new_m
    
    def decrypt(self, key):
        new_m = final_msg(msg,key)
        return new_m


if __name__ == "__main__":

    m = input("Enter the message: ")

    msg = message(m)

    print("1.Encrypt\n2.Decrypt")
        
    ch = input("Enter your choice(1/2): ")
    if ch=="1":
        key = int(input("Enter the Key: "))
        print(msg.encrypt(key))
    elif ch=="2":
        key = int(input("Enter the Key: "))
        print(msg.decrypt(key))
    else:
        print("Enter a valid choice.")