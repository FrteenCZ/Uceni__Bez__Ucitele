# lineární
![image.png](../../img/Pasted%20image%2020251030091240.png)
$$
\begin{align}
\text{curve}:&& ax+b=\hat{y} \\
\text{data}:&&\{ p_{1}, p_{2},\dots,p_{n} \} \\
 \\
\text{error}:&& e_{i}=y_{i}-\hat{y_{i}} = y_{i}-(ax_{i}+b)  \\
&&S(a,b)=\sum_{i=1}^ne_{i}  \\
\text{MSE}:&& e_{i}=(y_{i}-\hat{y_{i}})^{2} = \left(y_{i}-(ax_{i}+b) \right)^{2}  \\
&&S(a,b)=\frac{1}{n}\sum_{i=1}^ne_{i} \\
 \\
\text{minimum}:&& \frac{\delta S}{\delta a}=0;~\frac{\delta S}{\delta b}=0 \\
&& \frac{\delta S}{\delta a}= \sum_{i=1}^n2\left(y_{i}-(ax_{i}+b) \right)(-x_{i}) =0\\
&& \frac{\delta S}{\delta b}= \sum_{i=1}^n2\left(y_{i}-(ax_{i}+b) \right)(-1) =0 \\
 \\
b=\frac{\sum_{i=1}^ny_{i}-a\sum_{i=1}^nx_{i}}{n} && a = \frac{n\sum_{i=1}^nx_{i}y_{i}-\sum_{i=1}^nx_{i}\cdot\sum_{i=1}^ny_{i}}{n\sum_{i=1}^nx_{i}^{2}-\left(\sum_{i=1}^nx_{i}\right)^{2}}
\end{align}
$$
```python
import numpy as np
import matplotlib.pyplot as plt

def linearRegression(x,y):
    n=len(x)

    a = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - a*np.sum(x)) / n
    return a,b

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])

a,b = linearRegression(x,y)
print(f"a: {a}, b: {b}")

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, a*x + b, color='red', label='Best fit line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()
```
