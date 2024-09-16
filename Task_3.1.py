from collections import Counter
import pandas as pd

with open("combined_text.txt", "r") as file:
    text = file.read().lower().split()  # Convert to lowercase and split by spaces
    word_counts = Counter(text).most_common(30)

# Convert to DataFrame for saving as CSV
df = pd.DataFrame(word_counts, columns=['Word', 'Count'])
df.to_csv('top_30_common_words.csv', index=False)
