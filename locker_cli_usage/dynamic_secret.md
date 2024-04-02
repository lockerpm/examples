Dynamic secrets are credentials or access tokens that are generated dynamically by a secret management system. These secrets are typically used to provide temporary access to resources or services, such as databases, cloud services, or APIs. Dynamic secrets are generated on-demand and have a limited lifespan, reducing the risk of exposure and unauthorized access.

To generate a dynamic secret, we can use this simple command instead of accessing the web interface
```
locker secret create --key=MYSQL_PASSWORD --random-value
```