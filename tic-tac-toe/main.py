def wincheck(x):#проверка победы, сделал функцией чтобы код было удобнее читать
    if any([board[0]==board[1]==board[2]==x, board[3]==board[4]==board[5]==x, board[6]==board[7]==board[8]==x]): #проверка горизонтали
        return True
    if any([board[0]==board[3]==board[6]==x, board[1]==board[4]==board[7]==x, board[2]==board[5]==board[8]==x]):#проверка вертикали
        return True
    if any([board[0]==board[4]==board[8]==x, board[2]==board[4]==board[6]==x]):#проверка диагонали
        return True
    return False
def current_score (): #функция для вывода результата после хода игроков + правил
    print(' | '.join(board[0:3]))
    print('— — — — — ')
    print(' | '.join(board[3:6]))
    print('— — — — — ')
    print(' | '.join(board[6:9]))
    return
board = list(map(str,[1,2,3,4,5,6,7,8,9]))#заполение "поля" номерами клеток для удобства
#раньее считал, что нормера лучше заранее стирать, но понял что играть без них не очень то удобно
print("Добро пожаловать в крестики нолики! Правила игры просты.")
current_score()
print("Два игрока X и О ходят по очереди вводя номер клетки в которую они хотят сходить.")
print("Победит тот, кто первым выстроит в ряд 3 свои фигуры, по вертикали, горизонтали или диагонали.")
print('Удачи!')
turn = 'X' #ставим первый ход за крестиком
space=9;

while True:
    print('Ходит '+turn+': ')
    vvod=int(input())
    while board[vvod-1] == 'X'or board[vvod-1] =='O': #проверка занятости клетки
        print("Клетка уже занята! Выберите другую")
        vvod=int(input())
    board[vvod-1] = turn
    if wincheck(turn):#проверяем победил ли игрок после того как поставил фигуру
        current_score()
        print(turn + ' победил!')
        break
    space-=1
    if space == 0:#проверка на ничью, сначала думал делать цикл for на проверку всех элементов списка, но решил что этот вариант будет менее ресурсозатратным
        current_score()
        print('Ничья!')
        break
    if turn == 'X': #меняем каждый шаг цикла с одной фигруры на другую
        turn = 'O'
    else:
        turn = 'X'
    current_score()
input("Нажмите Enter для выхода из программы")#для игры из консоли(которая закрывается сразу после конца, и не дает увидеть результат)