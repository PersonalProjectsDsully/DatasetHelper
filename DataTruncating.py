import os

# Define the path to the input file
input_file = "/home/david/Desktop/SFMethodHelperForVSCodeUsers.txt"

# Define the desired word count per article
word_count_per_article = 3000

# Define the output directory where the parts will be saved
output_directory = "/home/david/Desktop/parts/"

os.makedirs(output_directory, exist_ok=True)

# Read the input file
with open(input_file, "r") as file:
    content = file.read()

words = content.split()

articles = []
current_article = []
current_word_count = 0
for word in words:
    current_article.append(word)
    current_word_count += 1
    if current_word_count >= word_count_per_article:
        articles.append(current_article)
        current_article = []
        current_word_count = 0

# If there are remaining words, create an additional article
if current_article:
    articles.append(current_article)

# Save the articles as separate files
for i, article in enumerate(articles):
    output_file = os.path.join(output_directory, f"article{i}.txt")
    with open(output_file, "w") as file:
        file.write(" ".join(article))

print("Splitting complete! Parts can be found in", output_directory)
