from lib.bar_chart import bar_chart
from lib.cake_chart import cake_chart
from lib.csv_reader import extract_population_by_country, extract_world_population


def get_country_bar(csv_path: str, country: str = "Colombia"):
    """
    Extracts population data for a specified country from a CSV file and displays it as a bar chart.

    Args:
        csv_path (str, optional): The path to the CSV file containing the population data. Defaults to 'data.csv'.
        country (str, optional): The name of the country for which the population data is to be extracted. Defaults to
        'Colombia'.

    Returns:
        None

    Example Usage:
        get_country_bar(csv_path='data.csv', country='Colombia')

    This code will extract the population data for Colombia from the 'data.csv' file and display it as a bar chart with
    the x-axis labeled as 'years', the y-axis labeled as 'population', and the chart title as 'Colombia population'.
    """
    years, population = extract_population_by_country(
        country=country, csv_path=csv_path
    )
    bar_chart(
        x_data=years,
        y_data=population,
        x_label="years",
        y_label="population",
        chart_title=country + " population",
    )


def get_population_cake(csv_path: str):
    """
    Extracts data from a CSV file and creates a pie chart showing the population distribution of different countries.

    :param csv_path: Optional string specifying the path to the CSV file. Defaults to "data.csv".
    :return: None
    """

    countries, population = extract_world_population(csv_path=csv_path)
    cake_chart(data=population, labels=countries)


def run(option: int, csv_path: str = "data.csv", country: str = "Colombia"):
    """
    Extracts population data for a specified country from a CSV file and displays it as a bar chart.

    Args:
        csv_path (str, optional): The path to the CSV file containing the population data. Defaults to 'data.csv'.
        country (str, optional): The name of the country for which the population data is to be extracted. Defaults to
        'Colombia'.

    Returns:
        None

    Example Usage:
        run(csv_path='data.csv', country='Colombia')

    This function extracts the population data for a specified country from a CSV file and displays it as a bar chart.
    It also creates a pie chart showing the population distribution of different countries.
    """

    if option == 1:
        get_country_bar(csv_path=csv_path, country=country)
    else:
        get_population_cake(csv_path=csv_path)


if __name__ == "__main__":
    # search_country = input("Enter the name of country you want to know about: ")
    # search_country = search_country.strip()
    run(option=2)
