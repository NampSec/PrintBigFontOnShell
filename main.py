# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#尝试使用bityarry数据结构
from fontTools.ttLib import TTFont
#X轴应该是0-1000，y轴应该是-500-1000
CHART_XMAX = 100
CHART_XMIN = 0
CHART_YMAX = 100
CHART_YMIN = 0

n = CHART_XMAX - CHART_XMIN
m = CHART_YMAX - CHART_YMIN
oldpoint = None

mychart = [[0 for i in range(n)] for j in range(m)]

def PointCoordinateConvert(coordinate):
    return tuple((round(coordinate[0]*(CHART_XMAX - CHART_XMIN)/1000),round((coordinate[1] + 500)*(CHART_YMAX - CHART_YMIN)/1500)))


def PortrayChart(data):
    n = 0
    num = len(data)
    global oldpoint
    if oldpoint is not None:

        for midstpoint in ConnectLineGernerate(oldpoint, PointCoordinateConvert(data[0])):
            print("x: " + str(midstpoint[0]) + " y:" + str(round(midstpoint[1])))
            mychart[round(midstpoint[1])][midstpoint[0]] = 1

    while(n < num):
        point = PointCoordinateConvert(data[n])
        print("convert point:")
        print("x: " + str(point[0]) + " y:" + str(point[1]))
        n += 1
        #为什么前面是列数后面是序数
        mychart[point[1]][point[0]] = 1
    oldpoint = point

def PrintFront(character):
    unicode = uniMap[int(ord(character))]
    point_data = font['glyf'][unicode].coordinates
    print(point_data)
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
#                print(f'{x},{y}')
                print('#',end='')
            else:
                print(' ',end='')
            x += 1

        y += 1
        print('')

class ConnectLineGernerate():
    def __init__(self,startpoint,endpoint):
        self.point_base = startpoint
        self.point_end = endpoint
        self.point = list(startpoint)
        self.tan = (endpoint[1] - startpoint[1])/(endpoint[0] - startpoint[0])
        self.flag = 1
        if startpoint[0] > endpoint[0]:
            self.flag = -1
    def __iter__(self):
        return self
    def __next__(self):
        if abs(self.point[0] - self.point_end[0]) > 1 :
            self.point[0] += self.flag
            self.point[1] += self.tan
            return tuple(self.point)

        raise StopIteration



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
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


