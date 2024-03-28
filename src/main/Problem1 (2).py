import numpy as np

#given, the values of x and y in the table and the value inside of f(), represented as target
x = np.array([ 3.6, 3.8, 3.9])
y = np.array([1.675, 1.436, 1.318])
target = 3.7

def neville(x, y, target):
  n = len(x)
  p = np.zeros((n, n))
  
  for i in range(n):
    p[i][0] = y[i]
    
  for j in range(1, n):
    for i in range(n-j):
      p[i][j] = ((target - x[i+j])*p[i][j-1] + 
        (x[i] - target)*p[i+1][j-1]) / (x[i] - x[i+j])
  
  return p[0][-1]

def main():
  result=neville(x,y,target)
  print(result)

if __name__ == "__main__":
  main()