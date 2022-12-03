"TicTacToe"


def main():
    "TicTacToe"
    fff = [input() for _ in range(3)]
    res = []
    if len(check_row(fff)) != 0:
        res.append(check_row(fff))
    elif len(check_col(fff)) != 0:
        res.append(check_col(fff))
    elif len(check_cross_l(fff)) != 0:
        res.append(check_cross_l(fff))
    elif len(check_cross_r(fff)) != 0:
        res.append(check_cross_r(fff))
    if len(res) != 0:
        print(*res[0])
    else:
        print("DRAW")


def check_row(lis):
    "SSS"
    result = []
    for i in range(3):
        reso = lis[i].count("O")
        resx = lis[i].count("X")
        if reso == 3:
            result.append("O WIN")
        elif resx == 3:
            result.append("X WIN")
        else:
            reso, resx = 0, 0
    return result


def check_col(lis):
    "SSS"
    result = []
    reso = 0
    resx = 0
    for i in range(3):
        for j in range(3):
            reso += lis[j][i].count("O")
            resx += lis[j][i].count("X")
        if reso == 3:
            result.append("O WIN")
            reso = 0
            resx = 0
        elif resx == 3:
            result.append("X WIN")
            reso = 0
            resx = 0
        else:
            reso, resx = 0, 0
    return result


def check_cross_l(lis):
    "SSS"
    result = []
    reso = 0
    resx = 0
    reso += lis[0][0].count("O")
    reso += lis[1][1].count("O")
    reso += lis[2][2].count("O")
    resx += lis[0][0].count("X")
    resx += lis[1][1].count("X")
    resx += lis[2][2].count("X")
    if reso == 3:
        result.append("O WIN")

    elif resx == 3:
        result.append("X WIN")
    return result


def check_cross_r(lis):
    "SSS"
    result = []
    reso = 0
    resx = 0
    reso += lis[0][2].count("O")
    reso += lis[1][1].count("O")
    reso += lis[2][0].count("O")
    resx += lis[0][2].count("X")
    resx += lis[1][1].count("X")
    resx += lis[2][0].count("X")
    if reso == 3:
        result.append("O WIN")

    elif resx == 3:
        result.append("X WIN")
    return result


main()
