# Exploratory Data Analysis function

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
