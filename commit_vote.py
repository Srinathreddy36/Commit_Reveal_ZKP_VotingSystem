import hashlib
import json
import os
import secrets

VOTERS = ["voter1", "voter2"]
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

def commit_vote():
    name = input("Enter your voter name: ").strip().lower()
    if name not in VOTERS:
        print("❌ Voter not registered.")
        return

    print("Candidates: 0 for Alice, 1 for Bob")
    try:
        vote_index = int(input("Enter your vote (0 or 1): ").strip())
        if vote_index not in (0, 1):
            raise ValueError
    except ValueError:
        print("❌ Invalid vote input.")
        return

    vote = CANDIDATES[vote_index]
    nonce = secrets.token_hex(16)
    commitment = sha3_256_hash(vote + nonce)

    votes = load_votes()
    votes[name] = {
        "commitment": commitment,
        "revealed": False
    }
    save_votes(votes)

    print(f"✅ Vote committed successfully for {name}")
    print(f"📌 Save this nonce for revealing phase: {nonce}")

if __name__ == "__main__":
    commit_vote()
