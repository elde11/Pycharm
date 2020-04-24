# Example CSV http://siepietowski.pl/course/data.csv
import csv
from functools import reduce
class CsvReader:
    # __init__ wczytanie pliku csv poprzez podanie scieżki + stworzenie 2 pól _path, _sheet (2d list)
    # get_sheet zwórcenie sheeta
    def __init__(self, filepath):  # to jest konstruktor
        self.filepath = filepath  # przypisujemy do prywatnego pola jaki jest filepath
        with open(filepath) as file:
            temp = csv.reader(file)  # import danych z pliku csv
            self._content = list(temp)[1:]  # zwróci wszytsko z listy oprócz pierwszego wiersza
    def get_content(self):  # druga metoda
        return self._content  # metodfa zwraca nam content który jest prywatny (bo podłoga)
    #  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola
class SheetCalculator:
    pass
    def __init__(self, content):
        self._content = content  # to jest pole naszej klasy
# get_column
    def get_column(self, column):
        return list(x[column] for x in self._content)   #tutaj użyjemy list comprehension
# get_row
    def get_row(self, num):
        return self._content[num]
# count_column
    def count_column(self):
        return len(self._content[1])
# count_row
    def count_row(self):
        return len(self._content)
# sum_column
    def sum_column(self, column):
        return reduce(lambda el1, el2 : int(el1) + int(el2), self.get_column(column))
# mul_column
    def mul_column(self, column):
        return reduce(lambda el1, el2: int(el1)*int(el2), self.get_column(column))
# mean_column
    def mean_column(self, column):
        return self.sum_column(column)/self.count_row()
# apply_function_on_column

        # High order functions
    def apply_function_on_column(self, number, function):
        return reduce(function, self.get_column(number))
        # apply_function_on_column



file1 = CsvReader('data/data.csv')  # scieżka do pliku na którym chcemy pracować
content = file1.get_content()  # przypisanie funkcji do contentu
print(content)
SheetCalculator(content)  # tworzenie nowego obiektu i przypisanie go do zmiennej
sheet_calculator = SheetCalculator(content)
print(sheet_calculator)
print(sheet_calculator.get_row(7))
print(sheet_calculator.count_column())
print(sheet_calculator.get_column(5))
print(sheet_calculator.sum_column(5))
print(sheet_calculator.mul_column(0))
print(sheet_calculator.mean_column(0))
sheet_calculator = SheetCalculator(CsvReader("data/data.csv").get_sheet())
print(sheet_calculator.apply_function_on_column(1, lambda x, y: x + y))
print(sheet_calculator.apply_function_on_column(6, lambda x, y: int(x) + int(y)))
print(sheet_calculator.apply_function_on_column(6, lambda x, y: int(y)))