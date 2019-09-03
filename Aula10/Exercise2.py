def eval_loop():
    while True:
        exp = input('>>> ')
        if exp == 'done':
            return result
        else:
            result = eval(exp)
            print(result)

eval_loop()
