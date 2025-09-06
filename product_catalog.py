from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
for p in products[:3]:
    print(p)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences=[]

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    if preference:
        customer_preferences.append(preference)
    # Add the customer preference to the list

    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)
print(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name":product["name"],
        "tags":set(product["tags"])
    })



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations =[]
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append((product["name"],matches))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations


# TODO: Step 7 - Call your function and print the results

results = recommend_products(converted_products, customer_preferences)

print("\nRecommended Products:")
for product, matches in results:
    print(f"{product} ({matches} matching tags)")

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
#For a majority of this assignment I used a lot of if statements a long with obviously a couple of loops and intersections due to the nature of the problem. This is because I needed to one, streamline my program and two, it was necessary in order to complete a few of the tasks such as the looping and the intersection of the tags in order to output a proper response. More specifically, for part 7 the loop function allowed me to run through each product and create a set for the tags instead of going through each product and running it's own line of code, which would make this program extremely inefficient. As for the if statements, the same thing applies because it allows me to easily run a function if specific situations occur. Lastly, I used the intersection operation in order to count and print the matched results to an integer. 
#If the database was a lot larger, for one I would most likely look at sorting the products within the dataset at first. Next, I would find a more efficient way for checkings tags and such due to a function checking through 1,000 products would not run too efficiently. I feel as though this basic understanding is enough for what I have and if the dataset were to drastically increase, I would do more restructuring to the data and the program so that it one, runs well and two, does not kill my computer. With all that being said. working through this assignment gave me a clear insight to how product recommendation could work on a smaller scale and I have more of an understanding as to how I could change the program around to fit a larger problem. 