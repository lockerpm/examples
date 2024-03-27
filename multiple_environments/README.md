## Storing and Retrieving Private Keys of Two Different Environments with Locker

Managing the private keys of two different environments is a critical aspect of devops. In this example, we'll demonstrate how to use Locker Secrets Manager to securely store and retrieve private
keys of 2 environment (ex staging and product)

### Getting Started

Follow these steps to store and retrieve private keys of 2 environments using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your application.

#### Step 2: Store and retrieve Private Key using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your application.

3. Click on the "Environments" section.

4. Create 2 environments for storing the private key of your application. Name the environment appropriately, such
   as `staging` and `product`.

5. Click on the "Secrets" section.

6. Create secret for each environment.

#### Step 3: Store and retrieve Private Key using Locker SDK

1. Install the SDK based on
   your [programming language](https://support.locker.io/en/locker-secrets-manager/developer-tools/secrets-sdk).

2. Integrate the SDK into your code by using [examples](../multiple_environments/)
