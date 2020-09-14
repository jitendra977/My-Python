def divide(a, b):
    try:
        print(f'{a}/{b},is Equal to {a / b}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print('No Exceptions Error')


divide(8, 2)
