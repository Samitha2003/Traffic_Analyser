# 🚦 Traffic Data Analyser

A Python-based traffic data analysis tool that processes junction survey data from CSV files, computes key traffic statistics, and visualises hourly vehicle frequency via an interactive histogram.

---

## 📋 Features

- **Date-validated input** — Prompts users for a survey date (DD/MM/YYYY) with full validation including leap year, month-length, and range checks.
- **Comprehensive traffic statistics** — Calculates a wide range of metrics per dataset:
  - Total vehicles, trucks, electric vehicles, and two-wheeled vehicles
  - Buses heading North at Elm Avenue/Rabbit Road
  - Vehicles travelling straight through both junctions
  - Percentage of trucks and scooters
  - Average bicycles per hour
  - Vehicles exceeding the speed limit
  - Peak traffic hours at Hanley Highway/Westway
  - Total hours of rain recorded
- **Results export** — Appends computed outcomes to a `results.txt` file for persistent record keeping.
- **Tkinter histogram** — Displays a side-by-side bar chart of hourly vehicle counts for both junctions.
- **Multi-file processing** — Allows users to load and analyse multiple CSV datasets in a single session without restarting.

---

## 🗂️ Project Structure

```
traffic_data_anlyser/
│
├── analyser.py                  # Main application script
├── traffic_data15062024.csv     # Sample dataset – 15 June 2024
├── traffic_data16062024.csv     # Sample dataset – 16 June 2024
├── traffic_data21062024.csv     # Sample dataset – 21 June 2024
└── results.txt                  # Auto-generated output file (created on first run)
```

---

## ⚙️ Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)
- `csv` (built-in Python module)

No third-party packages are required.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Samitha2003/Traffic_Analyser.git
cd Traffic_Analyser
```

### 2. Run the analyser

```bash
python analyser.py
```

### 3. Follow the prompts

```
Please enter the day of the survey in the format DD: 15
Please enter the month of the survey in the format MM: 06
Please enter the year of the survey in the format YYYY: 2024
```

The program will:
1. Load the corresponding CSV file (e.g., `traffic_data15062024.csv`)
2. Print all computed statistics to the console
3. Save results to `results.txt`
4. Open a Tkinter histogram window showing hourly traffic per junction
5. Ask if you want to analyse another dataset

---

## 📊 CSV Data Format

The input CSV files must contain the following columns:

| Column | Description |
|--------|-------------|
| `timeOfDay` | Time of the record (HH:MM format) |
| `VehicleType` | Type of vehicle (e.g., Car, Truck, Bicycle, Scooter) |
| `elctricHybrid` | Whether the vehicle is electric/hybrid (`True`/`False`) |
| `JunctionName` | Junction where the vehicle was recorded |
| `travel_Direction_in` | Direction the vehicle entered (N/S/E/W) |
| `travel_Direction_out` | Direction the vehicle exited (N/S/E/W) |
| `VehicleSpeed` | Speed of the vehicle (integer) |
| `JunctionSpeedLimit` | Speed limit at the junction (integer) |
| `Weather_Conditions` | Weather at time of record (e.g., Clear, Light Rain, Heavy Rain) |

---

## 📈 Sample Output

```
************************************************

Selected data file is traffic_data15062024.csv

************************************************
The total number of vehicles recorded for this date is 1254
The total number of trucks recorded for this date is 87
The total number of electric vehicles recorded for this date is 312
...
The highest number of vehicles in an hour on Hanley Highway/Westway is 98
The most vehicles through Hanley Highway/Westway were recorded between Between 08:00 and 9:00
The number of hours of rain for this date is 3
```

---

## 🏗️ Architecture Overview

| Component | Description |
|-----------|-------------|
| `validate_date_input()` | Validates DD/MM/YYYY input with full calendar logic |
| `process_csv_data()` | Reads and computes all traffic statistics from a CSV file |
| `display_outcomes()` | Prints formatted results to the console |
| `process_hourly_trafic()` | Builds hourly vehicle count per junction for histogram |
| `save_results_to_file()` | Appends results to `results.txt` |
| `HistogramApp` | Tkinter GUI class for rendering the bar chart |
| `MultiCSVProcessor` | Orchestrates multi-file processing and user interaction loop |

---

## 👤 Author

**Samitha Bandara**  
Student ID: 21198520  
Date: 23/11/2024

---

## 📄 License

This project was developed as part of an academic coursework submission. All rights reserved.
