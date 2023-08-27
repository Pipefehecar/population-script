import matplotlib.pyplot as plt


def bar_chart(
    x_data: list,
    y_data: list,
    x_label: str,
    y_label: str,
    chart_title: str = "bar chart",
):
    """
    Create a bar chart using the matplotlib library in Python.

    Args:
        x_data (list): The data for the x-axis of the bar chart.
        y_data (list): The data for the y-axis of the bar chart.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        chart_title (str, optional): The title of the bar chart. Defaults to 'bar chart'.

    Returns:
        None. The function only displays the bar chart.
    """
    plt.bar(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)
    plt.show()
