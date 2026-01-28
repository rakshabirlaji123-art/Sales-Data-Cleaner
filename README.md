# Sales Data Cleaner - ETL Pipeline

## 1. Project Title & Goal
A Python ETL (Extract, Transform, Load) pipeline that processes messy CSV sales data, performs data cleaning, removes duplicates, converts USD to INR, and exports clean JSON data for further analysis.

## 2. Setup Instructions
1. Make sure Python 3 is installed on your system.
2. Place sales.csv and main.py in the same folder.
3. Open terminal in the project folder.
4. Run the script using the command:
   py main.py

## 3. The Logic (How you thought)

**Why this approach?**

- Used Python's built-in file handling with `open()` and `json.dump()` for simplicity
- Implemented deduplication using Python `set()` with tuple keys for efficient duplicate detection
- Kept the code minimal with no external dependencies for easy execution
- Used `indent=4` in JSON output for human-readable formatting

**Hardest Bug & Solution:**

**Bug:** Initially faced indentation errors because Python requires consistent indentation.The `for` loop and `if` statements needed proper tabs/spaces.

**Solution:** Fixed indentation and structured the code properly with consistent 4-space indentation throughout.

**Additional Implementation Details:**
1. **CSV Parsing:** Used simple `line.split(",")` instead of `csv` module for lightweight processing
2. **Data Cleaning:** Applied `strip()` and `replace()` methods for basic cleaning
3. **Deduplication:** Created unique keys using `(product_name, price_USD)` tuple combination
4. **JSON Output:** Used `indent=4` parameter for pretty-printing JSON file
5. **User Feedback:** Added `print()` statement to confirm successful execution

## 4. Output Screenshots

### Terminal Execution
![Terminal Output](Terminal_Output.png)

### Generated JSON File
![JSON Output](JSON_Output.png)

## 5. Future Improvements
If I had 2 more days, I would:

1. **Error Handling:** Add try-except blocks for file operations and data conversion.
2. **Input Validation:** Check if `sales.csv` exists and has correct format before processing.
3. **Command Line Interface:** Add support for command-line arguments for input/output file paths.
4. **Enhanced Cleaning:** Handle edge cases like missing values, extra columns, or malformed data.
5. **Progress Indicator:** Add a progress bar or counter for large CSV files.
6. **Configuration:** Make USD to INR conversion rate configurable via command line or config file.
7. **Logging:** Implement logging to track processing steps and errors.
