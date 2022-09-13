height = int(input("-| Напишите ваш рост(м): "))
mass = int(input("-| Напишите ваш вес(кг): "))
steps = int(input("-| Сколько шагов вы сегодня прошли: "))
activeTime = int(input("-| Сколько заняла времени тренировка(мин): "))


def countTrainingCost(M, H, S, T):

    distance = S * (H / 4 + 0.37)
    speed = int(distance/T)
    energy = int(0.035 * M + (speed ** 2 / H) * 0.029 * M)

    return distance, energy


print(f"Дистанция(м) - калории:{countTrainingCost(mass, height, steps, activeTime)}")
