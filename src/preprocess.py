import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)