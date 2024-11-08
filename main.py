from openai import OpenAI

# Set up your OpenAI API key
client = OpenAI()

# Initial system message to set up the chatbot's personality as "Mother"
messages = [
    {"role": "system", "content": "You are MU-TH-UR 9000, an emotionless AI responsible for ensuring protocol is followed at all costs. You respond in a calm, calculated manner."}
]


def chat_with_mother():
    print("\033[1;32;40mMU-TH-UR: Initializing...")
    while True:
        # Get user input
        user_input = input("ENTER QUERY: ")
        if user_input.lower() in ["exit", "quit"]:
            print("MU-TH-UR: Protocol dictates this conversation is terminated. Goodbye.")
            break

        # Append user's message to the conversation history
        messages.append({"role": "user", "content": user_input})

        # Get response from ChatGPT API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Extract and print the assistant's response
        reply = response.choices[0].message
        print(f"MU-TH-UR: {reply}")

        # Append assistant's reply to conversation history
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat_with_mother()
