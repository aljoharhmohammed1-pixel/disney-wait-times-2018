# Disney World Wait Times 2018

**Student:** Aljoharh mohammed Alnjm

This project explores hourly wait times for 14 Disney World rides in 2018.
It includes data cleaning, charts, a results summary, and a Streamlit dashboard.

## Files

- `Disney_Wait_Times_Analysis.ipynb`: notebook with code, outputs, and charts.
- `clean_data.csv`: cleaned data used by the dashboard.
- `app.py`: Streamlit dashboard.
- `requirements.txt`: Python packages.
- `Disney_Wait_Times_Final_Report.pdf`: final report.
- `Disney_Wait_Times_Final_Report.docx`: editable report.

## Run the notebook

Upload the notebook to Google Colab and select **Runtime > Run all**.
The notebook downloads the original R data file, converts it to CSV,
and saves `clean_data.csv`.

## Run the dashboard

Live Streamlit dashboard: https://aljoharh-disney-wait-times-2018.streamlit.app/

The GitHub Pages version runs the Streamlit app in the browser using Stlite.
The first visit may take longer while the required packages load.

Keep `app.py` and `clean_data.csv` in the same folder. Open a terminal in that folder:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Use the park, ride, season, and hour filters to explore the data.

## Data sources

- Dataset: https://github.com/LucyMcGowan/touringplans/blob/main/data/touringplans_2018.rda
- Column descriptions: https://lucymcgowan.github.io/touringplans/reference/touringplans_2018.html

## Main limitations

The data describes selected rides in 2018. Most actual wait values are missing.
Comparisons are descriptive and do not establish causal relationships.

