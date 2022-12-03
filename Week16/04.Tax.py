"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    year, engine, summer = int(input()), int(input()), 0
    summer += (min(600, engine)) * 0.5 if engine > 0 else 0
    summer += (min(1800, engine)-600) * 1.5 if engine > 600 else 0
    summer += (engine - 1800)*4 if engine > 1800 else 0

    discount = {6: 10, 7: 20, 8: 30, 9: 40}
    if year in discount:
        summer *= (100 - discount[year])/100
    elif year >= 10:
        summer *= 0.5
    print('%.2f' % summer)

another_one_bite_the_dust()

# ⠀⠀⠀⠀⠀⠀⢹⣄⣿⣦⣼⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⠿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⠟⠋⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢠⣟⣁⣴⡄⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢿⠛⢉⣠⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀1946-1991⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠈⣿⣿⠏⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣧⣤⣶⠖⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢻⡉⠁⠀⣀⣤⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠛⠛⠛⠁⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⣤⣶⠿⠀⣀⣤⣤⣶⣿⣿⠒⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⡄⣤⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣹⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣿⣿⣿⣿⣿⡿⠃⠀⠀⠻⣿⣿⣿⣿⣿⣿⠛⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠿⠿⣿⠟⠁⠀⠀⠀⠀⠈⠻⢿⣿⣿⡇⢰⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠉⠉⠁⢞⣿⠈⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⡄⠀⠀⠀⣠⣴⣾⣯⠖⠀⠀⠀⠀⠀⠹⡇⣰⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠉⢻⣿⣶⣆⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢧⢉⠇⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⢀⡴⠟⢻⡉⢿⠀⠀⣠⡤⠀⢀⡀⠀⠀⠀⠀⣾⡞⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⡴⣋⣤⣀⣰⠏⠀⠀⢸⠳⣼⣦⣴⣿⣿⣿⡿⠛⠀⠀⢀⣼⠟⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢠⣏⣴⣿⣿⣿⣿⠀⠀⢀⣿⣶⣿⣿⣿⡋⠭⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀
# ⠀⠀⠀⢀⣴⠿⠛⠛⠛⢿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⠿⣶⣶⣴⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀
# ⠀⠀⠠⣿⣁⣀⡀⠀⢀⣠⣽⣿⠿⠿⠿⣿⣿⣿⣿⠏⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀
# ⠀⠀⠀⠈⠉⣻⠇⠀⠘⠋⠁⣀⣀⣤⣴⠾⠟⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀
# ⠀⠀⢀⣴⠟⠋⠀⢠⣶⡾⠿⠛⣛⣩⣤⣤⣤⡿⠀⠀⠀⠀⠀⠀⠀⢀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠀⠘⡆⠀
# ⠀⠀⠸⣧⡀⠀⣀⠀⠀⣠⣶⠟⠛⠉⠉⠉⣽⠃⠀⠀⠀⠀⢀⣤⠾⠛⢉⡇⠀⠀⢀⣤⣶⠖⠀⠀⠀⠀⠀⠀⢸⠀⠀⢹⡀
# ⠀⠀⠀⠈⠛⠛⢻⡆⠀⠈⠀⣠⣶⠶⠿⢾⡟⠀⠀⠀⣠⡾⠟⠁⣠⠖⠋⣷⣠⣾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⣇
# ⠀⠀⠀⠀⠀⣠⣼⠇⠀⠀⠀⠉⠀⢀⣀⣿⠃⠀⢠⠚⠉⢀⡴⠟⠁⠀⢀⣸⣿⣀⣤⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⡿
# ⠀⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⠀⠐⠛⢻⡟⠀⠀⢸⣠⡶⠋⠀⠀⣠⡶⠟⠉⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡼⠁
# ⠀⠀⠀⠀⠻⣦⣤⣤⣄⠀⠀⠀⠀⠀⣿⠃⠀⠀⠈⠉⠀⣀⡴⠟⠉⠀⢀⣠⣿⣷⢀⣤⣴⡶⠄⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⢀⣀⣴⣾⡏⠀⠀⠀⢀⣤⣾⠋⠀⠀⣀⡴⠛⠁⠀⢻⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
# ⠀⠀⠀⠀⠀⠀⠀⣀⣿⠿⠛⠉⢸⣿⠇⠀⠀⠀⠈⡏⢿⣀⣴⠞⠉⠀⠀⣀⡴⠚⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀
# ⠀⠀⠀⢀⣤⠶⠛⠉⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠙⠼⠋⠁⠀⢀⣤⠞⠉⠀⠀⢻⣤⡾⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀
# ⠀⣠⡾⠋⠁⠀⣠⣴⠿⠛⣻⡿⢿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⡞⠋⠀⠀⠀⢀⡤⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀
# ⣰⠏⠀⠀⠀⠘⣋⣡⠶⠛⠁⠀⢸⡇⠀⠀⠀⠀⠀⢠⢺⠋⢻⡷⣀⣀⣤⠞⠋⠀⠀⣿⣆⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⣿⠀
# ⠙⠷⠶⠶⠶⠛⠉⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⢣⣣⣀⠳⡽⠋⠀⠀⠀⢀⣴⢿⣿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⣿⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠋⠀⠀⣀⣠⡶⠋⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢫⣿⢿⡀⠀⣠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⠊⠙⠙⠚⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀

