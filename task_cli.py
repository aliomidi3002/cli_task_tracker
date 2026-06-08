import sys
import json
import os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        print("add command recognized")
    elif command == "update":
        print("update command recognized")
    elif command == "delete":
        print("delete command recognized")
    elif command == "mark-in-progress":
        print("mark-in-progress command recognized")
    elif command == "mark-done":
        print("mark-done command recognized")
    elif command == "list":
        print("list command recognized")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()