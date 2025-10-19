def solve(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    Brute-force approach using nested loops.
    """
    if len(s) == 0:
        return 0

    max_len = 0
    for i in range(len(s)):  # Outer loop
        seen = {}
        for j in range(i, len(s)):  # Inner loop
            if s[j] in seen:
                max_len = max(max_len, j - i)
                break
            seen[s[j]] = 1
        else:
            # If inner loop completes without a break (unique till end)
            max_len = max(max_len, len(s) - i)
    return max_len


if __name__ == "__main__":
    s = input("Enter a string: ").strip()
    print("The length of the longest substring without repeating characters is:", solve(s))
