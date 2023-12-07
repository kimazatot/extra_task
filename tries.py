db = [
    {'name': 'hello', 'password': '1235678'},
    {'name': 'test123', 'password': 'helloworld'}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
        return False
# print(in_database('hello'))

def validate_password(password):
    if len(password) < 8:
        raise Exception('слишком короткий пароль')
    return True



def register(name, password):
    if in_database(name):
        raise Exception('юзер с таким именем уже есть')
    if validate_password(password):
        user = ({'name': name,'password': password})
        db.append(user)
        return 'вы успешно зарегистрировались'

# print(register('hello1', '123465789'))
# print(db)

def login(name, password):
    for user in db:
        if user['name'] == name:
            # if user['password'] == password:
            #     return('вы успешно залогинились')
            if user['password'] == password:
                return 'вы успешно залогинились'
    else:
        raise Exception('неверный пароль')
                
    
print(login('test123', 'helloworld'))