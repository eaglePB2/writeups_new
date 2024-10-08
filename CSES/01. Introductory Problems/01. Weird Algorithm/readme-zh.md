﻿
# 奇特的演算法
> 原文: [CSES - Weird Algorithm](https://cses.fi/problemset/task/1068)

## 簡介
這裏有一個正整數$n$，他被運用於一個很神奇的演算法中。這個演算法的規則如下：
- 若$n$是偶數，演算法將會把$n$除2。
- 若$n$是奇數，演算法將會把$n$乘3后加1。

該演算法會一直持續，直到$n$是1爲止。
擧個例子，假設$n$是3，那麽演算法將會這麽處理：

$3→10→5→16→8→4→2→1$

現在，寫出一個程式碼，來重現這個演算法。

## I/O
### 輸入
$n$
### 輸出
一整個系列的演化，用空格區隔。

## 限制

| | |
|--|--|
|時間| $1.00秒$ |
|記憶體| $512$MB |
|輸入範圍| $$1\le n\le 10^{6} $$|

## 測試
### 測試 1
輸入:
```
3
```
輸出:

```
3 10 5 16 8 4 2 1
```
