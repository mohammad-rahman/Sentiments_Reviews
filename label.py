from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Will take in a list of string reviews, pass this list to the open ai API. Eventually, it will
    return the output of a list of sentiments. It will also convey a mesasage if there is
    a wromg input. 
    
        Parameter:
            text (list): string reviews

        Returns:
            list: sentiments
    """

    #Messages if there is a wrong input". 

    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be an array of strings."
   
    if not text:
        return "Wrong input. text must be an array of strings."

 
    #This is an object

    client = OpenAI()

    
    #These are prompts given to open ai

    system_prompt = """"You are good at automatically labeling sentiments from the provided data \n
    (reviews by clients). 
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}

    """

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role" : "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
    ]
    )

    raw_output = response.choices[0].message.content

    output_list = []
    
    #Data cleaning and getting the output
    
    for line in raw_output.splitlines():
        clean_output = line.strip()

        if clean_output:
            output_list.append(clean_output.lower())

    print(output_list)

    return output_list