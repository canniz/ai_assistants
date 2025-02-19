# Prerequisites
- Python 3.6 or higher
- A Google account with Calendar and Gmail
- A Google Cloud Platform project with billing enabled
- An OpenAI API key to use

## Setting Up Google APIs
### Enable the APIs:
In your project, navigate to APIs & Services > Library and enable both the Google Calendar API and Gmail API.

### Create OAuth Credentials:
Under APIs & Services > Credentials, click Create Credentials > OAuth client ID.
- Configure the consent screen (see [Google's documentation](https://developers.google.com/identity/protocols/oauth2)) for guidance.
- Choose your application type (Desktop App is fine)
- Download the credentials.json file. 
- Place it in `credentials/client_secret_oauth2.json`

## Installation
1) Clone the repository:
2) (optional) Set up a virtual environment
Mac/Linux
```bash
python -m venv venv
source venv/bin/activate
```
3) Install the required packages:
```bash
pip install -r requirements.txt
```
   - The `requirements.txt` file includes packages necessary for interacting with Google APIs and OpenAI.

4) Create an `.env` file in the root folder and add the OPENAI_API_KEY using the `.env.example` as reference. 
   - Example content for `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
1) Run the app for the first time
```bash 
python main.py
```
2) You'll be redirected to Google OAuth 2 consent screen you configured before, accept everything. A token will be saved to your local repository. **DON'T EVER SHARE THAT TOKEN** :) 
   - This token is used to authenticate your requests to Google APIs and should be kept secure.

3) Chat with the bot via command line

## (optional) Customization
### Prompts
- You can customize prompts under `prompts.py`

### Actions
- You can customize the general experience by adding more actions:
1) Add the action in the `actions.py`
2) Implement the code of your action using a separate file (recommended)
3) Import the action function in the `action_module`
4) Add the action to the list of possible actions
5) Have fun

## Contribution
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.