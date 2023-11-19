
import numpy
import math
from numpy import matrix
from numpy import linalg
import numpy as np
import random


def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p

  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def dot_mod(A,B, dmod):
  Mul_max = A.dot(B)

  n = len(Mul_max)
  for i in range(n):
    for j in range(n):
      Mul_max[i][j] = Mul_max[i][j] % dmod

  return Mul_max



def Hash_1(M, iD, P,Imod):
  print("############################################")
  print("Generate Hash 1")
  a = random.randint(0,Imod)
  b = random.randint(0,Imod)
  c = random.randint(0,Imod)
  d = random.randint(0,Imod)
  R = [[a,b],[c,d]]
  R = np.array(R)
  H1 = iD + dot_mod(P,M,Imod)
  hash1 = [dot_mod(R,P,Imod), dot_mod(R,H1,Imod)]
  for i in hash1:
    print(i)
  return hash1

def Hash_23(M1,M2,IP,D,Imod):
  print("############################################")
  print("Generate Hash 2 and Hash 3")
  V1 = IP + dot_mod(M1,D)
  V2 = IP + dot_mod(M2,D)
  a = random.randint(0,Imod)
  b = random.randint(0,Imod)
  c = random.randint(0,Imod)
  d = random.randint(0,Imod)
  Rt = [[a,b],[c, d]]
  Rt = np.array(Rt)
  print("Hash2 : ")
  hash2 = [dot_mod(D,Rt,Imod), dot_mod(V1,Rt,Imod)]
  hash3 = [dot_mod(D,Rt,Imod), dot_mod(V2,Rt,Imod)]
  for i in hash2:
    print(i)
  print("Hash 3 : ")
  for i in hash3:
    print(i)
  return hash2, hash3

"""1. ORE_KEYGEN"""

def key_gen():
  print("############################################")
  input_mod = int(input("Input for mod : "))
  while True:
    try:
      a = random.randint(0,input_mod)
      b = random.randint(0,input_mod)
      c = random.randint(0,input_mod)
      d = random.randint(0,input_mod)
      p = [[a,b],[c,d]]
      P = np.array(p)
      inv_P = modMatInv(P, input_mod)
      a = random.randint(0,input_mod)
      b = random.randint(0,input_mod)
      c = random.randint(0,input_mod)
      d = random.randint(0,input_mod)
      D = [[a,b],[c,d]]
      D = np.array(D)
      inv_D = modMatInv(D,mod)
      break
    except:
      continue

  print("Key Generation")
  print("Key P \n" ,P)
  print("Key inv_P \n",inv_P)
  print("Key D \n",D)
  print("Key inv_D \n",inv_D)
  return P, inv_P, D, inv_D, input_mod

def convert_message():
  print("############################################")
  inp_num = int(input("input message : "))
  inp_num = format(inp_num, 'b').zfill(4)
  print(inp_num)
  a = int(inp_num[0])
  b = int(inp_num[1])
  c = int(inp_num[2])
  d = int(inp_num[3])

  print("Convert to binary number : ",a,b,c,d)
  bin_message = [[a,b],[c,d]]
  Mes = np.array(bin_message)
  return Mes

def convert_token():
  print("############################################")
  inp_num = int(input("input token : "))
  store_num = inp_num
  num1 = inp_num + 1
  inp_num = format(num1, 'b').zfill(4)
  print(inp_num)
  a = int(inp_num[0])
  b = int(inp_num[1])
  c = int(inp_num[2])
  d = int(inp_num[3])
  print("Convert to binary number : ",a,b,c,d)
  bin_message = [[a,b],[c,d]]
  tok1 = np.array(bin_message)
  print(tok1)
  num2 = store_num - 1
  inp_num = format(num2, 'b').zfill(4)
  a = int(inp_num[0])
  b = int(inp_num[1])
  c = int(inp_num[2])
  d = int(inp_num[3])
  print("Convert to binary number : ",a,b,c,d)
  bin_message = [[a,b],[c,d]]
  tok2 = np.array(bin_message)
  print(tok2)


  return tok1, tok2

def ore_test():
  print("############################################")
  print("Test")
  case1 = dot_mod(H1[0],H2[1])
  case2 = dot_mod(H1[1],H2[0])
  case3 = dot_mod(H1[0],H3[1])
  case4 = dot_mod(H1[1],H3[0])
  big = 0
  small = 0

  for i in range(2):
    for j in range(2):
      if(case1[i][j] == case2[i][j]):
        big += 1
  for i in range(2):
    for j in range(2):
      if(case3[i][j] == case4[i][j]):
        small += 1
  if(big == 4):
    print("Message > Query")
  elif(small == 4):
    print("Message < Query")
  else:
    print("Message == Equal")








