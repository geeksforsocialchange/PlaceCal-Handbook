# Add a custom domain name to your site

### Add a CNAME

Add a CNAME pointing from your domain to the PlaceCal server.

```
CNAME mysubdomain.mydomain.com placecal.org
```

### Update your PlaceCal site

Set the URL field on your Site to the new domain, including `https://`.

### Log in to the server and add the domain to Letsencrypt

{% hint style="warning" %}
This requires server access! We can do this for you when your domain is added.
{% endhint %}

```
dokku domains:add placecal mysubdomain.placecal.org
dokku letsencrypt:enable placecal
```
