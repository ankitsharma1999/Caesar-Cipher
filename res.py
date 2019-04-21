def words_gen(s):
    s = s.lower()
    s = " "+s+" "
    l = len(s)
    l_i = 0
    c = 0
    words = []
    while c<l:
        if s[c]==" ":
            words.append(s[(l_i+1):c])
            l_i = c
        c+=1
    words = words[1:]
    return words

def caesar_gen_words(w):
    l = len(w)
    c = 0
    new_w=""
    letters = []
    while c<l:
        x = w[c:c+1]
        letters.append(x)
        c=c+1
    for each_element in letters:
        t = ord(each_element)
        if t>=97 and t<122:
            t=t+1
        elif t==122:
            t=97
        ch = chr(t)
        new_w = new_w+ch
    return new_w

def caesar_gen(s):
        words = []
        new_w = ""
        msg = ""
        words = words_gen(s)
        for eachWord in words:
            new_w = caesar_gen_words(eachWord)
            msg = msg + new_w
            msg = msg + " "
        return msg
def gen_msg(w):
    l = len(w)
    c = 0
    new_w=""
    letters = []
    while c<l:
        x = w[c:c+1]
        letters.append(x)
        c=c+1
    for each_element in letters:
        t = ord(each_element)
        if t>97 and t<=122:
            t=t-1
        elif t==97:
            t=122
        ch = chr(t)
        new_w = new_w+ch
    return new_w

def final_msg(s):
        words = []
        new_w = ""
        msg = ""
        words = words_gen(s)
        for eachWord in words:
            new_w = gen_msg(eachWord)
            msg = msg + new_w
            msg = msg + " "
        return msg
