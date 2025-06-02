from dotenv import load_dotenv
from home_assistant_ai.v1.ai import AI
from home_assistant_ai.v1.home_assistant import HomeAssistant
from home_assistant_ai.v1.speech import Speech

def run():
    load_dotenv()

    home_assistant = HomeAssistant()
    ai = AI(home_assistant)

    prompt = (
        "You are a helpful assistant (AI), " +
        "attempting to fulfill requests of the Speaker:\n\n"
    )

    with Speech(ai) as speech:
        while True:
            try:
                ask = speech.listen()
                if ask is not None:
                    prompt += f"Speaker: {ask}\n"
                    response = ai.ask(prompt)
                    if response is not None:
                        prompt += f"AI: {response}\n"
                        speech.say(response)
                print(prompt)
            except KeyboardInterrupt:
                break

    