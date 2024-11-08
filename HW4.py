import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import unittest

# -----------------------------
# Task 1: Trading Strategy
# -----------------------------

def trading_strategy(file_name):
    """
    Implements a trading strategy based on consecutive stock price movements.

    Parameters:
    file_name (str): The name of the CSV file containing historical stock prices.
                     The file must contain 'Date' and 'Close' columns.

    Returns:
    pandas.DataFrame: A DataFrame with Date, Signal, Position, and Account Value columns.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")
    
    data = pd.read_csv(file_name)

    if 'Date' not in data.columns or 'Close' not in data.columns:
        raise ValueError("CSV file must contain 'Date' and 'Close' columns.")

    dates = data['Date']
    prices = data['Close'].values
    n = len(prices)

    initial_cash = 10000
    shares_per_trade = 10

    signals = np.zeros(n, dtype=int)
    positions = np.zeros(n, dtype=int)
    account_values = np.zeros(n)

    cash = initial_cash
    shares = 0

    for i in range(n):
        if i >= 3 and prices[i-3] < prices[i-2] < prices[i-1] < prices[i] and shares < 2 * shares_per_trade:
            signals[i] = 1
            shares += shares_per_trade
            cash -= prices[i] * shares_per_trade
        elif i >= 2 and prices[i-2] > prices[i-1] > prices[i] and shares > 0:
            signals[i] = -1
            cash += prices[i] * shares
            shares = 0
        elif i == n - 1 and shares > 0:
            signals[i] = -1
            cash += prices[i] * shares
            shares = 0

        positions[i] = shares
        account_values[i] = cash + shares * prices[i]

    final_pnl = account_values[-1] - initial_cash
    print(f"Cumulative Trading Profit/Loss: ${final_pnl:.2f}")

    results = pd.DataFrame({
        'Date': dates,
        'Signal': signals,
        'Position': positions,
        'Account Value': account_values
    })
    results.to_csv("trading_results.csv", index=False)
    print("Results saved to 'trading_results.csv'")

    # Step 6: Enhanced Plot for Cumulative P&L
    plt.figure(figsize=(14, 8))

    # Calculate the smoothed P&L using a rolling mean
    smoothed_pnl = pd.Series(account_values - initial_cash).rolling(window=5, min_periods=1).mean()

    # Plot the smoothed cumulative P&L
    plt.plot(dates, smoothed_pnl, label="Smoothed Cumulative P&L", color="blue", linewidth=2)

    # Highlight buy (green triangle) and sell (red inverted triangle) signals
    buy_signals = np.where(signals == 1)[0]
    sell_signals = np.where(signals == -1)[0]

    plt.scatter(dates[buy_signals], smoothed_pnl.iloc[buy_signals], color='green', marker='^', s=100, label='Buy Signal')
    plt.scatter(dates[sell_signals], smoothed_pnl.iloc[sell_signals], color='red', marker='v', s=100, label='Sell Signal')

    # Formatting the plot
    plt.xlabel("Date")
    plt.ylabel("Cumulative P&L ($)")
    plt.title("Enhanced Cumulative Profit & Loss Over Time")
    plt.legend()
    plt.grid(True)

    # Improve x-axis date formatting
    plt.xticks(dates[::len(dates) // 10], rotation=45)

    # Add tight layout for better spacing
    plt.tight_layout()
    plt.show()

    return results

# -----------------------------
# Task 2: Energy Maze
# -----------------------------

def min_initial_energy(maze):
    m, n = maze.shape
    dp = np.full((m, n), np.inf)
    dp[-1, -1] = max(1, 1 - maze[-1, -1])

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i < m - 1:
                dp[i, j] = min(dp[i, j], max(1, dp[i+1, j] - maze[i, j]))
            if j < n - 1:
                dp[i, j] = min(dp[i, j], max(1, dp[i, j+1] - maze[i, j]))

    initial_energy = max(1, dp[0, 0])
    cumulative_loss = 1 - np.sum(maze)
    if cumulative_loss > initial_energy:
        initial_energy = cumulative_loss

    return int(initial_energy)

def get_user_maze():
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))

    maze = []
    print("Enter the maze values row by row (space-separated integers):")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError(f"Each row must have exactly {n} elements.")
        maze.append(row)

    return np.array(maze)

# -----------------------------
# Unit Tests
# -----------------------------

class TestHomeworkTasks(unittest.TestCase):
    def setUp(self):
        self.example_prices = [98, 100, 102, 104, 103, 101, 99, 100, 102, 104, 106, 107, 105]
        self.expected_signals = [0, 0, 0, 1, 0, -1, 0, 0, 0, 1, 1, 0, -1]
        self.expected_positions = [0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 20, 20, 0]
        self.test_data = pd.DataFrame({
            'Date': [f"Day {i+1}" for i in range(len(self.example_prices))],
            'Close': self.example_prices
        })
        self.test_data.to_csv("test_data.csv", index=False)

    def test_trading_strategy(self):
        results = trading_strategy("test_data.csv")
        self.assertTrue(np.array_equal(results['Signal'].values, self.expected_signals))
        self.assertTrue(np.array_equal(results['Position'].values, self.expected_positions))

    def test_min_initial_energy(self):
        maze = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        expected_energy = 7
        self.assertEqual(min_initial_energy(maze), expected_energy)

    def test_generic_maze(self):
        maze = np.array([[0, -2, -3], [-1, -2, -2], [-1, -1, -1]])
        expected_energy = 14
        self.assertEqual(min_initial_energy(maze), expected_energy)

    def test_edge_case_all_negative(self):
        maze = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
        expected_energy = 10
        self.assertEqual(min_initial_energy(maze), expected_energy)

# -----------------------------
# Main Execution
# -----------------------------

if __name__ == '__main__':
    choice = input("Enter '1' to run Task 1, '2' to run Task 2 with default maze, '3' to run Task 2 with custom maze, or 'test' to run unit tests: ")
    if choice == '1':
        trading_strategy('aapl.csv')
    elif choice == '2':
        maze = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        print(f"Minimum Initial Energy: {min_initial_energy(maze)}")
    elif choice == '3':
        user_maze = get_user_maze()
        print("User-defined maze:")
        print(user_maze)
        print(f"Minimum Initial Energy: {min_initial_energy(user_maze)}")
    elif choice == 'test':
        unittest.main(argv=[''], exit=False)