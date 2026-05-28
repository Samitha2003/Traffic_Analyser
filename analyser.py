#Author: Samitha Bandara
#Date: 23/11/2024
#Student ID: 21198520

import tkinter as tk
import csv

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """   
    #Validate Date
    while True:
        date_input = input("Please enter the day of the survey in the format DD: ").strip()
        if date_input == "":
            print("Please enter the date to continue.")
            continue
        try:
            date = int(date_input)
            if date < 1 or date > 31:#Check if the date is between 1 and 31
                print("Out of range - Values must be in the range 1 and 31.")
                continue
            else:
                break
        except ValueError:
            print("Integer Required")
            continue
    
    #Validate Month
    while True:
        month_input = input("Please enter the month of the survey in the format MM: ").strip()
        if month_input == "":
            print("Please enter the month to continue.")
            continue
        try:           
            month = int(month_input)
            if month < 1 or month > 12:#Check if the month is between 1 and 12
                print("Out of range - Values must be in the range 1 and 12.")
                continue
            elif month in [4, 6, 9, 11] and date > 30:
                print("Invalid date: The selected month has only 30 days.")
                re_month =input("Press 'Y' to re-enter the month or 'N' to start over: ").strip().upper()
                if re_month == "Y":
                    continue
                elif re_month == "N":
                    return validate_date_input()
                else:
                    print("Input invalid : Enter the month again.")
                    continue
            else:
                break
        except ValueError:
            print("Integer Required")
            continue    
                
    #Validate Year
    while True:
        year_input = input("Please enter the year of the survey in the format YYYY: ").strip()
        if year_input == "":
            print("Please enter the year to continue.")
            continue
        try:            
            year = int(year_input)
            if year < 2000 or year > 2024:#Check if the date is between 2000 and 2024
                print("Out of range - Values must range from 2000 and 2024.")
                continue
            else:
                break
        except ValueError:
            print("Integer Required")
            continue
        
    #Validate leap year
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):  # Leap year check
            if date > 29:
                print("Invalid date: February in a leap year has only 29 days.")
                return validate_date_input()
        elif date > 28:
            print("Invalid date: February in a non-leap year has only 28 days.")
            return validate_date_input()        

    return f"{date:02}{month:02}{year}"

# Task B: Processed Outcomes
def process_csv_data(file_name):
    
    # Initialize counters and variables
    total_vehicles = 0
    total_trucks = 0
    total_electric = 0
    total_two_wheeled = 0
    busses_north = 0
    total_straight = 0    
    over_speed_limit = 0
    elm_vehicles = 0
    hanley_vehicles = 0
    elm_scooters = 0
    hourly_counts = {}
    total_bicycles = 0
    hours_with_bicycles = set()
    rain_hours = set()
    total_rain_hours = 0
    traffic_data = {"Elm Avenue/Rabbit Road": {}, "Hanley Highway/Westway": {}}
    
    try:
        #opening the file to read data
        with open(file_name,"r") as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                # Validate required fields
                if not row["VehicleType"] or not row["Weather_Conditions"]:
                    print(f"Skipping {row} due to missing data")
                    continue

                # Validate numeric fields
                if not row["VehicleSpeed"].isdigit() or not row["JunctionSpeedLimit"].isdigit():
                    print(f"Skipping {row} due to invalid numeric data ")
                    continue
                
                # Extract hours
                hour = row["timeOfDay"][:2] 
                
                # Total Number of Vehicles
                total_vehicles += 1 
                                
                # Total Number of Trucks
                if row["VehicleType"] == "Truck":
                    total_trucks += 1
                
                # Total Number of Electric Vehicles
                if row["elctricHybrid"].strip().lower() == "true":
                    total_electric += 1
                    
                # Total Number of Two-Wheeled Vehicles
                if row["VehicleType"] in ["Bicycle","Motorcycle","Scooter"]:
                    total_two_wheeled += 1                
                
                # Total Buses Leaving Elm Avenue/Rabbit Road Heading north
                if row["VehicleType"] == "Buss" and row["JunctionName"] == "Elm Avenue/Rabbit Road" and row["travel_Direction_out"] == "N":
                    busses_north += 1
                
                # Total Vehicles going straight
                if row["travel_Direction_in"] == row["travel_Direction_out"]:
                    total_straight += 1
                
                # Percentage of Trucks
                truck_percentage = round((total_trucks / total_vehicles) * 100)
                    
                # Total Vehicles Over the Speed Limit
                if int(row["VehicleSpeed"]) > int(row["JunctionSpeedLimit"]):
                    over_speed_limit += 1          
                
                # Vehicles Through Elm Avenue/Rabbit Road
                if row["JunctionName"] == "Elm Avenue/Rabbit Road":
                    elm_vehicles += 1
                    if row["VehicleType"] == "Scooter":
                        elm_scooters += 1
                    
                # Total Hours of Rain
                if row["Weather_Conditions"] == "Light Rain" or row["Weather_Conditions"] == "Heavy Rain":
                    if hour not in rain_hours:  # Check if the hour is already in the set
                        rain_hours.add(hour)  # Add the hour to the set
                    total_rain_hours = len(rain_hours)
                            
                # Percentage of Trucks
                truck_percentage = round((total_trucks / total_vehicles) * 100)
                
                # Percentage of Scooters Through Elm Avenue/Rabbit Road
                if elm_vehicles > 0:
                    percentage_elm_scooters = int((elm_scooters / elm_vehicles) * 100)
                else:
                    percentage_elm_scooters = 0
                
                # Average Number of Bicycles Per Hour
                if row["VehicleType"] == "Bicycle":
                    total_bicycles += 1 
                    hours_with_bicycles.add(hour) # add the hour to a list
                total_hours = len(hours_with_bicycles)
                avg_bicycles = round(total_bicycles / total_hours) if total_hours > 0 else 0
                
                # Peak hours for Hanley Highway/Westway
                # Count vehicles and find the peak hour count
                if row["JunctionName"] == "Hanley Highway/Westway":
                    hourly_counts[hour] = hourly_counts.get(hour, 0) + 1 # Count vehicle for each hour
                    
                            
            # Vehicles through Hanley Highway/Westway
            if hourly_counts:  # Check if there are any counts
                peak_hour_count = max(hourly_counts.values())  # Find the maximum count
            else:  # Handle the case where no data is available
                peak_hour_count = 0
            
            formatted_peak_hours = []  # Initialize as a list
            # Creating the list to output data 
            for hour, count in hourly_counts.items():
                if count == peak_hour_count:
                    next_hour = int(hour) + 1
                    formatted_peak_hours.append(f"Between {hour}:00 and {next_hour}:00")  # Append data to the list

            
            #Outputs to display            
            outcomes = {
                "************************************************\n\n"
                "Selected data file is": file_name,
                "\n************************************************\n"
                "The total number of vehicles recorded for this date is": total_vehicles,
                "The total number of trucks recorded for this date is": total_trucks,
                "The total number of electric vehicles recorded for this date is": total_electric,
                "The total number of two-wheeled Vehicles recorded for this date is": total_two_wheeled,
                "The total number of buses leaving Elm Avenue/Rabbit Road heading North is": busses_north,
                "The total number of vehicles through both junctions not turning left or right is": total_straight,
                "The percentage of total vehicles recorded that are trucks for this date is": f"{truck_percentage}%",
                "The average number of bikes per hour for this date is": avg_bicycles,
                "The total number of vehicles recorded as over the speed limit for this date is": over_speed_limit,
                "The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is": elm_vehicles,
                "The total number of vehicles recorded through Hanley Highway/Westway junction is": hanley_vehicles,
                f"{percentage_elm_scooters}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.": "",            
                "The highest number of vehicles in an hour on Hanley Highway/Westway is": peak_hour_count,
                "The most vehicles through Hanley Highway/Westway were recorded between": ", ".join(formatted_peak_hours),  # joining two parts
                "The number of hours of rain for this date is": total_rain_hours,
            }
            
            return outcomes
            
    except FileNotFoundError:
        print(f"Cannot process data : File {file_name} not found!")
        return None

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    for key, value in outcomes.items():
        print(f"{key} {value}")
        
def process_hourly_trafic(file_name):
    traffic_data = {"Elm Avenue/Rabbit Road": {}, "Hanley Highway/Westway": {}}
    try:
        with open(file_name, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                hour = row["timeOfDay"][:2]
                junction = row["JunctionName"]

                if junction in traffic_data:
                    traffic_data[junction][hour] = traffic_data[junction].get(hour, 0) + 1
        return traffic_data
    except FileNotFoundError:
        print(f"Cannot display histogram : File {file_name} not found!")
        return None
    
# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    with open(file_name,"a") as file:
        for key,value in outcomes.items():
            file.write(f"{key} {value}\n")
        file.write("\n\n")
        

# Task D: Histogram Display
class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.window = tk.Tk()
        self.window.title("Histrogram")
        self.canvas_width = 1150
        self.canvas_height = 600
        self.bar_width = 15
        self.margin = 50
        
    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        # Data for two junctions (by hour)
        # Data preparation
        hours = [f"{i:02}" for i in range(24)]
        junction_1 = self.traffic_data.get("Elm Avenue/Rabbit Road", {})
        junction_2 = self.traffic_data.get("Hanley Highway/Westway", {})

        junction_1_values = [junction_1.get(hour, 0) for hour in hours]
        junction_2_values = [junction_2.get(hour, 0) for hour in hours]
        
        #Scaling factors        
        max_value = max(max(junction_1_values), max(junction_2_values))
        scaling_factor = (self.canvas_height - 175) / max_value 
        
        # Drawing X axes
        self.canvas.create_line(self.margin, self.canvas_height - self.margin, self.canvas_width - self.margin,
                           self.canvas_height - self.margin, width=2)  # X-axis

                
        # Draw bars and labels
        for i, hour in enumerate(hours):
            x0 = self.margin + i * 3 * self.bar_width
            x1 = x0 + self.bar_width
            x2 = x1 + self.bar_width

            y1 = self.canvas_height - self.margin - junction_1_values[i] * scaling_factor
            y2 = self.canvas_height - self.margin - junction_2_values[i] * scaling_factor
            
            # Draw bars
            self.canvas.create_rectangle(x0, y1, x1, self.canvas_height - self.margin, fill="green", outline="black")
            self.canvas.create_rectangle(x1, y2, x2, self.canvas_height - self.margin, fill="red", outline="black")
            
            # Add bar labels (numbers above the bars)
            self.canvas.create_text(x0 + self.bar_width / 2, y1 - 10, text=str(junction_1_values[i]),
                                    fill= "green", font=("Arial", 8))
            self.canvas.create_text(x1 + self.bar_width / 2, y2 - 10, text=str(junction_2_values[i]),
                                    fill= "red", font=("Arial", 8))
            
            # Add hour labels            
            self.canvas.create_text(x0 + self.bar_width, self.canvas_height - self.margin + 10, text=hour,
                                    font=("Arial", 8))
            self.canvas.create_text(self.canvas_width / 2, self.canvas_height - self.margin/2 ,
                                    text = "Hours 00:00 to 24:00", fill = "#87837e",
                                    font=("Arial", 10, "bold"))


    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        # Add title and legend
        self.canvas.create_text(self.canvas_width / 2, self.margin / 2,
                                text=f"Histogram of Vehicle Frequency per Hour ({self.date[:2]}/{self.date[2:4]}/{self.date[4:]})",
                                font=("Arial", 14, "bold"))
        
        # Draw legend
        legend_rectangle_width = 20
        legend_rectangle_height = 20
         
        self.canvas.create_rectangle(self.margin, self.margin ,
                                     self.margin + legend_rectangle_width, self.margin + legend_rectangle_height,
                                     fill="green", outline="black")
        self.canvas.create_text(self.margin + 30, self.margin + 10, text="Elm Avenue/Rabbit Road", anchor="w",
                                fill = "#87837e",
                                font=("Arial", 10, "bold"))

        self.canvas.create_rectangle(self.margin, self.margin + 50,
                                     self.margin + legend_rectangle_width, self.margin + legend_rectangle_height +10,
                                     fill="red", outline="black")
        self.canvas.create_text(self.margin + 30, self.margin + 40, text="Hanley Highway/Westway", anchor="w",
                                fill = "#87837e",
                                font=("Arial", 10, "bold"))
        
    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window() #Set up the canvas for drawing
        self.draw_histogram()
        self.add_legend()
        self.window.mainloop()   
        
# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None
        
    def load_csv_file(self, file_path):
        """
        Loads a CSV file and processes its data.
        """
        return process_hourly_trafic(file_path)

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.current_data = None

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            #Ask user for their choice
            choice = input("Do you want to add a new dataset (Y/N): ").strip().upper()
            if choice == "Y" or choice =="N":
                return choice #Return valid input
            print ("Invalid input. Please enater your choice again.\nIf you want to continue enter 'Y' or if youn want to quit enter 'N'")

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            # Validating the date and creating the file name
            date_str = validate_date_input()
            file_path = f"traffic_data{date_str}.csv"
        
            # Process data and display outcomes
            outcomes = process_csv_data(file_path)
            if outcomes:
                display_outcomes(outcomes)
                #Save results to a text file
                save_results_to_file(outcomes)
                
            self.current_data = self.load_csv_file(file_path)

            if self.current_data:
                histogram_app = HistogramApp(self.current_data, date_str)
                histogram_app.run()
                
            # Check if the user wants to add another input
            if self.handle_user_interaction() == 'N':
                print("Exiting program")
                break
        
if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()


