**Hyper Text Markup Language**

The standard [[markup]] language for documents designed to be displayed in a web browser. 

Used in conjunction with [[CSS]] to style webpages. Can also link to [[JavaScript]].

[Mozilla - HTML Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[[#Differences between name, id & class]]


<hr>
## Visual Studio Shortcuts

Quickly create a element with a class - .

```HTML
<!-- .some-example -->
<div class="some-example"></div>

<!-- button.some-example -->
<button class="some-example"></button>
```

Quickly create a element with an id - #

```HTML
<!-- #some-example -->
<div id="some-example"></div>

<!-- button#some-example -->
<button id="some-example"></button>
```

---
<div id="craig"></div>
<div id="craig"></div>
<div id="craig"></div>
## Linking to a [[JavaScript]] file

Assuming same directory, place it at the bottom of the body tag

```HTML
<body>
    <h1 id="heading">Empty</h1>

    <p>Put stuff here...</p>

    <script src="app.js"></script>
</body>
```

<hr>
## Differences between name, id & class

```HTML
<body>
	<form>
		<input type="text" name="username">
		<input type="password" name="password">
	</form>
	
	<p id="intro">This is an introduction paragraph.</p>
	
	<p class="highlight">This paragraph will be highlighted.</p>
	<p class="highlight">This paragraph will also be highlighted.</p>
</body>
```

**name**
- Used for server requests

**id**
- Unique identifier for an element within the document.
- For use with JavaScript
- Can be styled using CSS (but classes are preferred)

**class**
- Used for styling one or more elements with similar characteristics or behaviour.
- Useful for selecting more than one element in JavaScript
- Can dynamically add / remove classes for extra functionality

<hr>
