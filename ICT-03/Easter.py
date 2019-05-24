class Easter:
    def solveEaster(self):
        a = self % 19
        print("a = " + str(a))
        b = self // 100
        print("b = " + str(b))
        c = self % 100
        print("c = " + str(c))
        d = b // 4
        print("d = " + str(d))
        e = b % 4
        print("e = " + str(e))
        f = (b + 8) // 25
        print("f = " + str(f))
        g = (b - f + 1) // 3
        print("g = " + str(g))
        h = (19 * a + b - d - g + 15) % 30
        print("h = " + str(h))
        i = c // 4
        print("i = " + str(i))
        k = c % 4
        print("k = " + str(k))
        r = (32 + 2 * e + 2 * i - h - k) % 7
        print("r = " + str(r))
        m = (a + 11 * h + 22 * r) // 451
        print("m = " + str(m))
        n = (h + r - 7 * m + 114) // 31
        print("n = " + str(n))
        p = (h + r - 7 * m + 114) % 31
        print("p = " + str(p))
        print("Easter in " + str(self) + " falls on " + (str(n)) + "/" + (str(p + 1)))

    solveEaster(2020)
