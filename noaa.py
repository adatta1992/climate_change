import pandas as pd


def read_crop_data(csv_paths, crop):
    dfs = []
    for path in csv_paths:
        df = pd.read_csv(path)
        # Select columns
        df = df[["NAME", "DATE", "PRCP", "TAVG", "TMAX", "TMIN"]]

        # Extract State Abbreviation
        df["STATE"] = df["NAME"].str.extract(r",\s*([A-Z]{2})\s")[0]
        df = df.drop(columns=["NAME"])

        # Extract Year and Month
        df["YEAR"] = df["DATE"].str.split("-").str[0]
        df["MONTH"] = df["DATE"].str.split("-").str[1]
        df = df.drop(columns={"DATE"})

        # Map of numerical month value to month
        month_mapping = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }

        # Replace numerical month value with month
        df["MONTH"] = df["MONTH"].replace(month_mapping)

        # Create column for corresponding crop type
        df["CROP"] = crop

        dfs.append(df)

    # Combining dataframes of the same crop
    df_combined = pd.concat(dfs, ignore_index=True)

    return df_combined

    # Relative paths for .csv data for each crop


corn_paths = ["noaa_csv_files/Corn_1.csv", "noaa_csv_files/Corn_2.csv"]
soybean_paths = ["noaa_csv_files/Soybean_1.csv", "noaa_csv_files/Soybean_2.csv"]
barley_paths = [
    "noaa_csv_files/Barley_1.csv",
    "noaa_csv_files/Barley_2.csv",
    "noaa_csv_files/Barley_3.csv",
]
oats_paths = ["noaa_csv_files/Oats_1.csv", "noaa_csv_files/Oats_2.csv"]

# Crop types
crops = ["corn", "soybean", "barley", "oats"]

# List of .csv paths
paths = [corn_paths, soybean_paths, barley_paths, oats_paths]

# Use for loop and read_crop_data() fo create crop dataframes
crop_data = {}
for path, crop in zip(paths, crops):
    crop_data[crop] = read_crop_data(path, crop)

for crop in crops:
    print(crop_data[crop].head())
