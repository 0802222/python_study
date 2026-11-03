import numpy as np
import matplotlib.pyplot as plt

# 기본 시각화
# 이제 첫 번째 데이터 배열을 얻었으니, 이를 시각화해 보겠습니다.
# IPython에서는 %matplotlib을 사용하면 그래프가 대화형으로 보입니다.

# 1) 데이터 준비
x = np.linspace(0, 2 * np.pi, 200)
y = np.cos(x)

# 2) 그래프 그리기
plt.plot(x, y, label='cos(x)', color='blue')
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# 3) 그래프 표시
# 일반 Python 스크립트에서는 plt.show()를 꼭 호출해야 합니다.
# IPython에서는 %matplotlib이 활성화되어 있으면 보통 자동으로 표시됩니다.
plt.show()

# IPython에서 실행할 때는 아래처럼 입력하면 됩니다:
# %matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.cos(x)
# plt.plot(x, y)
# plt.show()
