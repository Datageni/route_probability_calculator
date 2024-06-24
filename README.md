## Explanation of the Code

This Python script consists of three main classes: `Menus`, `Prob_Functions`, and `Help_Functions`. These classes facilitate user interaction, calculate transition probabilities between nodes, and provide menu display functions, respectively.

### Menus Class

The `Menus` class manages the user interaction, allowing users to input routes and calculate the probabilities of transitioning from one node to another. It has two primary methods:

- `route_menu()`: 
  - Prompts the user to enter a route as a comma-separated string.
  - Validates the input to ensure it contains only numeric characters and is within the allowed length.
  - Checks if the entered nodes are part of the predefined `main_nodes`.
  - If valid, it calls the `prob_calculator` method from the `Prob_Functions` class to compute the transition probabilities.
  - Provides an option to add more nodes to the route and recalculate probabilities.

- `main_menu()`: 
  - Displays the main menu with options for the user.
  - Calls the `route_menu` method when the user chooses to enter a route.

### Prob_Functions Class

The `Prob_Functions` class calculates the transition probabilities between nodes based on predefined routes. It includes:

- `count_times(sequence, next_num)`:
  - Counts how many times a given sequence (`sequence`) appears in the routes.
  - Counts how many times the `next_num` follows the sequence.
  - Returns these counts: `seq_count` and `next_num_count`.

- `prob_calculator(sequence)`:
  - For each node in `main_nodes`, calculates the probability that the node follows the given sequence.
  - Uses the formula:
$\left( \text{next_num} \mid \text{sequence} \right) = \frac{\text{next_num_count}}{\text{seq_count}}$
  - Prints the calculated probability.

### Help_Functions Class

The `Help_Functions` class provides utility functions for clearing the screen and displaying menus. It includes:

- `clear_screen(n=100)`: Clears the screen by printing empty lines.
- `menu(title, context, num_options, text_array, option_message="Option: ")`: Displays a menu with the given title, context, and options, and returns the selected option.

### How It Works with Mathematical Formulas

1. **Input Validation**:
   - The `route_menu()` method ensures the user input is valid and consists of nodes present in `main_nodes`.

2. **Counting Occurrences**:
   - The `count_times(sequence, next_num)` method iterates through all predefined routes to count:
     - `seq_count`: The number of times the sequence appears.
     - `next_num_count`: The number of times the `next_num` immediately follows the sequence.

3. **Calculating Probabilities**:
   - The `prob_calculator(sequence)` method uses the counts from `count_times` to compute the transition probability using:
     \[
     P(\text{{next\_num}} \mid \text{{sequence}}) = \frac{{\text{{next\_num\_count}}}}{{\text{{seq\_count}}}}
     \]
   - If `seq_count` is 0, the probability is set to 0 to avoid division by zero.
   - The method prints the calculated probability for each node in `main_nodes`.

### Main Execution

When the script is executed:

1. An instance of the `Menus` class is created.
2. The `main_menu()` method is called, displaying the main menu.
3. The user can choose to enter a route, which triggers the `route_menu()` method.
4. The entered route is validated, and transition probabilities are calculated and displayed.

This script allows users to understand the likelihood of transitioning from a given sequence of nodes to other nodes, based on predefined routes.
