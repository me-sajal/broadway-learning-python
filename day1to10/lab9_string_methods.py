a =  'hello world. ram'
print(a.capitalize()) # this capitalizes frist letter of the first word in a sentence
print(a.title()) # this capitalizes first letter of the all the words available
print(a.upper()) #this capitalizes all the words inside the ""
print(a.lower()) # this makes all the words availables into small case
print(a.split()) #breakes the words by defult from space
print(a.split("o")) #breakes the words by user defult when string o
lee = ['hello','worlds']

print(" ".join(lee)) #joins the string available in the lee with space

print("word ".join(lee)) #joins the string available in the lee with space as word

print(a.find("w")) # finds the position of w in the string

print(a.find("z")) # finds the position of z in the string which is not
#available so the -1 is the out come because 0 is also used for a indexing

print(a.find("o")) # finds the position of w in the string

print(a.find("o",5)) # finds the position of w in the string back from 5

print(a.replace("hello",'hi') )# replaces the wors 'hello' by ""Hi
