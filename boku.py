from board import board
from move import move
from MinMax import MinMax

playboard = board()

player = int(raw_input("Player colour? (1=White, 2=Black)"))
print "Player is %s; computer is %s"%("Black" if player == 2 else "White", 
                                      "White" if player == 2 else "Black")

level = int(raw_input("Computer level? (1-?)"))

computer = MinMax(level, 1 if player == 2 else 2)
                                      
turn_token = 1
while 1:
    playboard.display()
    print "Score: %d"%playboard.score()
    if turn_token == player:
        move_object = None
        while move_object == None:
            move_string = raw_input("%s move? (ROW, COLUMN or ROW, COLUMN, TAKE_ROW, TAKE_COLUMN) "%
                                    ("White" if (turn_token == 1) else "Black"))
            move_object = move(turn_token, string = move_string)
    else:
        move_object = computer.move(playboard)
    turn_token = 2 if (turn_token == 1) else 1
    playboard.move(move_object)
