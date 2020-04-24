import numpy as np

# Maps
colors = [['R', 'G'],
          ['R', 'R'],
          ['G', 'R'],
          ['R', 'G'],
          ['G', 'G']]

# Measurements
Measurement = ['R']

# motions
Motion = [1,0]

#Probablity of recognition
pHit    = 0.8
pMiss   = 0.2

#Probability of movement
pExact  = 0.6
pFront  = 0.1
pBack   = 0.1
pLeft   = 0.1
pRight  = 0.1

# Initialization of Hyperparameters
pinit = 1.0 / (float(len(colors)) * float(len(colors[0])))
p = np.zeros((5,2))
for i in range(len(colors)):
    for j in range(len(colors[0])):
        p[i][j] = pinit

# p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

# X-Maps，y-measurement
def sense(X, y): 
    q = np.zeros((5,2))
    for i in range(len(X)):
        for j in range(len(X[0])):
            hit = y[0] == X[i][j]
            q[i][j] = p[i][j] * (hit * pHit + (1-hit) * pMiss)
    s = np.sum(q)
    q[i][j] = q[i][j] / s

    return q

#
def move(X, Z):
    q = np.zeros((5,2))
    k1 = len(X)
    k2 = len(X[0])
    for i in range(len(X)):
        for j in range(len(X[0])):
            s =  X[(i+k1-Z[0]) % k1][(j+k2-Z[1]) % k2] * pExact
            s = s + X[(i+k1-Z[0]+1) % k1][(j+k2-Z[1]) % k2] * pFront
            s = s + X[(i+k1-Z[0]-1) % k1][(j+k2-Z[1]) % k2] * pBack
            s = s + X[(i+k1-Z[0]) % k1][(j+k2-Z[1]+1) % k2] * pRight
            s = s + X[(i+k1-Z[0]) % k1][(j+k2-Z[1]-1) % k2] * pLeft

            q[i][j] = s
    return q

def main():
    p = sense(colors,Measurement)
    q = move(p, Motion)
    print(q)

if __name__ == '__main__':
    print( main())
    


