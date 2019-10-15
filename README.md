
# Locator

## 简介

一个用于识别特定网格图异常点的 python 程序。

## 实现说明

实现算法主要基于这样的思想：对于每个像素点，计算出其邻域内所有点灰度值的方差。藉此，可以轻易地得到：

- 网格的具体位置
- 有异常的网格位置

目前的实现（为了方便）初始化部分是暴力处理的，初始化时间可能较长，未来可以优化（成一个线性过程）。

## 测试结果



![](https://i.imgur.com/NQkWeeJ.png)

![](https://i.imgur.com/EuCsB7y.png)

![](https://i.imgur.com/3MWcKP9.png)

