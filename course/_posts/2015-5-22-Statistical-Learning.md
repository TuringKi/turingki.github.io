---
layout: blog
comments: true
title: 【课程】统计学习
course_name: Statistical Learning
cover: SL.jpg
introduction: 本课程参照MIT的9.520:Statistical Learning Theory and Applications整理而成，它从正则(Regularization )的角度全面审视了包括Logistic 回归, 支持向量机，稀疏表示、流形正则等方法在内的多种机器学习方法。
---

>摘要：本课程参照MIT的[9.520:Statistical Learning Theory and Applications](http://www.mit.edu/~9.520/fall14/)整理而成，它从正则(Regularization )的角度全面审视了包括`Logistic 回归`, `支持向量机`，`稀疏表示`、`流形正则`等方法在内的多种机器学习方法。

##介绍

本课程主要讲解统计学习理论框架下的机器学习方法的一些最新进展。这既包括一些经典的方法，如正则网络和支持向量机，也会涉及一些几何(geometry)方法，稀疏(sparsity)，在线学习，特征选择(feature selection)，结构化输出和多任务学习等在内的一些前沿的技术。本课程也会谈到RBF和深度学习网络的联系。

过去15年中，如何有效的`学习`已经成为了研究AI的一个中心问题。

数学理论，算法实现和神经科学是机器学习的三大支柱。


<div align='center'><img src="../img/learnin_math_algorithm_neuroscience.png"  /><p class = "figure_caption">Figure 1.1.数学为机器学习的算法研究提供了理论工具以回答一些基础问题，例如什么样的学习模型具有泛化能力？如何提高学习算法的稳定性？这些问题都需要数学的介入。工程实践是对理论算法的实现，它需要针对实际问题对理论算法进行某种改造。而神经科学对于机器学习的作用是比较研究，站在神经科学的角度看待机器学习，你会发现机器学习可能在自然科学的研究中发挥其独特的作用：即回答什么是智能？</p></div>

机器学习和传统求解实际问题的数学模型(例如微分方程)最大的不同在于它需要关注模型的 `泛化能量(generalization)`，即对未知数据的预测能力，而不仅仅关注当前数据的拟合情况。更多的情况下，机器学习算法甚至需要在当前的数据(训练集)的拟合程度和泛化能力之间做出权衡。

##学习问题和正则

我们先给出`监督学习`的形式化定义。设存在一个product space（中文如何翻译?）$\mathbb{Z} = \mathbb{X} \times \mathbb{Y}$,其中$\mathbb{X}$是一个欧式空间，$\mathbb{Y}$是$\mathbb{R}$的一个子集。   在$\mathbb{Z}$中存在一个未知的`概率分布函数`$\mu (z)$。有`训练集` $S = \lbrace (\mathbf{x_1},y_1),(\mathbf{x_2},y_2),\dots,(\mathbf{x_N},y_N)\rbrace$`独立同分布（I.I.D）`地采样自$\mu$。设$\mathscr{H}$是一个函数空间:$\lbrace f \| f:\mathbb{X} \to \mathbb{Y} \rbrace$。那么监督学习算法是这样的一种映射:

$$

L:\mathbb{Z}^N \to \mathscr{H}
\label{supervised_learning}
$$

它通过考察训练集$S$并在$\mathscr{H}$中找到一个最佳的函数$f_S$使得$f_S (\mathbf{x}) \approx y$。

映射$\ref{supervised_learning}$几乎道尽了监督学习的玄机。要对一个监督学习算法进行研究，由这个映射我们知道，需要处理两个部分:1)训练集$\mathbb{Z}^N$，例如特征提取，特征选择，核方法等等；2)对假设空间$\mathscr{H}$进行处理，例如最大间隔超平面。

###期望风险，经验风险

给定一个风险函数$V(f,z)$,那么`期望风险`定义为：

$$
I[f] = \int_{\mathbb{Z}}{V(f,z)d \mu(z)}
$$

针对数据集$S$的`经验风险`定义为：

$$
I_S[f] = \frac{1}{N}\sum_{i = 1}^{N}{V(f,z_i)}
$$


###泛化能力

###稳定性

##数学补充(泛函分析和概率论)

##再生核空间

##字典，特征映射Mercer 理论

##Tikhonov 正则和表示理论

##正则最小二乘

##Logistic 回归和支持向量机

##Iterative Regularization via Early Stopping

##稀疏表示

##Proximal Methods

##Multiple Kernel Learning

##Generalization Bounds, Intro to Stability

##Stability of Tikhonov Regularization

##Consistency, Learnability and Regularization    

##Manifold Regularization

##Regularization for Multi-Output Learning

##学习数据表示:深度学习