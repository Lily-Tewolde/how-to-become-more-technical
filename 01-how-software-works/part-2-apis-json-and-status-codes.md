<sub>Lesson 1, Part 2 of 5 · about 15 min</sub>

# APIs, JSON and status codes

**In this part,** you'll read the request the salon's front end sends when someone taps **Book**, read the response that comes back, learn the status codes you'll see in bug reports, and watch real requests in your own browser.

## Why this matters

An API is the contract between two pieces of software. It's how the front end talks to the back end, and it's how the salon's back end talks to other companies, like a payment provider or an AI model.

Once you can read a request and a response, you can:
- tell whether a bug is the front end sending the wrong thing or the back end answering wrong
- read API docs from a vendor and see what their product can actually do
- write tickets that say exactly what should happen when something fails

## How it works

**API** stands for application programming interface. It's a menu of requests one program accepts from another, and what it sends back for each one.

Every request has the same parts:

| Part | What it is | Salon example |
|---|---|---|
| **Method** | The kind of thing you're asking for | `POST`, meaning "create something" |
| **Endpoint** | The address you're asking | `/api/bookings` |
| **Headers** | Labels about the request | "this is JSON", "here's who I am" |
| **Body** | The details, often in JSON | the service, time and customer |

And every response has a **status code**, its own headers, and usually a body.

### 3. Read the request

**Read what the front end actually sends when the customer taps Book.** This is the request from Part 1, written out the way it travels:

```http
POST /api/bookings HTTP/1.1
Host: api.polishandco.example
Content-Type: application/json

{
  "service_id": "gel-pedicure",
  "start_time": "2026-11-14T15:00",
  "customer_name": "Sam L.",
  "phone": "+1-604-555-0142"
}
```

Line by line:
1. **`POST /api/bookings`** is the method and the endpoint. "Create a booking."
2. **`Host`** says which server it's going to.
3. **`Content-Type: application/json`** says the body is written in JSON.
4. **The part in curly braces** is the body. It's the filled-in form.

Look at what's missing. There's no price in the request. The back end looks up the price itself, for the reason you saw in Part 1.

**JSON** (JavaScript Object Notation) is the most common way to write that body. It's labels and values, like a form someone filled in. Text goes in double quotes, numbers don't, and a comma goes between each pair. MDN has a friendly intro in [Working with JSON](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON).

The method tells the server what kind of thing you want. These are the ones you'll see most, with MDN's definitions from [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods):

| Method | MDN says | At the salon |
|---|---|---|
| `GET` | "requests a representation of the specified resource" | Get the free times for Saturday |
| `POST` | "submits an entity to the specified resource, often causing a change in state" | Create a new booking |
| `PATCH` | "applies partial modifications to a resource" | Move a booking to 4pm |
| `DELETE` | "deletes the specified resource" | Remove a booking |

### 4. Read the response

**Read what the back end sends back.** If everything checks out, the response looks like this:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "booking_id": "bk_1042",
  "status": "confirmed",
  "service": "Gel pedicure",
  "start_time": "2026-11-14T15:00",
  "price": 60,
  "deposit_due": 20
}
```

The first line carries the status code, `201 Created`. The body gives the front end what it needs to show "You're booked!" and the $20 deposit. Notice the price came *back* from the server. The server is the one that knows it.

### 5. Read the status code

**Use the first digit to know who had the problem.** Status codes come in five groups ([MDN, HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)):
- **1xx** informational
- **2xx** it worked
- **3xx** go somewhere else (a redirect)
- **4xx** the request was the problem
- **5xx** the server was the problem

These are the ones you'll actually meet, with what each would mean at Polish & Co.:

| Code | Name | At the salon |
|---|---|---|
| `200` | OK | Here are Saturday's free times |
| `201` | Created | The booking is saved |
| `400` | Bad Request | The request was garbled, like broken JSON |
| `401` | Unauthorized | Not signed in. MDN notes it really means "unauthenticated" |
| `403` | Forbidden | Signed in, but trying to see someone else's bookings |
| `404` | Not Found | No service called `gel-pedi` (a typo in the request) |
| `409` | Conflict | Someone booked 3pm a second ago |
| `422` | Unprocessable Content | Well formed, but it makes no sense, like a Monday booking when the salon's closed |
| `429` | Too Many Requests | Someone's sending hundreds of requests a minute |
| `500` | Internal Server Error | A bug on the salon's server |
| `503` | Service Unavailable | The server is down or overloaded |

Teams don't all use these the same way. One team might send `422` for a closed day and another might send `400`. What matters is that the team picks one and the front end knows what to do with it.

**Error states are product decisions.** A `409` shouldn't become "Something went wrong." It should become "That time just got booked. Want 4:30 instead?" When you write a ticket for a new endpoint, list the codes it can send and what the customer sees for each one.

<details>
<summary><strong>Stuck?</strong></summary>

- **"401 and 403 sound the same."** 401 means "I don't know who you are". 403 means "I know who you are, and you're not allowed". Sign-in is the first one, permission is the second.
- **"Why is a 409 the client's fault?"** It's not really anyone's fault. The 4 just means the problem is with this request, so trying the same request again won't help. Picking another time will.
</details>

### 6. Watch real requests in your browser

**Open your browser's developer tools and watch a website make API calls.** Every browser has a built-in panel that shows each request and response. Looking at it is completely safe. Here's how in Chrome or Edge ([Chrome DevTools, Inspect network activity](https://developer.chrome.com/docs/devtools/network)):
1. Open any site that loads things as you use it, like a weather site or a store.
2. Press **Command+Option+J** on a Mac or **Control+Shift+J** on Windows. That opens DevTools on the Console tab.
3. Click the **Network** tab.
4. Click the **Fetch/XHR** filter. That hides images and styles, so you mostly see API calls.
5. Reload the page, or click around on it.
6. Click any request in the list. Check the **Headers** tab for the method and status code, the **Payload** tab for what was sent, and **Preview** or **Response** for what came back.

You're done when you've found one request, and you can say its method, its status code and one label from its response.

<details>
<summary><strong>Stuck?</strong></summary>

- **"The list is empty."** DevTools only records while it's open. Reload the page with the Network tab showing.
- **"I'm on Firefox."** Firefox has the same panel in its web developer tools, called the Network Monitor. The idea is the same.
- **"It's all gibberish."** Lots of it will be. Look for a request with a readable name and a Preview that shows labels and values. That's JSON.
- **Safety note.** Looking is fine. Never paste code into the Console because someone online told you to. That's a common way people get their accounts taken over.
</details>

<details>
<summary><strong>Go deeper (safe and idempotent methods, headers, and REST)</strong></summary>

- **Safe and idempotent.** In MDN's table, only `GET` is **safe**, meaning it shouldn't change anything. `GET`, `PUT` and `DELETE` are **idempotent**, meaning sending the same request twice ends in the same state as sending it once. `POST` isn't. Send the same booking `POST` twice and you might get two bookings. [Extra credit](extra-credit.md) covers how teams protect against that.
- **Headers do a lot of quiet work.** An `Authorization` header carries proof of who's asking. Caching headers say how long a response can be reused. Most bugs about "it works for me but not for her" end up in headers.
- **REST** is a common style for designing APIs, where endpoints are nouns (`/bookings`, `/services`) and methods are the verbs. It's a convention, not a law, so APIs vary. Other styles you'll hear about are GraphQL and gRPC.
- **The real standard** for all of this is [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110). It's reference reading, not a place to start.
</details>

## Quick check

<details>
<summary>1. A bug report says the booking screen got a <code>409</code>. What probably happened?</summary>

The time was taken between when the customer saw it and when she tapped Book. The fix is a better message and a new time to pick, not a server fix.
</details>

<details>
<summary>2. What's the difference between a 4xx and a 5xx code?</summary>

A 4xx means the problem is with the request, like a typo or a time that's taken. A 5xx means the server hit a problem, like a bug or being down.
</details>

<details>
<summary>3. Why doesn't the booking request include the price?</summary>

Because the back end decides the price. If the request carried it, anyone could change it on their phone.
</details>

---

**Next: [Part 3 (Databases)](part-3-databases.md)** | [Back to the lesson](README.md)
