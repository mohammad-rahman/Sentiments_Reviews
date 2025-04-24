from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Will return the list of sentiments generated from the open AI API calss. 
    
        Parameters:
            filepath (str): file with data

        Returns:
            sentiments (list): generated from the Open AI API call. 
 
    """
    # open the json object
    with open(filepath, 'r') as file:
        file_data=json.load(file)


    # extract the reviews from the json file
    reviews=file_data.get("results", [])

    # get a list of sentiments for each line using get_sentiment
    list = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(list)

    # return sentiments
    return list


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
