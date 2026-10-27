# Baseball Calculator
# Name: Noah Deng
# Description: This calculator takes input for basic baseball statistics and calculates more complicated ones.
# ================================

# Your code below:
choice = input("Welcome to the baseball statistic calculator. Would you like to calculate pitching or hitting(P/H)? ")
if choice == "H" or choice == "h":
    hr = float(input("Home runs: "))
    hits = float(input("Hits: "))
    doubles = float(input("Doubles: "))
    triples = float(input("Triples: "))
    ab = float(input("At bats: "))

    print("")

    singles = hits - (hr + doubles + triples)
    avg = (hr + singles + doubles + triples)/ (ab)
    total_bases = ((singles) + (2 * doubles) + (3 * triples) + (4 * hr))
    slg = (total_bases/ab)

    print(f"Batting average: {avg:.3f}")
    print(f"Total bases: {total_bases}")
    print(f"Slugging average: {slg:.3f}")

    print("")
elif choice == "P" or choice == "p":
    w = float(input("Pitching wins: "))
    l = float(input("Pitching losses: "))
    so = float(input("Strikeouts: "))
    er = float(input("Earned runs: "))
    ip = float(input("Innings pitched (without any decimal): "))
    fraction_ip = float(input("Decimal for innings pitched: "))
    ip = ip + (fraction_ip * 0.333)
    bf = float(input("Batters faced: "))
    bb = float(input("Walks: "))

    print("")

    era = ((er / ip)*9)
    wpct = (w/(w + l))
    sopct = ((so / bf) * 100)
    so_per_bb = (so/bb)

    print(f"Earned Run Average: {era:.2f}")
    print(f"Win Percentage: {wpct:.3f}")
    print(f"Strikeout Percentage: {sopct:.1f}%")
    print(f"Strikeouts per walk: {so_per_bb:.2f}")
    
    print("")
else:
    print("Invalid option! Please run this program again.")
print("Goodbye. See you next time.")

