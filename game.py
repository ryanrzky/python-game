name = input("Masukan nama Monster kamu : ")
monster = {"name": name, "power": 50}

def startGame():
    choice = input("Kamu mau apa?\n1.Makan 2.LihatStatus 3.LihatLevel 4.Keluar = ")
    if choice == "1":
        eat()
    elif choice == "2":
        status()
    elif choice == "3":
        seeLevel()
    else:
        exit()

def eat():
    print("\n Nyam... enakk \n")
    monster["power"] += 100
    startGame()

def status():
    print(f"\nNama Hero: {monster['name']}\nPower: {monster['power']}\n")
    startGame()

def seeLevel():
    level = monster["power"]
    if level < 200:
        print("\nMonster Level 1\n")
    elif level in range(200, 299):
        print("\nMonster Level 2\n")
    elif level >= 300:
        print("\nMonster Level Max\n")
    startGame()

def exit():
    print("\nSelamat tinggal...")

startGame()