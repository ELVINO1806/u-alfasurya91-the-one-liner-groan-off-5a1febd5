
import os

LINE = "My dad named his boat Unsinkable II. Nobody at the marina asks about the first one."
# Catatan revisi: lelucon groan-off satu baris ini bekerja karena nama kapal menyiratkan kapal pertama sudah tenggelam.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
