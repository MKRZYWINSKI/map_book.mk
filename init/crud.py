def read(users: list[dict[str, str]]) -> None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikwał {user["post"]} ')

def add_user(lista: list) -> None:
    user_name = input('Podaj imię:')
    user_surname = input('podaj nazwisko:')
    user_post = input('Podaj ile postów:')
    lista.append({'name': user_name, 'surname': user_surname, 'post': user_post}, )

    def remove_user(users: list[dict[str, str]]) -> None:
        user_name = input('kogo skasować')
        for user in users[1:]:
            if user['name'] == user_name:
                print(f'zanloziono xnajmowego{user['name']}  ')
                users.remove(user)

    remove_user(users)



