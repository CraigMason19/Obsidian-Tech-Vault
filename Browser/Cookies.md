A cookie is a small piece of data that a website asks your browser to store on its behalf. Your browser stores it and sends it back on subsequent matching requests.

The [[HTTP]] protocol browsers use to communicate with web servers, is essentially stateless. This means that each request is independent. The server doesn't automatically know that the person making this request is the same person who made the previous one.

| Cookie purpose  | What it does                    |
| --------------- | ------------------------------- |
| Login           | Keeps you signed in             |
| Shopping basket | Remembers your basket           |
| Preferences     | Remembers light/dark mode       |
| Session         | Identifies your current session |
| Analytics       | Helps understand website usage  |

For Example:
- Signing into a website:
	- Stie authenticates you.
	- Site creates a session and gives your browser a `sessionid` cookie.
    - Browser stores that cookie.
- Close the browser, come back tomorrow. The cookie is still there, so you're still recognised.
 
 