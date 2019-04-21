from res import caesar_gen, final_msg

class message(str):
    def __init__(self,msg):
        self.msg = msg
    

    def encrypt(self):
        new_m = caesar_gen(msg)
        return new_m
    
    def decrypt(self):
        new_m = final_msg(msg)
        return new_m


if __name__ == "__main__":

    m = input("Enter the mesaage: ")
    msg = message(m)

    print("1.Encrypt\n2.Decrypt")
        
    ch = input("Enter your choice(1/2): ")
    if ch=="1":
        print(msg.encrypt())
    elif ch=="2":
        print(msg.decrypt())
    else:
        print("Enter a valid choice.")