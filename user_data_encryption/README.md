## Encrypting the Sensitive Data of User with Locker

If your system has some sensitive user data such as addresses, identification card, bank accounts, etc..., 
you should not save directly to the database. The data should be encrypted before saving to the database.
Managing the encryption key is a critical issue. In this example, we'll demonstrate how to create, save, 
and use these encryption keys in the process of encrypting and decrypting sensitive user data.


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

1. Install the SDK based on your [programming language](https://support.locker.io/en/locker-secrets-manager/developer-tools/secrets-sdk).

2. Integrate the SDK into your code by using [examples](user_data_encryption.py)

