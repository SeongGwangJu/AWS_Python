import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [2,3,4,5]
x2 = np.array(x)
y2 = np.array([4,1,3,6])
x3 = np.array(x)
y3 = np.array([3,5,3,10])
x4 = np.array(x)
y4 = np.array([12,10,1,15])

##일반 그래프
plt.plot(x, y)
plt.show()

##막대형그래프
plt.bar(x,y)
plt.show()

## 꺽은선 그래프
figure = plt.figure() # 그래프의 테두리(틀)
axes = figure.add_subplot(111) # 틀 안에 들어있는 그래프들.

# 그래프의 선 : 빨간색, dashed(--------), 데이터 위치에 ^로 표기
## 색상 종류 : https://matplotlib.org/examples/color/named_colors.html
## marker 종류 : https://matplotlib.org/2.0.2/examples/lines_bars_and_markers/marker_reference.html
axes.plot(x,y, color="red", linestyle="dashed", marker="^")
axes.plot(x2,y2, color="k", linestyle="dotted", marker="o")
plt.show()

# 여러개의 그래프를 한 화면에
figure = plt.figure() #위에거 초기화

axes1 = figure.add_subplot(221) # 1행 2열에서 1열 'ㅁ'ㅁ
axes1.plot(x,y)
axes1.plot(x2,y2, color="red", linestyle="dashed")

axes2 = figure.add_subplot(222) # 1행 2열에서 2열 ㅁ'ㅁ'
axes2.plot(x2,y2)

axes3 = figure.add_subplot(223) # 3번째 = 2행 1열
axes3.plot(x3,y3)

axes4 = figure.add_subplot(224)
axes4.plot(x4,y4)
plt.show()

# 막대형 + 중첩
figure = plt.figure()
axes = figure.add_subplot(111)

axes.bar(x,y)
axes.bar(x2,y2)
plt.show()

#하나의 그래프에 여러 y축: twinx (동일한 x축 or  서로 다른 범위)
figure = plt.figure()
axes1 = figure.add_subplot(111)
axes2 = axes1.twinx()
axes1.bar(x, y, color="blue", label="bar")
axes2.plot(x2, y2, color="red", label="plot")
plt.show()


from matplotlib import font_manager, rc
rc("font", family="Hancom Gothic")
#점그래프 scatter
figure = plt.figure()
axes = figure.add_subplot(111)

x = [1,2,3,4]
y = [2,4,6,8]
x2 = [1,1,3,4]
y2 = [6,2,4,6]
axes.scatter(x,y)
axes.scatter(x2,y2)
plt.title("제목")
plt.xlabel("x축 이름")
plt.ylabel("y축 이름")

plt.show()

#원형 그래프

#label의 한글 깨지는거 해결
from matplotlib import font_manager, rc

font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
for font in font_list:
    if font.find("Gothic") != -1:
        print(font)

rc("font", family="Hancom Gothic")

figure = plt.figure()
axes = figure.add_subplot(111)

label = ["a", "b", "야구", "배구"]
data = [10, 20, 5, 30]

axes.pie(data,labels=label)
# plt.show()
# plt.savefig("test")
import matplotlib.image as img
image = img.imread("test.png")
print(image)
plt.imshow(image)
