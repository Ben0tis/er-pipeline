import pandas as pd
import sqlite3
import seaborn as sns

def connect_to_db(db_path="data/processed/qc_er_data.db"):
    """
    Connect to SQLite database and return a pandas DataFrame.
    """
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM qc_er_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def visualize_trends(df):
    visits_by_year = df.groupby("annee")["nb_visites_total"].sum().reset_index()
    ax = sns.lineplot(data=visits_by_year, x="annee", y="nb_visites_total", marker="o")
    ax.set(
        title="Total Visits by Year",
        xlabel="Year",
        ylabel="Number of Visits"
    )
    sns.despine()
    return ax

def visualize_regions(df):
    avg_stay_by_region = df.groupby("region")["dms_total"].mean().reset_index().sort_values(by="dms_total")
    ax = sns.barplot(data=avg_stay_by_region, x="dms_total", y="region", color="orange")
    ax.set(
        title="Average Stay by Region",
        xlabel="Average Length of Stay (days)",
        ylabel="Region"
    )
    sns.despine()
    return ax

def visualize_ratios(df):
    avg_ratios = {
        "75+ Ratio": df["75ans_et_plus_vs_total_ratio"].mean(),
        "Mental Health Ratio": df["sante_mentale_vs_total_ratio"].mean()
    }
    ratios_df = pd.DataFrame(list(avg_ratios.items()), columns=["Ratio Type", "Value"])
    ax = sns.barplot(data=ratios_df, x="Ratio Type", y="Value", color="green")
    ax.set(
        title="Average Ratios (Elderly and Mental Health)",
        ylabel="Average Ratio"
    )
    sns.despine()
    return ax

def visualize_worst_locations(df):
    worst_locations = df.loc[df.groupby("region")["dms_total"].idxmax()]
    ax = sns.barplot(data=worst_locations, y="region", x="dms_total", hue="nom_installation", palette="Reds_d")
    ax.set(
        title="Worst Locations by Average Length of Stay (DMS)",
        xlabel="Average Length of Stay (days)",
        ylabel="Region"
    )
    sns.despine()
    return ax

def visualize_care_delays(df):
    delays = df.groupby("region")[["delai_pec_ambulatoire", "delai_pec_sur_civiere"]].mean().reset_index()
    delays_melted = delays.melt(id_vars="region", var_name="Care Type", value_name="Average Delay")
    ax = sns.barplot(data=delays_melted, x="region", y="Average Delay", hue="Care Type", palette="Purples_d")
    ax.set(
        title="Average Delays for Ambulatory vs. Stretcher Care",
        xlabel="Region",
        ylabel="Average Delay (hours)"
    )
    sns.despine()
    return ax

def visualize_heatmap(df):
    delays = df.groupby("region")[["delai_pec_ambulatoire", "delai_pec_sur_civiere"]].mean()
    ax = sns.heatmap(delays, annot=True, fmt=".2f", cmap="coolwarm")
    ax.set(
        title="Delays by Region and Care Type",
        xlabel="Care Type",
        ylabel="Region"
    )
    return ax

def visualize_top_regions(df):
    """
    Visualize top-performing regions based on average delays and length of stay.
    """
    regional_performance = df.groupby("region").agg({
        "dms_total": "mean",
        "delai_pec_total": "mean"
    }).reset_index()
    ax = sns.scatterplot(data=regional_performance, x="delai_pec_total", y="dms_total", hue="region", palette="coolwarm")
    ax.set(
        title="Region Performance: Delays vs. Length of Stay",
        xlabel="Average Delay (hours)",
        ylabel="Average Length of Stay (days)"
    )
    sns.despine()
    return ax
