import json

with open("story.json") as f:
    story = json.load(f) # <-- Дерево истории

current = "start" # <-- Текущий узел графа

while True:
    # 1. Вывести story[current]["text"]
    print(story[current]["text"])

    # 2. варианты
    if len(story[current]["next"]) == 0:
        print("Конец игры!")
        break 

    # Цикл по элементам story[current]["next"]
    # Для каждого n:
    #   1. Вывести номер варианта (начиная с 1)
    #   2. Вевести story[n]["name"]
    #   Пример вывода:
    #   Вы Онегин, бла-бла-бла
    #   
    #   Что Вы хотите сделать?
    #   1. Уехать в деревню
    #   2. ...
    #   
    print()
    print("Что выбираешь?\n")
    choices_keys = []
    for i, n in enumerate(story[current]["next"]):
        # i <-- Индекс варианта
        # n <-- Словарь варианта
        choices_keys.append(n)
        print(f"{i+1}.\t{story[n]["name"]}")

    choice = input("> ")
    if not choice.isdigit() or len(choices_keys) <= (choice := int(choice) - 1):
        print("Такого варианта нету")
        continue

    # 1. Проверить, что вариант есть (в choices_keys есть индекс choice)
    # 2. Если вариант есть, перескочить на него
    # choice <-- Вариант, который выбрал пользователь
    # choices_keys <-- Доступные варианты
    current = choices_keys[choice]
    print("\n========================\n")
    
