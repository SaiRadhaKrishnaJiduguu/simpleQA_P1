import os
from langchain.llms import HuggingFaceHub

# Set the Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

#We can get this acess token in hugging face website.

# Create an instance of HuggingFaceHub and specify the repository ID
llm = HuggingFaceHub(repo_id="google/flan-t5-large")

# Define the query
our_query = "what is the currency of India?"

# Invoke the model to get the completion
completion = llm.invoke(our_query)

# Print the completion
print(completion)
