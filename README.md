# cows_and_bulls
<https://en.wikipedia.org/wiki/Bulls_and_cows>
## How to Play

1. **Setup**: 
    - The code is a 4-digit number.
    - All digits in the code are unique.
    - The player has to guess the code.

2. **Input Check**:
    - The game checks if the input code is a 4-digit number.
    - All digits must be unique.

3. **Game Mechanics**:
    - For each guess, the game provides feedback in the form of "bulls" and "cows".
    - **Bulls**: The number of digits that are correct in both value and position.
    - **Cows**: The number of digits that are correct in value but not in position.

4. **Winning Condition**:
    - The game continues until the player guesses the correct code.
    - The number of guesses is recorded.

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/Siiha/cows_and_bulls
    ```

2. Navigate to the repository directory:
    ```sh
    cd cows_and_bulls
    ```

3. Run the script:
    ```sh
    python cows_and_bulls.py
    ```
