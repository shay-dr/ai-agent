import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    #Check for command line argument
    if len(sys.argv) < 2:
        print("Error: Please add a quoted prompt as an argument")
        sys.exit(1)

    prompt = sys.argv[1]
    
    #check for empty/whitespace
    if not prompt.strip():
        print("Error: The quoted prompt cannot be empty")
        sys.exit(1)

    # load the environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment")
        sys.exit(1)

    #create a messages list to be used to maintain context later.
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    # Create Gemini client and get reply:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )

    # Display results
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"{response.text} \n Prompt tokens: {prompt_tokens} \n Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()