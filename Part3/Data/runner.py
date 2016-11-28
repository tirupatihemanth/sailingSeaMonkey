import os
import time
import random
import string
# for j in range(1,1000):
h = open("aes.key","w")
key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
h.write(key); h.close();
# print("x"+str(j)+" = [")
for i in range(5,21):
	os.system("gcc encrypt.c")
	f = open("alice.txt","r")
	g = open("tmp.txt","w")
	s = f.read(2**i); f.close();
	g.write(s);	g.close();
	os.system("./a.out tmp.txt aes.key op.txt")
	os.system("gcc decrypt.c")
	start = time.time()
	os.system("./a.out op.txt aes.key dec.txt")
	end = time.time()
	print(end - start,",")
# print("]")

# for j in range(1,1000):
# 	print("x = [x;x"+str(j)+"']")