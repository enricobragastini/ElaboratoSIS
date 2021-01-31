import random

f = open("cmd.blif", "w")
f.write("")
f.close()

f = open("cmd.blif", "a")
for n in range(random.randint(40, 100)):
    for i in range(random.randint(1, 3)):
        f.write("source script.rugged\n")
        
    for i in range(random.randint(8, 15)):
        f.write("map -m 0\n")
        
f.write("map -s")
    
f.close()
