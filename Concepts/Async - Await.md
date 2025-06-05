#concept 

Normal code is run sequentially. create a variable calculate a value then use that value


However more complex tasks like talking to an API or Database over the Internet might take much longer (traffic, read speed, etc...) They will often not return the result straight away but will return a promise. 

In [[JavaScript]] (A promise is an Object representing the eventually completion or failure of an asynchronous operation and it's value)

```javascript
// Handle fulfilled (resolved) promises
promise.then((result) => { })

// Handle failed (rejected) promises
promise.catch((error) => { })

// May be called before the other errors if they haven't finished
console.log('Hello world!')

// To solve this we can use the await keyword. Wait for the promise to be completed before going onto the next line. 
// await must be used in a function marked with the async keyword

async function getSomeAPIData() {
	try {
		let response = await request.get('some-url');
		console.log(response.data.whatever); // Will not be called until the request has finished
	}
	catch(error) {
		console.error(error);
	}
}
```

Another  [Promise example](https://www.youtube.com/watch?v=RvYYCGs45L4&list=WL&index=15) from [Fireship](https://www.youtube.com/@Fireship)

```Javascript
const ride = new Promise((resolve, reject) => {
    const arrived = false;

    if(arrived) {
        resolve('Driver arrived');
    }

    else {
        reject('Driver bailed');
    }
});

ride
    .then(value => {
        console.log(value);
    })
    .catch(error => {
        console.log(error);
    })
    .finally(() => {
        console.log('All done');
    });
```