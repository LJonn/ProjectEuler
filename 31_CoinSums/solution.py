a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
counter = 0
value = 0
target = 200


def update(counter, value):
    value = a+2*b+5*c+10*d+20*e+50*f+100*g+200*h
    if (value == target):
        counter += 1
    return counter, value


while (value < target):
    while (value < target):
        while (value < target):
            while (value < target):
                while (value < target):
                    while (value < target):
                        while (value < target):
                            while (value < target):
                                a += 1
                                counter, value = update(counter, value)
                            a = 0
                            b += 1
                            counter, value = update(counter, value)
                        b = 0
                        c += 1
                        counter, value = update(counter, value)
                    c = 0
                    d += 1
                    counter, value = update(counter, value)
                d = 0
                e += 1
                counter, value = update(counter, value)
            e = 0
            f += 1
            counter, value = update(counter, value)
        f = 0
        g += 1
        counter, value = update(counter, value)
    g = 0
    h += 1
    counter, value = update(counter, value)

print(counter)
