
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(
    '/content/drive/MyDrive/Datasets/electricity_prod_source_stacked.csv')

# Short column names
short_columns = [
    "Entity",
    "Code",
    "Year",
    "Other_Renewables_TWh",
    "Bioenergy_TWh",
    "Solar_TWh",
    "Wind_TWh",
    "Hydro_TWh",
    "Nuclear_TWh",
    "Oil_TWh",
    "Gas_TWh",
    "Coal_TWh"
]
data.columns = short_columns
data.head()

# Function to create a line graph for electricity production by sources


def plot_global_electricity_trends(df):
    """
    Creates a line graph showing global electricity production trends over time by source.

    Parameters:
    df (DataFrame): The filtered global dataset containing electricity production data.
    """
    sources = [
        'Other_Renewables_TWh',
        'Bioenergy_TWh',
        'Solar_TWh',
        'Wind_TWh',
        'Hydro_TWh',
        'Nuclear_TWh',
        'Oil_TWh',
        'Gas_TWh',
        'Coal_TWh']

    plt.figure(figsize=(14, 7))

    for source in sources:
        plt.plot(df['Year'], df[source], label=source)

    plt.xlabel('Year')
    plt.ylabel('Electricity Production (TWh)')
    plt.title('Global Electricity Production Trends by Source')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to create a bar graph


def plot_bar_For_usa_china_comparison(df):
    """
    Creates a bar graph comparing electricity production from different sources for the USA and China,
    with values displayed on the bars.

    Parameters:
    df (DataFrame): The filtered dataset for the USA and China.
    """
    sources = [
        'Other_Renewables_TWh',
        'Bioenergy_TWh',
        'Solar_TWh',
        'Wind_TWh',
        'Hydro_TWh',
        'Nuclear_TWh',
        'Oil_TWh',
        'Gas_TWh',
        'Coal_TWh']

    plt.figure(figsize=(14, 7))

    for i, country in enumerate(df['Entity']):
        production = df[df['Entity'] == country][sources].iloc[0]
        bar_positions = [x + i * 0.35 for x in range(len(sources))]
        plt.bar(bar_positions, production, width=0.35, label=country)

        # Add values on top of each bar
        for pos, value in zip(bar_positions, production):
            plt.text(
                pos,
                value,
                f'{value:.1f}',
                ha='center',
                va='bottom',
                fontsize=9)

    plt.xlabel('Electricity Source')
    plt.ylabel('Electricity Production (TWh)')
    plt.title(
        f'Comparison of Electricity Production by Source in {year} for the USA and China')
    plt.xticks([x + 0.35 / 2 for x in range(len(sources))],
               sources, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to create a box plot for electricity production by source


def plot_box_plot_for_sources(df, sources):
    """
    Creates a box plot for electricity production from different sources.

    Parameters:
    df (DataFrame): The filtered dataset to use for the box plot.
    sources (list): List of column names representing the electricity sources.
    """
    plt.figure(figsize=(14, 7))
    df.boxplot(column=sources)

    plt.xlabel('Electricity Source')
    plt.ylabel('Electricity Production (TWh)')
    plt.title('Box Plot of Electricity Production by Source')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# Filter global data from the dataset (assuming 'Entity' indicates
# different regions)
global_data = data[data['Entity'] == 'World']
# Call the function to create the plot
plot_global_electricity_trends(global_data)

# Filter data for the USA and China for a specific year and create a copy
year = 2020
df_year_filtered_usa_china = data[(data['Year'] == year) & (
    data['Entity'].isin(['United States', 'China']))].copy()

# Calculate total production for each country
df_year_filtered_usa_china['Total_Production_TWh'] = df_year_filtered_usa_china[
    ['Other_Renewables_TWh', 'Bioenergy_TWh', 'Solar_TWh', 'Wind_TWh', 'Hydro_TWh',
     'Nuclear_TWh', 'Oil_TWh', 'Gas_TWh', 'Coal_TWh']
].sum(axis=1)
# Call the function to create the plot
plot_bar_For_usa_china_comparison(df_year_filtered_usa_china)

# Filter data for global analysis outside the function
sources_to_plot = [
    'Other_Renewables_TWh',
    'Bioenergy_TWh',
    'Solar_TWh',
    'Wind_TWh',
    'Hydro_TWh',
    'Nuclear_TWh',
    'Oil_TWh',
    'Gas_TWh',
    'Coal_TWh']
filtered_global_data = data[data['Entity'] == 'World']

# Invoke the function to create the box plot
plot_box_plot_for_sources(filtered_global_data, sources_to_plot)
