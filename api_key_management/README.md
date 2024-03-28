## API Key management

A web application calls an external service with an API that is not generally open without prior authorization.
An API key is not a form of authorization itself; it is used as an identity verifier. The API Key Consists of 2 fields:
Client ID – identifies who you are; Client secret – shared secret between you and the server. API key is never 
stored locally with the application on disk. In this example, we'll demonstrate how to Locker Secrets Manager to 
securely store and retrieve API Keys.


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

