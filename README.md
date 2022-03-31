#  使用说明

## 1. 文件说明

```
D:.
│  211大学名单.xlsx
│  requirements.txt
│  UniversityExcel.py
│  UniversityName.py
│
└─data
        清华大学.xlsx
```

1. `清华大学.xlsx`为 `UniversityExcel.py`生成的示例文件。

2. `大学名单.xlsx`为`UniversityExcel.py`批量执行的大学目录。
3. `UniversityExcel.py`根据大学名单生成相应的EXCEL，合并EXCEL文件后可反向查看某些专业课对应的学校。
4. `UniversityName.py`可根据院校和代码查询相应专业课信息，比直接上研招网点击操作更快。

## 2. 使用的库

```
pandas==1.3.4
requests==2.26.0
lxml==4.6.3
```

## 
