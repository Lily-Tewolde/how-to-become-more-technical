<sub>Lesson 1, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check what you've got against the list, draw a request path on your own as the challenge, and practise the questions you'd get in an interview.

## What I learned doing this

The habit that's helped me most is checking two ways. When the screen says "You're booked!", I also look for the row in the database. The screen is the front end telling you what it thinks happened. The row is what actually happened. One check isn't a pass.

A few other things I'd tell myself at the start:
- **Ask where the rule lives.** If a rule only lives on the front end, someone can get around it. Prices, deposits and anything to do with money belong on the back end.
- **Test as a normal user.** I've seen a feature look perfect from an admin account and show nothing to regular users. You can't test permissions from an account with every permission, because that access is exactly what hides the bug.
- **Ask whether it changes data.** That one question tells you how scary a release is, because code rolls back and data doesn't.

## You're done when

- [ ] You can say what the front end and back end each do, with a salon example of each
- [ ] You can explain why the price is decided on the back end
- [ ] You can read a request and name its method, endpoint and body
- [ ] You know what 201, 404, 409 and 500 mean
- [ ] You've opened the Network tab and found one real request
- [ ] You've checked 2pm and 3pm against `appointments.csv` and added `bk_1042`
- [ ] You can name the three environments and what lives in a repo

## Challenge

**Draw the request path for a cancellation.** Sam booked `bk_1042`, the gel pedicure on Saturday at 3pm. On Friday at 6pm she opens the assistant and taps **Cancel**.

Draw it on paper or in any tool you like, the same shape as the diagram in [Part 1](part-1-front-end-and-back-end.md). Include:
1. The method and endpoint the front end calls
2. The rule the back end checks (the FAQ's cancellation section)
3. What changes in the appointments table
4. The status code and what the response body says
5. What Sam sees on screen

<details>
<summary>One good answer</summary>

1. **`PATCH /api/bookings/bk_1042`** with a body like `{"status": "cancelled"}`. A `DELETE` would also work, but changing the status keeps the row, so the salon can still count cancellations and track the deposit.
2. **The 24-hour rule.** The appointment is at 3pm Saturday and it's 6pm Friday, so that's 21 hours' notice. Under 24 hours means the deposit isn't refunded.
3. **The `status` on `bk_1042` changes to `cancelled`.** Nothing is deleted.
4. **`200 OK`** with something like `{"status": "cancelled", "deposit_refunded": false}`.
5. **A kind message**, like "Your appointment is cancelled. Because it's less than 24 hours away, your $20 deposit isn't refunded."

Bonus points if you added what happens when she isn't signed in (`401`), or tries to cancel someone else's booking (`403`).
</details>

Want more? The [Extra credit](extra-credit.md) page (optional, Advanced) covers what happens before the request even leaves the phone, how sign-in works, and why tapping **Book** twice can make two bookings.

## Check yourself (interview style)

<details>
<summary><strong>1. What happens when a customer taps Book in an app?</strong></summary>

The front end packs the details into a request and sends it to the back end's API. The back end checks the rules, like the real price and whether the time is free, then writes a new row to the database. It sends back a response with a status code, like 201 if it worked or 409 if the time was taken, and the front end shows the result.
</details>

<details>
<summary><strong>2. Where should a business rule like a deposit live, and why?</strong></summary>

On the back end. The front end runs on the customer's device, so anything there can be changed. The front end can show the rule to be helpful, but the back end has to enforce it.
</details>

<details>
<summary><strong>3. Explain an API to a stakeholder who isn't technical.</strong></summary>

It's the menu one piece of software offers to another. Each item on the menu is a request it accepts, like "create a booking", and a promise about what it sends back. It's how our app talks to our own servers, and how we talk to outside services like payments or an AI model.
</details>

<details>
<summary><strong>4. What's the difference between a 401 and a 403?</strong></summary>

A 401 means the server doesn't know who you are, so you need to sign in. A 403 means it knows who you are and you're not allowed to do that.
</details>

<details>
<summary><strong>5. Why have a staging environment, and why do things still break in production?</strong></summary>

Staging lets the team test a change in a real setting without touching real customers or real data. Things still break in production because staging is never an exact copy. The data, the traffic and some settings are different. So I'd check every release in production too, ideally two ways, on screen and in the data.
</details>

<details>
<summary><strong>6. Walk me through what happens from a branch to production.</strong></summary>

A developer makes the change on a branch and tests it locally. They open a pull request, which gets a preview deploy, tests and a review. Once it's approved, it's merged into main, and that usually triggers a production deploy. Then someone checks it in production, and if it's wrong, the team rolls back to the last good version. I'd also ask whether it changed any data, because rolling back the code doesn't undo that.
</details>

## Further reading

**Start here**
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works), MDN. Clients, servers and HTTP in one short page.
- [What happens when...](https://github.com/alex/what-happens-when), a community GitHub repo. Everything that happens after you type a URL and press Enter. A classic interview question, answered in depth.
- [CS50x](https://cs50.harvard.edu/x/), Harvard. The free intro to computer science. Its later weeks cover SQL and building a web app, which puts this whole lesson into practice.
- [SQLBolt](https://sqlbolt.com/). Short, interactive SQL lessons in your browser. Great after Part 3.

**Go deeper**
- [Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview), MDN. The request and response model in more detail.
- [Client-server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview), MDN. What the back end does with a request, including static and dynamic sites.
- [Inspect network activity](https://developer.chrome.com/docs/devtools/network), Chrome DevTools. A full tour of the Network panel from Part 2.
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/), MIT. The tools nobody teaches, like the terminal and git.
- [Environments](https://vercel.com/docs/deployments/environments), Vercel. How local, preview and production work on a real hosting platform.
- [The Twelve-Factor App](https://12factor.net/dev-prod-parity). Why environments should stay alike, and the gaps that cause bugs.

**Primary sources**
- [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) and [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), MDN. The references I used for the tables in Part 2.
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), IETF (2022). The actual HTTP standard.
- [RFC 8259, The JSON Data Interchange Format](https://www.rfc-editor.org/info/rfc8259/), IETF (2017). The JSON standard.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), PostgreSQL docs. Tables, rows and SQL from the people who make the database.

## Next lesson

**Next: [Lesson 2, How LLMs and agents work](../02-how-llms-and-agents-work/).** You'll see that calling an AI model is just another API request, find out why it answers differently every time, and learn what turns a chatbot into an agent that can check the appointment book itself.

[Back to the lesson](README.md) | **Next: [Lesson 2, How LLMs and agents work](../02-how-llms-and-agents-work/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
