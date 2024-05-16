from models.data import users
from init.crud import read,add_user


if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')
    print('6.wyswietl mape dla uzytkownika')



    read(users)
    add_user(users)
    read(users)
    if menu_option =='6' : map_single_users(users)


