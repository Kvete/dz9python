class Position:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


a = Position('ilia', 'kvetenadze', 'student', {'wage': 4000, 'bonus': 3000})
b = Position('ilia', 'kvetenadze', 'student', {'wage': 4000, 'bonus': 3000})
d = Position('ilia', 'kvetenadze', 'student', {'wage': 4000, 'bonus': 3000})
c = a
my_list = [a, b, c]
