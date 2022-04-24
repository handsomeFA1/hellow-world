def create_plot(x, y, styles, lables, axlables):
    plt.figure(figsize=(10, 6))
    for i in range(len(x)):
        plt.plot(x[i], y[i], styles[i], label = lables[i])
        # 遍历参数，对于每个分量都画出指定样式的图像
        plt.xlabel(axlables[0])
        plt.ylabel(axlables[1])
    plt.legend(loc = 0)
        # 标签定义
