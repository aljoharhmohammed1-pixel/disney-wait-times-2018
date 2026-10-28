from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Disney Wait Times", layout="wide")
st.title("Disney World Wait Times 2018")
st.sidebar.write("Hourly wait times for selected Disney World rides in 2018.")
data_path = Path(__file__).parent / "clean_data.csv"
if not data_path.exists():
    st.error("Place clean_data.csv next to app.py. Run the notebook to create it.")
    st.stop()
df = pd.read_csv(data_path, parse_dates=["Date"])
parks = st.sidebar.multiselect("Park", sorted(df["Park"].unique()), default=sorted(df["Park"].unique()))
rides = st.sidebar.multiselect("Ride", sorted(df["Ride"].unique()), default=sorted(df["Ride"].unique()))
seasons = st.sidebar.multiselect("Ticket season", sorted(df["Season"].unique()), default=sorted(df["Season"].unique()))
hours = st.sidebar.slider("Hour", 0, 23, (0, 23))
data = df[df["Park"].isin(parks) & df["Ride"].isin(rides) & df["Season"].isin(seasons) & df["Hour"].between(*hours)]
if data.empty:
    st.info("No records match these filters. Select different options.")
    st.stop()
a, b, c = st.columns(3)
a.metric("Hourly records", f"{len(data):,}")
b.metric("Mean posted wait", f"{data['PostedWait'].mean():.1f} min")
c.metric("Actual wait missing", f"{data['ActualWait'].isna().mean():.1%}")
st.subheader("Data preview")
st.dataframe(data.head(20))
st.subheader("Summary statistics")
st.dataframe(data[["PostedWait", "ActualWait", "WaitDifference"]].describe())
st.subheader("Mean posted wait by ride")
ride_mean = data.groupby("Ride")["PostedWait"].mean().sort_values(ascending=False)
st.bar_chart(ride_mean)
st.subheader("Mean posted wait by hour")
st.line_chart(data.groupby("Hour")["PostedWait"].mean())
st.subheader("Insights for the selected data")
st.write(f"The ride with the highest mean posted wait is {ride_mean.idxmax()} ({ride_mean.max():.1f} minutes).")
paired = data.dropna(subset=["PostedWait", "ActualWait"])
if not paired.empty:
    st.write(f"In {len(paired):,} paired records, the mean posted-minus-actual wait is {paired['WaitDifference'].mean():.1f} minutes. The median is {paired['WaitDifference'].median():.1f} minutes.")
st.caption("Historical data from 2018. Hourly records are not individual visitors. Differences are descriptive; missing actual waits limit the paired comparison.")
st.download_button("Download filtered data", data.to_csv(index=False), "filtered_data.csv", "text/csv")
