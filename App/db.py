import csv
import os

# Define the CSV file path for storing ratings
ratings_file = 'user_ratings.csv'

# Function to save user ratings to the CSV file
def save_user_rating(query, rating):
    # Check if the file exists
    file_exists = os.path.isfile(ratings_file)
    
    # Open the file in append mode
    with open(ratings_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writerow(["Query", "Rating"])
        # Write the query and rating
        writer.writerow([query, rating])

# Function to retrieve all user ratings from the CSV file
def get_all_ratings():
    ratings = []
    if os.path.isfile(ratings_file):
        # Read the file
        with open(ratings_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            # Skip the header
            next(reader, None)
            # Read each row
            for row in reader:
                ratings.append(row)
    return ratings

# Example usage:
# save_user_rating("What are the nutritional benefits of kale?", 5)
# all_ratings = get_all_ratings()
# print(all_ratings)
