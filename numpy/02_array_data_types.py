import numpy as np

"""
기본 데이터 유형
"""

# dtype : 배열의 데이터 유형 확인
m = np.array([1, 2, 3])
print("m:", m)
print("m dtype:", m.dtype)

# 실수 배열
n = np.array([1., 2., 3.])
print("n:", n)
print("n dtype:", n.dtype)

# dtype 지정
o = np.array([1, 2, 3], dtype=float)
print("o:", o)
print("o dtype:", o.dtype)

# 기본 데이터 형식 : float64
p = np.ones((3, 3))
print("p dtype:", p.dtype)

# bool : True/False
q = np.array([True, False, False, True])
print("q:", q)
print("q dtype:", q.dtype)

# 문자열
r = np.array(['Bonjour', 'Hello', 'Hallo'])
print("r:", r)
print("r dtype:", r.dtype)
