ART={
    "Pawn" : ["      ","  ██  "," ▀▀▀▀ "],
    "Rook" : [" ▄▄▄▄ ","  ██  "," ▀▀▀▀ "],
    "Knight":["  ▄▄▄ "," ▀▀██ ","  ▀▀▀ "],
    "Bishop":["  ▄▄  "," ▀██▀ "," ▀▀▀▀ "],
    "Queen": [" ▄  ▄ "," ▀██▀ "," ▀▀▀▀ "],
    "King" : [" ▄▄▄▄ "," ▀██▀ ","  ▀▀  "]
}

PC={
    "P":{"ART":ART["Pawn"]},
    "R":{"ART":ART["Rook"]},
    "N":{"ART":ART["Knight"]},
    "B":{"ART":ART["Bishop"]},
    "Q":{"ART":ART["Queen"]},
    "K":{"ART":ART["King"]}
}

START=[ # 2=Black 1=White 0=Blank
    "2R 2N 2B 2Q 2K 2B 2N 2R",
    "2P 2P 2P 2P 2P 2P 2P 2P",
    " 0  0  0  0  0  0  0  0",
    " 0  0  0  0  0  0  0  0",
    " 0  0  0  0  0  0  0  0",
    " 0  0  0  0  0  0  0  0",
    "1P 1P 1P 1P 1P 1P 1P 1P",
    "1R 1N 1B 1Q 1K 1B 1N 1R"
]

def render(board):
    for i in range(len(board)):
        board[i]=board[i].replace("  "," ").replace("  "," ").strip().split(" ")
    bgb="43"
    bgw="42"
    pcb="30"
    pcw="1"
    out=[]
    for Y in range(8):
        out.append([])
        for y in range(3):
            out[Y].append("")
            for X in range(8):
                out[Y][y]+=f"\033[{[bgw,bgb][(X+Y)%2]}m"
                if board[Y][X][0]=="1":
                    out[Y][y]+=f"\033[{pcw}m"
                elif board[Y][X][0]=="2":
                    out[Y][y]+=f"\033[{pcb}m"
                if board[Y][X]!="0":
                    out[Y][y]+=PC[board[Y][X][-1]]["ART"][y]
                else:
                    out[Y][y]+="      "
            out[Y][y]+="\033[0m"
        out[Y]="\n".join(out[Y])
    out="\n".join(out)
    return out
print(render(START))