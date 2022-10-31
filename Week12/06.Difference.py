'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    n_len = int(input())
    m_len = int(input())
    set_a, set_b, result = set({}), set({}), set({})
    for _ in range(n_len):
        set_a.add(int(input()))
    for _ in range(m_len):
        set_b.add(int(input()))

    for i in set_a:
        if i not in set_b:
            result.add(i)
    result = sorted(result)
    print(*result)


better_call_saul()
