import numpy as np

# indexing
a = np.arange(10)
print("a:", a)

print("a[0]:", a[0], "a[2]:", a[2], "a[-1]:", a[-1])

print(a[::-1])  # 역순으로 출력

a = np.diag(np.arange(3))
print("a:\n", a)

print([a[1, 1]])

a[2, 1] = 10
print(a)

# slicing
a = np.arange(10)
print("a:", a)

a[2:9:3] # start:stop:step

a[:4]

a[1:3]

a[::2]
a[3:]

# 할당과 슬라이싱 결합
a = np.arange(10)
a[5:] = 10
print(a)

b = np.arange(5)
a[5:] = b[::-1]
print(a)

# 뷰 : 슬라이싱 연산은 원본 배열의 뷰를 반환합니다.
# 뷰를 수정하면 원본 배열도 수정됩니다.
a = np.arange(10)
print("a:", a)

b = a[::2]
print("b:", b)

np.may_share_memory(a, b)  # True

b[0] = 12
print("b:", b)
print("a:", a)  # a도 수정됨

a = np.arange(10)
c = a[::2].copy()  # 복사본 생성
c[0] = 12
print("a:", a)  # a는 수정되지 않음
print("c:", c)  # c는 수정됨

np.may_share_memory(a, c)  # False

"""
소수 판별
: 에라토스테네스 체
"""

# bool 배열 생성
is_prime = np.ones((100,), dtype=bool)

# 소수가 아닌 0과 1을 지운다.
is_prime[:2] = 0

# 2부터 시작하는 각 정수에 대해 j, 그보다 큰 배수를 모두 지운다.
N_max = int(np.sqrt(len(is_prime) -1))
for j in range(2, N_max + 1):
    is_prime[2 * j :: j] = False


"""
고급 인덱싱
"""

# 불리언 마스크 사용
rng = np.random.default_rng(27446968)
a = rng.integers(0, 21, 15)
print("a:", a)

print(a % 3 == 0)  # 3의 배수인지 여부

mask = (a % 3 == 0)
extract_from_a = a[mask]
print("extract_from_a:", extract_from_a)

a[a % 3 == 0] = -1
print("a:", a)

# 정수 배열을 사용한 인덱싱
a = np.arange(0, 100, 10)
print("a:", a)

# 정수 배열을 사용한 인덱싱 ( 동일 인덱스 여러번 반복 )
print(a[[2, 3, 2, 4, 2]])

# 이러한 방식을 이용해 새로운 값 할당
a[[9, 7]] = -100
print("a:", a)

# 정수배열의 인덱싱을 이용하여 새 배열 생성 시 , 새 배열은 원래 정수배열과 동일한 shape을 갖습니다.
a = np.arange(10)
idx = np.array([[3, 4], [9, 7]])
idx.shape  # (2, 2)

a[idx]  # shape (2, 2)


# 고급인덱싱과 브로드캐스팅
a = np.arange(12).reshape((3, 4))
print("a:\n", a)

i = np.array([[0, 1], [1, 2]])
a[i, 2] # shape (2, 2)