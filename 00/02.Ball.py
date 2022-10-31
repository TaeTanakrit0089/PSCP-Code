'''Pre'''

def main():
    'Pre'
    text_input = input()
    ball_position = 1
    for i in text_input:
        if i == 'A':
            if ball_position == 1:
                ball_position = 2
            elif ball_position == 2:
                ball_position = 1
        elif i == 'B':
            if ball_position == 2:
                ball_position = 3
            elif ball_position == 3:
                ball_position = 2
        elif i == 'C':
            if ball_position == 1:
                ball_position = 3
            elif ball_position == 3:
                ball_position = 1
    print(ball_position)

main()
