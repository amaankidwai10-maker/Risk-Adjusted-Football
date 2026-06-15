import random
teams = {
    "Argentina": 1850,
    "France": 1840,
    "Brazil": 1820,
    "Spain": 1810,
    "England": 1800,
    "Portugal": 1790,
    "Germany": 1780,
    "Netherlands": 1770
}

def get_win_probability(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def play_game(team_a, team_b):
    prob_a_wins = get_win_probability(teams[team_a], teams[team_b])
    
    # Roll a virtual dice between 0.0 and 1.0 to account for volatility
    if random.random() < prob_a_wins:
        return team_a
    else:
        return team_b


def run_tournament():
    # Quarterfinals
    sf1 = play_game("Argentina", "Netherlands")
    sf2 = play_game("Brazil", "Germany")
    sf3 = play_game("France", "England")
    sf4 = play_game("Spain", "Portugal")
    
    # Semifinals
    f1 = play_game(sf1, sf2)
    f2 = play_game(sf3, sf4)
    
    # Final
    champion = play_game(f1, f2)
    return champion

if __name__ == "__main__":
    win_counts = {team: 0 for team in teams}
    iterations = 1000000

    print(f"Running {iterations} simulations...\n")

    for _ in range(iterations):
        winner = run_tournament()
        win_counts[winner] += 1

    print("--- TOURNAMENT WIN PROBABILITIES ---")
    
    # Sorting teams by highest win count
    sorted_results = sorted(win_counts.items(), key=lambda x: x[1], reverse=True)
    
    for team, wins in sorted_results:
        win_percent = (wins / iterations) * 100
        print(f"{team:<12}: {win_percent:>4.1f}%")