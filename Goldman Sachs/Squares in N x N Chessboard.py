def countSquares(n):
    return (n*(n+1)*(2*n+1)/6)   # Sum of N^2 = n*(n+1)*(2n+1)/6

# Driver code
n = 8
print("Count of squares is ",
      countSquares(n))