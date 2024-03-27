## Storing and Retrieving Private Keys of Crypto Wallets with Locker

Managing the private keys of crypto wallets is a critical aspect of blockchain and cryptocurrency development. In this example, we'll demonstrate how to use Locker Secrets Manager to securely store and retrieve private keys, ensuring the sensitive information is well-protected throughout the development lifecycle.

### Getting Started

Follow these steps to store and retrieve private keys of crypto wallets using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your crypto wallet application.

#### Step 2: Store and retrieve Private Key using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your crypto wallet application.

3. Click on the "Secrets" section.

4. Create a new secret for storing the private key of your crypto wallet. Name the secret appropriately, such as `wallet_address_0x01`.

5. Paste the private key into the designated field and save the secret.

#### Step 3: Store and retrieve Private Key using Locker SDK

1. Install the SDK based on your [programming language](https://support.locker.io/en/locker-secrets-manager/developer-tools/secrets-sdk).

2. Integrate the SDK into your code by using [examples](store_retrieve_private_keys.js)
