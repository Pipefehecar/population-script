from lib.csv_reader import extract_population
from lib.bar_chart import bar_chart

def run(csv_path: str = 'data.csv', country: str = 'Colombia'):
    years, population = extract_population(country=country, csv_path=csv_path)
    bar_chart(x_data=years, y_data=population, x_label='years', y_label='population', chart_title= country + ' population')

if __name__ == '__main__':
    run()
