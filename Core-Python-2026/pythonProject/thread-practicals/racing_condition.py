from time import sleep
from threading import *
import threading
from tkinter.font import names


class Account:

    def __init__(self):
        self.balance = 0

    def set_balance(self, balance):
        sleep(1)
        self.balance = balance

    def get_balance(self):
        sleep(1)
        return self.balance

    def diposite(self, amount):
        bal = self.get_balance()
        self.set_balance(bal + amount)


class Racing(Thread):
    def __init__(self, account: Account, name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.diposite(100)
            print(self.name, self.account.get_balance())


def main_task():
    acc = Account()
    t1 = Racing(acc, 'abc')
    t2 = Racing(acc, 'xyz')

    t1.start()
    t2.start()


main_task()
