import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        x = input.data  # データを取り出す
        y = x ** 2  # 実際の計算
        output = Variable(y)    # Variableとして返す
        return output


x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))
print(y.data)
