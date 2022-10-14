############################# TO DO #####################################

# write import statement for psycopg2
import psycopg2
# write import statement to import Error from psycopg2
from psycopg2 import Error
# import the get_connected function from your database.py file
from database import get_connected
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

try:
    # connection to database
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

############################# TO DO #####################################

##### create product_revenue_query with the query from parts 3 and 4 which get the total revenue from each product category
    product_revenue_query = """ SELECT product_category, SUM(unit_price*quantity)
                                FROM invoices
                                GROUP BY product_category
                                ORDER BY SUM DESC """


#### follow the project directions to create a function called get_revenue which fetches the results from the product_revenue_query
    def get_revenue():
        with connection:
            with cursor:
                cursor.execute(product_revenue_query)
                return cursor.fetchall()

#### create a variable called product_revenue and set it equal to the get_revenue function invoked 
#### print the product_revenue variable to look at the structure of the variable to help you write the next function
    product_revenue = get_revenue()
    print(product_revenue)

#### write a function which loops through the product_revenue variable and creates two lists - one with product categories and one with total revenue values
    # for revenue in product_revenue:  # Ask for help about how to do this as a for loop

    product_categories = []
    total_revenue = []
    count = 0
    index = 0

    while count < (len(product_revenue)):

        product_categories.append(product_revenue[index][0])
        total_revenue.append(int(product_revenue[index][1]))

        count += 1
        index += 1

#### follow the project directions to create a function which makes a bar chart in matplotlib using the total revenue from each product category
    def create_bar_chart():
        figure = plt.figure()
        data = total_revenue
        labels = product_categories

        plt.xticks(range(len(labels)), labels, rotation=85)

        plt.title('Product Revenue by Category')
        plt.xlabel('Product Category')
        plt.ylabel('Revenue(USD)')

        new_colors = ['#5B3445', '#683C4F', '#754358', '#824A61', '#8E526B', '#9B5975', '#A6647F', '#AD718A', '#B57D94', '#BC8A9F', '#C397AA', '#CBA4B5', '#D2B1C0', '#DABECB', '#E1CBD5', '#E9D8E0']

        plt.bar(labels, data, color=new_colors)

        return figure


#### invoke the create_bar_chart function
    create_bar_chart()

#### use plt.show() to show a pop-up of the bar chart you created
    plt.show()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")