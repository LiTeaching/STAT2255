class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**0.5
    def __lt__(a, b):
        return a.dist_from_origin() < b.dist_from_origin()
    def __gt__(a, b):
        return a.dist_from_origin() > b.dist_from_origin()
    def __eq__(a, b):
        return a.dist_from_origin() == b.dist_from_origin()

import uuid

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

class SavingAccount(Account):
    def __init__(self, initial_amount, max_num_withdrawals=1,
                 minimum=1000, interest_rate=0.10,
                 bonus_contribution=0.15):
        super().__init__(initial_amount, minimum, interest_rate)
        # 1) Set the number of withdrawals to 0 (only SavingsAccounts track the number
        #    of withdrawals
        self._num_withdrawals = 0
        # 2) Set the _max_num_withdrawals attribute to the value given in the argument
        #    of the constructor
        self._max_num_withdrawals = max_num_withdrawals
        # 3) Set the _bonus_contribution to the value given in the argument of
        #    the constructor
        self._bonus_contribution = bonus_contribution

    def get_num_withdrawals(self):
        # Simply return the number of withdrawals
        return self._num_withdrawals

    def withdraw(self, w_amount):
        # 1) If the number of withdrawals is larger than or equal to the maximal
        #  number of withdrawals allowed throw and exception:
        #  raise ValueError("Savings accounts allow only {} withdrawals.".format(self._max_num_withdrawals))
        if self._num_withdrawals >= self._max_num_withdrawals:
            raise ValueError("Savings accounts allow only {} withdrawals.".format(self._max_num_withdrawals))
        # 2) Increase the withdrawal counter by 1
        else: self._num_withdrawals += 1
        # 3) Call the parent's implementation of withdraw as it does the rest of
        #    things for us
        super().withdraw(w_amount)

    def add_bonus(self):
        # According to the banks rewards scheme, increase the amount held by the
        # (percent bonus contribution) * (minimal amount ever held) + 100
        self._amount_held += 0.15 * self._min_ever_held + 100

    def close_account(self):
        # 1) Add bonus
        self.add_bonus()
        # 2) Call the parent's close_account method as it does lots of stuff already
        return super().close_account()
