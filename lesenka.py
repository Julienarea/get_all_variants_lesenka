def get_all_variants_lesenka(n):
    res =[[n]]
    a = [n,0]
    while True:
        perm_stage = try_get_permutation_stage(a)
        if perm_stage == -1:
            print(f"Не найдено возможности перестановки с текущим количеством этажей: {a}")
            if a[-1] == 1:
                print(f"Конец {a}")
                break
            if a[-1] == 2:
                big_stage = try_get_big_stage(a)
                if big_stage == -1:
                    print(f"Конец {a}")
                    break
                else:
                    expand_array(a)
                    throw_top(big_stage,a)
                    res.append(a.copy()) if a.count(0) == 0 else 0
                    break

            else:
                expand_array(a)
                throw_up(len(a)-2, a)

        throw_up(perm_stage, a)
        res.append(a.copy()) if a.count(0) == 0 else 0

    return res

def try_get_big_stage(a):
    for stage in range(len(a)-1):
        if get_difference_between(stage, a) == 2:
            return stage
    else:
        print(f"Разница: {get_difference_between(stage, a)}")
        return -1


def try_get_permutation_stage(a):
    for stage in range(len(a)-1):
        if get_difference_between(stage, a) >2:
            return stage
    else:
        print(f"Разница: {get_difference_between(stage, a)}")
        return -1

def get_difference_between(index, a):
    return a[index] - a[index+1]

def expand_array(a):
    a = a.append(0)

def throw_top(index, a):
    a[index] -=1
    a[-1] +=1

def throw_up(index, a):
    a[index] -= 1
    a[index+1] +=1

print(get_all_variants_lesenka(12))
