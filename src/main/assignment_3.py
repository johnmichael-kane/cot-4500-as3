import numpy as np


#function t-y^2
#range 0<t<2 ----- a<t<b
#iterations: 10  ----- N
# initial point: f(0)=1 ------- f(a)=y_0
#dy/dt=y-t^2
def euler_method(N, a, b, w):
  h = (b - a) / N
  #w starts as w_0, and it'll change as we calculate through the iterations
  #Taylor's theorem:
  for i in range(N):
    t = a + i * h
    w = w + h * (w - (t)**2)

    #w1=w0+h(w0+(t0)^2)
    #print("i: " + str(i) + "\tti: " + str(t))
    #print("w" + str(i+1) + ": " + str(w))

  return w


def runge_kutta(N, a, b, w):
  x = 1

def guassian_elim(M, solutions):
  # Step 1: Form the augmented matrix
  n = len(M)
  for i in range(n):
    M[i].append(solutions[i])
  # Step 2: Apply Gaussian Elimination to form upper triangular matrix
  for i in range(n):
    # Search for maximum in this column
    max_el = abs(M[i][i])
    max_row = i
    for k in range(i+1, n):
      if abs(M[k][i]) > max_el:
        max_el = abs(M[k][i])
        max_row = k
    # Swap maximum row with current row (column by column)
    for k in range(i, n+1):
      tmp = M[max_row][k]
      M[max_row][k] = M[i][k]
      M[i][k] = tmp
      # Make all rows below this one 0 in current column
    for k in range(i+1, n):
      c = -M[k][i] / M[i][i]
      for j in range(i, n+1):
        if i == j:
          M[k][j] = 0
        else:
          M[k][j] += c * M[i][j]

    # Step 3: Perform backward substitution
  x = [0 for i in range(n)]
  for i in range(n-1, -1, -1):
    x[i] = M[i][n] / M[i][i]
    for k in range(i-1, -1, -1):
      M[k][n] -= M[k][i] * x[i]

  return x


#Problem 4, the factorization part
def LUFactorization(M):
  n = len(M)
  L = np.zeros((n, n))
  U = np.zeros((n, n))

  for i in range(n):
    #upper triangular
    for k in range(i, n):
      #Summation of L(i,j) * U(j,k)
      sum = 0
      for j in range(i):
        sum += (L[i][j] * U[j][k])

      U[i][k] = M[i][k] - sum

    #lower triangular
    for k in range(i, n):
      if (i == k):
        L[i][i] = 1
      else:
        sum = 0
        for j in range(i):
          sum += (L[k][j] * U[j][i])

        L[k][i] = (M[k][i] - sum) / U[i][i]

  return L, U


def matrix_determinant(U):
  return U


def diagonal_dominate(M):
  M = np.array(M)
  for i in range(len(M)):
    diag_element = abs(M[i, i])
    off_diag_sum = sum(abs(M[i])) - diag_element

    if diag_element <= off_diag_sum:
      return False

  return True


def positive_def(M):
  M = np.array(M)
  eigenvalues = np.linalg.eigvals(M)
  return np.all(eigenvalues > 0)


def main():
  #Problem 1
  a = 0
  b = 2
  iterations = 10
  w = 1
  print(euler_method(iterations, a, b, w))
  print()
  #expected output: 1.2446380979332121

  #Problem 2
  #runge_kutta(iterations, a, b, w)
  #expected output: 1.251316587879806

  #Problem 3
  #use guassian elimination/backwards subst.
  #to solve the linear system in aug. matrix
  variables = [[2, -1, 1],
               [1, 3, 1],
               [-1, 5, 4]]
  solutions = [6, 0, -3]

  elimination = guassian_elim(variables, solutions)
  elimination = [int(num) for num in elimination]
  print(elimination)
  #expected output [2 -1 1]

  #Problem 4
  matrix4 = [[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]]

  L, U = LUFactorization(matrix4)  #LU Factorization on the matrix
  #print(matrix_determinant(U)) create this function!!!
  print()
  print(L)  #L Matrix
  print()
  print(U)  #U matrix
  print()

  #determinant: 38.99999999999999
  #L Matrix
  #[[1. 0. 0. 0.]
  #[2. 1. 0. 0.]
  #[3. 4. 1. 0.]
  #[-1. -3. 0. 1.]]
  #U Matrix
  #[[1. 1. 0. 3.]
  #[0. -1. -1. -5.]
  #[0. 0. 3. 13.]
  #[0. 0. 0. -13]]

  #Problem 5
  matrix5 = [[9, 0, 5, 2, 1], [3, 9, 1, 2, 1], [0, 1, 7, 2, 3],
             [4, 2, 3, 12, 2], [3, 2, 4, 0, 8]]
  print(diagonal_dominate(matrix5))
  print()
  #expected outcome False

  #Problem 6
  matrix6 = [[2, 2, 1], [2, 3, 0], [1, 0, 2]]

  print(positive_def(matrix6))
  #expected outcome True


if __name__ == "__main__":
  main()
