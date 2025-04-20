from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    
    if not isinstance(text, list) or not all(isinstance(item, str) for item in text):
        return "Wrong input. text must be an array of strings."
    #if not isinstance(text, list) or not isinstance(str, list):
    #    return "wrong input; must be strings and texts"
    if not text:
        return "Wrong input. text must be an array of strings."

 

    client = OpenAI()

    system_prompt = """"You are an expert sentiment classifier. For each review:\n
    Classify each review with one of these labels: positive, neutral, negative, or irrelevant.\n
    Return only one label per line.\n
    Never Split the review into multiple lines.\n
    Do NOT include numbering, punctuation, brackets, or extra formatting.\n
    Be sensitive to emotional tone, sarcasm, irony, or context.\n
    Watch for transitions like 'but', 'however', or 'overall', as these may indicate a negative sentiment.\n
    Always base your label on the full review, not just a portion.\n
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
    
    for line in raw_output.splitlines():
        clean_output = line.strip()

        if clean_output:
            output_list.append(clean_output.lower())

    print(output_list)

    return output_list