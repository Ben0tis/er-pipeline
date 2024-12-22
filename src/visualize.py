import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

def connect_to_db(db_path="data/processed/qc_er_data.db"):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM qc_er_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def visualize_trends(df):
    visits_by_year = df.groupby("annee")["nb_visites_total"].sum().reset_index()
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(data=visits_by_year, x="annee", y="nb_visites_total", marker="o")
    ax.set(
        title="Total Visits by Year",
        xlabel="Year",
        ylabel="Number of Visits (Millions)"
    )
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))  # Format y-axis in millions
    sns.despine()
    plt.tight_layout()
    return ax

def visualize_regions(df):
    avg_stay_by_region = df.groupby("region")["dms_total"].mean().reset_index().sort_values(by="dms_total")
    plt.figure(figsize=(8, 10))
    ax = sns.barplot(data=avg_stay_by_region, x="dms_total", y="region", color="orange")
    ax.set(
        title="Average Stay by Region",
        xlabel="Average Length of Stay (days)",
        ylabel="Region"
    )
    sns.despine()
    plt.tight_layout()
    return ax

def visualize_ratios(df):
    avg_ratios = {
        "75+ Ratio": df["75ans_et_plus_vs_total_ratio"].mean() * 100,  # Convert to percentage
        "Mental Health Ratio": df["sante_mentale_vs_total_ratio"].mean() * 100  # Convert to percentage
    }
    ratios_df = pd.DataFrame(list(avg_ratios.items()), columns=["Ratio Type", "Value"])
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(data=ratios_df, x="Ratio Type", y="Value", color="green")
    ax.set(
        title="Average Ratios (Elderly and Mental Health)",
        ylabel="Percentage (%)"
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f%%")  # Add bar labels as percentages
    sns.despine()
    plt.tight_layout()
    return ax

def visualize_worst_locations(df):
    worst_locations = df.loc[df.groupby("region")["dms_total"].idxmax()]
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=worst_locations, y="region", x="dms_total", hue="nom_installation", palette="Reds_d")
    ax.set(
        title="Worst Locations by Average Length of Stay (DMS)",
        xlabel="Average Length of Stay (days)",
        ylabel="Region"
    )
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Move legend outside plot
    sns.despine()
    plt.tight_layout()
    return ax

def visualize_care_delays(df):
    delays = df.groupby("region")[["delai_pec_ambulatoire", "delai_pec_sur_civiere"]].mean().reset_index()
    delays_melted = delays.melt(id_vars="region", var_name="Care Type", value_name="Average Delay")
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=delays_melted, x="region", y="Average Delay", hue="Care Type", dodge=True, palette="Purples_d")
    ax.set(
        title="Average Delays for Ambulatory vs. Stretcher Care (Hours)",
        xlabel="Region",
        ylabel="Average Delay (Hours)"
    )
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Move legend outside plot
    plt.xticks(rotation=45, ha="right")
    sns.despine()
    plt.tight_layout()
    return ax

def visualize_heatmap(df):
    delays = df.groupby("region")[["delai_pec_ambulatoire", "delai_pec_sur_civiere"]].mean()
    plt.figure(figsize=(12, 8))
    ax = sns.heatmap(delays, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Delay (Hours)'})
    ax.set(
        title="Delays by Region and Care Type",
        xlabel="Care Type",
        ylabel="Region"
    )
    plt.tight_layout()
    return ax