import numpy as np

"""
1차원 배열 생성
"""

a = np.array([0, 1, 2, 3])
print("a:", a)

# ndim : 배열의 차원 수
print("a.ndim:", a.ndim)

# shape : 배열의 형태 (1행 4열)
print("a.shape:", a.shape)

# size : 배열의 총 요소 수
print("a.size:", a.size)

# len() : 배열의 길이
print("len(a):", len(a))

"""
2차원 배열 생성
"""

b = np.array([[0, 1, 2], [3, 4, 5]])
print("b:", b)

print("b.ndim:", b.ndim)
print("b.shape:", b.shape)
print("b.size:", b.size)
print("len(b):", len(b))

"""
3차원 배열 생성
"""

c = np.array([[[1], [2]], [[3], [4]]])
print("c:", c)
print("c.shape:", c.shape)

"""
배열을 생성하는 함수들
"""

# arange() : 지정한 범위 내에서 균일한 간격으로 배열 생성
d = np.arange(10)
print("d:", d)

# arange() : 시작, 끝, 간격
e = np.arange(1, 9, 2)
print("e:", e)

# linspace() : 지정한 범위 내에서 균일한 간격으로 배열 생성
f = np.linspace(0, 1, 6)
print("f:", f)

# endpoint=False 옵션 사용
g = np.linspace(0, 1, 5, endpoint=False)
print("g:", g)

# ones() : 모든 요소가 1인 배열 생성
h = np.ones((3, 3))
print("h:\n", h)

# zeros() : 모든 요소가 0인 배열 생성
i = np.zeros((2, 2))
print("i:\n", i)

# eye() : 단위 행렬 생성
j = np.eye(3)
print("j:\n", j)

# diag() : 대각선 요소를 지정하여 배열 생성
k = np.diag(np.array([1, 2, 3, 4]))
print("k:\n", k)

# random.default_rng() : 난수 생성기 생성
rng = np.random.default_rng(27446968)
l = rng.random(4)
print("l:", l)

