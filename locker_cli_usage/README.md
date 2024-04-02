## Locker CLI usage

Managing secrets efficiently is an essential demand of both DevOps engineers and developers. There are a lot of use cases involving sensitive data usage among the daily tasks.  In this example, we'll illustrate how to simply interact with secrets in staging and development environment.

### Getting Started

Follow these steps to encrypt data of users using Locker:

#### Step 1: Register and Create a Project

1. Visit the [Locker Secrets Manager](https://secrets.locker.io) and register for an account.

2. Log in and create a new project dedicated to your application.


#### Step 2: Create and retrieve the Access Key of the Project using Web interface

1. Log in to your Locker account.

2. Navigate to the project created for your user data encryption application.

3. Click on the "Secrets" section.

4. Create some new secrets for storing the database credentials. Name the secret appropriately, such as `MYSQL_USERNAME`, `MYSQL_PASSWORD`,...

5. Paste the MySQL username and password into the designated field and save the secret.

#### Step 3: Interact with secrets using CLI

Follow other examples to see how we can manage sensitive data securely