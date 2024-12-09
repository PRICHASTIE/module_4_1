def divide(first, second):
    if second == 0:
        return 'ошибка'
    else:
        return first / second
if __name__ == '__main__':
    result = divide(69,0)
    print(result)

