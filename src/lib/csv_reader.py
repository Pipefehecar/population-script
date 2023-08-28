import csv


def extract_population_by_country(country: str, csv_path: str) -> tuple:
    """
    Extracts the population density data for a specified country from a CSV file.

    Args:
        country (str): The name of the country for which the population density data is to be extracted.
        csv_path (str): The path to the CSV file containing the population data.

    Returns:
        tuple: A tuple containing the header (years) and the population density data for the specified country.
    """

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file)
        header = [i.split(" ")[0] for i in next(csv_data)][5:13]

        for row in csv_data:
            if row[2] == country.title():
                density_data = list(map(int, row[5:13]))
                return (header, density_data)
        raise ValueError("Country not found")


def extract_world_population(csv_path: str) -> tuple:
    """
    Extracts the countries and their corresponding populations from a CSV file.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing two lists - the list of countries and the list of populations.

    Example:
        countries, populations = extract_world_population("world_population.csv")
        print(countries)
        print(populations)
    """
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file)
        next(csv_data)
        countries: list[str] = []
        population: list[int] = []
        for row in csv_data:
            if row[4] == "South America":
                countries.append(row[2])
                population.append(float(row[16]))
        return countries, population
