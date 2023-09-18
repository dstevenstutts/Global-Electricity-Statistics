import pandas as pd
import numpy as np

# Original data
# Country, Features, Region, 1980-2021
data_df = pd.read_csv(
    '/Users/stevenstutts/Programming Projects/Data-Science/Global Electricity Statistics/Global-Electricity-Statistics.csv')
print(data_df.columns)
# Converting the year columns in the original data_df to numeric
for col in data_df.columns[3:]:
    data_df[col] = pd.to_numeric(data_df[col], errors='coerce')

# Strip cells with strings and replace spaces in the features column
data_df = data_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data_df["Features"] = data_df["Features"].str.replace(" ", "_")

# Using linear interpolation to fill missing values
data_df.interpolate(method='linear', inplace=True)

net_generation_df = data_df[data_df['Features'] == 'net_generation']
net_consumption_df = data_df[data_df['Features'] == 'net_consumption'].copy()
imports_df = data_df[data_df['Features'] == 'imports'].copy()
exports_df = data_df[data_df['Features'] == 'exports'].copy()
net_imports_df = data_df[data_df['Features'] == 'net_imports'].copy()
installed_capacity_df = data_df[data_df['Features']
                                == 'installed_capacity'].copy()
distribution_losses_df = data_df[data_df['Features']
                                 == 'distribution_losses'].copy()

# List of important dataframes for use with functions
data_list = [net_generation_df, net_consumption_df, imports_df, exports_df, net_imports_df,
             installed_capacity_df, distribution_losses_df]


# Exploratory Data Analysis
def descriptive_stats(data_list):
    # Names based on common naming patterns observed from your initial list
    names_list = ['net_generation', 'net_consumption', 'imports',
                  'exports', 'net_imports', 'installed_capacity', 'distribution_losses']

    stats_dict = {}

    for idx, df in enumerate(data_list):
        # Getting the name based on the DataFrame's order in the list
        name = names_list[idx]
        stats_dict[name] = {}

        # Dropping non-numeric columns for statistical calculations
        numeric_df = df.drop(
            columns=['Country', 'Region', 'Features'], errors='ignore')

        # Central Tendency
        stats_dict[name]['mean'] = numeric_df.mean()
        stats_dict[name]['median'] = numeric_df.median()
        mode_df = numeric_df.mode()
        stats_dict[name]['mode'] = mode_df.iloc[0] if not mode_df.empty else None

        # Dispersion
        stats_dict[name]['range'] = numeric_df.max() - numeric_df.min()
        stats_dict[name]['variance'] = numeric_df.var()
        stats_dict[name]['std_dev'] = numeric_df.std()
        stats_dict[name]['iqr'] = numeric_df.quantile(
            0.75) - numeric_df.quantile(0.25)

        # Skewness
        stats_dict[name]['skewness'] = numeric_df.skew()

        # Kurtosis
        stats_dict[name]['kurtosis'] = numeric_df.kurt()

    return stats_dict


stats = descriptive_stats(data_list)
print(data_df['Country'].unique)
