import os
import openai

# Your OpenAI API key
openai.api_key = ''
#print(openai.Model.list())
# Directory where the text files are located
directory = "/home/david/Desktop/parts/"
# Open the output file
with open('summary.txt', 'w') as outfile:
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.startswith("article") and filename.endswith(".txt"):
            # Open the current file
            with open(directory + filename, 'r') as infile:
                # Read the contents of the file
                content = infile.read()
                # Print out the content
                print(f"Content of {filename}:")
                print(content[:100])  # print out the first 100 characters
                # Prepare the prompt
                prompt = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": content},
                    {"role": "user", "content": f"""Given the following natural language descriptions of  behaviors and their corresponding code, generate more examples:

                    Description: "NPC with ID 1 is under the player"
                    Code: [2, NPC, isNPCUnderMyPlayer, {{true}}, 1:[1]]

                    Description: "NPC with ID 2 is facing the player"
                    Code: [2, NPC, isNPCFacingMyPlayer, {{true}}, 1:[2]]

                    Description: "NPC with ID 3 is moving towards the North"
                    Code: [2, NPC, getDirection, 1:[3], 1:North]

                    More examples:{content}"""}
                ]


                # Use the OpenAI API to generate a summary
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=prompt,
                    temperature=0.8,
                    max_tokens=5000
                )
                print(f"Response from the API for {filename}:")
                print(response['choices'][0]['message']['content'].strip())

                # Write the filename and summary to the output file
                outfile.write(f"{filename}:\n")
                outfile.write(f"{response['choices'][0]['message']['content'].strip()}\n")
                outfile.write("\n----------------------\n")
                                # Flush the output file
                outfile.flush()
                os.fsync(outfile.fileno())
