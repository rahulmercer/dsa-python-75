def maxPieces(n, a, b, c, memo=None):
    if memo is None:
        memo = {}
    
    if n == 0:
        return 0
    
    if n < 0:
        return -1
    
    if n in memo:
        return memo[n]
    
    res_a = maxPieces(n - a, a, b, c, memo)
    res_b = maxPieces(n - b, a, b, c, memo)
    res_c = maxPieces(n - c, a, b, c, memo)
    
    max_pieces = max(res_a, res_b, res_c)
    if max_pieces == -1:
        memo[n] = -1
    else:
        memo[n] = max_pieces + 1
    
    return memo[n]

n = 7
a = 5
b = 2
c = 3
print("Maximum pieces:", maxPieces(n, a, b, c))
