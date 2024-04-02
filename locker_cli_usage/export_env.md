Sometimes we need to quickly consolidate and organize the sensitive information into a single, easily accessible file format. By exporting secrets to an .env file, we benefit from improved organization and consistency in the configuration management practices. Whether it's for local development environments, continuous integration pipelines, or production deployments, Locker CLI empowers users to seamlessly integrate secrets into their workflows while maintaining robust security measures.

Run this command to export all secrets into `.env` file
```
locker secret list > .env
```