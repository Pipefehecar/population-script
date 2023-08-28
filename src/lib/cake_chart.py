import matplotlib.pyplot as plt


def cake_chart(data: list, labels: list, chart_title: str = "cake population chart"):
    """
    Create a pie chart using the matplotlib library in Python.

    Args:
        data (list): The data for the pie chart.
        labels (list): The labels for each data point in the pie chart.
        chart_title (str, optional): The title of the pie chart. Defaults to "cake population chart".

    Returns:
        None. The function only displays the pie chart.
    """
    plt.figure(figsize=(16, 16))  # Tamaño de la figura
    plt.pie(
        data, labels=labels
    )  # Crea el gráfico de torta
    plt.axis("equal")  # Aspecto de un círculo
    plt.title(chart_title)  # Título del gráfico
    # Mostrar el gráfico
    plt.show()
    # Mostrar el gráfico
    plt.show()
