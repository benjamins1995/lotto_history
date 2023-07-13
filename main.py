import csv
from collections import defaultdict


def read_and_analyze(filename):
    # Initialize the dictionaries
    column_counts = [defaultdict(int) for _ in range(7)]

    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            for i in range(7):
                # Convert the str to an int and count it
                column_counts[i][int(row[i])] += 1

    # Analyze the results
    for i, counts in enumerate(column_counts):
        # Sort the counts in descending order
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # Print the most frequent numbers
        print(f"Column {i + 1}")
        for j in range(min(10, len(sorted_counts))):
            print(f"{j+1} place: Number {sorted_counts[j][0]} with {sorted_counts[j][1]} entries")


if __name__ == "__main__":
    read_and_analyze("lotto_history_1970.csv")
