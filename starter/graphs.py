############################# TO DO #####################################

# write import statement for psycopg2

# write import statement to import Error from psycopg2

# import the get_connected function from your database.py file

# import matplotlib.pyplot as plt


try:
    # connection to database
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

############################# TO DO #####################################

##### create product_revenue_query with the query from parts 3 and 4 which get the total revenue from each product category

#### follow the project directions to create a function called get_revenue which fetches the results from the product_revenue_query

#### create a variable called product_revenue and set it equal to the get_revenue function invoked 

#### print the product_revenue variable to look at the structure of the variable to help you write the next function

#### write a function which loops through the product_revenue variable and creates two lists - one with product categories and one with total revenue values

#### follow the project directions to create a function which makes a bar chart in matplotlib using the total revenue from each product category

#### invoke the create_bar_chart function

#### use plt.show() to show a pop-up of the bar chart you created

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")