import json
import os
from collections import Counter

VOTES_FILE = "votes.json"

def tally_votes():
    if not os.path.exists(VOTES_FILE):
        print("No votes found.")
        return

    with open(VOTES_FILE, "r") as file:
        votes = json.load(file)

    revealed_votes = [info["revealed"] for info in votes.values() if info.get("revealed")]
    if not revealed_votes:
        print("No valid revealed votes yet.")
        return

    tally = Counter(revealed_votes)
    print("📊 Voting Results:")
    for candidate, count in tally.items():
        print(f"🗳️ {candidate}: {count} vote(s)")

if __name__ == "__main__":
    tally_votes()
