#PURPOSE: Write a Python package to enable API calls to do the following:
'''
1. Access or create a Vector DB pod.
    A. Attempt to create a vector database through the EquoAI platform programmatically;
    Requires API KEY, which can be obtained from Landing Page 
    (Add a feature for generating unique API keys for registered users of the platform.)
    B. Access existing pod, using unique user developer API_KEY and POD_ID.
2. Store and query data (to and from!) the pod. 
We may add a data deletion feature if desired (basically removal of a node from a BST-
normally this algorithm is doable albeit quite tricky.)
'''

import requests
import tiktoken


class equoai_db:
# class EquoDB:
    def __init__(self,api_key):
        self.api_key=api_key
        self.tokenizer="gpt-3.5-turbo"
    
    def get_num_tokens(self,query_sentences):
        token_encoding = tiktoken.encoding_for_model(self.tokenizer)
        num_tokens = []
        for i in range(len(query_sentences)):
            token_count = len(token_encoding.encode(query_sentences[i]))
            num_tokens.append(token_count)
        return num_tokens

    def create_new_project(self, query, query_embeddings, project_title):
        tokens_in = self.get_num_tokens(query)
        # url = 'http://10.0.0.132:5000/query' #Localhost testing purposes
        url = 'https://evening-everglades-40994-f3ba246c1253.herokuapp.com/query'
        project_name =  project_title
        obj = {
            'query_sentences':query,#Stores array of strings
            'query_embeddings':query_embeddings,
            'num_input_tokens':tokens_in,
            'api_key':self.api_key,
            # 'api_key':api_key,
            'pod_id': project_name,
            'is_query':False,
            'create_new_project':True,
            'top_k':0
        }
        r = requests.post(url, json=obj)
        print(r.json())
        return r.json()
    
            
    #Request data from 
    def similarity_search(self, query, query_embeddings, project_title, top_k=5):
        #Mitigate the following serialization error by converting to list:
        #TypeError: Object of type ndarray is not JSON serializable
        # url = 'http://10.0.0.132:5000/query' #Localhost testing purposes
        url = 'https://evening-everglades-40994-f3ba246c1253.herokuapp.com/query'
        project_name =  project_title
        tokens_in = self.get_num_tokens(query) 
        obj = {
            'query_sentences':query,#Stores array of strings
            'query_embeddings':query_embeddings,
            'num_input_tokens':tokens_in,#
            'api_key':self.api_key,
            'pod_id': project_name,
            'is_query':True,
            'create_new_project':False,
            'top_k':top_k
        }
        r = requests.post(url, json=obj)
        # print('RESPONSE: ', r.json())
        # k_most_similar_results = r.json()['documents']
        # return k_most_similar_results
        return r.json()


    def update_embeddings(self, query, query_embeddings, project_title):
        # url = 'http://10.0.0.132:5000/query' #Localhost testing purposes
        url = 'https://evening-everglades-40994-f3ba246c1253.herokuapp.com/query'
        project_name =  project_title
        tokens_in = self.get_num_tokens(query)
        obj = {
            'query_sentences':query,#Stores array of strings
            'query_embeddings':query_embeddings,
            'num_input_tokens':tokens_in,#
            'api_key':self.api_key,
            # 'api_key':api_key,
            'pod_id': project_name,
            'is_query':False,
            'create_new_project':False,
            'top_k':0

        }
        r = requests.post(url, json=obj)
        print(r.json())
        return r.json()

    
'''LEGACY CODE'''
 