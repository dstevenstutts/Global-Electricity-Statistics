import pandas as pd


# Original data
# Country, Features, Region, 1980-2021
data_df = pd.read_csv(
    '/Users/stevenstutts/Programming-Projects/Data-Science/Global-Electricity-Statistics/data/Global-Electricity-Statistics.csv')

# Converting the year columns in the original data_df to numeric
for col in data_df.columns[3:]:
    data_df[col] = pd.to_numeric(data_df[col], errors='coerce')

# Strip cells with strings and replace spaces in the features column
data_df = data_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data_df["Features"] = data_df["Features"].str.replace(" ", "_")

# Using linear interpolation to fill missing values
data_df.interpolate(method='linear', inplace=True)

net_generation_df = data_df[data_df['Features'] == 'net_generation'].copy()
net_consumption_df = data_df[data_df['Features'] == 'net_consumption'].copy()
imports_df = data_df[data_df['Features'] == 'imports'].copy()
exports_df = data_df[data_df['Features'] == 'exports'].copy()
net_imports_df = data_df[data_df['Features'] == 'net_imports'].copy()
installed_capacity_df = data_df[data_df['Features']
                                == 'installed_capacity'].copy()
distribution_losses_df = data_df[data_df['Features']
                                 == 'distribution_losses'].copy()

BRICS = ['Brazil', 'Russia', 'India', 'China', 'South Africa']

G7 = ['Canada', 'France', 'Germany', 'Italy',
                'Japan', 'United Kingdom', 'United States']

G19 = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China',
       'France', 'Germany', 'India', 'Indonesia', 'Italy',
                 'Japan', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa',
                 'South Korea', 'Turkey', 'United Kingdom', 'United States']

OECD = ['Australia', 'Austria', 'Belgium', 'Canada', 'Chile',
        'Colombia', 'Czechia', 'Denmark', 'Estonia', 'Finland',
        'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
                  'Ireland', 'Israel', 'Italy', 'Japan', 'South Korea',
                  'Latvia', 'Lithuania', 'Luxembourg', 'Mexico', 'Netherlands',
                  'New Zealand', 'Norway', 'Poland', 'Portugal', 'Slovakia',
                  'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey',
                  'United Kingdom', 'United States']

OPEC = ['Algeria', 'Angola', 'Congo-Kinshasa', 'Equatorial Guinea', 'Gabon',
        'Iran', 'Iraq', 'Kuwait', 'Libya', 'Nigeria',
        'Saudi Arabia', 'United Arab Emirates', 'Venezuela']

ASEAN = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia',
                   'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

EU = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus',
      'Czechia', 'Denmark', 'Estonia', 'Finland', 'France',
      'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy',
      'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
                'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia',
                'Spain', 'Sweden']

Least_Developed = [
    # Africa
    "Angola", "Benin", "Burkina Faso", "Burundi", "Central African Republic", "Chad",
    "Comoros", "Democratic Republic of the Congo", "Djibouti", "Eritrea", "Ethiopia",
    "Gambia", "Guinea", "Guinea-Bissau", "Lesotho", "Liberia", "Madagascar", "Malawi",
    "Mali", "Mauritania", "Mozambique", "Niger", "Rwanda", "Sao Tome and Principe",
    "Senegal", "Sierra Leone", "Somalia", "South Sudan", "Sudan", "Togo", "Uganda",
    "United Republic of Tanzania", "Zambia",
    # Asia
    "Afghanistan", "Bangladesh", "Bhutan", "Cambodia", "Laos",
    "Myanmar", "Nepal", "Timor-Leste", "Yemen",
    # Caribbean
    "Haiti",
    # Pacific
    "Kiribati", "Solomon Islands", "Tuvalu"
]
Developing = [
    # Africa
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)",
    "Congo (Kinshasa)", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast",
    "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania",
    "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
    "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
    "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda",
    "Zambia", "Zimbabwe",

    # Asia
    "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan",
    "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran",
    "Iraq", "Israel", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon",
    "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
    "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia",
    "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand",
    "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen",

    # Americas
    "Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", "Belize", "Bolivia",
    "Brazil", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic",
    "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras",
    "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Suriname", "Trinidad and Tobago",
    "Uruguay", "Venezuela",

    # Oceania
    "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "Palau",
    "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu",

    # Europe
    "Albania", "Bosnia and Herzegovina", "Kosovo", "Macedonia", "Moldova", "Montenegro", "Serbia", "Ukraine"
]
Developed = ["Switzerland", "Norway", "Iceland", "Hong Kong", "Australia", "Denmark",
             "Sweden", "Ireland", "Germany", "Netherlands", "Finland", "Singapore",
             "Belgium", "New Zealand", "Canada", "Liechtenstein", "Luxembourg", "United Kingdom",
             "Japan", "South Korea", "United States", "Israel", "Slovenia", "Malta",
             "Austria", "United Arab Emirates", "Spain", "France", "Cyprus", "Italy",
             "Estonia", "Czech Republic", "Greece", "Poland", "Saudi Arabia", "Lithuania",
             "Bahrain", "Portugal", "Latvia", "Croatia", "Andorra", "Chile", "Qatar",
             "San Marino", "Slovakia", "Hungary", "Argentina", "Turkey", "Montenegro",
             "Kuwait", "Russia", "Brunei", "Romania", "Oman", "Bahamas", "Kazakhstan",
             "Trinidad And Tobago", "Costa Rica", "Uruguay", "Belarus", "Panama", "Malaysia",
             "Serbia", "Georgia", "Mauritius", "Thailand"
             ]

Regions = ['Africa' 'Eurasia' 'Europe' 'Asia & Oceania' 'Middle East'
           'North America' 'Central & South America']


# List of important dataframes organized by feature
data_list = [net_generation_df, net_consumption_df, imports_df, exports_df, net_imports_df,
             installed_capacity_df, distribution_losses_df]

BRICS_data_list = [df[df['Country'].isin(BRICS)] for df in data_list]
G7_data_list = [df[df['Country'].isin(G7)] for df in data_list]
G19_data_list = [df[df['Country'].isin(G19)] for df in data_list]
OECD_data_list = [df[df['Country'].isin(OECD)] for df in data_list]
OPEC_data_list = [df[df['Country'].isin(OPEC)] for df in data_list]
ASEAN_data_list = [df[df['Country'].isin(ASEAN)] for df in data_list]
EU_data_list = [df[df['Country'].isin(EU)] for df in data_list]
Least_Developed_data_list = [
    df[df['Country'].isin(Least_Developed)] for df in data_list]
Developing_data_list = [df[df['Country'].isin(Developing)] for df in data_list]
Developed_data_list = [df[df['Country'].isin(Developed)] for df in data_list]
Africa_data_list = [df[df['Region'] == 'Africa'] for df in data_list]
Asia_Oceania_data_list = [
    df[df['Region'] == 'Asia & Oceania'] for df in data_list]
Eurasia_data_list = [df[df['Region'] == 'Eurasia'] for df in data_list]
Europe_data_list = [df[df['Region'] == 'Europe'] for df in data_list]
Middle_East_data_list = [df[df['Region'] == 'Middle East'] for df in data_list]
North_America_data_list = [
    df[df['Region'] == 'North America'] for df in data_list]
Central_South_America_data_list = [
    df[df['Region'] == 'Central & South America'] for df in data_list]


data_names = ['net_generation', 'net_consumption', 'imports', 'exports', 'net_imports', 'installed_capacity',
              'distribution_losses']
conglomerate_list = [BRICS, G7, G19, OECD, OPEC, ASEAN, EU]
conglomerate_names = ['BRICS', 'G7', 'G19', 'OECD', 'OPEC', 'ASEAN', 'EU']


# Function for producing dataframes related to relevant conglomerates
def filter_dataframes_by_conglomerate(conglomerate_names, conglomerate_list, data_names, data_list):
    """
    Filters a list of dataframes based on lists of countries (conglomerates).

    Parameters:
    - conglomerate_names: List of strings representing the names of each conglomerate
    - conglomerate_list: List of lists with countries for each conglomerate
    - data_names: List of strings representing the names of each dataframe (minus '_df')
    - data_list: List of DataFrames with a 'Country' column

    Returns:
    - Nested dictionary. The outer dictionary's keys are conglomerate names and values are 
      inner dictionaries. The inner dictionaries' keys are the data names, and the values 
      are the filtered DataFrames.
    """
    result = {}

    for conglomerate, conglom_name in zip(conglomerate_list, conglomerate_names):
        inner_dict = {}
        for df, df_name in zip(data_list, data_names):
            # Filter the DataFrame based on the current conglomerate's countries
            filtered_df = df[df['Country'].isin(conglomerate)]
            inner_dict[df_name] = filtered_df

        result[conglom_name] = inner_dict

    return result
