class ValidadeInput:
    def __init__(self, user: str) -> str:
        self.user = user

    def userChar(self):
        if len(self.user) < 12:
            return self.user
        else:
            return f"{self.user} has {len(self.user)} char, failed!"

    def userSpaces(self):
        if not self.user.find(' ') -1:
            return f"There's {self.user.count(' ')} space in your name, failed!"
        else:
            return self.user

    def userDigits(self):
        if not self.user.isalpha():
            return f"There's digits in your name, failed!"
        else:
            return self.user

    def __str__(self) -> str:
        return self.user

p1 = ValidadeInput('Matheuzxz xcczd')

print(p1.userChar())