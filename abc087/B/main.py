#!/usr/bin/env python3

# う，全探索か……．50^3 なるほど．再帰でも解けると思うんだけどこれは python 力不足．あとでリセットしてやり直そう．

import sys

def solve(A: int, B: int, C: int, X: int):
    C500_max, mod = divmod(X, 500)
    C100_max, mod = divmod(X, 100)
    _C50_max, mod = divmod(X, 50)
#    print("A B C X / C500_max C100_max mod", A, B, C, X, "/", C500_max, C100_max, mod)
    counter = 0
    if A != 0:
        for i in range(0, min(C500_max, A) + 1):
            counter = counter + solve(0, B, C, X - i * 500)
    elif B != 0:
        if X <= 100 * B:
            for i in range(0, min(C100_max, B) + 1):
                counter = counter + solve(0, 0, C, X - i *100)
    else:
        if mod == 0 and X <= 50 * C:
            counter = counter + 1
    return counter
# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int

    print(solve(A, B, C, X))

if __name__ == '__main__':
    main()
