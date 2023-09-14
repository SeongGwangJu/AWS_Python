import pandas as pd
import numpy as np
# numpy는 수치를 다루기에 용이하게 리스트 형식으로 나열
# pandas는 넘파이, 리스트 등을 보기 좋게 보여줌

##########################[Series]##########################
#일반 Array와 Numpy의 차이
a = pd.Series({"a":1, "b":2, "c":3})
print("a")
print(a)
print("a.index")
print(a.index) #int64

# numpy는 숫자가 아니면 모든 요소를 object 형태로 선언
a = np.arange(1,5)
# pandas는 인덱스가 0부터 시작
b = pd.Series(a)
print("b")
print(b)
print("b.index")
print(b.index)
print("b.index.values")
print(b.index.values)

##########################[DataFrame]##########################
print("\n##########################[DataFrame]##########################\n")
a = {"a": [1,2,3],
    "b":[4,5,6],
    "c":[7,8,9]}
b = pd.Series(a) # series는 컬럼? 이 없음
c = pd.DataFrame(a)
d = pd.DataFrame(a, index=["a", "b", "c"])

print("pd.Series(a)")
print(b) # key-value 형태

print("pd.DataFrame(a)")
print(c) #행렬형태 : 2차원 배열과 유사

print("c.index.values")
print(c.index.values)
print("c.columns")

print(c.columns)
print(("pd.DataFrame(a, index=[a, b, c])"))

print(d)

a = pd.DataFrame({"a":(1,2,3), "b":1, "c":3})
print("a(value changed)")
print(a)

a.index=["x", "y", "z"]
a.columns=["i", "j", "k"]
print("a(index & value change)")
print(a)

# loc = location
# iloc = index_location : 인덱스를 가지고 위치차직
print("a.loc[]")
print(a.loc["x"])
print("a.iloc[0]")
print(a.iloc[0])

n = a.__dataframe__().dataFrame