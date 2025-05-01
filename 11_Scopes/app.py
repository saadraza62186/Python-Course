def func(num):
    def func2(x):
        return x ** num
    return func2

func1 = func(2)
func3 = func(3)

print(func1(2))  
print(func3(3))  