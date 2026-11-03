import numpy as np
import matplotlib.pyplot as plt

# IPython에서 2차원 배열 이미지를 그리는 예제
# 먼저 대화형 백엔드를 활성화합니다.
# %matplotlib

rng = np.random.default_rng(27446968)
image = rng.random((30, 30))

plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.title('Random 2D Image')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# IPython에서 실행할 때는 아래처럼 입력하면 됩니다:
# %matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# rng = np.random.default_rng(27446968)
# image = rng.random((30, 30))
# plt.imshow(image, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()
