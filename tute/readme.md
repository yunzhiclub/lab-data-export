## 环境
python3.9

```
Package         Version
--------------- -------
aenum           3.1.0
dbf             0.99.1
numpy           1.21.2
pandas          1.3.3
pip             21.1.2
python-dateutil 2.8.2
pytz            2021.1
setuptools      57.0.0
six             1.16.0
wheel           0.36.2
xlrd            2.0.1
```

## 使用步骤
1. 按最新的课程编号更新task表中的课程编号
2. 将原始档案号做为sheet的名称,新建sheet并将对应实验大纲中的内容复制到excel表中.
3. 运行main.py，查看运行结果。
4. x_symc.DBF与x_syxm.DBF则为需要上报的数据
5. 将 x_symc.DBF与x_syxm.DBF连同上级下发的x_dw.dbf以及x_kck.dbf复制到那款优秀软件的根目录或子目录
6. 打开那款优秀的软件，继续执行：
7. 4 -> D数据安装
8. 选择x_syxm x_symc x_kck x_dw四项，点开始还原。选择5步中的文件夹后确认还原。
9. 1 -> E数据整理
10. 1 -> D -> B实验项目基础信息
11. 1 -> D -> D本学年实验项目信息
12. 4 -> 数据备份，选择 x_symc.DBF与x_syxm.DBF导出，并上交上级部分

## 注意事项
在excel表中的实验大纲不能有合并的单元格，否则会引发数据抓取错误。
注意：不能有合并的单元格。