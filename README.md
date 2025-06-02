# Home Assistant AI Assistant

This project aims to create an AI assistant integrated with Home Assistant to automate various smart home functionalities.

## Version 1 (V1) - Simple Light Control AI

The initial version of this AI assistant focuses on basic control of smart lights within your home.

### Features

-   **Voice-activated light control**: Turn lights on and off using simple voice commands.
-   **Integration with Home Assistant**: Seamlessly connects with your existing Home Assistant setup.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/home-assistant-ai.git
    cd home-assistant-ai
    ```
2.  **Install dependencies with Poetry**:
    ```bash
    poetry install
    ```
3.  **Configure Home Assistant API**:
    Create a `.env` file in the root directory of the project and add your Home Assistant API token and URL:
    ```
    HOME_ASSISTANT_URL=http://your_home_assistant_ip:8123
    HOME_ASSISTANT_TOKEN=YOUR_LONG_LIVED_ACCESS_TOKEN
    ```
    Replace `your_home_assistant_ip:8123` with your Home Assistant instance's address and `YOUR_LONG_LIVED_ACCESS_TOKEN` with a generated long-lived access token from your Home Assistant profile.

4.  **Configure Gemini API**:
    Add your Gemini API key to the `.env` file:
    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```
    Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

### Usage

To start the AI assistant, run the main script:

```bash
poetry run python -m home_assistant_ai
```

Once running, you can use voice commands to control your lights. For example:

- "Turn on the living room lights"
- "Switch off the bedroom lamp"

### Technologies Used

-   **Python**: Core programming language.
-   **Home Assistant API**: For interacting with Home Assistant.
-   **Speech Recognition**: For processing voice commands.
-   **AI/NLP**: For understanding and interpreting commands.
