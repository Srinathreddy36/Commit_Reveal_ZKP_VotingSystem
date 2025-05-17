import hashlib
import json
import os

CANDIDATES = ["Alice", "Bob"]
VOTES_FILE = "votes.json"

def sha3_256_hash(data):
    return hashlib.sha3_256(data.encode()).hexdigest()

def load_votes():
    if not os.path.exists(VOTES_FILE):
        return {}
    with open(VOTES_FILE, "r") as file:
        return json.load(file)

def save_votes(votes):
    with open(VOTES_FILE, "w") as file:
        json.dump(votes, file, indent=4)

def reveal_vote():
    name = input("Enter your voter name: ").strip().lower()
    vote = input("Enter your vote (Alice or Bob): ").strip()
    nonce = input("Enter your secret nonce: ").strip()

    data = vote + nonce
    hash_val = sha3_256_hash(data)

    votes = load_votes()

    if name not in votes:
        print("❌ Voter not found.")
        return

    if votes[name]["commitment"] == hash_val:
        votes[name]["revealed"] = vote
        print("✅ Vote revealed and verified.")
    else:
        print("❌ Vote tampered or wrong data.")

    save_votes(votes)

if __name__ == "__main__":
    reveal_vote()
