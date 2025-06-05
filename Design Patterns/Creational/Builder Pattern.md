[[Design Pattern]]

A creational design pattern that creates complex objects on a step by step basis.

Takes the creation code out of it's own class and moves it into separate objects called builders.

Helps avoid very large constructors (especially for multiple optional parameters) as well as multiple overloaded constructors.  
 
**NOTE: The Builder pattern simulates named optional parameters. So therefore obsolete in languages like Python which has support for keyword arguments**

---
Example

``` js
// A example of a very long constructor
constructor(username, email, isActive=true, hasSubscription=false, role='user', loginAttempts=0, id=0, isEmailVerified=false) {
	...
}

// Hard to see what the booleans, ints etc... refer to in normal construction
const user1 = new UserProfile('jane_doe', 'jane.doe@example.com', false, true, 'admin', 5, 1234, true);

// A UserProfile built using a builder. Much easier to read
let userProfileBuilder = new UserProfileBuilder('john_doe', 'john.doe@example.com');
const user2 = userProfileBuilder
    .setIsActive(true)
    .setHasSubscription(true)
    .setRole('admin')
    .setLoginAttempts(5)
    .setIsEmailVerified(true)
    .build();

// Default values will be used if not specified
let userProfileBuilder = new UserProfileBuilder('jane_doe', 'jane.doe@example.com');
const user3 = userProfileBuilder
    .setIsActive(true)
    .setHasSubscription(true)
    .setIsEmailVerified(true)
    .build();
```

---
