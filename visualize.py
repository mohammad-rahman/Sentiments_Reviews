import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    
    """
 
# This initializes counts
    counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "irrelevant": 0
    }

    # This counts manually 
    
    for sentiment in sentiments:
        sentiment = sentiment.strip().lower()
        if sentiment in counts:
            counts[sentiment] += 1
   


  # Use Counter to count occurrences of each sentiment label.
    #valid_labels = {"positive", "neutral", "negative", "irrelevant"}
    x_labels = list(counts.keys())
    y_labels = list(counts.values())
 
    plt.figure(figsize=(7,5))

    plt.bar(x_labels, y_labels, color = "#008000")
    plt.title("Sentiment Counts")
    plt.xlabel("Sentiment Category")
    plt.ylabel("Count")
    plt.tight_layout()
    

    plt.savefig("images/visualize.png")
    print(counts)
    plt.close()





