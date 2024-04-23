users:list[dict[str, str]] = [
{'name':'Kacper','surname':'Macioch','post': 1},
{'name':'Stanisław','surname':'Grzymski','post': 3},
{'name':'Michał','surname':'Krzywiński','post': 4},
{'name':'Tymoteusz','surname':'Grabianka','post': 5},
{'name':'Michał','surname':'Lembork','post': 2},
]
print(f'witaj {users[0]["name"]}')

 def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikwał {user["post"]} ')

read(users)


