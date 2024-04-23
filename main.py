from models.data import users
from init.crud import read,add_user


if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')



while True:
        print('0.zakoncz program')
        print('1.wyswietl uzytkownikow: ')
        print('2.wyswiatl znajmych')
        print('3.wyswietl')
        print('4.usun znajmowego')
        menu_option=input('wybierz opcje menu')
        if menu_option == '0':break
        if menu_option == '1':read(users)
        if menu_option == '2':add_user(users)
        if menu option == "3": search(users)
        if menu option == "4": remove.user(users)




