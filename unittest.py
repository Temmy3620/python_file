"""_summary_
レポート１　有理数、複素数の四則演算

"""
q1 = (7, 3)
q2 = (-12, 5)
c1 = (3, -2)
c2 = (-4, 5)


import unittest
from fractions import Fraction

qadd = lambda a,b,c,d : a/b + c/d
qsub = lambda a,b,c,d : a/b - c/d
qmul = lambda a,b,c,d : float(a/b) * float(c/d)
qdiv = lambda a,b,c,d : float(a/b) / float(c/d)
cadd = lambda a,b,c,d : (a+c) + (b+d)* 1j
csub = lambda a,b,c,d : (a-c) + (b-d)* 1j
cmul = lambda a,b,c,d : a * c - (b * d) + (b * c + a * d) * 1j
cdiv = lambda a,b,c,d : ((a * c + b * d) + (b * c - a * d) * 1j) / (c * c + d * d)

class AddTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(qadd(q1[0],q1[1],q2[0],q2[1]),float(Fraction(q1[0],q1[1])) + float(Fraction(q2[0],q2[1])))
    def test2(self):
        self.assertEqual(qsub(q1[0],q1[1],q2[0],q2[1]),float(Fraction(q1[0],q1[1])) - float(Fraction(q2[0],q2[1])))
    def test3(self):
        self.assertEqual(qmul(q1[0],q1[1],q2[0],q2[1]),float(Fraction(q1[0],q1[1])) * float(Fraction(q2[0],q2[1])))
    def test4(self):
        self.assertEqual(qdiv(q1[0],q1[1],q2[0],q2[1]),float(Fraction(q1[0],q1[1])) / float(Fraction(q2[0],q2[1])))
    def test5(self):
        self.assertEqual(cadd(c1[0],c1[1],c2[0],c2[1]),complex(c1[0],c1[1]) + complex(c2[0],c2[1]))
    def test6(self):
        self.assertEqual(csub(c1[0],c1[1],c2[0],c2[1]),complex(c1[0],c1[1]) - complex(c2[0],c2[1]))
    def test7(self):
        self.assertEqual(cmul(c1[0],c1[1],c2[0],c2[1]),complex(c1[0],c1[1]) * complex(c2[0],c2[1]))
    def test8(self):
        x = cdiv(c1[0],c1[1],c2[0],c2[1])
        y = complex(c1[0],c1[1]) / complex(c2[0],c2[1])
        self.assertEqual(round(x.real,10) + round(x.imag,10) * 1j,round(y.real,10) + round(y.imag,10) * 1j)
        
        
unittest.main()