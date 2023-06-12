
import pandas as pd
import openai as ai
import time
import ssl
from tqdm import tqdm


# text-davinci-003	limit rates: 60 (Requests P/Min)	150,000 (Tokens P/Min)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        api_key = input('Enter OpenAI credentials (API key): ') 
        if api_key.upper() == 'QUIT':
            print('-- EXITING --')
            quit()
        
        ai.api_key = api_key
        
        Key_verification = ai.Completion.create(engine="text-davinci-003", prompt="Hello, world!", max_tokens=5)

        break
    
    except ai.error.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        continue

    except ai.error.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}")
        continue
    
    except ai.error.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}")
        continue
    
    except ai.error.Timeout as e:
        print(f"OpenAI API request timed out: {e}")
        continue
    
    except ai.error.InvalidRequestError as e:
        print(f"Invalid request to OpenAI API: {e}")
        continue
    
    except ai.error.AuthenticationError :
        print(f"Authentication error with OpenAI API Key: Insert valid key")
        continue
    
    except ai.error.ServiceUnavailableError as e:
        print(f"OpenAI API service unavailable: {e}")
        continue
    
    

def perform_sentiment_analysis(text):
    
    prompt = f"restrict your answer to one character - number. Interpret the sentiment of the following text between 0 (negative), 1 (neutral) 2 (positive): {text} "

    # Send the request to OpenAI API
    response = ai.Completion.create(
        engine='text-davinci-003',  
        prompt=prompt,
        max_tokens=3,  
        temperature=0.5,  
        n=1,  
        stop=None,  
    )
    
    sentiment_rating = int(response.choices[0].text.strip())
    
    return sentiment_rating

while True:
    try:
        print('-- WARNING: column destinated for the analysis must be named "text" --')
        data = input('Enter your Data (.csv file): ')
        
        if data.upper() == 'QUIT' :
            print('-- EXITING --')
            quit()
           
        dataset = pd.read_csv(data)

        for i, row in tqdm(dataset.iterrows(), total=len(dataset), desc='Processing'):
            text = row['text']
            sentiment_label = perform_sentiment_analysis(text)
            dataset.loc[i, 'Sentiment'] = sentiment_label
            time.sleep(2)  # Add a delay of 2 seconds between API calls
        break
 
    except FileNotFoundError:
        print(f'File "{data}" not found. Make sure the file path is correct.')
        continue

    except pd.errors.ParserError:
        print(f'Error parsing the file "{data}". Make sure it is a valid CSV file.')
        continue

    except ValueError as e:
        print(str(e))
        continue
    

dataset.to_csv(data, index=False)


print('Your sentiment analysis was completed with success! Check your dataset to view the results.')
    
    


    
    