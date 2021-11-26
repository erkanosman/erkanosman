import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range

plt.plot(x, np.sin(x))   # Plot the sine of each x point
plt.grid()
plt.show()  # Display the plot

x= np.linspace(0,10,100)
plt.plot(x, x**3)
plt.grid()
plt.show()

#import matplotlib.pyplot as plt
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x2, y + 0.5, 'bs')
plt.ylim([-0.5, 1])
#(-0.5, 1)
plt.show()

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()



