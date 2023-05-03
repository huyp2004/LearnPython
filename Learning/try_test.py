squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i < len(squares)):
    if squares[i] not in new_squares and squares[i] == 'orange':
        new_squares.append(squares[i])
    i += 1
print(new_squares)