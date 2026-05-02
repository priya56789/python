# Q4. Build a Loan class that:
# Has a common interest rate for all loans.
# Each object stores borrower name and principal.
# Calculates total payable amount.
# Provides a function to update the interest rate.
# Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# Creating multiple loan accounts.
# Updating interest rates.
# Checking eligibility and total repayment for borrowers.



class Loan:
    interest_rate = 10

    def __init__(self, borrower_name, principal):
        self.borrower_name = borrower_name
        self.principal = principal

    def total_payable_amount(self):
        interest = (self.principal * 1 * self.interest_rate) / 100
        print(interest)

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def Loan_eligibility(salary):
        if salary > 100 and salary < 10000:
            return True
        else:
            return False


account1 = Loan("Priyanka", 10000)
account2 = Loan("Eswar", 8000)
print(account1.borrower_name, account1.principal)
print(account2.borrower_name, account2.principal)
account1.total_payable_amount()
print(account1.total_payable_amount())
Loan.change_interest_rate(20)
print(Loan.interest_rate)
print(Loan.Loan_eligibility(8000))
print(Loan.Loan_eligibility(80))
