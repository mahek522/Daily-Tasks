import csv
import json
import os

def csv_to_json_by_battery_ranges(csv_filename, json_filename):
    data = {
        "battery_0_to_10": [],
        "battery_10_to_20": [],
        "battery_20_to_30": [],
        "battery_30_to_40": [],
        "battery_40_to_50": [],
        "battery_50_to_60": [],
        "battery_60_to_70": [],
        "battery_70_to_80": [],
        "battery_80_to_90": [],
        "battery_90_to_100": []
    }

    with open(csv_filename, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            battery = int(row["Battery"])

            vehicle_data = {
                "Hub": row["Fleet-Hub"],
                "Vehicle-ID": row["Vehicle ID"],
                "Model": row["Model"],
                "Battery": battery,
                "Type": row["Type"]
            }

            if 0 <= battery < 10:
                data["battery_0_to_10"].append(vehicle_data)

            elif 10 <= battery < 20:
                data["battery_10_to_20"].append(vehicle_data)

            elif 20 <= battery < 30:
                data["battery_20_to_30"].append(vehicle_data)

            elif 30 <= battery < 40:
                data["battery_30_to_40"].append(vehicle_data)

            elif 40 <= battery < 50:
                data["battery_40_to_50"].append(vehicle_data)

            elif 50 <= battery < 60:
                data["battery_50_to_60"].append(vehicle_data)

            elif 60 <= battery < 70:
                data["battery_60_to_70"].append(vehicle_data)

            elif 70 <= battery < 80:
                data["battery_70_to_80"].append(vehicle_data)

            elif 80 <= battery < 90:
                data["battery_80_to_90"].append(vehicle_data)

            elif 90 <= battery <= 100:
                data["battery_90_to_100"].append(vehicle_data)

    with open(json_filename, "w") as file:
        json.dump(data, file, indent=4)


csv_to_json_by_battery_ranges("fleet_data.csv", "battery_sorted.json")

