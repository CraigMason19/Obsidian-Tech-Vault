#concept 
Cross-site Request Forgery

One domain is forging a request to another.

Every time you design a form on the web to be submitted (POST, PUT, DELETE) it must have CSRF on it. This sends a token along with the request.
## Links

Computerphile
https://www.youtube.com/watch?v=vRBihr41JTo&list=WL&index=18

PwnFunction
https://www.youtube.com/watch?v=eWEgUcHPle0&list=WL&index=19

<hr>

In [[Django]]

```HTML
<form id='post-form' method="POST" action="create">
	{% csrf_token %}
	<!-- form stuff...-->
</form>
```

In [[Laravel]]