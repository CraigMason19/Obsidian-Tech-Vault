Asynchronous [[JavaScript]] and XML

**NOTE:**  Today, people mostly use it with **JSON** instead of **XML**.

---

Links
- [YT - CodeLucky - AJAX for Beginners: Asynchronous JavaScript Explained Simply](https://www.youtube.com/watch?v=CGmk9uZDgYs&list=WL&index=49)

[[#Overview]]

---
## Overview

 Allows data updates to a web page asynchronously without page reloads. Done by making HTTP requests in the background

- Enhances experiences with dynamic content
- Allows real-time interactions with server-side data
- Feels more responsive and interactive

Originally `AJAX` were made using **`XMLHttpRequest`** but now calls are made using `fetch()`. This was because it was a cleaner, promise-based API.

So, for example, using modern JS:

```javascript
fetch('/api/data')
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(err => console.error(err));
```

By default the `fetch()` method uses `get`.

```javascript
fetch('/api/data');
fetch('/api/data', { method: 'GET' });
```

You can tell if the request is a `AJAX` request by passing the appropriate headers with the request.

```javascript
fetch(`/api/data/?${query.toString()}`, {
	// This 'XMLHttpRequest' is a convention that marks it as AJAX request. 
	headers: { 'X-Requested-With': 'XMLHttpRequest' } 
})
```

And in Django, for example.

```python
def tools(request):
	# Return the requested page data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': 'AJAX mode'})
        
    # Otherwise, return the page
    else:
        return render(request, 'tools.html')
```

---