class Translator:
    d = {}

    def add(self, eng, rus):
        self.d[eng] = self.d.get(eng, []) + [rus]

    def remove(self, eng):
        return self.d.pop(eng)

    def translate(self, eng):
        return self.d.get(eng)

    def rrg(self):
        return self.d


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(tr.rrg())
print(*tr.translate('go'))
