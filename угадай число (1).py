from random import randint

attempt_count = 0
while True:
    n = randint(1, 10)
    guess = input("Угадай число от 1 до 10 ")
    while not guess.isdigit() or int(guess) != n:
        if guess.isdigit():
            if int(guess) > n:
                print("Твое число больше загадонного!")
            else:
                print("Твое число меньше загадонного!")
        else:
            print("Вводи цифры!")
        attempt_count += 1
        if attempt_count >= 3:
            print("Ты проиграл! Загаданное число было: " + str(n))
            break
        guess = input("Попробуй еще раз!: ")

    if guess.isdigit() and int(guess) == n or attempt_count >= 3:
        break
    print("Ты угадал! Число было: " + str(n))
    if input("Повторить игру? д/н  ") == 'н':
        break
    attempt_count = 0