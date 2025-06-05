[[Design Pattern]]

Makes different implementations work together through a common interface

- Useful when using 3rd party or legacy code that can't be changed

Imagine going from a TV to a and needing to use an adapter to switch from USB to HDMI.

---
## Basic Example

```js
// 3rd party
class ThirdPartyTemperatureService {
    constructor(fahrenheit) {
        this.fahrenheit = fahrenheit;
    }
    getTemperatureF() {
        return this.fahrenheit;
    }
}

class TemperatureAdapter {
    static fromF(f) { return (f - 32) * 5/9; }
}

// Example usage:
const sensor = new ThirdPartyTemperatureService(95);
console.log(TemperatureAdapter.fromF(sensor.getTemperatureF())); // 35°C
```

---
## Class Example

```js
class LegacyLogger {
    logMessage(message, level) {
        console.log(`[${level.toUpperCase()}] - ${message}`);
    }
}

class ModernLogger {
    logInfo(message) { /* Logs as info */ }
    logWarning(message) { /* Logs as warning */ }
    logError(message) { /* Logs as error */ }
}

class LoggerAdapter {
    constructor(legacyLogger) {
        this.legacyLogger = legacyLogger;
    }
    
    logInfo(message) { this.legacyLogger.logMessage(message, "info"); }
    logWarning(message) { this.legacyLogger.logMessage(message, "warning"); }
    logError(message) { this.legacyLogger.logMessage(message, "error"); }
}

const modernLogger = new LoggerAdapter(new LegacyLogger());
modernLogger.logInfo("System started"); // [INFO] - System started
```

---