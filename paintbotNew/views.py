import os
from django.shortcuts import render
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"
query = "hey"
def main(request):
    if request.method == 'POST':
        query = request.POST.get('user_input', '')  # Get the user input from the form
        print("Your query:", query)

        # Specify the correct encoding when loading the TextLoader
        loader = TextLoader('data.txt', encoding='utf-8')  # Replace 'data.txt' with your file path and 'utf-8' with the actual encoding if different

        index = VectorstoreIndexCreator().from_loaders([loader])

        results = index.query(query)
        print(results)

        # Now you have 'results', which contains the query results from the index
        # You can do something with the results, like displaying them in the template
        context = {
            'name': 'John',  # Assuming you want to display a name initially
            'query_results': results,
        }
        return render(request, 'main.html', context)

    # If the request method is GET (initial page load), display the form with a default greeting
    context = {
        'name': 'John',  # Assuming you want to display a name initially
    }
    return render(request, 'main.html', context)
