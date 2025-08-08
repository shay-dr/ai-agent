import os
import sys
import config
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info


def main():
    #Check for command line argument
    if len(sys.argv) < 2:
        print("Error: Please add a quoted user_prompt as an argument")
        sys.exit(1)

    verbose_mode = False

    # Verbose
    if '--verbose' in sys.argv:
        verbose_mode = True
        sys.argv.remove('--verbose')
    

    # Assign user_prompt to argument
    user_prompt = sys.argv[1]

    #check for empty/whitespace
    if not user_prompt.strip():
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
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Define available functions to the LLM
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )

    # Pass available_functions to the config's 'tools' parameter
    sysconfig = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=config.SYSTEM_PROMPT  # or system_prompt if that's your variable
    )



    # Create Gemini client and get reply: 
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=sysconfig,
    
    )

    # Result data
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count


    # Display results with or without verbose
    if verbose_mode:
        print(f"User prompt:  {user_prompt} \n Prompt tokens: {prompt_tokens} \n Response tokens: {response_tokens}\n")
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f"{response.text}")    


if __name__ == "__main__":
    main()