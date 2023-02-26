import openai as ia

ia.api_key = "your_api_key"

while True:
    prompt = input("\nMake a question: ")

    if prompt == "Exit":
        break

    completion = ia.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        n=1,
        max_tokens=2048
    )

    print(completion.choices[0].text)