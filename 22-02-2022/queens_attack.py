def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    moves = {'n': n - r_q, 'nw': min(n - r_q, c_q-1), 'ne': min(n - r_q, n - c_q),
            's': r_q-1, 'sw': min(r_q-1, c_q-1), 'se': min(r_q-1, n - c_q), 'w': c_q-1, 'e': n - c_q}
    for _ in range(k):
        r, c = map(int, input().split())
        if c == c_q:
            if r > r_q:
                moves['n'] = min(r-r_q-1, moves['n'])
            else:
                moves['s'] = min(r_q-r-1, moves['s'])
        elif r == r_q:
            if c > c_q:
                moves['e'] = min(c-c_q-1, moves['e'])
            else:
                moves['w'] = min(c_q-c-1, moves['w'])
        elif c - r == c_q - r_q:
            if c < c_q and r < r_q:
                moves['sw'] = min(min(c_q-c-1, r_q-r-1), moves['sw'])
            elif c > c_q and r > r_q:
                moves['ne'] = min(min(c-c_q-1, r-r_q-1), moves['ne'])
        elif c + r == c_q + r_q:
            if c < c_q and r > r_q:
                moves['nw'] = min(min(r-r_q-1, c_q-c-1), moves['nw'])
            elif c > c_q and r < r_q:
                moves['se'] = min(min(r_q-r-1, c-c_q-1), moves['se'])
queensAttack(4,)
