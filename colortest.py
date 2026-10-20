print("    0      1      2      3      4      5      6      7      8      9")
for y in range(11):
    line=str(y*10)
    line=(" "*(3-len(line)))+line+" "
    for x in range(5):
        line+=f"\033[{(y*10)+(x*2)}mHello,\033[0m \033[{(y*10)+(x*2)+1}mWorld!\033[0m "
    print(line)
