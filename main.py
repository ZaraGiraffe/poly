class Polynomial:
    def __init__(self, coefs):
        self.coeffs = [0]
        if isinstance(coefs, int):
            self.coeffs[0] = coefs
        elif isinstance(coefs, list) or isinstance(coefs, tuple):
            st = 0
            while st < len(coefs) and not coefs[st]:
                st += 1
            if st >= len(coefs):
                return
            self.coeffs = list(coefs[st:])

    def degree(self):
        return len(self.coeffs)-1

    def evalAt(self, point):
        num = 0
        for i in range(0, len(self.coeffs)):
            num += self.coeffs[i] * point**(self.degree()-i)
        return num

    def __str__(self):
        return f"Polynomial(coeffs={self.coeffs})"

    def coeff(self, point):
        return self.coeffs[self.degree()-point]

    def __eq__(self, other):
        if isinstance(other, int):
            return [other] == self.coeffs
        elif isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        point = 700
        return self.evalAt(point)

    def scaled(self, num):
        return Polynomial([self.coeffs[i] * num for i in range(len(self.coeffs))])

    def derivative(self):
        return Polynomial([self.coeffs[i] * (self.degree()-i) for i in range(self.degree())])

    def addPolynomial(self, other):
        if not isinstance(other, Polynomial):
            return None
        a = self.coeffs
        b = other.coeffs
        if len(a) < len(b):
            a, b = b, a
        b = [0 for i in range(len(a) - len(b))] + b
        new = [a[i] + b[i] for i in range(len(a))]
        return Polynomial(new)

    def multiplyPolynomial(self, other):
        n = self.degree()+1
        m = other.degree()+1
        new = [0 for i in range(self.degree() + other.degree() + 1)]
        for i in range(n):
            for j in range(m):
                new[i+j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(new)


class Quadratic(Polynomial):
    def __init__(self, coefs):
        super().__init__(coefs)
        if len(self.coeffs) != 3:
            raise SyntaxError('wrong number of coefs')

    def __str__(self):
        a, b, c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
        return f"Quadratic(a={a}, b={b}, c={c})"

    def discriminant(self):
        a, b, c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
        return b**2 - 4 * a * c

    def numberOfRealRoots(self):
        dis = self.discriminant()
        if dis > 0:
            return 2
        elif dis == 0:
            return 1
        else:
            return 0

    def getRealRoots(self):
        a, b, c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
        dis = self.discriminant()
        res = []
        if dis >= 0:
            res.append((-b - dis**0.5) / (2 * a))
            if dis > 0:
                res.append((-b + dis ** 0.5) / (2 * a))
        return res
