names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz',
'Edward', 'Piotr', 'Jan', 'Denis', 'Amir', 'Igor', 'Borys',
'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel']

name_dict = {}

for name in names:
    v = name_dict.setdefault(name[0], set())
    v = v | {name}
    name_dict[name[0]] = v

print(name_dict)