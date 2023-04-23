answerSet = set()

siz = 9999
for a in range(siz):
    a_str = str(a)
    aSet = set(a_str)
    if ('0' not in aSet and len(a_str) == len(aSet)):
        for b in range(siz):
            b_str = str(b)
            bSet = set(b_str)
            if ('0' not in bSet and len(b_str) == len(bSet)):
                if (set(aSet).isdisjoint(bSet)):
                    ab_str = str(a*b)
                    abSet = set(ab_str)
                    if ('0' not in abSet and len(abSet) == len(ab_str) and set(abSet).isdisjoint(aSet) and set(abSet).isdisjoint(bSet)):
                        if (len(a_str)+len(b_str)+len(ab_str) == 9):
                            if a*b not in answerSet:
                                answerSet.add(a*b)
                                print(a, b, a*b)


print(sum(answerSet))
