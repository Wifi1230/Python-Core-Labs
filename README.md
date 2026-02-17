This repository documents my journey in mastering Python's backend capabilities. It contains a collection of CLI (Command Line Interface) tools that solve specific engineering problems—from data security (encryption) to state management in game logic.

📂 Project Showcase

🎰 01. Casino
A multi-game platform featuring Blackjack and Dice, designed with a focus on code modularity.
Key Tech: modular programming (`import` modules), global state management, game loop logic.
Highlight: The project is split into separate logic files (`blackjack.py`, `diceroll.py`) controlled by a main interface, ensuring code maintainability.

🔐 02. File Encryption Tool
A security utility that encrypts and decrypts text data using custom substitution ciphers.
Key Tech: File I/O (`read`/`write` operations), string manipulation, randomization algorithms.
Highlight: Demonstrates the ability to interact with the OS file system to persist encrypted data locally.

🛒 03. Shopping Cart Manager
A Point-of-Sale simulation managing product stock, pricing, and user carts.
Key Tech: Nested Dictionaries, Exception Handling (`try-except`), dynamic data formatting.
Highlight: Handles complex edge cases (e.g., negative input, stock depletion) to ensure data integrity during transactions.

🏦 04. Banking App
A logic-focused financial application handling deposits and withdrawals.
Key Tech: Input validation, f-string formatting, float precision handling.
Highlight: Prevents logical errors (like overdrafts) through rigorous conditional checks.

 🧠 05. Knowledge Quiz
A dynamic testing tool utilizing Python's collection framework.
Key Tech: `random` library sampling, list of dictionaries structure.
