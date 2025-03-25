
import uuid
class Phone:
    def __init__(self, user_name, color, size):
        self.user_name = user_name
        self.color = color
        self.size = size
        self.apps = []
        self._password = None
    def show_user_name(self):
        print("The User name is", self.user_name)
    def Download_app(self, app_name):
        self.apps.append(app_name)
    def Uninstall_app(self, app_name):
        self.apps.remove(app_name)
    def set_password(self, old_password = None, new_password = None):
        if self._password == old_password:
            self._password = new_password
        else:
            print("Old Password not match!")
    def __le__(self, a):
        return self.size <= a.size
    def __ge__(self, a):
        return self.size >= a.size
    def __eq__(self, a):
        return self.size == a.size
    def __ne__(self, a):
        return self.size != a.size
    def __lt__(self, a):
        return self.size < a.size
    def __gt__(self, a):
        return self.size > a.size
    def __str__(self):
        return "user_name => {}, color => {}".format(self.user_name, self.color)

class Account:
    def __init__(self, initial_amount, minimum, interest_rate):
        if (initial_amount < minimum):
            raise ValueError("When creating this account, the initial amount must be >= {}.".format(minimum))
        self._id = str(uuid.uuid4())[:5]
        self._minimum       = minimum
        self._amount_held   = initial_amount
        self._min_ever_held = initial_amount
        self._interest_rate = interest_rate
        self._good_standing = True   
        self._is_active     = True
    def get_amount_held(self):
        return self._amount_held
    def get_minimum(self):
        return self._minimum
    def get_min_ever_held(self):
        return self._min_ever_held
    def get_interest_rate(self):
        return self._interest_rate
    def is_in_good_standing(self):
        return self._good_standing
    def is_active(self):
        return self._is_active;
    def withdraw(self, w_amount):
        if (w_amount > self._amount_held):
            raise ValueError("Cannot withdraw more than you have.")
        self._amount_held = self._amount_held - w_amount
        if (self._amount_held < self._minimum):
            self._good_standing = False;
        if (self._amount_held < self._min_ever_held):
            self._min_ever_held = self._amount_held
    def deposit(self, amount):
        self._amount_held += amount;
        if (self._amount_held >= self._minimum):
            self._good_standing = True
    def close_account(self):
        self._is_active = False;
        self._amount_held += self._min_ever_held * self._interest_rate
        return self._amount_held