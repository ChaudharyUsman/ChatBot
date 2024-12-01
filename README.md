# ChatGPT-Based Python Chatbot

This is a simple chatbot built using Python and the OpenAI GPT-3.5 model. The chatbot supports continuous conversations by maintaining context with a conversation history.

## Features
- Utilizes OpenAI's `gpt-3.5-turbo` model for natural language responses.
- Maintains a conversation history for better contextual replies.
- Easy-to-use interface via the terminal.
- Customizable prompts for tailoring the chatbot's behavior.

## Prerequisites
- Python 3.7 or higher
- An OpenAI API key. You can generate one from [OpenAI's API Keys](https://platform.openai.com/account/api-keys).

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yChaudharyUsman/chatbot.git
    cd chatbot
    ```

2. Install required Python packages:
    ```bash
    pip install openai
    ```

3. Set up your OpenAI API key:
    - Replace `"sk-your-api-key"` in the code with your actual API key, or
    - Set the environment variable:
      ```bash
      export OPENAI_API_KEY=sk-your-api-key
      ```

## Usage
1. Run the chatbot script:
    ```bash
    python main.py
    ```
2. Start chatting with the bot in the terminal. Type `quit`, `exit`, or `bye` to end the conversation.

## Example

