# Prerequisites
- Python 3.6 or higher
- A Google account with Calendar and Gmail
- A Google Cloud Platform project with billing enabled
- An OpenAI API key

## Setting Up Google APIs
### Enable the APIs:
1. In your Google Cloud project, navigate to APIs & Services > Library
2. Enable both the Google Calendar API and Gmail API

### Create OAuth Credentials:
1. Under APIs & Services > Credentials, click Create Credentials > OAuth client ID
2. Configure the consent screen (see [Google's documentation](https://developers.google.com/identity/protocols/oauth2) for guidance)
3. Choose "Desktop App" as your application type
4. Download the credentials.json file
5. Place it in `credentials/client_secret_oauth2.json`

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd ai_secretary
```

2. (Optional) Set up a virtual environment:
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create an `.env` file in the root folder:
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` with your settings:
   ```
   OPENAI_API_KEY="your-openai-api-key-here"
   OPENAI_MODEL="gpt-4o-mini"  # Or your preferred OpenAI model
   ```

## Usage
1. Run the app:
```bash 
python main.py
```

2. On first run:
   - You'll be redirected to Google's OAuth consent screen
   - Accept the requested permissions
   - A token will be saved to your local repository
   > **IMPORTANT**: Never share this token - it grants access to your Google account

3. Chat with the assistant via command line
   - Type your messages and press Enter
   - Type "close" to exit

## Customization
### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: The OpenAI model to use (defaults to "gpt-4o-mini" if not set)

### Prompts
- Customize the assistant's behavior by editing `prompts.py`

### Actions
Add new capabilities by extending the actions:
1. Add the action in `actions.py`
2. Implement the action logic in a separate file (recommended)
3. Import and register the action in `action_module.py`
4. Add the action to the available tools list

## Contributing
If you would like to contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.