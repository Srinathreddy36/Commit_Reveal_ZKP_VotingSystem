🗳️ Project 15 – Garuda Commit-Reveal Voting System
A secure and tamper-resistant voting system built using the Commit-Reveal cryptographic technique. This system ensures that no vote is revealed until all commitments are locked in, providing fairness and integrity during digital elections.

📌 Features
🔒 Commit Phase: Voters commit to a vote using a secure cryptographic hash (SHA3-256) with a secret nonce.

🔓 Reveal Phase: Voters reveal their vote along with the nonce, which is verified against the commitment.

📊 Tally Phase: Only successfully revealed and verified votes are counted.

🚫 Ensures vote privacy, non-repudiation, and protects against vote tampering.

🛠️ Technologies & Libraries Used
Python 3.10+

hashlib – for SHA3-256 hashing

secrets – to generate secure nonces

json & os – for vote storage and file handling

🔧 How It Works
✅ Commit Phase (commit_vote.py)
Voter inputs their name and casts a vote (0 for Alice, 1 for Bob).

A random nonce is generated.

The system computes commitment = SHA3-256(vote + nonce) and saves it to votes.json.

Voter is instructed to save the nonce for reveal phase.

🔍 Reveal Phase (reveal_vote.py)
Voter enters their name, vote, and saved nonce.

System verifies the hash matches the earlier commitment.

If verified, the vote is marked as revealed.

📈 Tally Phase (tally_votes.py)
Reads all revealed votes and counts them.

Tampered or unrevealed votes are ignored.
👨‍🏫 Real-World Application: University-Level Secure Elections
This project is designed to be easily extendable into real university elections. Here's how:

🧑‍🎓 Each registered student will receive a secure nonce ahead of time.

✅ Only students with valid nonces can cast a vote (to prevent impersonation).

🖥️ Simple UI (Tkinter or Flask) will be implemented in future versions for a better user experience.

🔐 Ensures that voter identity and vote are both protected and verified without revealing the actual vote prematurely.

🔮 Future Enhancements
🌐 Web-based UI (Flask/Django)

🔑 Public/Private key-based voter authorization

🗃️ Database integration instead of flat files

📬 Email/SMS nonce distribution system

📲 Mobile support for student elections

⚠️ Notes
Voter names and candidate names must not be the same.

Voters must save their nonce after the commit phase for successful verification.

This system assumes a trusted setup for voter registration and nonce distribution.
