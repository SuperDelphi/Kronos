import kronos as k


def add(x, y):
    return x ** y


results = k.kalk(add, display=True, iteration_count=10000, complete_data=True, x=2000, y=3000)
