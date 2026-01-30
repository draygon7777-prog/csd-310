import csv
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib import Path

script_dir = Path(__file__).resolve().parent

filename = script_dir / 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

# Instructions for user before starting loop
print("This program will print a graph of the high and low temperatures recorded at Sitka Airport")
user_input = 'continue'
exit_command = 'exit'

while exit_command not in user_input.lower():
    user_input =input("Type highs for high temperature plot and lows for low temperature plot, or type exit to end:")

    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    if user_input.lower() == 'highs':
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
    elif user_input.lower() == 'lows':
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
    elif user_input.lower() == 'exit':
        break
    else:
        print('Please input a valid response.')

    # Format plot.    
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

print('Closing program.')