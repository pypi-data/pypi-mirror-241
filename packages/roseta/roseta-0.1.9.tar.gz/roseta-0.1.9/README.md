# Roseta

[![Pypi](https://img.shields.io/pypi/v/roseta.svg)](https://pypi.org/project/roseta/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/roseta/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/roseta.svg)](https://github.com/Ailln/roseta/stargazers)

🧪 从「非结构化数据」到「结构化数据」！

> 如果需求多，就开始做，否则就慢慢推进～
> 1. 欢迎「提需求」🎉；
> 2. 欢迎「供数据」🎉。

## 1 功能

- [x] 转化「长度」描述；
  - 身高
  - 胸围
  - 腰围
  - 臀围
  - 肩宽
- [x] 转化「重量」描述；
- [x] 转化「城市」描述；
- [x] 转化「年龄」描述；
- [x] 转化「罩杯」描述；
- [ ] 转化「日期」描述；
- [ ] 转化「地点」描述。


## 2 安装

```bash
pip install roseta -U

# or
git clone https://github.com/Ailln/roseta.git
cd roseta && python setup.py install
```

## 3 使用

```python
from roseta import trans

## 转化「长度」
num, unit = trans("一米八")
# (180, 'cm')
num, unit = trans("1.8米", cls="length", unit="cm")
# (180.0, 'cm')
num, unit = trans("180厘米", unit="m")
# (1.8, 'm')
num, unit = trans("两尺")
# (66.67, 'cm')
num, unit = trans("2.1尺", cls="length")
# (70.0, 'cm')
num, unit = trans("2尺", cls="length", unit="m")
# (0.6667, 'm')

## 转化「重量」
num, unit = trans("一斤八")
# (0.9, 'kg')
num, unit = trans("1.8公斤", cls="weight", unit="kg")
# (1.8, 'kg')
num, unit = trans("180kg", unit="g")
# (180000, 'g')

## 转化「城市」
text, unit = trans("杭州市")
# ('杭州市', '市')
text, unit = trans("杭州", cls="city")
# ('杭州市', '市')
text, unit = trans("杭州市", unit="省")
# ('浙江省杭州市', '省')

## 转化「年龄」
num, unit = trans("一岁")
# (1, 'year')
num, unit = trans("二个月", cls="age")
# (0.2, 'year')
num, unit = trans("二个月", unit="year")
# (0.2, 'year')

## 转化「罩杯」
# 类别不可以省略
num, unit = trans("c36", cls="cup")
# ([96, 80], 'cm')，96 为上胸围，80 为下胸围
num, unit = trans("九五F", cls="cup", unit="m")
# ([1.17, 0.95], 'm')
```

## 4 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
