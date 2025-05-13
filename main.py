import random

# Чтение имен из файла
names = []
with open("characters.txt", 'r', encoding='utf-8') as f:
    for line in f:
        name = line.strip()
        if name:  # Проверяем, что строка не пустая
            names.append(name)

# Создание словаря со статусами
characters = {}
for name in names:
    status = random.choice(['жив', 'мертв'])
    characters[name] = status

# Запись в output.txt
with open("output.txt", 'w', encoding='utf-8') as file:
    for name in characters:
        file.write(f"{name} - {characters[name]}\n")

# Фильтрация живых персонажей
alive_characters = []
for name in characters:
    if characters[name] == 'жив':
        alive_characters.append(name)

# Фильтрация мертвых персонажей
dead_characters = []
for name in characters:
    if characters[name] == 'мертв':
        dead_characters.append(name)

# Запись живых персонажей в файл
with open("alive-characters.txt", 'w', encoding='utf-8') as file:
    for name in alive_characters:
        file.write(f"{name}\n")

# Запись мертвых персонажей в файл
with open("dead-characters.txt", 'w', encoding='utf-8') as file:
    for name in dead_characters:
        file.write(f"{name}\n")

# Обновление characters.txt (только мертвые персонажи)
with open("characters.txt", 'w', encoding='utf-8') as file:
    for name in dead_characters:
        file.write(f"{name}\n")