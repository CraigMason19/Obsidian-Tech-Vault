Cascading Style Sheet 

Used to set out the style of the page or entire websites.

[Links]
[Bro Code YT - Learn CSS in 1 Hour](https://www.youtube.com/watch?v=wRNinF7YQqQ&list=WL&index=2)
[24 CSS Projects](https://www.youtube.com/watch?v=TzuWIHGFKCQ)
[Slaying The Dragon YT - Media Queries](https://www.youtube.com/watch?v=K24lUqcT0Ms&list=WL&index=38&t=50s)

[Dynamic textareas](https://www.youtube.com/watch?v=ElELqkwzcYM&list=WL&index=47)

[[#CSS Reset]]
[[#Chained Class selector]]
[[#Debugging]]
[[#Units]]
[[#Z-Index]]
[[#constants.css & Imports]]

[[#Icons]]
- [[#Ionicons]]

[[#Media Queries]]

---
## CSS Reset

A common technique used because different browsers use different default margins.
- Causes sites to look different by margins. 
- The * means "all elements" (a universal selector)
- So we are setting all elements to have zero margins, and zero padding, thus making them look the same in all browsers. 

```css
/* CSS reset
   Sets a default for all elements in the CSS.
   This ignores browser defaults to ensure a consistent baseline across different browsers.
*/
* {
    margin: 0;
    padding: 0;
    font-family: 'Oswald', sans-serif;
}
```

---
## Chained Class selector

Allows you to specify multiple classes that must be present on an element to select

```css
.class-a.class-b.class-c { /* styles here */ }
```

```html
<div class="class-a">This will NOT be styled.</div> 
<div class="class-a class-b">This will NOT be styled.</div>
<div class="class-a class-b class-c">This will be styled.</div>
```

---
## Debugging

This is a trick that outlines ALL CSS elements so that you can see the outline of all CSS elements

```css
.show-borders {
	outline: 1px solid Black
}
```

Then you can toggle this behaviour in JavaScript

```javascript
// DEBUG
document.addEventListener('keydown', function(event) {
    if (event.key === 'd' || event.key === 'D') {
        document.body.classList.toggle('show-borders');
    }
});

// OR

//DEBUG
document.addEventListener('keydown', function(event) {
	if (event.key === 'd' || event.key === 'D') {
		document.querySelectorAll('*').forEach(el => {
			el.classList.toggle('show-borders');
		});
	}
});
```

---
## Units

### px (pixel)
- Absolute size. Parent element has no effect
- Good for small things such as drop shadows or offsets.
### rem vs em
- em - Size relative to the parent element
- rem - Equal to the root font size, which on most browsers is 16px. So 1rem == 16px
	- relative to default font size, adapts to users preferences
	- will be displayed the same no matter where it is on the page
### %
- Based upon the size of the parent element




width: % in combination with a max-width, ch -> max width roughly x characters wide
 
height: question urself "do i rly need to set height" if yes -> use a min-height instead of height
vh -> problems with mobile e.g. keyboard coming up.

padding/margin: rem or em, kevin often uses em for padding of buttons
media queries: em



---


Padding is top, right, bottom, left - Clockwise
```CSS
padding: 10px 20px 30px 40px;
```




## Math

Contains calc(), min() & max() functions

Can be used to do simple + - / * calculations

```css
left: calc(50% - (var(--size-center) / 2));
```



Variables

```css
:root {
    --color-a: #9AC5F4;
    --color-b: #99DBF5;
    --color-c: #A7ECEE;
    --color-d: #FFEEBB;
}
  
.color-1 {
    background-color: var(--color-a);
}
```



## Extending

```css
// Class
.center {
    position: absolute;
    border-radius: 50%;
}

#hour-center, center {
    width: var(--size-hour-center);
    height: var(--size-hour-center);
    left: calc(50% - (var(--size-hour-center) / 2));
    bottom: calc(50% - (var(--size-hour-center) / 2));
    background-color: var(--color-hour);
}
```

OR

```css
#second-hand, #minute-hand, #hour-hand {
    position: absolute;
    width: 2px; /* adjust width and height as needed */
    height: 80px;
    background-color: black;
    transform-origin: bottom center;
}
```

---
## Z-Index

The higher the value the higher the higher it is placed on other elements in it's respected div.

---
## constants.css & Imports

I like to make a constants.css file and import that into other files

```css
/* constants.css */
:root {
    --color-theme: #333;
    --color-background: #f0f0f0;
    --debug-outline: 2px solid darkcyan;
}

/* other.css */
@import './constants.css';

background-color: var(--color-background);
```

---
## Icons

### Ionicons
https://ionic.io/ionicons
https://ionic.io/ionicons/usage

---
## Media Queries

**NOTE:**  I had to add this line to the header class to get it to work
- <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">

- Use max-width if making desktop first
- Use min-width if making mobile first to make responsive on bigger viewports

```css
@media (max-width: 500px) {} /* Tagets anything below 500px */
@media (min-width: 500px) {} /* Tagets anything above 500px */

/* For example, target multiple classes */
.header, .title {
	font size: 1.5rem;
}
```

```
/* Example set for screen sizes rather than for every break point
   in example he used min because he designed this mobile first */

/* xs */
@media (min-width: 475px) {}

/* sm */
@media (min-width: 640px) {}

/* md */
@media (min-width: 768px) {}

/* lg */
@media (min-width: 1024px) {}

/* xl */
@media (min-width: 1280px) {}

/* 2xl */
@media (min-width: 1536px) {}
```