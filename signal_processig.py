import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
image = misc.face(gray=True).astype(np.float32)
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(image, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) +
         signal.sepfir2d(ck, [1], derfilt))

plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()
