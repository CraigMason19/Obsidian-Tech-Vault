[[Design Pattern]]

- Define a set of interchangeable algorithms (strategies) that can be swapped dynamically at runtime.
- Use it when you need to dynamically switch behaviour at runtime.

---
## JS Example

```js
class PaymentStrategy {
    pay(amount) {
        throw new Error('*** ERROR *** PaymentStrategy is an abstract class that must implement the pay() method.');
    }
}

class CreditCardPayment extends PaymentStrategy {
    pay(amount) {
        console.log(`Processing $${amount} with Credit Card`);
    }
}

class PayPalPayment extends PaymentStrategy {
    pay(amount) {
        console.log(`Processing $${amount} with PayPal`);
    }
}

class BitCoinPayment extends PaymentStrategy {
    pay(amount) {
        console.log(`Processing $${amount} with Bitcoin`);
    }
}

class PaymentProcessor {
    constructor(method) {
        this.method = method;
    }

    setMethod(method) {
        this.method = method;
    }

    pay(amount) {
        this.method.pay(amount);
    }
}

// Example Usage
const processor = new PaymentProcessor(new CreditCardPayment());
processor.pay(50); // Processing $50 with Credit Card

processor.setMethod(new PayPalPayment());
processor.pay(75); // Processing $75 with PayPal

processor.setMethod(new BitCoinPayment());
processor.pay(100); // Processing $100 with Bitcoin
```