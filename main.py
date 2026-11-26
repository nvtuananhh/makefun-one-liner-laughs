ENTRY = "I'm your password — 'Password123!' — and after 47 breaches you still blame the hackers, not the genius who picked me."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
