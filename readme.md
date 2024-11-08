# Homework Assignment: Trading Strategy and Energy Maze

## Overview

This Python project consists of two main tasks:

1. **Task 1: Trading Strategy** - Implements a trading strategy based on historical stock price data using Python and Numpy. The strategy generates buy/sell signals based on price trends, calculates positions, and visualizes cumulative Profit & Loss (P&L) over time.
2. **Task 2: Energy Maze** - Solves an energy optimization problem where the goal is to traverse a maze with varying energy values, ensuring that the total energy never drops below 1. The function calculates the minimum initial energy required to complete the traversal and supports both predefined and user-defined maze inputs.

## Project Structure

```
├── HW4.py                 # Main Python script for Task 1 and Task 2
├── aapl.csv               # Sample input data for Task 1 (historical stock prices)
├── test_data.csv          # Test input data for unit tests of Task 1
├── trading_results.csv    # Output file for Task 1 results
└── README.md              # This README file
```

## Requirements

- Python 3.7 or higher
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `unittest`

You can install the required libraries using:

```bash
pip install numpy pandas matplotlib
```

## Task 1: Trading Strategy

### Problem Description

Task 1 involves implementing a trading strategy using historical stock prices. The strategy is defined as follows:

1. **Buy Signal**: If the stock price increases for three consecutive days and the current position is less than twice the number of shares per trade, buy 10 shares.
2. **Sell Signal**: If the stock price decreases for two consecutive days and shares are held, sell all shares.
3. **End of Period**: On the last day, if shares are held, sell all shares.

### Input

- A CSV file (`aapl.csv`) containing historical stock prices with the following columns:
  - `Date`: The date of the price record.
  - `Close`: The closing price of the stock.

### Output

- A CSV file (`trading_results.csv`) containing:
  - `Date`: The date of each record.
  - `Signal`: The generated trading signal (1 = Buy, -1 = Sell, 0 = Hold).
  - `Position`: The number of shares held at the end of each day.
  - `Account Value`: The total value of the account (cash + value of held shares).

- A plot of the cumulative P&L over time.

### How to Run Task 1

To run Task 1 using the provided input data:

```bash
python HW4.py
```

Then, enter `1` when prompted to run Task 1.

The output will include:
- A printed summary of the cumulative P&L.
- A saved CSV file (`trading_results.csv`).
- A plot showing the cumulative P&L over time.

### Example Output

- Cumulative P&L: `$1377.38`
- Plot: An enhanced plot showing smoothed P&L and highlighted buy/sell signals.

### Unit Test for Task 1

The unit test for Task 1 checks:
1. Correct generation of trading signals.
2. Accurate calculation of positions over time.
3. Proper calculation of the final account value.

To run the unit test:

```bash
python HW4.py
```

Then, enter `test` when prompted.

## Task 2: Energy Maze

### Problem Description

In Task 2, you are given a maze represented as a 2D Numpy array. Each cell in the maze has an associated energy value, which can be positive (energy gain) or negative (energy loss). The objective is to find the minimum initial energy required to traverse the maze from the top-left corner to the bottom-right corner without the energy dropping below 1.

### New Feature: User-Defined Maze

In addition to using a predefined maze, Task 2 now supports arbitrary maze input from the user. The user can specify the maze dimensions and enter custom values for each cell.

### Input

- **Option 1**: Use the predefined example maze from the assignment.
- **Option 2**: Enter a custom maze when prompted by the script.

### Output

- An integer representing the minimum initial energy required to complete the maze.

### How to Run Task 2

To run Task 2 with the predefined example maze:

```bash
python HW4.py
```

Then, enter `2` when prompted to run Task 2.

To run Task 2 with a user-defined maze:

```bash
python HW4.py
```

Then, enter `3` when prompted to provide custom maze input.

### Example Run for Custom Maze

```bash
Enter '1' to run Task 1, '2' to run Task 2 with default maze, '3' to run Task 2 with custom maze, or 'test' to run unit tests: 3
Enter the number of rows (m): 3
Enter the number of columns (n): 3
Enter the maze values row by row (space-separated integers):
Row 1: 0 -2 -3
Row 2: -1 -2 -2
Row 3: -1 -1 -1
User-defined maze:
[[ 0 -2 -3]
 [-1 -2 -3]
 [-1 -1 -1]]
Minimum Initial Energy: 15
```

### Unit Test for Task 2

The unit test for Task 2 includes:
1. Validation using the example maze from the assignment.
2. Testing with a generic maze input.
3. Edge cases:
   - All positive values (minimum energy should be `1`).
   - All negative values (continuous energy loss).
   - Single cell maze (simplest scenario).

To run the unit test:

```bash
python HW4.py
```

Then, enter `test` when prompted.



## Additional Notes

- **Error Handling**: The code includes validation checks for missing files and incorrect data formats.
- **Plot Customization**: The cumulative P&L plot in Task 1 is enhanced with smoothing and markers for buy/sell signals.
- **Generic Input Support**: Task 2 handles arbitrary maze inputs, making the solution flexible for different scenarios.

## Conclusion

This project implements a comprehensive solution for both tasks as per the homework requirements. It includes robust error handling, clear output, and thorough testing using the `unittest` framework. The code is optimized for readability and performance, and the interactive terminal interface makes it user-friendly.

