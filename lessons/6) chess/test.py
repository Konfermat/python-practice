# # refferences
# def print_chessboard(n=8):
#     """
#     Выводит шахматное поле размером n x n в консоль.
#     :param n: Размер стороны доски.
#     """
#     for i in range(n):
#         row = ""
#         for j in range(n):
#             # Определяем цвет клетки: 0 - черная, 1 - белая
#             if (i + j) % 2 == 0:
#                 row += "███"  # Символ для черной клетки
#             else:
#                 row += "░░░"  # Символ для белой клетки
#         print(row)
#
# # Вызываем функцию для печати стандартной доски 8x8
# print_chessboard(8)

# print("""Король: ♔ (белый), ♚ (чёрный)
# Ферзь: ♕ (белый), ♛ (чёрный)
# Ладья: ♖ (белый), ♜ (чёрный)
# Слон: ♗ (белый), ♝ (чёрный)
# Конь: ♘ (белый), ♞ (чёрный)
# Пешка: ♙ (белый), ♟ (чёрный)""")


chess1 = chr(int("0x265F", 16)) # hex to decimal to str
chess2 = hex(ord(chess1)) # str to decimal to hex
chess3 = hex(ord('█')) # str to decimal to hex
chess4 = hex(ord('░')) # str to decimal to hex

# print(chess1)
# print(chess2)
print(chess3)
print(chess4)



