import csv


def extract_population(country: str, csv_path: str) -> tuple:
    """
    Extracts the population density data for a specified country from a CSV file.

    Args:
        country (str): The name of the country for which the population density data is to be extracted.
        csv_path (str): The path to the CSV file containing the population data.

    Returns:
        tuple: A tuple containing the header (years) and the population density data for the specified country.
    """

    with open(csv_path, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        header = [i.split(' ')[0] for i in next(csv_data)][5:13]
        print(header)
        for row in csv_data:
            if row[2] == country.title():
                density_data = row[5:13]
                return (header, density_data)
