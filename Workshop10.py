# __________________Задача 1_________________________

# class MinStat:

#     def __init__(self):
#         self.list_number = []

#     def add_number(self, number:int):
#         self.list_number.append(number)

#     def result(self):
#         return min(self.list_number)

# class MaxStat:

#     def __init__(self):
#         self.list_number = []


#     def add_number(self, number:int):
#         self.list_number.append(number)

#     def result(self):
#         return max(self.list_number)

# class AverageStat:

#     def __init__(self):
#         self.list_number = []


#     def add_number(self, number:int):
#         self.list_number.append(number)

#     def result(self):
#         return sum(self.list_number) / len(self.list_number)

# min_stat = MinStat()
# max_stat = MaxStat()
# average = AverageStat()
# values = [1, 4, 6, 9, 3, 6]

# for i in values:
#     min_stat.add_number(i)
#     max_stat.add_number(i)
#     average.add_number(i)

# print(f'Минимальное число = {min_stat.result()}\n\
# Максимальное число = {max_stat.result()}\n\
# Среднее арифметическое = {round(average.result(), 2)}')

# __________________Задача 2_________________________

class Table:

    def __init__(self, row:int, col:int):
        self.table = [[0] * col for i in range(row)]

    def get_value(self, row:int , col:int):
        return (self.table[row][col] if 0 <= row < len(self.table) and 0 <= col < len(self.table[0]) 
        else None)

    def set_value(self, row:int, col:int, value:int):
        self.table[row][col] = value

    def n_rows(self):
        return len(self.table)
    
    def n_cols(self):
        return len(self.table[0])

    def delete_row(self, row:int):
        self.table.pop(row)

    def delete_col(self, col:int):
        for row in self.table:
            row.pop(col)
    
    def add_row(self, row:int):
        self.table.insert(row, [0 for i in range(len(self.table[0]))])

    def add_col(self, col:int):
        for row in self.table:
            row.insert(col, 0)



table = Table(2,2)
# table.set_value(0,1,10)
# table.set_value(1,2,20)
# table.set_value(2,3,30)

for i in range(table.n_rows()):
    for j in range(table.n_cols()):
        print(table.get_value(i,j), end=' ')
    print()
print()

table.set_value(0,0,10)
table.set_value(0,1,20)
table.set_value(1,0,30)
table.set_value(1,1,40)
# table.add_col(2)

for i in range(table.n_rows()):
    for j in range(table.n_cols()):
        print(table.get_value(i,j), end=' ')
    print()
print()

for i in range(-1, table.n_rows()+1):
    for j in range(-1, table.n_cols()+1):
        print(table.get_value(i, j), end=' ')
    print()
print()