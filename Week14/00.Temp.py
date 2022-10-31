"Impostor"
import json
def main():
    "Impostor"
    player = {}
    player2 = {}
    play_list = []
    impos = 0
    while True:
        text = input()
        if text == "Start":
            break
        elif text != "Start":
            text2 = json.loads(text)
            player.update(text2)
    while True:
        text3 = input()
        if text3 == "End":
            break
        play_list.append(text3)
    
    for x in play_list:
        player2.update({x:player.pop(x)})
    
    for i in player:
        if player[i] == "Impostor":
            impos += 1
    print(impos, "Impostor Remains")
    print("***Alive***")   
    for i in player:
        print(i, ":", player[i])

main()