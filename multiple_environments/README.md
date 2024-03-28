## Storing and Retrieving Private Keys of Two Different Environments with Locker

Managing the private keys of two different environments is a critical aspect of devops. In this example, we'll
demonstrate how to use Locker Secrets Manager to securely store and retrieve private
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

1. Install the SDK

   1.1. Install for .NET project

   Using the .NET Core command-line interface tools

   ```shell
   dotnet add package lockerpm
   ```
   Using NuGet command-line interface

   ```shell
   nuget install lockerpm
   ```
   1.2. Install for Java Project
   
    Maven users

    ```xml
    <dependency>
       <groupId>io.locker</groupId>
       <artifactId>lockerpm</artifactId>
       <version>0.0.3</version>
    </dependency>
    ```
    Gradle users
           
    ```
    implementation 'io.locker:lockerpm:0.0.3'
    ```

2. Integrate the SDK into your code by using [.net](.net/) or [java](java/) examples
