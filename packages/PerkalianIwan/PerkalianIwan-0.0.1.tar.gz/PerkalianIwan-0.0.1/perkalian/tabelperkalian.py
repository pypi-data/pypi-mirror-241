class Calculator:
    def multiplication_table(self, angka):
        for i in range(1, 11):
            print(angka, 'x', i, '=', angka * i)