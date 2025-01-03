# l = ["A", "B", "C", "D", "E", "F"]
# for i in range(len(l)):
#     print("(" + l[i] + ")" + " -- " + "(" + l[(i + 1) % len(l)] + ")")
#     print("(" + l[i] + ")" + " -- " + "(" + l[(i + 2) % len(l)] + ")")

for i in range(8):
    if (i % 2 == 0):
        if (i/2) % 2 == 0:
            x = 0
        else:
            x = 1
    else:
        if ((i+1)/2) % 2 == 0:
            x = 5
        else:
            x = 6
    print(f"\\node[defaultNode] (node{i}) at ({x},{0.4*i});")
