# Example
  if the json content is like below
  ```json
  "email_1":{
	"username":"example@gmail.com",
    "password":"your password"
}
  ```
  and execute this code
  ```python
  readUnseen=EmailUnreadCount()
  results=readUnseen.getUnseen()
  print(results)
  ```
  then the output it will be like this
  ```string
  {'email_1': 'FAILED'}
  ```
 don't worry about the FAILED, this happens because the script didn't have the correct email credentials. Just replace the credentials on the json file and it will run correctly.Now if you want to get only the count of unseen emails, you should execute the previous code like this:
 ```python
  readUnseen=EmailUnreadCount()
  results=readUnseen.getUnseen()
  print(results['email_1'])
  ```
  and if you have more than one email accounts, you can also run the previous code like this:
 ```python
readUnseen=EmailUnreadCount()
results=readUnseen.getUnseen()
keys=results.keys()
for i in keys:
	print("email: ",i," has ",results[i]," unseen emails.")
```
