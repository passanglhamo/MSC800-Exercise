import pandas as pd

def main():
    file_name = "junk.txt"

    # 1. Calculate total number of lines
    with open(file_name, "r", encoding="utf-8") as file:
        total_lines = sum(1 for line in file)

    print("Total number of lines:", total_lines)

    # 2. Add a new line at the end of the file containing exactly: `text file nanalyssis`
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("\ntext file nanalyssis")


    # 3. Read the updated file and convert all text to lowercase
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read().lower()

    # 4. Save the processed file
    with open("processed_junk.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Processed file saved as processed_junk.txt")

if __name__ == "__main__":
    main()