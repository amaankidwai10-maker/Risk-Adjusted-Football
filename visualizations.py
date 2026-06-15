import random
import matplotlib.pyplot as plt

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
    if random.random() < prob_a_wins:
        return team_a
    else:
        return team_b

def run_tournament():
    sf1 = play_game("Argentina", "Netherlands")
    sf2 = play_game("Brazil", "Germany")
    sf3 = play_game("France", "England")
    sf4 = play_game("Spain", "Portugal")
    f1 = play_game(sf1, sf2)
    f2 = play_game(sf3, sf4)
    champion = play_game(f1, f2)
    return champion

win_counts = {team: 0 for team in teams}
iterations = 1000000

print(f"Running {iterations} simulations...\n")
for _ in range(iterations):
    winner = run_tournament()
    win_counts[winner] += 1

sorted_results = sorted(win_counts.items(), key=lambda x: x[1], reverse=True)
teams_list = [team for team, _ in sorted_results]
probabilities = [(wins/iterations)*100 for _, wins in sorted_results]

# Chart 1 - Vertical Bar Chart
plt.figure(figsize=(12, 6))
colors = ['gold' if i == 0 else 'steelblue' for i in range(len(teams_list))]
bars = plt.bar(teams_list, probabilities, color=colors, edgecolor='black', linewidth=0.5)

for bar, prob in zip(bars, probabilities):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             f'{prob:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.title('World Cup Win Probabilities (1,000,000 Monte Carlo Simulations)',
          fontsize=14, fontweight='bold')
plt.xlabel('Team', fontsize=12)
plt.ylabel('Win Probability (%)', fontsize=12)
plt.tight_layout()
plt.savefig('win_probabilities.png', dpi=150)
plt.show()
print("Chart 1 saved!")

# Chart 2 - Horizontal Bar Chart
plt.figure(figsize=(10, 6))
colors_h = ['gold' if i == len(teams_list)-1 else 'steelblue' for i in range(len(teams_list))]
plt.barh(teams_list[::-1], probabilities[::-1], color=colors_h, edgecolor='black')

for i, prob in enumerate(probabilities[::-1]):
    plt.text(prob + 0.1, i, f'{prob:.1f}%', va='center', fontweight='bold')

plt.title('World Cup Win Probabilities - Risk Assessment',
          fontsize=14, fontweight='bold')
plt.xlabel('Win Probability (%)', fontsize=12)
plt.tight_layout()
plt.savefig('risk_assessment.png', dpi=150)
plt.show()
print("Chart 2 saved!")

# Chart 3 - Pie Chart
plt.figure(figsize=(10, 6))
colors_pie = ['gold', 'silver', '#CD7F32', 'steelblue', 'coral', 'green', 'purple', 'orange']
plt.pie(probabilities, labels=teams_list, autopct='%1.1f%%',
        colors=colors_pie, startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})

plt.title('Tournament Win Probability Distribution\n(1,000,000 Simulations)',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('probability_distribution.png', dpi=150)
plt.show()
print("Chart 3 saved!")
print("\nAll charts saved successfully!")