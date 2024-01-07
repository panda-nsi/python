def f(x):
    return 27*x**3-27*x**2-18*x+8


def findMyO(a,b):
    points = []
    dot = a

    while dot <= b:
        print(f(dot), dot)
        if(f(dot) == 0):
            points.append(dot)
        dot += 0.1    
    return points


print(findMyO(-1, 2))