# generates words from a sentence
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
    #return print(s.split(' '))

# converts words to caesar cipher
def caesar_gen_words(w,key):
    l = len(w)
    c = 0
    new_w=""
    letters = []
    while c<l:
        x = w[c:c+1]
        letters.append(x)
        c=c+1
    for each_element in letters:

        t = ord(each_element)-97
        t = (t+key)%26
        ch = chr(t+97)

        new_w = new_w+ch

    return new_w

# converts sentence to caesar cypher
def caesar_gen(s,key):
    words = []
    new_w = ""
    msg = ""
    words = words_gen(s)
    for eachWord in words:

        new_w = caesar_gen_words(eachWord, key)
        msg = msg + new_w
        msg = msg + " "

    return msg

# converts words back to readable form        
def gen_msg(w,key):
    l = len(w)
    c = 0
    new_w=""
    letters = []
    while c<l:
        x = w[c:c+1]
        letters.append(x)
        c=c+1
    for each_element in letters:

        t = ord(each_element)-97
        t = (t-key)%26
        ch = chr(t+97)

        new_w = new_w+ch

    return new_w

# converts sentence back to readable form
def final_msg(s,key):
    words = []
    new_w = ""
    msg = ""
    words = words_gen(s)
    for eachWord in words:

        new_w = gen_msg(eachWord, key)
        msg = msg + new_w
        msg = msg + " "

    return msg
print(words_gen("hi there you"))