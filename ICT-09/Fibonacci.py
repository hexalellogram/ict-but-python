class Fibonacci:
    def calc_fib(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.calc_fib(x - 1) + self.calc_fib(x - 2)

    def calc_mult(self, a, b):
        if a == 0:
            return 0
        else:
            a = a - 1
            return self.calc_mult(a, b) + b


fib = Fibonacci()
print("Fibonacci:")
print(str(fib.calc_fib(0)))
print(str(fib.calc_fib(3)))
print(str(fib.calc_fib(11)))
print()
print("Multiplication:")
print(str(fib.calc_mult(0, 4)))
print(str(fib.calc_mult(3, 1)))
print(str(fib.calc_mult(7, 8)))
print(str(fib.calc_mult(5, 0)))
print(str(fib.calc_mult(45, 11)))