#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1. Read in all text files in the review directory.
2. creat dictionary from the contents of the fies with keys title, name, date, and feedback
3. use requests module to post dictionary to the specified URL.
4. Print the response from the server.

"""

import os
import json
import requests

# Test functions

def test_read_reviews(review_directory):
    #test readd_reviews funtion is properly reading and creating dictionary
    reviews = read_reviews(review_directory)
    if not reviews:
        print("No reviews found.")
    else:
        print(f"Found {len(reviews)} reviews.")
        dict = read_reviews(review_directory)
        print("Reviews read successfully.")
        print(dict)
        
# Execution funtions

def read_reviews(directory):
    reviews = []
    # Read all text files in the specified directory and append dictionart to list 'reviews'
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return reviews
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if content:
                    parts = content.split('\n', 3)
                    if len(parts) == 4:
                        review = {
                            'title': parts[0],
                            'name': parts[1],
                            'date': parts[2],
                            'feedback': parts[3]
                        }
                        reviews.append(review)
    return reviews

def post_reviews(url, reviews_dictionary):
    # Post each review dictionary to the specified URL
    for item in reviews_dictionary:
        response = requests.post(url, json=item)
        if response.status_code != 201:
            raise Exception('POST error status={}'.format(response.status_code))
        print('Created feedback ID: {}'.format(response.json()["id"]))
            

def main():
    review_directory = '/data/feedback'  # Replace with the actual path to your review directory
    url = 'http://example.com/feedback'  # Replace with the actual URL

    #Test functions: Can be commented out after testing
    #test_read_reviews(review_directory)
    
    # Read in reviews and send to post request. Return response code
    reviews = read_reviews(review_directory)
    post_reviews(url, reviews)

    

if __name__ == '__main__':
    main()  