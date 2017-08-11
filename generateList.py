from entoru import translate

with open("wlist.txt") as f:
    wl = f.readlines()

rl = []
for w in wl:
    if w != "":
        try:
            s = translate(w)
        except:
            s = "Could not translate"
        print(s)
        rl.append(s)

# with open("translation.txt", "w") as f:
#     for t in rl:
#         f.write("{}.\n".format(t))
