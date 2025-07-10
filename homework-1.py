import os
from dotenv import load_dotenv
from openai import OpenAI
from pprint import pprint

def main():
	"""Homework for lesson 1 by test-student-23456"""
	
	# get api key from .env
	load_dotenv()

	# Get OpenAI API key
	api_key = os.getenv('OPENAI_API_KEY')
	if not api_key:
        	print("Error: OPENAI_API_KEY not found in environment variables.")
        	print("Please set your OpenAI API key in a .env file as:")
        	print("OPENAI_API_KEY=your_api_key_here")
        	return

	# initial bot test
	client = OpenAI(api_key=api_key)

	completion = client.chat.completions.create(
		model="gpt-4o-mini",
		store=False,
  		messages=[
			{"role": "user", "content": "write a haiku about ai"}
			]
	)

	pprint(completion)
	pprint(completion.choices[0].message.content);


if __name__ == "__main__":
    main()

