from django.shortcuts import render
from app.models import db
import datetime
from pyecharts import Map, GeoLines
from pyecharts_javascripthon.api import TRANSLATOR

# Create your views here.
REMOTE_HOST = "./static/js/map/province"
HOST = "/static/js/assets/js"


def index(request):
    if request.method == "POST":
        pass
    else:
        confirmed_count, confirmed_date = get_confirmed()
        scater_data_x, scater_data_y = get_scater_date()
        gauge_data = get_Gauge_data()
        map_option = draw_map_confirmed_count()
        line_date, line_confirmed_count_gx = get_gx_data()
        gx_city, bar_confirmed_count_gx, pie_data = get_bar_data()

        geolines = draw_geoline()
        myechart=geolines.render_embed()
        script_list=geolines.get_js_dependencies()
        host=HOST

        # js_province_list = os.listdir(REMOTE_HOST)
        return render(request, 'index.html', locals())


def draw_geoline():
    """
    绘制地理坐标系线图（GeoLines）
    :return:绘制好的GeoLines对象
    """
    sql = """select m.source_province_name, m.target_province_code, m.value, a.map_name from migrate_data_2017 m 
    left join area_china a on(m.target_province_code=a.area_code) where source_province_code=420000"""
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()
    geoline_data = []
    for s_name, t, v, name in data:
        geoline_data.append(['湖北', name, v])
    geoline = GeoLines()
    geoline.add('', geoline_data, line_curve=0.3, line_type='dashed', geo_effect_symbol='arrow', border_color='#c5f80e',
                geo_normal_color='rgba(255,255,255, .5)', is_toolbox_show=False, geo_emphasis_color='yellow')
    # geoline.render('geolines.html')
    return geoline


def get_bar_data():
    """
    从mysel数据库中获取绘制柱形图所需的数据
    因为绘制饼图需要的数据一样，封装的格式不同而已，所以一起获取也ok
    :return:
        gx_city：广西省市名称  list
        bar_confirmed_count_gx：广西累计确诊   list
        pie_data：{'value':广西累计确诊, 'name':广西省市名称}    list套字典
    """
    sql = """select sum(confirmed_count), city_name from covid_data_2017 where province_code=450000 and 
    update_time='2020-02-29' group by city_code """
    # 获取数据库的连接
    mydb = db()
    # 获取查询到的游标
    cur = mydb.get_cur(sql)
    # 获取所有数据
    data = cur.fetchall()
    bar_confirmed_count_gx = []
    gx_city = []
    pie_data = []
    for c, city in data:
        bar_confirmed_count_gx.append(int(c))
        gx_city.append(city)
        pie_data.append({'value':int(c), 'name':city})
    return gx_city, bar_confirmed_count_gx, pie_data


def get_gx_data():
    """
    获取：二月份广西每天的新增确诊人数，用于绘制折线图(Line)
    :return:返回两个列表类型的数据：时间、value
    """
    sql = """select update_time, sum(confirmed_add) from covid_data_2017 where province_code=450000 group by update_time"""
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()
    line_date = []
    line_confirmed_add_gx = []
    for d, a in data:
        line_date.append(d.day)
        line_confirmed_add_gx.append(int(a))
    return line_date, line_confirmed_add_gx


def draw_map_confirmed_count():
    """
    查询全国各省市的累计确诊人数，绘制一个地图(Map)
    :return: echarts所需的option
    """
    sql = """select sum(c.confirmed_count),a.map_name from covid_data_2017 c left join area_china a 
    on(c.province_code=a.area_code) where c.update_time='2020-02-29' group by a.area_code"""
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()
    confirmed_count_map_value = []
    confirmed_count_map_attr = []
    for value, attr in data:
        confirmed_count_map_value.append(int(value))
        confirmed_count_map_attr.append(attr)
    pieces = [
        {'min': 0, 'max': 50},
        {'min': 51, 'max': 100},
        {'min': 101, 'max': 500},
        {'min': 501, 'max': 1000},
        {'min': 1001, 'max': 2000},
        {'min': 2001}
    ]
    map = Map()
    map.add('', confirmed_count_map_attr, confirmed_count_map_value, is_visualmap=True, is_toolbox_show=False,
            visual_range=[min(confirmed_count_map_value), max(confirmed_count_map_value)], is_label_show=False,
            pieces=pieces, is_piecewise=True, visual_pos='right')
    option = map.get_options()
    option = TRANSLATOR.translate(option).as_snippet()
    # map.render('map.html')
    return option


def get_Gauge_data():
    """
    获取截止到2020年2月29日全国感染新冠肺炎的死亡率，用于绘制仪表盘(Gauge)
    :return: 死亡率（百分比）
    """
    sql = """select sum(dead_count)/sum(confirmed_count) from covid_data_2017 where update_time='2020-02-29'"""
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchone()
    # 保留两位小数
    data = round(data[0]*100, 2)
    return data


def get_scater_date():
    """
    获取各省市从湖北迁入的人口比例与该省累计确诊人数的关系，用于绘制散点图(Scatter)
    :return:两个列表：   一个是从0到21的占比值（占比值最小0,最大不到20）   一个嵌套列表：[迁徙占比值、确诊人数]
    """
    sql = 'select m.value, c.confirmed_count, c.province_code, c.province_name from migrate_data_2017 m right join ' \
          'covid_data_2017 c on (m.target_province_code=c.province_code) where m.source_province_code=420000 ' \
          'group by c.province_code order by m.value'
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()
    data_x = [i for i in range(0, 22)]
    data_y = []
    for value, count, code, name in data:
        # print(value, count, name, code)
        data_y.append([value, count])
    # print(data_x)
    return data_x, data_y


def get_confirmed():
    """
    获取二月份全国每天的新增确诊人数（去除13号），用于绘制折线图(Line)
    :return:两个列表：   新增确诊人数、日期
    """
    sql = 'select sum(confirmed_add), update_time from covid_data_2017 group by update_time'
    mydb = db()
    cur = mydb.get_cur(sql)
    data = cur.fetchall()
    confirmed_count = []
    confirmed_date = []
    for confirmed, date in data:
        if date == datetime.date(2020, 2, 13):
            continue
        else:
            confirmed_count.append(int(confirmed))
            confirmed_date.append(date.day)
    return confirmed_count, confirmed_date
