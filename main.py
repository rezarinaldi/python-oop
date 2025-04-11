from bankaccount import BankAccount

reza_account = BankAccount("Reza", 1000)
jessy_account = BankAccount("Jessy", 2000)

reza_account.check_balance()
jessy_account.check_balance()

reza_account.deposit(400)
jessy_account.withdraw(600)

reza_account.check_balance()
jessy_account.check_balance()