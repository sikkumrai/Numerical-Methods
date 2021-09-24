import numpy as n
import matplotlib.pyplot as plt
a=1.0
l1=0
l2=1
Nx=100
Nt=100000
tFin=1
def f(x,t):
    return 0.0
def s(x):
    return n.sin(n.sin(n.pi*x)+0.1*n.sin(100*n.pi*x))
def leftbound(t):
    return 0
def rightbound(t):
    return 0

x=n.linspace(l1,l2, Nx+1)
dx= x[1]-x[0]
t= n.linspace(0,tFin,Nt+1)
dt=t[1]-t[0]
f=a*dt/dx**2
T=n.zeros(Nx+1)
t_old=n.zeros(Nx+1)
print(x)
print(f)
for i in range (0, Nx+1):
    t_old[i]= s(x[i])
A=n.zeros((Nx+1,Nx+1))
rhs=n.zeros(Nx+1)
for N in range (Nt):

    if N%1000==0:
        plt.plot(x,t_old)
        plt.axis([0,1,0,1])
    for i in range(Nx):
        rhs[i]=t_old[i]
        A[i][i]=1+2*f
        if i>0:
            A[i][i-1]=-f
            
        if i<Nx:
            A[i][i+1]=-f
            
    A[0,:]=0;   A[Nx,:]=0
    A[0,0]=1;   A[Nx,Nx]=1
    rhs[0]=0;   rhs[0]=0
    T[:]=n.linalg.solve(A,rhs)
    t_old=T
    plt.show ()