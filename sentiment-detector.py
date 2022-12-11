# Import the langdetect and TextBlob libraries
from textblob import TextBlob
from deep_translator import GoogleTranslator


# Function to classify the sentiment of the input text
def classify_sentiment(text):
  # Detect the language of the input text

  translated = GoogleTranslator(source='auto', target='en').translate(text)
  # Create a TextBlob object from the input text, specifying the language
  analysis = TextBlob(translated)

  # Check the sentiment of the input text
  if analysis.sentiment.polarity > 0:
    return "positive"
  elif analysis.sentiment.polarity == 0:
    return "neutral"
  else:
    return "negative"

# Test the function with some example input text in different languages
print(classify_sentiment('Kocham ten film!'))
print(classify_sentiment("Je déteste ce film!"))
print(classify_sentiment("Eu amo esse filme!"))