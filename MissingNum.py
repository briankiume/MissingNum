def soln(a):
    a.sort()
    missing = 0
    for i in range(a[0], a[-1]):
        if i not in a:
            missing = i
    return missing


print(soln([2, 3, 1, 5]))
