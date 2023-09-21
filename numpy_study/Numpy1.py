# 넘파이(Numpy)
# 고성능(대량) 수치계산
#벡터, 행렬 연산

numArray1 = [1,2,3,4,5]
numArray2 = [6,7,8,9,10]

#두 배열을 합치려면? for문을 써야함.
numArray3 = []
for i in range(len(numArray1)):
    numArray3.append(numArray1[i] + numArray2[i])

print(numArray3)

#Numpy로 하면?
import numpy as np

npArray1 = np.array(numArray1)
npArray2 = np.array(numArray2)
npArray3 = npArray1 + npArray2

print(npArray3)

npDoubleArray1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
npDoubleArray2 = np.array([[11,12,13,14,15], [16,17,18,19,100]])
print("npDoubleArray")
print(npDoubleArray1)
print("npDoubleArray2")
print(npDoubleArray2)
print("npDoubleArray + npDoubleArray2")
print(npDoubleArray1 + npDoubleArray2)

#shape : 행렬의 크기를 알려줌 n행m열
print("npArray1.shape")
print("npDoubleArray1.shape")
print(npDoubleArray1.shape)

npArray4 = np.arange(1, 11)
print("npArray4 : np.arange(1,11)")
print(npArray4)
npArray5 = np.zeros(10)
print("npArray5 : np.zeros(10)")
print(npArray5)

npArray6 = np.zeros_like(npDoubleArray1)
print("npArray6 : zeros_like")
print(npArray6)
npArray7 = np.ones(10)
print("npArray7 : ones(10) ")
print(npArray7)
npArray8 = np.ones_like(npDoubleArray1)
print("npArray8 : ones_like()")
print(npArray8)
npArray9 = np.full((5,3), 5)
print("npArray9")
print(npArray9)

print(npArray9 * 2)
