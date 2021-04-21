player1 = {"name":"zilong", "power":100}
player2 = {"name":"hilda", "power":250}

def train(player):
    player["power"] += 100 # ini seperti player1["power"] = player1["power"] + 100

def attack(attacker, defender):
    if(attacker["power"]) > defender["power"]:
        print("serangan berhasil, kamu hebat", attacker["name"])
    else:
        print("serangan gagal, kamu lemah", attacker["name"])

train(player1)
attack(player1, player2)
