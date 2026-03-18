Application Programming Interface

- A way of interacting with a Service (Google, Spotify, ...) via requests and responses.

[[#Requests]]
[[#Routes]]
[[#Status Codes]]


Resources
- [JSON Place Holder](https://jsonplaceholder.typicode.com)
	- Free fake and reliable API for testing and prototyping
- [[#Useful API's]]

---
## Requests

Requests are HTTP Methods for interacting with a Server.

FETCH -> the **modern, built-in** JS way to make HTTP requests. then you determine what type of request it is and how to handle it

| Request Type | Description            |
| ------------ | ---------------------- |
| GET          | Retrieves data         |
| POST         | Creates data           |
| PUT          | Entirely updates data  |
| PATCH        | Partially updates data |
| DELETE       | Removes data           |

---
## Routes

Below is an example of how to document routes used for an API

| GET    | /posts/1           |
| ------ | ------------------ |
| GET    | /posts/1/comments  |
| GET    | /comments?postId=1 |
| POST   | /posts             |
| PUT    | /posts/1           |
| PATCH  | /posts/1           |
| DELETE | /posts/1           |

---

## Status Codes

[HTTP response status codes list](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

Requests can return codes to let you know if something went wrong or succeeded.

There are many but these are the most useful / common ones.

| Code | Description           |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Resource Created      |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 404  | Not Found             |
| 405  | Method Not Allowed    |
| 500  | Internal Server Error |

---
## Useful API's

### Free

https://api.nasa.gov
**[JokeAPI](https://github.com/Sv443/JokeAPI)**
**[Open Trivia Database API](https://opentdb.com/api_config.php)**


https://quotes.rest (Lovely website)