import json
import random
import time
import sys

# Constants
LEADERBOARD = "leaderboard.json"
WORDLIST = "wordlist.json"

def update_leaderboard(username, wpm):
    leaderboard = load_leaderboard()

    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)

    with open(LEADERBOARD, 'w') as f:
        json.dump(leaderboard, f)

def show_leaderboard():
    leaderboard = load_leaderboard()

    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        print("Leaderboard:")
        for idx, entry in enumerate(leaderboard, start=1):
            print(f"{idx}. {entry['username']} - {entry['wpm']} WPM")

def load_leaderboard():
    try:
        with open(LEADERBOARD, 'r') as f:
            leaderboard = json.load(f)
        return leaderboard
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_words_from_json():
    try:
        with open(WORDLIST, 'r') as f:
            words = json.load(f)
        return words
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_user_input(prompt=""):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        return None

def main():
    words = load_words_from_json()

    if not words:
        print("Wordlist is empty. Please provide a valid wordlist.")
        return

    username = input("Enter your username: ")
    while True:
        print("\n1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            random.shuffle(words)
            start_time = time.time()
            words_typed = 0
            wrong_typed = 0

            for word in words:
                print(f"Type the word: {word}")
                user_input = get_user_input("Your input: ")

                if user_input is None:
                    break

                if user_input == word:
                    words_typed += 1
                else:
                    wrong_typed+=1
                    print("Incorrect! Try again.\n")

            end_time = time.time()
            elapsed_time = end_time - start_time
            wpm = int((words_typed / elapsed_time) * 60) if elapsed_time > 0 else 0

            print("\nTyping Test Results:")
            print(f"Words Typed: {words_typed}")
            print(f"Wrong Words Typed: {wrong_typed}")
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm} WPM")

            update_leaderboard(username, wpm)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("Exiting the Typing Master.")
            sys.exit(0)

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
