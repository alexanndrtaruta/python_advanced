
from datetime import date
import string


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.reg_date = date.today()
    def check_valid(self):
        for i in Model.user_info:
            if i.get("login", "") == self.login:
                print('Login is already exists')
                return False

        if len(self.password) < 8:
            print('Password should be more than 8 chars')
            return False
        elif not self.login.translate(string.punctuation).isalnum():
            print('Login should consist only latin letters and digits')
            return False
        elif len(self.login) < 4:
            print('Login should be more than 4 chars')
            return False
        elif not self.password.translate(string.punctuation).isalnum():
            print('Password should consist only latin letters and digits')
            return False
        else:
            self.save_user()
            return True

    def save_user(self):
        model = Model()
        model.user_info.append(dict({'login': self.login, 'password': self.password, 'data': self.reg_date}))
        print(model.user_info)

class Model:
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance: cls._instance = super().__new__(cls)
        return cls._instance

    user_info = []
    user_posts = []

class SignIn(Registration):

    def __init__(self, login, password):
        super().__init__(login, password)
        self.login = login
        self.password = password

    def check_user(self):
        for i in range(len(Model.user_info)):
            if Model.user_info[i]['login'] == self.login and Model.user_info[i]['password'] == self.password:
                return True

class User:

    def __init__(self, login):
        self.login = login

    def add_post(self,post):
        Model.user_posts.append(dict({'login': self.login, 'post': post, 'date': date.today()}))


class Admin(User):
    def __init__(self, login):
        super().__init__(login)
        self.login = login

    @staticmethod
    def show_users():
        print(Model.user_info)

    @staticmethod
    def delete_user(login):
        for i in range(len(Model.user_info)):
            if Model.user_info[i]['login'] == login:
                Model.user_info.pop(i)



class Controller:
    admin_password = '1'
    current_user = None
    choice = ''
    def __init__(self):
        self.show_sing_in()

    def show_sing_in(self):
        self.choice = input('1 for registration , 2 for sign in, press 3 to create admin account: ')
        if self.choice == '1':
            self.registration_form()
        elif self.choice == '2':
            self.sign_in_form()
        elif self.choice == '3':
            admin_access = input('Enter admin password to create an admin account: ')
            if admin_access == self.admin_password and admin_access.isdigit():
                self.registration_form()
            else:
                print('wrong choice')
                self.show_sing_in()
        else:
            print('wrong choice')

    def registration_form(self):
        login = input('Enter your new login: ')
        password = input('Enter your password: ')
        register_user = Registration(login, password)
        if not register_user.check_valid():
            self.show_sing_in()
        else:
            self.sign_in_form()

    def sign_in_form(self):
        login = input('Enter your login: ')
        password = input('Enter your password: ')
        signed_user = SignIn(login, password)
        if signed_user.check_user() and self.choice == '1':
            self.current_user = User(login)
            print('Success')
            self.control_panel()
        elif signed_user.check_user() and self.choice == '3':
            self.current_user = Admin(login)
            print('Success')
            self.admin_panel()
        else:
            self.sign_in_form()

    def admin_panel(self):
        self.choice = input('Press 1 to get users info , press 2 to delete user, press 3 to log out')
        if self.choice == '1':
            self.current_user.show_users()
        elif self.choice == '2':
            user_login_to_delete = input('Enter user login to delete')
            if user_login_to_delete in Model.user_info:
                self.current_user.delete_user(user_login_to_delete)
        elif self.choice == '3':
            self.current_user = None
            self.sign_in_form()


    def control_panel(self):

        choice = input('Press 1 to make post press 2 to log out')
        if choice == '1':
            post = input('Create post')
            self.current_user.add_post(post)
            self.control_panel()
        elif choice == '2':
            self.current_user = None
            self.show_sing_in()
        else:
            print("wrong choice ")
            self.sign_in_form()

Controller()