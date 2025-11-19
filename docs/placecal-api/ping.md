# Ping

```javascript
/* 
An empty call that tests if your code is working and responds
with a simple message.
*/

query("{ping}")
  .then( (response) => {
    console.log(response);
  });

/* response */
{
  data: { ping: 'Hello World! The time is 2022-03-21 11:10:20 +0000' }
}
```
