Dear Developer,

Thankyou for downloading our Python web client.

The documentation for this package shall be updataed continually at
https://documentation.equo.ai/documentation/fundamentals, 
so stay tuned.

HOW TO GET STARTED
In order to use any of the software in this package, you will need to generate 
a personal API Key by going to https://equo.ai/signin to signin to your account, 
and then navigating to https://equo.ai/developers. 
Click the big purple button to generate your API Key.
Once the key is generated, click on it to copy it and save it somewhere secure, because you won't
get to see it again! 

(Should any issues arise, contact us at https://equo.ai/request-demo, and we'll help you set your 
account up again!)

Some sample code 

Now that you've got your api key, simply install the library and get cooking!
Activate the Python environment you want to work with.
Go to your terminal and run the following bash script to download our software:

pip install equoai

Then in either your jupyter notebook or Python file, import
# Access your developer account. All you need is the API
api_key='u0YQoEwcl23O2mW0GqAzJ2bPsoAfFRjB'#Rick Sanchez's API Key
equoai = equodb(api_key)

# Create a name for your new vector database project.
project_name='davesdb'

# Create the project, and upload some text for your query!
# In this example, the CEO is uploading some of his spicy takes to his own vector database
query = [  
           "Canada is one of Britain's oldest former colonies",
           "Lamb of God is an awesome heavy metal band. Black Veil Brides isn't really my thing.", 
           "Starbucks has the best customer service and best tasting coffee of any coffee chain ever. Sorry Tim Horton's",
           "Pineapples definitely belong on pizza", 
           "Jojo's bizarre adventure is one of the greatest animes of all time."
]

equoai.create_new_project(query, project_name)

# Now let's say we wanted to query these embeddings via similarity search.

query = "What is the name of an awesome heavy metal band?"
#Similarity search. 
response = equoai.query_vector_store(query, project_name, is_query=True)

print(response)
# Lamb of God is an awesome heavy metal band. Black Veil Brides isn't as great. 

# Let's update our vector store in order to add more stuff to it.


query = [
    "I should definitely use this vector store with Cohere and Langchain to improve my search queries"
]
# set is_query to False to indicate that we're not searching for an embedding, but rather 
# we're trying to add more embeddings to the existing project.
equoai.query_vector_store(query, project_name, is_query=False)

# Let's query our vector store again and see if we've successfully added the new embeddings.
query = "What software should I use with my vector store?"
response = equoai.query_vector_store(query, project_name, is_query=True)
print(response)

# I should definitely use this vector store with Cohere and Langchain to improve my search queries

And there you go. That's on how to use the vector db for the current version of Equoai's Python Client.
Stay tuned



