# %%
import pandas as pd
import glob

# %%
files = glob.glob('*.xlsx')
df = pd.read_excel(files[0])

df["DateTime"] = df["DATE TIME"]
# df["DateTime"] = pd.to_datetime(df["DATE TIME"], format='%d-%m-%y %H:%M')
date = df["DateTime"].dt.date
time = df["DateTime"].dt.time
df["Date"] = date
df.drop(['DATE TIME', "DISTRICT", "SL", "UPAZILA", "RIVER", "STATION ID", "STATION NAME", "DATA TYPE", "TYPE OF STATION", "LATITUDE", "LONGITUDE"], axis=1, inplace=True)
# df

# %%
date_range = pd.date_range(df["Date"].min(), df["Date"].max())
missing_dates = date_range[~date_range.isin(df["Date"])]
df.drop("Date", axis=1, inplace=True)

if len(missing_dates) > 0:
    print(f"The missing dates: {missing_dates}")
    input()
else:
    print("There is no missing dates")

# %%
duplicates = df[df.duplicated(subset='DateTime', keep=False)]
df = df.drop_duplicates(subset='DateTime', keep='first')
# duplicates

# %%
i = 1
while True:
    if (df.iloc[i, 1] - df.iloc[i-1, 1]) != pd.Timedelta(hours=3) and (df.iloc[i+1, 1] - df.iloc[i, 1]) != pd.Timedelta(hours=3):
        if (df.iloc[i, 1] - df.iloc[i-1, 1]) < pd.Timedelta(hours=1, minutes=30):
            df.iloc[i-1, 0] = df.iloc[i, 0]
        else:
            df.iloc[i+1, 0] = df.iloc[i, 0]

    i += 1
    if i == len(df)-1:
        break

# %%
df = df[df["DateTime"].dt.hour % 3 == 0]
df = df[df["DateTime"].dt.minute == 0]
# df

# %%
df['DateTime'] = pd.to_datetime(df['DateTime'])
df = df.set_index('DateTime')
df = df.resample('3H').asfreq()

# %%
df = df.reset_index()

# %%
df['WL (mMSL)'].fillna(df['WL (mMSL)'].shift(4), inplace=True)

# %%
df.to_csv("test.csv", index=False)
print("Done")

# %%



