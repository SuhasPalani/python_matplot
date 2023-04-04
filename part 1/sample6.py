from sample5 import *
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x,dev_y,color='#444444',linestyle='--',label='All Devs')
plt.plot(dev_x,py_dev_y,color='#5a7d9a',label='Python')
plt.plot(py_dev_x,js_dev_y,color='#adad3b',label='Javascript')

plt.xlabel('Ages')
plt.ylabel('Median Salary USD')
plt.title('Median Salary USD by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()