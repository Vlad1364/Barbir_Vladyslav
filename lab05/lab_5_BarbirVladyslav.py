################Task01##############
my_list = [1, 2, 3, 4, 5]
index_to_replace = int(input("Введіть індекс числа, яке ви хочете замінити: "))
new_value = int(input("Введіть нове число: "))
my_list[index_to_replace] = new_value

my_list.pop()

print("Довжина списку:", len(my_list))
print("Оновлений список:", my_list)
################Task02##############
my_list = [64, 16, 25, 12, 22, 2, 90]

n = len(my_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print("Відсортований список:", my_list)
################Task03##############
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = []

for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

print("Список без дублікатів:", unique_list)
################Task04##############
chess_board = [["_" for _ in range(8)] for _ in range(8)]

chess_board[0][0] = "T"
chess_board[0][7] = "T"
chess_board[7][0] = "T"
chess_board[7][7] = "T"

# Виведення шахової дошки
for row in chess_board:
    print(" ".join(row))