class DateCalculator:
    def __init__(self, year, month, day):
        if month < 3:
            month += 12
            year -= 1

        self.q = day
        self.m = month
        self.K = year % 100
        self.J = year // 100

    def get_day(self):
        h = (self.q + (13 * (self.m + 1)) // 5 + self.K + self.K // 4 + self.J // 4 + 5 * self.J) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

# Example
y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))

calc = DateCalculator(y, m, d)
print("Day of the week is:", calc.get_day())
