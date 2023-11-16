import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Specify the file to write to
    output_path = os.path.join("Analysis", "PyPoll.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as datafile:
        # Initialize csv.writer
        csvwriter = csv.writer(datafile, delimiter=',')

        # Write the header to the output file
        csvwriter.writerow(["Election Analysis"])
        csvwriter.writerow(["________________________________________________"])

        # Create dictionaries to store results
        candidate_votes = {}
        unique_counts = {}
        total_rows = 0  # Added to count all rows for the ballot ID

        # Loop through each row
        for row in csvreader:
            ballot_id, county, candidate = row

            # Calculate the total number of ballot votes each candidate won independently
            candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

            # Count all rows for the ballot ID
            total_rows += 1

        # Print results for each candidate
        print("\nElection Results")
        print("________________________________________________")

        # Print the total number of rows for the ballot ID
        print(f"Total Votes: {total_rows}")

        print("________________________________________________")

        for candidate, votes in candidate_votes.items():
            total_votes = sum(candidate_votes.values())
            percentage = (votes / total_votes) * 100

            print(f"{candidate}: {percentage:.2f}% ({votes})")

        print("________________________________________________")
        # Determine the winner (candidate with the highest number of votes)
        winner = max(candidate_votes, key=candidate_votes.get)
        print(f"\nWinner: {winner}")
        print("________________________________________________")

        # Write the Election results to the output file

        csvwriter.writerow([f"Total Votes: {total_rows}"])

        csvwriter.writerow(["________________________________________________"])

        for candidate, votes in candidate_votes.items():
            total_votes = sum(candidate_votes.values())
            percentage = (votes / total_votes) * 100

            csvwriter.writerow([f"{candidate}: {percentage:.2f}% ({votes})"])

        csvwriter.writerow(["________________________________________________"])

        csvwriter.writerow([f"\nWinner: {winner}"])

        csvwriter.writerow(["________________________________________________"])

