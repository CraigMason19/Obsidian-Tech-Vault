[[Design Pattern]]

---
## Example

```js
class Stock {
    #investors = []; // Private
    
    constructor(company, price) {
        this.company = company;
        this.price = price;
    }
    
    setPrice(price) {
        this.price = price;
        this.#notify();
    }
    
    #notify() {
        this.#investors.forEach(i => {
            i.update(this.company, this.price);
        });
    }
    
    subscribe(investor) {
        this.#investors.push(investor);
    }
    
    unsubscribe(investor) {
        const index = this.#investors.indexOf(investor);
        if (index > -1) {  
            this.#investors.splice(index, 1);
        }
    }
}

// Observers
class Investor {
    constructor(name) {
        this.name = name;
    }
    
    update(company, value) {
        console.log(`${this.name} is notified: ${company} new price is $${value}`);
    }
}

const appleStock = new Stock("AAPL", 150);
const investor1 = new Investor("Alice");
const investor2 = new Investor("Bob");

appleStock.subscribe(investor1);
appleStock.subscribe(investor2);

appleStock.setPrice(155); 
// Output:
// Alice is notified: AAPL new price is $155
// Bob is notified: AAPL new price is $155

appleStock.unsubscribe(investor1);
appleStock.setPrice(160);
// Output:
// Bob is notified: AAPL new price is $160
```