import sympy
from numpy import random
from fractions import Fraction


def generate_A(n=2):
    if n == 2:
        matrix = [[random.randint(-20, 20) for i in range(n)] for k in range(n)]
    else:
        matrix = []
        while True:
            summa_stolb = 0
            a = []
            for k in range(n):
                rnd = random.randint(-20, 20)
                a.append(rnd)
                summa_stolb += rnd ** 2
            if type(sympy.sqrt(summa_stolb)) is sympy.core.numbers.Integer:
                matrix.append(a)
            if len(matrix) == n:
                break
    # ====================================================================
    return matrix


def transpose(mtx):
    return [list(i) for i in zip(*mtx)]


def to_orthogonal(mtx, i=0, q=None):
    if i == len(mtx):
        return q
    if i == 0:
        under_sqrt = sum(j ** 2 for j in mtx[i])  # знаменатель q_1
        q = [[Fraction(k, 1) * (1 / sympy.sqrt(under_sqrt)) for k in mtx[i]]]  # считается столбец q_1
    else:
        sum_under_sqrt = 0  # то, что получается под корнем (сумма квадратов каждого значения a_энного) для q_энного (n>=1)
        a_p = []  # список элементов в a_энном_перпендикулярном
        scalar = []  # скалярное произведение <a_n,q_k>q_k
        scalar_sum = []
        for g in range(len(q)):
            scalar.append([sum(mtx[i][k] * q[g][k] for k in range(len(mtx))) * q[g][j] for j in range(len(mtx))])
        summa = scalar[0]
        if i > 1:
            for j in range(len(mtx)):
                for k in range(1, len(scalar)):
                    summa[j] += scalar[k][j]
        scalar_sum.append(summa)
        for j in range(len(mtx)):
            t = (mtx[i][j] - scalar_sum[0][j])
            a_p.append(t)
            sum_under_sqrt += t ** 2
        s = 1 / sympy.sqrt(sum_under_sqrt)
        if type(s) != sympy.core.numbers.Rational and (i != 1 and len(mtx) < 4):
            return 0
        q.append([s * a_p[k] for k in range(len(mtx))])
    return to_orthogonal(mtx, i + 1, q)


def printer(mtx):
    try:
        mtx = transpose(mtx)
        if len(mtx) == 2:
            tmp = 0
            for i in range(len(mtx)):
                for j in range(len(mtx)):
                    if type(mtx[i][j]) is sympy.core.mul.Mul and mtx[i][j] != sympy.core.numbers.nan:
                        try:
                            tmp = (str(mtx[i][j]).split('*')[1])
                            verx, niz = tmp.split('/')
                            mtx[i][j] /= sympy.sqrt(int(verx.split('(')[1].split(')')[0]))
                            mtx[i][j] *= int(niz)
                        except:
                            tmp = str(mtx[i][j])
                            verx, niz = (tmp.split('/'))
                            mtx[i][j] /= sympy.sqrt(int(verx.split('(')[1].split(')')[0]))
                            mtx[i][j] *= int(niz)
            if tmp != 0:
                if tmp[0] == 's':
                    print(tmp, ' * ', end='')
                    print()
                else:
                    tmp = tmp[1:]
                    print(tmp, ' * ', end='')
                    print()
            for i in mtx:
                print(i)
        else:
            for i in mtx:
                print(i)
    except:
        raise Exception


def generateQ(n):
    while True:
        matrix = to_orthogonal(generate_A(n))
        tmp = []
        if type(matrix) is list and len(matrix) < 4:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if type(matrix[i][j]) is sympy.core.numbers.Rational:
                        tmp.append(int(str(matrix[i][j]).split('/')[1]))
            tmp = list(set(tmp))
            if len(tmp) > 0:
                tmp = max(list(set(tmp)))
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        matrix[i][j] *= tmp
            return matrix
        elif type(matrix) is list and len(matrix) >= 4:
            return matrix
        else:
            matrix = to_orthogonal(generate_A(n))


printer(generateQ(3))
