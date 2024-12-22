import pandas as pd

def transform_data(input_file="data/raw/raw_data.csv", output_file="data/processed/processed_data.csv", sort_by="nb_visites_total"):
    """
    Transform raw data for analysis by cleaning and filtering.
    """
    
    # Load raw data
    df = pd.read_csv(input_file)

    # Filter columns and only keep relevant information
    columns_of_interest = [
    "annee",
    "region",
    "nom_etablissement",
    "nom_installation",
    "nb_visites_total",
    "dms_total",  # Average length of stay for all patients
    "nb_usagers_pec_total",
    "delai_pec_total",  # Total time to first care
    "nb_visites_ambulatoire",
    "dms_ambulatoire",  # Average length of stay for ambulatory cases
    "nb_usagers_pec_ambulatoire",
    "delai_pec_ambulatoire",
    "nb_visites_sur_civiere",
    "dms_sur_civiere",  # Average length of stay on stretchers
    "nb_usagers_pec_sur_civiere",
    "delai_pec_sur_civiere",
    "nb_usagers_75ans_et_plus_total",
    "nb_usagers_sante_mentale_total",
    ]
    df = df[columns_of_interest]

    # Filter rows to exclude totals
    df = df[df["region"] != "Total provincial"]
    df = df[df["nom_etablissement"] != "Total régional"]
    df = df[df["nom_installation"] != "Total établissement"]

    # Handle missing values if any
    df = df.fillna(0)

    # Add columns for ratios
    df["75ans_et_plus_vs_total_ratio"] = df["nb_usagers_75ans_et_plus_total"] / df["nb_visites_total"].replace(0, 1) # Avoid division by zero
    df["sante_mentale_vs_total_ratio"] = df["nb_usagers_sante_mentale_total"] / df["nb_visites_total"].replace(0, 1)

    # Sort data by total visits
    df = df.sort_values(by=sort_by, ascending=False)

    # Save transformed data
    df.to_csv(output_file, index=False)
    print(f"Data successfully transformed and saved to {output_file}")

if __name__ == "__main__":
    try:
        transform_data()
    except Exception as e:
        print(f"An error occurred during data transformation: {e}")
