1.绘制全国每天的新增确诊人数的时候从数据库查询出来的数据格式  
是datetime.date((2020, 2, 1))和Decimal('2014'),这些格式  
echarts不能识别，直接传会出错误
   * datetime.date((2020, 2, 1)) 直接取day，直接获取日期  
   * Decimal('2014') 则直接强制转为int类型
