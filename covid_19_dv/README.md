![image](https://github.com/caisi35/DataVisualization/blob/master/images/covid_19_dv_screenshot.png)
### 将数据导入mysql数据库
 1.创建visual_db_2017数据库  
 create database visual_db_2017  
 2.导入数据  
 use visual_db_2017  
 source your_filepath/visual_data_2017.sql

### 修改连接密码
在covid_19_dv/app/models.py文件下的db类修改成你的数据库密码

### 安装requirements.txt下的库文件


### 说明
1.绘制全国每天的新增确诊人数的时候从数据库查询出来的数据格式  
是datetime.date((2020, 2, 1))和Decimal('2014'),这些格式  
echarts不能识别，直接传会出错误
   * datetime.date((2020, 2, 1)) 直接取day，直接获取日期  
   * Decimal('2014') 则直接强制转为int类型
