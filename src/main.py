import extract
import transform
import load
import visualize
import matplotlib.pyplot as plt

def run_etl():
    """
    Run the ETL pipeline
    """
    print("Starting ETL pipeline...")
    try:
        print("Extracting data...")
        extract.get_data()
        print("Data extraction complete.")
        
        print("Transforming data...")
        transform.transform_data()
        print("Data transformation complete.")
        
        print("Loading data into database...")
        load.load_to_sqlite()
        print("Data loaded into SQLite database.")
        
    except Exception as e:
        print(f"An error occurred during the ETL pipeline: {e}")
        return False
    
    print("ETL pipeline completed successfully!")
    return True


def generate_visualizations():
    """
    Generate and save visualizations.
    """
    print("Generating visualizations...")
    try:
        df = visualize.connect_to_db()

        # Save visualizations
        print("Saving Total Visits by Year...")
        ax = visualize.visualize_trends(df)
        ax.figure.savefig("visualizations/total_visits_by_year.png")

        print("Saving Average Stay by Region...")
        ax = visualize.visualize_regions(df)
        ax.figure.savefig("visualizations/average_stay_by_region.png")

        print("Saving Average Ratios...")
        ax = visualize.visualize_ratios(df)
        ax.figure.savefig("visualizations/average_ratios.png")

        print("Saving Worst Locations by Region...")
        ax = visualize.visualize_worst_locations(df)
        ax.figure.savefig("visualizations/worst_locations.png")

        print("Saving Care Delays...")
        ax = visualize.visualize_care_delays(df)
        ax.figure.savefig("visualizations/care_delays.png")

        print("Saving Delays Heatmap...")
        ax = visualize.visualize_heatmap(df)
        ax.figure.savefig("visualizations/delays_heatmap.png")

    except Exception as e:
        print(f"An error occurred during visualization: {e}")


if __name__ == "__main__":
    # Run the ETL pipeline
    if run_etl():
        # Generate and save visualizations if ETL is successful
        generate_visualizations()
        print("All visualizations saved successfully!")