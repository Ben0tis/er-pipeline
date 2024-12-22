# Quebec Emergency Room Data Pipeline

### **By:** Benjamin Desmeules Otis  
**GitHub and EdX:** Ben0tis  
**From:** Quebec, Canada  
**Video Demo:** Coming soon!
---

### **Project Overview**
The Quebec Emergency Room Data Pipeline is an ETL (Extract, Transform, Load) pipeline designed to analyze emergency room (ER) data in Quebec. The project leverages public datasets to generate insights and visualizations that showcase trends, performance, and areas for improvement in ER operations. This project was developed as part of the CS50X final project, showcasing skills in Python, data analysis, and visualization.

---

### **Features**
#### **ETL Pipeline**
1. **Extract:**
   - Fetch raw data from the Quebec ER room public API.
   - Save the data in CSV format for transformation.

2. **Transform:**
   - Clean and filter raw data.
   - Add calculated columns, such as ratios for elderly (75+) and mental health visits.
   - Format data to ensure compatibility with downstream analysis.

3. **Load:**
   - Load the transformed data into an SQLite database for structured storage and querying.

#### **Visualizations**
Generate meaningful plots that illustrate:
- Total visits by year (line plot).
- Average length of stay by region (horizontal bar plot).
- Ratios of elderly and mental health visits (bar plot with percentages).
- Worst-performing locations by region (horizontal bar plot).
- Average delays for ambulatory and stretcher care (bar plot).
- Delays by region and care type (heatmap).

---

### **Data Analysis**
The dataset provides insights into emergency room operations across Quebec. Key observations include:
- **Total Visits Over Time:**
  - Visits are rapidly increasing year after year, from 1.7M to 2.4M, since the start of the dataset.
- **Regional Performance:**
  - Certain regions show significantly longer average stays, indicating potential inefficiencies.
- **Elderly and Mental Health Ratios:**
  - Elderly patients constitute approximately 15% of total visits, while mental health cases account for about 7%.
- **Care Delays:**
  - Delays for stretcher care are generally higher than ambulatory care, highlighting bottlenecks in critical patient management.

---

### **Design Decisions**
1. **Focus on ETL Pipeline:**
   - An ETL structure ensures modularity and scalability for processing and analyzing data.
   - Transformations focus on meaningful metrics, such as ratios and delays, to enable targeted visualizations.

2. **SQLite Database Integration:**
   - Using SQLite facilitates structured storage and querying, supporting both current visualizations and future extensions.

3. **Visualization Choices:**
   - Visualizations were selected to provide actionable insights, such as identifying bottlenecks and trends.
   - Horizontal bar plots were used for regions to accommodate long names, while heatmaps highlight data intensity.

4. **Notes:**
   - The original dataset was already pretty "clean", but I still wanted to practice implementing best practices. 
   - The dataset is already available as a csv file, but I wished to practice pulling from APIs.
   - I used Seaborn to simplify layouts instead of having to deep dive in Matplotlib's documentation.
   - The data analysis is kept short here as the focus of this project is the code itself.

---

### **Technical Implementation**
1. **Extract (`extract.py`):**
   - Uses the Requests library to fetch data from the **Données Quebec** public API.
   - Saves raw data in the `data/raw/` directory as a CSV file.

2. **Transform (`transform.py`):**
   - Processes raw data to filter irrelevant rows and columns.
   - Adds calculated columns, such as ratios for elderly visits and mental health cases.
   - Outputs cleaned data to the `data/processed/` directory.

3. **Load (`load.py`):**
   - Loads transformed data into an SQLite database (`qc_er_data.db`).
   - Overwrites existing tables to ensure consistency.

4. **Visualize (`visualize.py`):**
   - Generates plots using Seaborn and Matplotlib.
   - Saves visualizations to the `visualizations/` directory for easy access.

---

### **Usage**

#### **Running the ETL Pipeline**
1. Clone the repository:
   ```bash
   git clone https://github.com/Ben0tis/er-pipeline.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the `main.py` script to execute the full pipeline:
   ```bash
   python src/main.py
   ```

#### **Viewing Visualizations**
- The visualizations will be saved in the `visualizations/` directory.

---

### **Directory Structure**
```
.
├── src/
│   ├── extract.py          # Extracts data from API
│   ├── transform.py        # Cleans and transforms data
│   ├── load.py             # Loads data into SQLite
│   ├── visualize.py        # Generates visualizations
│   └── main.py             # Orchestrates the ETL and visualization
├── data/
│   ├── raw/                # Raw extracted data
│   ├── processed/          # Transformed data and SQLite database
│   └── visualizations/     # Generated visualizations
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── listevariables(...).pdf # Dataset documentation
```

---

### **Future Enhancements**
- Add way to focus on specific years or regions.
- Add interactivity through a Jupyter Notebook or a lightweight web interface.
- Include additional performance metrics, such as patient satisfaction or wait times.

---

### **Acknowledgments**
- **CS50X:** For providing the foundation to develop this project.
- **Données Québec:** For access to the public datasets.

---

