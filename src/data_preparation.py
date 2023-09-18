import pandas as pd


# Original data
# Country, Features, Region, 1980-2021
data_df = pd.read_csv(
    '/Users/stevenstutts/Programming-Projects/Data-Science/Global-Electricity-Statistics/data/Global-Electricity-Statistics.csv')
print(data_df.columns)
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

# List of important dataframes for use with functions
data_list = [net_generation_df, net_consumption_df, imports_df, exports_df, net_imports_df,
             installed_capacity_df, distribution_losses_df]
