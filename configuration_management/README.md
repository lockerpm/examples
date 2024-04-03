# Configuration management

Applications can store many configuration settings in a key-value database. By using the Locker Secrets Manager, 
we can easily update and retrieve without restarting the application.

In this example, we'll showcase how to utilize the Locker Secrets Manager to securely store and retrieve 
configuration settings.


In this example, we'll showcase how to utilize the Locker Secrets Manager to securely store and retrieve API keys.


### Getting Started

Follow these steps to encrypt data of users using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your application.


#### Step 2: Create and retrieve the Access Key of the Project using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your user data encryption application.

3. Click on the "Secrets" section.

4. Create a new secret for storing the configuration. Name the secret appropriately, such as `MAIL_SERVER`.

5. Paste the secret settings into the designated field and save the secret.


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

2. Run the Flask application

```
flask --app configuration_management run
```

Now, go to `http://127.0.0.1:5000/configuration` to see the SMTP and SSO settings returned.

