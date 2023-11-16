# ---encoding:utf-8---
# @Time    : 2023/8/1 21:29
# @Author  : caishengxiang
# @Email   : 383301857@qq.com
# @File    : echarts_draw.py
# @Project : caishengxiang
try:
    from pyecharts.charts import Line
    from pyecharts import options as opts
except:
    raise Exception('you need: pip install pyecharts')


class Draw:
    def __init__(self, y_name, x_name, title='draw', save_path='./draw.html'):
        self.y_name = y_name
        self.x_name = x_name
        self.title = title
        self.save_path = save_path
        self.x_datas = []
        self.y_datas = []

    def add_data(self, x_data, y_data):
        # 添加 x 轴数据

        self.x_datas.append(x_data)

        # 添加 y 轴数据
        self.y_datas.append(y_data)

    def draw(self):
        line_chart = Line()
        line_chart.add_xaxis(self.x_datas)
        line_chart.add_yaxis(self.y_name, self.y_datas)

        # 设置图表标题和 x 轴、y 轴标签
        line_chart.set_global_opts(title_opts=opts.TitleOpts(title=self.title),
                                   xaxis_opts=opts.AxisOpts(name=self.x_name),
                                   yaxis_opts=opts.AxisOpts(name=self.y_name))
        return line_chart

    def save(self):
        line_chart = self.draw()
        # 将图表保存为 HTML 格式的文件
        line_chart.render(self.save_path)


if __name__ == '__main__':
    from pyecharts.charts import Grid,Page

    grid = Grid()
    d = Draw(y_name='1使用率%', x_name='时间', title='{}: cpu监控'.format('localhost'),
             save_path='./cpu.html')
    d.add_data(1, 2)
    d.add_data(2, 2)
    d.add_data(3, 2)
    d.add_data(3, 2)
    d.add_data(3, 2)
    d.add_data(3, 2)

    d2 = Draw(y_name='2使用率%', x_name='时间', title='{}: cpu监控'.format('localhost'),
             save_path='./cpu.html')
    d2.add_data(1, 2)
    d2.add_data(2, 2)
    d2.add_data(2, 2)
    d2.add_data(2, 2)
    d2.add_data(4, 2)

    d3 = Draw(y_name='3使用率%', x_name='时间', title='{}: cpu监控'.format('localhost'),
             save_path='./cpu.html')
    d3.add_data(1, 2)
    d3.add_data(2, 2)
    d3.add_data(2, 2)
    d3.add_data(2, 2)
    d3.add_data(2, 2)
    d3.add_data(4, 2)

    page=Page()
    page.add(d.draw())
    page.add(d2.draw())
    page.add(d3.draw())
    page.render('./cpu.html')
    # grid_chart = Grid()
    # grid_chart.add(d.draw(), grid_opts=opts.GridOpts(pos_top="0%", pos_bottom='70%'))
    # grid_chart.add(d2.draw(), grid_opts=opts.GridOpts(pos_top="30%", pos_bottom='40%'))
    # grid_chart.add(d3.draw(), grid_opts=opts.GridOpts(pos_top="60%"))
    # grid_chart.render('./cpu.html')
    # d.save()
