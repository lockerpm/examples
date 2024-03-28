## Encrypting the Sensitive Data of User with Locker

When dealing with sensitive user data like addresses, identification cards, and bank accounts, it's crucial not to store it directly in the database. Instead, encrypt the data before saving it. Proper management of encryption keys is paramount. 

In this example, we'll illustrate the process of generating, storing, and utilizing encryption keys for securing sensitive user information.

### Getting Started

Follow these steps to encrypt data of users using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your crypto wallet application.


#### Step 2: Create and retrieve the Access Key of the Project using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your user data encryption application.

3. Click on "Access Keys" section.

4. Generate new access key with "Write" permission. Save your new access key.

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

2. Integrate the SDK into your code by using [examples](user_data_encryption.py)

