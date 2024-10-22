from threading import Thread, Lock
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add_amount = randint(50, 500)
            self.balance += add_amount
            print(f'Пополнение: {add_amount}, Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            remove_amount = randint(50, 500)
            print(f'Запрос на: {remove_amount}')
            if remove_amount <= self.balance:
                self.balance -= remove_amount
                print(f'Снятие: {remove_amount}, Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')