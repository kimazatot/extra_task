import json

def load_users(file_name):
    try:
        with open(file_name, 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = []
    
    return users_data

def save_users(file_name, users_data):
    with open(file_name, 'w') as file:
        json.dump(users_data, file, indent=2)

def create_user(users_data, user_data, filename):
    users_data.append(user_data)
    save_users(filename, users_data)
    print(f"Пользователь {user_data['name']} успешно создан.")

def update_user(user_id, updated_data, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    for user in data:
        if user.get('id') == user_id:
            user.update(updated_data)
            break

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print("Данные пользователя успешно обновлены.")

def delete_user(user_id, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    data = [user for user in data if user.get('id') != user_id]

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print("Пользователь успешно удален.")

# user_data1 = {"id": 1, "name": "Kim Ade", "email": "kimazatot@gmail.com", "password": "987654321"}
# user_data2 = {"id": 2, "name": "Lee Aisha", "email": "leeaisha@gmail.com", "password": "258963"}
# user_data3 = {"id": 3, "name": "Bakytov Aidar", "email": "bakytov_aidar@gmail.com", "password": "kimazatot"}

# create_user(load_users('users.json'), user_data1, 'users.json')
# create_user(load_users('users.json'), user_data2, 'users.json')
# create_user(load_users('users.json'), user_data3, 'users.json')

# update_user(3, {"age": 18}, 'users.json')
# update_user(2, {"email": "kim@gmail.com"}, 'users.json')
# update_user(3, {"password": "jsbest"}, 'users.json')

# delete_user(2, 'users.json')
# delete_user(2, 'users.json')