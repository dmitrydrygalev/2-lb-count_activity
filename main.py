height = int(input("-| Напишите ваш рост(м): "))
mass = int(input("-| Напишите ваш вес(кг): "))
steps = int(input("-| Сколько шагов вы сегодня прошли: "))
activeTime = int(input("-| Сколько заняла времени тренировка(мин): "))


def countTrainingCost(M, H, S, T):
    distance = S * (H / 4 + 0.37)
    speed = int(distance / T)
    energy = int(0.035 * M + (speed ** 2 / H) * 0.029 * M)

    if distance <= 2000:
        motivateText = ' Продолжаем в том же духе! '
    elif distance <= 4000:
        motivateText = ' Ого мы уже ушли так далеко, не время останавливаться '
    elif distance > 4000:
        motivateText = ' Вы молодец! Невероятная дистанция! '

    return distance, energy, motivateText


print(f"Дистанция(м) - калории:{countTrainingCost(mass, height, steps, activeTime)}")
