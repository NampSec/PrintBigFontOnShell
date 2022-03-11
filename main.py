# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#尝试使用bityarry数据结构
from fontTools.ttLib import TTFont
CHART_XMAX = 100
CHART_XMIN = 0
CHART_YMAX = 100
CHART_YMIN = -50

n = CHART_XMAX - CHART_XMIN
m = CHART_YMAX - CHART_YMIN
mychart = [[0 for i in range(n)] for j in range(m)]

# mychart = [[0 for i in range(CHART_XMAX - CHART_XMIN)] for j in range(CHART_YMAX - CHART_YMIN)]
# mychart = [[0] * (CHART_XMAX - CHART_XMIN)] * (CHART_YMAX - CHART_YMIN)

def PointCoordinateConvert(coordinate):
    return tuple((int(coordinate[0]*10/(CHART_XMAX - CHART_XMIN)),int((coordinate[1] - CHART_YMIN)*10/(CHART_XMAX - CHART_XMIN))))


def PortrayChart(data):
    n = 0
    jj = 0
    num = len(data)
    print("data:")
    print(data)
    print("num:")
    print(len(data))
    while(n < num):
        point = PointCoordinateConvert(data[n])
        print("convert point:")
        print("x: " + str(point[0]) + " y:" + str(point[1]))
        n += 1
        mychart[point[0]][point[1]] = 1
        print('第' + str(jj) + '个')
        jj = jj + 1



def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
def PrintFront(character):
    unicode = uniMap[int(ord(character))]
    point_data = font['glyf'][unicode].coordinates
    #每个笔画的点
    PortrayChart(point_data[0:font['glyf'][unicode].endPtsOfContours[0] + 1])
    i = 0
    while(i+1 < font['glyf'][unicode].numberOfContours):
        counter_start = font['glyf'][unicode].endPtsOfContours[i] + 1
        counter_end =font['glyf'][unicode].endPtsOfContours[i+1] + 1
        PortrayChart(point_data[counter_start:counter_end])
        i = i+1


    #笔画数
    # print(str(font['glyf'][unicode].numberOfContours))
    # print("Xmin:" + font['glyf'][unicode].xMin + "Ymin:" + font['glyf'][unicode].yMin +"Xmax:" +font['glyf'][unicode].xMax + "Ymax:" +font['glyf'][unicode].yMax)




def PrintPoint(mychart):
    x = 0
    y = 0
    while(y < len(mychart)):
        x = 0
        while(x < len(mychart[0])):
            if(mychart[y][x] != 0):
                print('#',end='')
            else:
                print(' ',end='')
            x += 1

        y += 1
        print('')




# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    font = TTFont("default.ttf")
    # 输出的uniMap是一个字典，key代表的unicode的int值，value代表unicode的名字
    uniMap = font['cmap'].tables[0].ttFont.getBestCmap()
    # print(uniMap[20320])
    PrintFront("你")
    PrintPoint(mychart)
    print(mychart)

    # with open("./text.txt") as file_obj:
    #     content = file_obj.readline()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


