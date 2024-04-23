from models.data import users
from init.crud import read,add_user


if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')



    read(users)
    add_user(users)
    read(users)


