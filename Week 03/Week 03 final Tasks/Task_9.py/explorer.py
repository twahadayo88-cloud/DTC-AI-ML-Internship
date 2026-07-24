import pandas as pd
import matplotlib.pyplot as plt
df = None

def menu():

    print("      CSV EXPLORER SYSTEM")

    print("1. Load CSV File")
    print("2. Display Dataset")
    print("3. Search Record")
    print("4. Filter Rows")
    print("5. Sort Data")
    print("6. Statistics")
    print("7. Charts")
    print("8. Exit")

    print("===================================")

# STEP : MAIN LOOP

while True:

    menu()

    choice = input("Enter your choice (1-8): ")


    # STEP  : LOAD CSV FILE
    
    if choice == "1":

        filename = input("Enter CSV File Name: ")

        try:

            df = pd.read_csv(filename)

            print("\nCSV File Loaded Successfully!")

            print(df.head())

        except FileNotFoundError:

            print("\nFile Not Found!")



    # STEP   DISPLAY DATASET
    
    elif choice == "2":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            print("\nDataset Preview")

            print(df.head(10))

    # STEP 7  SEARCH RECORD
    
    elif choice == "3":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            city = input("Enter City Name: ")

            result = df[df["City"].str.lower() == city.lower()]

            if result.empty:

                print("\nNo Record Found!")

            else:

                print("\nSearch Result")

                print(result)


    # STEP 8 : FILTER ROWS
    
    elif choice == "4":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            category = input("Enter Category (Furniture / Office Supplies / Technology): ")

            result = df[df["Category"].str.lower() == category.lower()]

            if result.empty:

                print("\nNo Record Found!")

            else:

                print("\nFiltered Data")

                print(result)


    # STEP 9  SORT DATA
    
    elif choice == "5":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            column = input("Enter Column Name (Sales, Profit, Quantity): ")

            result = df.sort_values(
                by=column,
                ascending=False
            )

            print("\nSorted Data")

            print(result.head(10))


#-------------------------------------------------------------------------------
    # STEP  10: STATISTICS
    
    elif choice == "6":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            print("\n DATASET STATISTICS ")

            print(df.describe())


    # STEP 11 : CHARTS
    
    elif choice == "7":

        if df is None:

            print("\nPlease Load a CSV File First!")

        else:

            print("\nCreating Bar Chart...")

            sales = df.groupby("Category")["Sales"].sum()

            plt.figure(figsize=(8,5))

            plt.bar(
                sales.index,
                sales.values
            )

            plt.title("Sales by Category")

            plt.xlabel("Category")

            plt.ylabel("Total Sales")

            plt.grid(True)

            plt.show()


    # STEP 12 : EXIT & INVALID CHOICE
   
    elif choice == "8":

        print("\nThank You for Using CSV Explorer!")
        print("Program Closed Successfully.")
        break

    else:

        print("\nInvalid Choice!")
        print("Please Enter a Number Between 1 and 8.")