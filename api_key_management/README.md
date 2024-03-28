## API Key management

A web application interacts with an external service through an API, which typically requires prior authorization for access. An API key serves as an identity verifier rather than a form of authorization. 

It comprises two essential fields: 
- `Client ID` - which identifies the user, 
- `Client Secret` - a shared confidential code between the user and the server. 

It's crucial to note that the API key should never be stored locally on the application's disk. In this example, we'll showcase how to utilize the Locker Secrets Manager to securely store and retrieve API keys.


### Getting Started

Follow these steps to encrypt data of users using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your crypto wallet application.


#### Step 2: Create and retrieve the Access Key of the Project using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your user data encryption application.

3. Click on the "Secrets" section.

4. Create a new secret for storing the API Key. Name the secret appropriately, such as `SLACK_WEBHOOK`.

5. Paste the secret API Key into the designated field and save the secret.


### Step 3: Encrypt your data using Locker SDK

1. Install the Python SDK

- **Creating a Virtual Environment**

```
python3 -m venv projectenv
```

- **Activating the Virtual Environment**

On Linux/MacOS
```
source projectenv/bin/activate
```

On Windows
```
projectenv\Scripts\activate
```

- **Install the Python SDK**

```
pip install -r requirements.txt
```

2. Integrate the SDK into your code by using [examples](api_key_management.py)

