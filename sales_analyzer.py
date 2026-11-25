
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class SalesDataAnalyzer:

    # 1. Constructor
    def __init__(self):
        self.data = pd.DataFrame()
        print("Sales Data Analyzer Initialized!")

    # 2. Destructor
    def __del__(self):
        print("Sales Data Analyzer Closed!")

    # 3. Load CSV Data
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("\nDataset loaded successfully!")
            print(self.data)

        except FileNotFoundError:
            print("File not found! Please enter a valid path.")

        except Exception as e:
            print("Error:", e)

    # Check whether data is loaded
    def check_data(self):
        if self.data.empty:
            print("Please load the dataset first!")
            return False
        return True

    # 4. Explore Data
    def explore_data(self):
        if not self.check_data():
            return

        print("\n1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Column names")
        print("4. Data types")
        print("5. Basic information")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data.head())

        elif choice == "2":
            print(self.data.tail())

        elif choice == "3":
            print(self.data.columns)

        elif choice == "4":
            print(self.data.dtypes)

        elif choice == "5":
            self.data.info()

        else:
            print("Invalid choice!")

    # 5. Clean Data
    def clean_data(self):
        if not self.check_data():
            return

        print("\n1. Display missing values")
        print("2. Fill missing values with mean")
        print("3. Drop missing rows")
        print("4. Replace missing values")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data.isnull().sum())

        elif choice == "2":
            for col in self.data.select_dtypes(include=np.number).columns:
                self.data[col] = self.data[col].fillna(
                    self.data[col].mean()
                )
            print("Missing numerical values filled with mean.")

        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Missing rows removed.")

        elif choice == "4":
            value = input("Enter replacement value: ")
            self.data.fillna(value, inplace=True)
            print("Missing values replaced.")

        else:
            print("Invalid choice!")

    # 6. Mathematical Operations
    def mathematical_operations(self):
        if not self.check_data():
            return

        print("\nNumerical columns:")
        print(self.data.select_dtypes(include=np.number).columns)

        col = input("Enter column name: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        if not pd.api.types.is_numeric_dtype(self.data[col]):
            print("Please select a numerical column!")
            return

        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice: ")

        try:
            num = float(input("Enter number: "))

            if choice == "1":
                self.data[col] = self.data[col] + num

            elif choice == "2":
                self.data[col] = self.data[col] - num

            elif choice == "3":
                self.data[col] = self.data[col] * num

            elif choice == "4":
                if num == 0:
                    print("Cannot divide by zero!")
                    return
                self.data[col] = self.data[col] / num

            else:
                print("Invalid choice!")
                return

            print("Operation completed!")
            print(self.data.head())

        except ValueError:
            print("Please enter a valid number!")

    # 7. Combine DataFrames
    def combine_data(self, other_dataframe):
        if not self.check_data():
            return

        self.data = pd.concat(
            [self.data, other_dataframe],
            ignore_index=True
        )

        print("DataFrames combined successfully!")
        print(self.data)

    # 8. Split DataFrame
    def split_data(self):
        if not self.check_data():
            return

        col = input("Enter column name for splitting: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        for value, group in self.data.groupby(col):
            print("\nGroup:", value)
            print(group)

    # 9. Search, Sort and Filter
    def search_sort_filter(self):
        if not self.check_data():
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter choice: ")

        if choice == "1":
            col = input("Enter column name: ")

            if col not in self.data.columns:
                print("Column not found!")
                return

            value = input("Enter search value: ")

            result = self.data[
                self.data[col].astype(str).str.contains(
                    value, case=False, na=False
                )
            ]

            print(result)

        elif choice == "2":
            col = input("Enter column name: ")

            if col not in self.data.columns:
                print("Column not found!")
                return

            self.data.sort_values(
                by=col, inplace=True
            )

            print(self.data)

        elif choice == "3":
            col = input("Enter column name: ")

            if col not in self.data.columns:
                print("Column not found!")
                return

            value = input("Enter value to filter: ")

            result = self.data[
                self.data[col].astype(str) == value
            ]

            print(result)

        else:
            print("Invalid choice!")

    # 10. Aggregate Functions
    def aggregate_functions(self):
        if not self.check_data():
            return

        col = input("Enter numerical column name: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        if not pd.api.types.is_numeric_dtype(self.data[col]):
            print("Please select a numerical column!")
            return

        print("Sum:", self.data[col].sum())
        print("Mean:", self.data[col].mean())
        print("Count:", self.data[col].count())
        print("Maximum:", self.data[col].max())
        print("Minimum:", self.data[col].min())

    # 11. Statistical Analysis
    def statistical_analysis(self):
        if not self.check_data():
            return

        print("\nDescriptive Statistics:")
        print(self.data.describe())

        print("\nStandard Deviation:")
        print(self.data.std(numeric_only=True))

        print("\nVariance:")
        print(self.data.var(numeric_only=True))

        print("\n25%, 50%, 75% Quantiles:")
        print(self.data.quantile(
            [0.25, 0.50, 0.75],
            numeric_only=True
        ))

    # 12. Pivot Table
    def create_pivot_table(self):
        if not self.check_data():
            return

        print("Available columns:")
        print(self.data.columns)

        index_col = input("Enter index column: ")
        value_col = input("Enter value column: ")

        if index_col not in self.data.columns or value_col not in self.data.columns:
            print("Invalid column name!")
            return

        if not pd.api.types.is_numeric_dtype(self.data[value_col]):
            print("Value column must be numerical!")
            return

        pivot = pd.pivot_table(
            self.data,
            index=index_col,
            values=value_col,
            aggfunc="sum"
        )

        print("\nPivot Table:")
        print(pivot)

    # 13. NumPy Array Operations
    def numpy_operations(self):
        if not self.check_data():
            return

        col = input("Enter numerical column name: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        if not pd.api.types.is_numeric_dtype(self.data[col]):
            print("Please select a numerical column!")
            return

        arr = self.data[col].dropna().to_numpy()

        print("\nNumPy Array:")
        print(arr)

        print("\nFirst element:")
        print(arr[0] if len(arr) > 0 else "Array is empty")

        print("\nArray slicing:")
        print(arr[0:3])

        print("\nAddition:")
        print(arr + 10)

        print("\nMultiplication:")
        print(arr * 2)

        print("\nSum:", np.sum(arr))
        print("Mean:", np.mean(arr))
        print("Standard Deviation:", np.std(arr))
        print("Variance:", np.var(arr))

    # 14. Data Visualization
    def visualize_data(self):
        if not self.check_data():
            return

        print("\n1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap")
        print("8. Box Plot")

        choice = input("Enter your choice: ")

        numeric_cols = self.data.select_dtypes(
            include=np.number
        ).columns.tolist()

        if choice == "4":
            col = input("Enter category column: ")

            if col not in self.data.columns:
                print("Column not found!")
                return

            values = self.data[col].value_counts()

            values.plot(
                kind="pie",
                autopct="%1.1f%%"
            )

            plt.title("Sales Pie Chart")
            plt.ylabel("")
            plt.show()
            return

        if choice == "7":
            sns.heatmap(
                self.data[numeric_cols].corr(),
                annot=True,
                cmap="coolwarm"
            )

            plt.title("Sales Data Heatmap")
            plt.show()
            return

        if choice == "8":
            col = input("Enter numerical column: ")

            if col not in numeric_cols:
                print("Invalid numerical column!")
                return

            sns.boxplot(x=self.data[col])
            plt.title("Sales Box Plot")
            plt.show()
            return

        if choice == "6":
            if len(numeric_cols) < 2:
                print("At least two numerical columns required!")
                return

            plt.stackplot(
                range(len(self.data)),
                *[
                    self.data[c].fillna(0).to_numpy()
                    for c in numeric_cols[:3]
                ],
                labels=numeric_cols[:3]
            )

            plt.title("Sales Stack Plot")
            plt.legend()
            plt.show()
            return

        if choice in ["1", "2", "3"]:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            if x not in self.data.columns or y not in self.data.columns:
                print("Invalid column name!")
                return

            if choice == "1":
                self.data.plot(
                    x=x, y=y, kind="bar"
                )
                plt.title("Sales Bar Plot")

            elif choice == "2":
                self.data.plot(
                    x=x, y=y, kind="line"
                )
                plt.title("Sales Line Plot")

            elif choice == "3":
                self.data.plot(
                    x=x, y=y, kind="scatter"
                )
                plt.title("Sales Scatter Plot")

            else:
                return

            plt.xlabel(x)
            plt.ylabel(y)
            plt.tight_layout()
            plt.show()

        elif choice == "5":
            col = input("Enter numerical column: ")

            if col not in numeric_cols:
                print("Invalid numerical column!")
                return

            plt.hist(self.data[col].dropna(), bins=10)
            plt.title("Sales Histogram")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()

        else:
            print("Invalid choice!")

    # 15. Save Visualization
    def save_visualization(self):
        if not self.check_data():
            return

        col = input("Enter numerical column for graph: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        if not pd.api.types.is_numeric_dtype(self.data[col]):
            print("Please select a numerical column!")
            return

        plt.figure()
        plt.plot(self.data[col])
        plt.title("Sales Visualization")
        plt.xlabel("Index")
        plt.ylabel(col)

        filename = input(
            "Enter file name (e.g. sales.png): "
        )

        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            print("Please use a PNG or JPEG filename!")
            plt.close()
            return

        plt.savefig(filename)
        plt.close()

        print("Visualization saved successfully!")


# ======================================
# MAIN PROGRAM - MENU DRIVEN INTERFACE
# ======================================

obj = SalesDataAnalyzer()

while True:

    print("\n========== SALES DATA ANALYZER ==========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform Mathematical Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Combine DataFrames")
    print("9. Split DataFrame")
    print("10. Search, Sort and Filter")
    print("11. Aggregate Functions")
    print("12. Create Pivot Table")
    print("13. NumPy Operations")
    print("14. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        path = input("Enter CSV file path: ")
        obj.load_data(path)

    elif choice == "2":
        obj.explore_data()

    elif choice == "3":
        obj.mathematical_operations()

    elif choice == "4":
        obj.clean_data()

    elif choice == "5":
        obj.statistical_analysis()

    elif choice == "6":
        obj.visualize_data()

    elif choice == "7":
        obj.save_visualization()

    elif choice == "8":
        if obj.check_data():
            path = input("Enter second CSV file path: ")
            try:
                other = pd.read_csv(path)
                obj.combine_data(other)
            except Exception as e:
                print("Error:", e)

    elif choice == "9":
        obj.split_data()

    elif choice == "10":
        obj.search_sort_filter()

    elif choice == "11":
        obj.aggregate_functions()

    elif choice == "12":
        obj.create_pivot_table()

    elif choice == "13":
        obj.numpy_operations()

    elif choice == "14":
        print("Thank you for using Sales Data Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")

