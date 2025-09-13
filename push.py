import os
import subprocess
from datetime import datetime
# Ask user for problem details
problem_title = input("Enter Problem Title: ").strip()
problem_link = input("Enter Problem Link: ").strip()
folder = input("Enter Folder (e.g., GFG/Arrays or HackerRank/Strings): ").strip()
file_name = input("Enter Solution File Name (with extension, e.g., two_sum.py): ").strip()

# Create folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

# Create README.md inside folder
readme_path = os.path.join(folder, "README.md")
with open(readme_path, "a", encoding="utf-8") as f:
    f.write(f"## {problem_title}\n")
    f.write(f"🔗 [Problem Link]({problem_link})\n")
    f.write(f"- **Solution:** `{file_name}`\n")
    f.write(f"- **Date:** {datetime.today().strftime('%d-%b-%Y')}\n\n")

# Git commands
subprocess.run(["git", "add", "."])
commit_msg = f"Added {problem_title} solution"
subprocess.run(["git", "commit", "-m", commit_msg])
subprocess.run(["git", "push"])
