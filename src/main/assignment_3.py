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

def range_kutta(N, a, b, w):
   x=1

def gaussian_elim(A, b):
   print(b)

def matrix_determinant(M):
    print(M)

def LMatrix(M):
   print(M)

def UMatrix(M):
   print(M)

def diagonal_dominate(M):
   print(M)

def positive_def(M):
   print(M)

def main():
    #Problem 1
    print(euler_method(10, 0, 2, 1))
    #expected output: 1.2446380979332121

    #Problem 2
    #range_kutta(10, 0, 2, 1)
    #expected output: 1.251316587879806

    #Problem 3
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
    matrix_determinant(matrix4)
    #expected output 38.99999999999999
    LMatrix(matrix4)
    #[[1. 0. 0. 0.]
    #[2. 1. 0. 0.]
    #[3. 4. 1. 0.]
    #[-1. -3. 0. 1.]]
    UMatrix(matrix4)
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