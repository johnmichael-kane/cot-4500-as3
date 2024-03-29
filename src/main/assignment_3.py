import numpy as np
#function t-y^2
#range 0<t<2 ----- a<t<b
#iterations: 10  ----- N
# initial point: f(0)=1 ------- f(a)=y_0
#dy/dt=y-t^2
def euler_method(N, a, b, w):
    h=(b-a)/N
    #w starts as w_0, and it'll change as we calculate through the iterations
    #Taylor's theorem:
    for i in range(N):
      t=a+i*h
      w=w+h*(w-(t)**2)

      #w1=w0+h(w0+(t0)^2)
      #print("i: " + str(i) + "\tti: " + str(t))
      #print("w" + str(i+1) + ": " + str(w))

    return w

def runge_kutta(N, a, b, w):
   x=1

def gaussian_elim(A, b):
   print(b)

#Problem 4, the factorization part
def LUFactorization(M):
   n=len(M)
   L=np.zeros((n,n))
   U=np.zeros((n,n))
   
   for i in range(n):
      #upper triangular
      for k in range(i,n):
         #Summation of L(i,j) * U(j,k)
         sum=0
         for j in range(i):
            sum += (L[i][j] * U[j][k])
         
         U[i][k] = M[i][k] - sum
   
      #lower triangular
      for k in range(i,n):
         if (i==k):
            L[i][i]=1
         else:
            sum=0
            for j in range(i):
               sum += (L[k][j] * U[j][i])

            L[k][i] = (M[k][i] - sum)/ U[i][i]

   return L,U

def matrix_determinant(U):
   return U

def diagonal_dominate(M):
   print(M)

def positive_def(M):
   print(M)

def main():
    #Problem 1
    #function: t-y^2, range 0<t<2, 
    #iterations:10, initial point: f(0)=1
    #Solve using euler's method
    print(euler_method(10, 0, 2, 1))
    #expected output: 1.2446380979332121

    #Problem 2
    #function: t-y^2, range 0<t<2, 
    #iterations:10, initial point: f(0)=1
    #Solve using runge_kutta
    #runge_kutta(10, 0, 2, 1)
    #expected output: 1.251316587879806

    #Problem 3
    #use guassian elimination/backwards subst.
    #to solve the linear system in aug. matrix
    variables=[[2, -1, 1],
               [1, 3, 1],
               [-1, 5, 4]]
    solutions=[6, 0, 3]
    gaussian_elim(variables, solutions)
    #expected output [2 -1 1]

    #Problem 4
    matrix4=[[1, 1, 0, 3],
             [2, 1, -1, 1],
             [3, -1, -1, 2],
             [-1, 2, 3, -1]]
    
    L,U=LUFactorization(matrix4) #LU Factorization on the matrix
    #print(matrix_determinant(U)) create this function!!!
    print(L) #L Matrix
    print(U) #U matrix

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
    matrix5=[[9, 0, 5, 2, 1],
             [3, 9, 1, 2, 1],
             [0, 1, 7, 2, 3],
             [4, 2, 3, 12, 2],
             [3, 2, 4, 0, 8]]
    #diagonal_dominate(matrix5)
    #expected outcome False

    #Problem 6
    matrix6=[[2, 2, 1],
             [2, 3, 0],
             [1, 0, 2]]
    
    #positive_def(matrix6)
    #expected outcome True

if __name__ == "__main__":
  main()