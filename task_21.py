def max_correct_braces(s): # ejudge: https://codeforces.com/problemset/problem/5/C
    nest = 0
    best = 0 
    best_cnt = 0 
    start_at = 0

    def stop():
        global nest, best, best_cnt, start_at

    for i, c in enumerate(s):
        if c == ')':
            nest -= 1
            if i == len(s)-1 and nest >= 0:
                print(nest)
                start_at += nest
                nest = 0
                i = len(s)-1
            if nest == 0: 
                curr = i-start_at+1
                if curr == best: 
                    best_cnt += 1
                elif curr > best:
                    best = max(best, curr)
                    best_cnt = 1
            if nest < 0:
                nest = 0
                start_at = i+1
        else:
            nest += 1

    if not best:
        best_cnt = 1

    return best, best_cnt 

s = input()
print(*max_correct_braces(s))
        
