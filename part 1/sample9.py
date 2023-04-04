from sample5 import *

devy = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x,devy,color='#444444',linestyle='--',label='All Devs')
plt.plot(dev_x,py_dev_y,color='#5a7d9a',label='Python')
plt.plot(py_dev_x,js_dev_y,color='#adad3b',label='Javascript')

plt.xlabel('Ages')
plt.ylabel('Median Salary USD')
plt.title('Median Salary USD by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('Figure_9.png')
plt.show()