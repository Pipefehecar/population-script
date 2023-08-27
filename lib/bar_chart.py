import matplotlib.pyplot as plt


def bar_chart(x_data: list, y_data: list, x_label: str, y_label: str, chart_title: str = 'bar chart'):
    plt.bar(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)
    plt.show()
