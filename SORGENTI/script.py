import random

f = open("cmd.blif", "w")
f.write("")
f.close()

f = open("cmd.blif", "a")
for n in range(random.randint(40, 70)):
    for i in range(random.randint(0, 5)):
        f.write("source script.rugged\n")
        
    for i in range(random.randint(3, 10)):
        f.write("map -m 0\n")
        
f.write("map -s")
    
f.close()
