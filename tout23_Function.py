def func(a, b):
    print("Hello We are in func", "Total is :", a + b)


def func2(a, b):
    """"
    this function contain calculate the average of the two
    numbers work we writing inside the doc string
    printing idea is print(func2.__doc__)
    """
    average = (a + b) / 2
    print("Average is:",average)


func(5, 6)
func2(10, 15)
