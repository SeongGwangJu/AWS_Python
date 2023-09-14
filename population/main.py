import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("202108_202308_주민등록인구및세대현황_월간.csv", encoding="cp949")
print("##### data.columns #####")
print(data.columns)
print("##### data.index #####")
print(data.index)
print("##### data #####")
print(data)

# 행정구역별 월간 거주자 인구
print("##### 월별 행정구역당 거주자 인구 #####")
print("# data.iloc[1,0] :2행 1열 ")
print(data.iloc[1,0])
print("# data.iloc[1, range(1, len(data.columns), 6)")
print(data.iloc[1, range(1, len(data.columns), 6)])
# 데이터를 보면, 총 인구수는 6행마다 월간 총 인구수를 보여줌


#가야제1동 세대당 인구

# print(f"""
#     {data.query('행정구역.str.contains("가야제1동")')}
# """)
# contains(찾을내용) : 해당 지역 검색을 해줌. 출력 내용을 보면, 인덱스는 [0]을 참조해야함
rowindex = data.query('행정구역.str.contains("가야제1동")').index.values[0];

print("##### 월간 세대당 인구수 #####")
print("data.iloc[14,0] : 15행 1열")
print(data.iloc[14,0])
#iloc함수 : ( (n-1)번째열, (n-1)번째행 )
#range함수 : ( start, stop, step )
print(data.iloc[rowindex, range(3, len(data.columns), 6)])

