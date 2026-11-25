# 📊 Pandas Analyzer & Data Visualization

## 📌 Project Overview

The **Pandas Analyzer & Data Visualization** project is a Python-based Sales Data Analysis tool developed using Object-Oriented Programming (OOP).

This project allows users to load sales datasets in CSV format, explore data, clean missing values, perform mathematical and statistical operations, and generate different visualizations.

The project uses Pandas for data manipulation, NumPy for numerical calculations, Matplotlib and Seaborn for data visualization.

🎥 Project Demonstration Video

I have also recorded a video explaining the project, its functionalities, implementation and working process.

Watch the Project Explanation Video:

▶️ Click here to watch the project demonstration

## 🎯 Objectives

- To understand and analyze sales datasets.
- To perform data cleaning and data manipulation.
- To apply mathematical and statistical operations.
- To use NumPy arrays for numerical calculations.
- To create different types of data visualizations.
- To implement Object-Oriented Programming concepts.
- To develop a menu-driven Python application.

## 🚀 Features

1. **Load Dataset**
   - Import sales data from CSV files.
   - Handle file loading errors.

2. **Explore Data**
   - Display first and last five rows.
   - Display column names and data types.
   - Display basic dataset information.

3. **Data Cleaning**
   - Identify missing values.
   - Fill missing numerical values using mean.
   - Remove rows containing missing values.
   - Replace missing values with specific values.

4. **Mathematical Operations**
   - Addition
   - Subtraction
   - Multiplication
   - Division

5. **DataFrame Operations**
   - Combine multiple DataFrames.
   - Split datasets using grouping criteria.

6. **Search, Sort and Filter**
   - Search for specific records.
   - Sort data based on selected columns.
   - Filter records according to user input.

7. **Aggregate Functions**
   - Sum
   - Mean
   - Count
   - Minimum and Maximum

8. **Statistical Analysis**
   - Mean and standard deviation.
   - Variance.
   - Percentile and quantile calculations.
   - Descriptive statistics.

9. **NumPy Operations**
   - Array conversion.
   - Indexing and slicing.
   - Mathematical calculations.
   - Numerical statistics.

10. **Data Visualization**
    - Bar Plot
    - Line Plot
    - Scatter Plot
    - Pie Chart
    - Histogram
    - Stack Plot
    - Heatmap
    - Box Plot

11. **Save Visualization**
    - Save generated graphs in PNG or JPEG format.

## 🛠️ Python Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructor (`__init__`)
- Destructor (`__del__`)
- Encapsulation
- Functions and Methods
- Conditional Statements
- While Loop
- Exception Handling
- File Handling
- Menu-Driven Programming

## 📚 Libraries Used

- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical calculations and array operations.
- **Matplotlib:** Data visualization and graph creation.
- **Seaborn:** Statistical data visualization.

## 📂 Project Structure

```text
Pandas Analyzer Project/
│
├── sales_analyzer.py
├── sales_data.csv
│
└── README.md
```

## ▶️ How to Run the Project

**Step 1:** Install Python on your system.

**Step 2:** Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn
```

**Step 3:** Keep `sales_analyzer.py` and `sales_data.csv` in the same folder.

**Step 4:** Open the project folder in VS Code.

**Step 5:** Run the Python file.

```bash
python sales_analyzer.py
```

**Step 6:** Select the required operations from the main menu.

## 💻 Sample Program Output

```text
========== SALES DATA ANALYZER ==========

1. Load Dataset
2. Explore Data
3. Perform Mathematical Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Combine DataFrames
9. Split DataFrame
10. Search, Sort and Filter
11. Aggregate Functions
12. Create Pivot Table
13. NumPy Operations
14. Exit

Enter your choice: 1

Enter CSV file path: sales_data.csv

Dataset loaded successfully!
```

## ⚠️ Input Validation Rules

- The dataset must be available in CSV format.
- Valid column names must be entered for operations.
- Numerical operations require numerical columns.
- Division by zero is not allowed.
- Invalid menu choices are handled.
- File loading errors are handled using exception handling.

## 📝 Assumptions

- The sales dataset contains columns such as SalesID, Date, Product, Region, Sales, Profit and Year.
- Numerical operations are performed on numerical columns.
- The project uses a sample sales dataset for demonstration.
- The user must load the dataset before performing analysis.

## 🔮 Future Enhancements

- Add interactive dashboards using Plotly.
- Implement advanced pivot table operations.
- Add more statistical analysis features.
- Generate automated sales reports.
- Export analysis results into Excel and PDF formats.

## 👩‍💻 Author

**Dhruvi Das**

Student | Python Programming & Data Analytics Project

## 📄 License

This project is developed for educational and learning purposes. No open-source license has been specified.

---

✨ Happy Coding! ✨
