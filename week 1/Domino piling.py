import math
m,n = map(int, input().split())
board_area = m*n
domino_area = 2

dominos = m*n/domino_area
dominos = math.floor(dominos)
print(dominos)