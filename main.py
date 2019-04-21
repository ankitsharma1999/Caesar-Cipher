from res import caesar_gen

class message(str):
    def __init__(self,msg):
        self.msg = msg
    

    def encrypt(self):
        new_m = caesar_gen(msg)
        return new_m


if __name__ == "__main__":
    msg = message("This is a caesar cypher")
    print(msg.encrypt())