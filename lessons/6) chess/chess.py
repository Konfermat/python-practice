def print_help():
    print("\n=== Шпаргалка по фигурам и их ходам ===")
    print("P (Пешка):     Ход вперёд на 1, бьёт по диагонали") # U+265F
    print("R (Ладья):     По вертикали и горизонтали")
    print("N (Конь):      Ход \"буквой Г\" (2+1)")
    print("B (Слон):      По диагонали")
    print("Q (Ферзь):     Слон + Ладья (все направления)")
    print("K (Король):    На 1 клетку в любом направлении")
    print("Пример хода:   e2 e4")
    print("Введите 'help' чтобы снова увидеть это меню\n")
# print(print_help())

# белый шахматный король	white chess king	♔	U+2654	&#9812;	&#x2654;
# белый шахматный ферзь	white chess queen	♕	U+2655	&#9813;	&#x2655;
# белая шахматная ладья	white chess rook	♖	U+2656	&#9814;	&#x2656;
# белый шахматный слон	white chess bishop	♗	U+2657	&#9815;	&#x2657;
# белый шахматный конь	white chess knight	♘	U+2658	&#9816;	&#x2658;
# белая шахматная пешка	white chess pawn	♙	U+2659	&#9817;	&#x2659;
# чёрный шахматный король	black chess king	♚	U+265A	&#9818;	&#x265A;
# чёрный шахматный ферзь	black chess queen	♛	U+265B	&#9819;	&#x265B;
# чёрная шахматная ладья	black chess rook	♜	U+265C	&#9820;	&#x265C;
# чёрный шахматный слон	black chess bishop	♝	U+265D	&#9821;	&#x265D;
# чёрный шахматный конь	black chess knight	♞	U+265E	&#9822;	&#x265E;
# чёрная шахматная пешка	black chess pawn	♟	U+265F	&#9823;	&#x265F;

# 0x2654 # белый король
# 0x2655 # белый ферзь
# 0x2656 # белая ладья
# 0x2657 # белый слон
# 0x2658 # белый конь
# 0x2659 # белая пешка
# 0x265A # черный король
# 0x265B # черный ферзь
# 0x265C # черная ладь
# 0x265D # черный слон
# 0x265E # черный конь
# 0x265F # черная пешка
# 0x2591 # белая клетка
# 0x2588 # черная клетка

print('█')
print('░')
figures = {
    'Пешка': chr(int("265F", 16)),
}

# print('\U0001F603')
# print('♟')
# print(ord('♟'))
# print(chr(9823))

print(figures['Пешка'])
print(chr(int("265F", 16)))

def init_board():
    pass
def print_board(board):
    pass
def get_moves(piece, position, board):
    pass
def linear_moves(position, board, direrctions):
    pass
