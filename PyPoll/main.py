import csv
import os.path as path

csv_path = path.join("Resources", "election_data.csv")

with open(csv_path, "r") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")

    vote_data = []
    vote_per_candidate = []
    vote_percent = []
    vote_total = 0
    candidate_list = []
    vote_winner = ""
    current_winner_vote_count = 0


    for row in lines:
        vote_data.append(row)
    
    del vote_data[0]
    
    vote_total = len(vote_data)

    for rows in vote_data:
        if(rows[2] not in candidate_list):
            candidate_list.append(rows[2])
            vote_per_candidate.append(0)
            vote_percent.append(0)
    
    for rows in vote_data:
        for i in range(len(candidate_list)):
            if(candidate_list[i] == rows[2]):
                vote_per_candidate[i] = vote_per_candidate[i] + 1
    
    for i in range(len(vote_percent)):
        vote_percent[i] = vote_per_candidate[i] / vote_total
        vote_percent[i] = vote_percent[i] * 100
        vote_percent[i] = float(format(vote_percent[i], ".3f"))
    
    for i in range(len(vote_per_candidate)):
        if(vote_per_candidate[i] > current_winner_vote_count):
            current_winner_vote_count = vote_per_candidate[i]
            vote_winner = candidate_list[i]
    
    print(f"Election Results")
    print(f"-----------------------")
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {vote_percent[i]}% ({vote_per_candidate[i]})")
    
    print(f"-----------------------")
    print(f"Winner: {vote_winner}")
    print(f"-----------------------")

    with open("election_results.txt", mode="w") as out_file:
        print(f"Election Results", file=out_file)
        print(f"-----------------------", file=out_file)
        for i in range(len(candidate_list)):
            print(f"{candidate_list[i]}: {vote_percent[i]}% ({vote_per_candidate[i]})", file=out_file)
        print(f"-----------------------", file=out_file)
        print(f"Winner: {vote_winner}", file=out_file)
        print(f"-----------------------", file=out_file)