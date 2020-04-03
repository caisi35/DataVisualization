from pyecharts import Page, Overlap, Timeline, Grid
from drawTest import histogram, LadderDiagram, PieCharts, PieRadiusChart,StackBar,StackBar2,StackBarChart,\
    StackChart, TreeChart, TreeMapChart


def page_container():
    page = Page(page_title="Page_Container")
    hot_dog = histogram.hdc_bar()
    ladder = LadderDiagram.ladder_diagram()
    pie_chart = PieCharts.pie_charts()
    pie_radius = PieRadiusChart.pie_radiud_chart()
    stack_bar = StackBar.stack_bar()
    stack_bar2 = StackBar2.stack_bar2()
    tree_map = TreeMapChart.tree_map()
    tree_chart = TreeChart.tree_chart()
    stack_bar_chart = StackBarChart.stack_bar_chart2()
    stack_line = StackChart.starck_line_chart()

    page.add(hot_dog)
    page.add(ladder)
    page.add(stack_bar2)
    page.add(stack_bar)
    page.add(stack_bar_chart)
    page.add(stack_line)
    page.add(pie_chart)
    page.add(pie_radius)
    page.add(tree_chart)
    page.add(tree_map)
    return page


def overlap_container():
    overlap = Overlap(page_title="Overlap Container")

    stack_bar, line = StackBar.stack_bar()

    overlap.add(stack_bar)
    overlap.add(line)
    return overlap


def time_line():
    timeline = Timeline(page_title="Time Line")
    stack_bar, line = StackBar.stack_bar()
    tree_chart = TreeChart.tree_chart()
    stack_bar_chart = StackBarChart.stack_bar_chart2()
    stack_line = StackChart.starck_line_chart()

    timeline.add(stack_line, time_point=7)
    timeline.add(stack_bar_chart, time_point=8)
    timeline.add(tree_chart, time_point=6)
    timeline.add(stack_bar,time_point=2)
    timeline.add(line, time_point=3)
    timeline.render("timeline.html")


def grid():
    page = Grid(page_title="Grid Container", width=1600, height=900)

    hot_dog = histogram.hdc_bar()
    ladder = LadderDiagram.ladder_diagram()
    stack_bar, line = StackBar.stack_bar()
    stack_line = StackChart.starck_line_chart()

    page.add(hot_dog, grid_width=600, grid_height=300, grid_left=50, grid_top=50)
    page.add(ladder, grid_width=600, grid_height=300, grid_left=800, grid_top=50)
    page.add(stack_bar, grid_width=600, grid_height=300, grid_left=800, grid_top=450)
    page.add(stack_line,  grid_width=600, grid_height=300, grid_left=50, grid_top=450)

    page.render("grid.html")


if __name__ == '__main__':
    # page = page_container()
    # page.render("Page_container.html")
    # overlap = overlap_container()
    # overlap.render("overlap_container.html")
    # time_line()
    grid()