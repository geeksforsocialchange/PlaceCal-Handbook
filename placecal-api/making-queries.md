# Making queries

Currently we only serve read queries and no mutations. The examples are written in javascript.

The following code is a bare-bones query wrapper using the `node-fetch` npm module.

```javascript
import fetch from 'node-fetch';

const endPoint = 'http://192.168.0.39:3000/api/v1/graphql';

function query (query, variables) {
  return new Promise((resolve, reject) => {
    fetch(endPoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        variables,
        query
      })
    })
    .then(r => r.json())
    .then(data => resolve(data))
  });
}
```
