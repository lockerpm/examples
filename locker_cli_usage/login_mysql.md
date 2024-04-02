### Login MySQL securely

Users may need to access MySQL databases regularly to perform tasks such as data entry, data analysis, reporting, system administration, or application development. In a typical business setting, multiple departments and teams rely on MySQL databases to manage critical data related to sales, finance, customer information, inventory, and more.

Normally, users will be prompted to enter MySQL password in the process of logging in. Instead of spending time looking for the saved password, now we can do this task with one command. In this case MySQL password will be fetched by Locker CLI and used as input for the next command.

```
locker secret get --name=MYSQL_PASSWORD | mysql -h example.database.com -u admin -p
```
