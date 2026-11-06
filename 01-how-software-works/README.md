# How does software actually work?

When you tap a button in an app, your phone sends a short message to a computer somewhere else, that computer checks the rules and saves a record in a database, and then it sends a short message back. Almost every app you use works this way, from a salon booking widget to your banking app.

![Level: Beginner](https://img.shields.io/badge/Level-Beginner-brightgreen) ![Type: Learn](https://img.shields.io/badge/Type-Learn-blue) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** The part you see and tap is the front end. It runs on your phone or in your browser. The part that makes decisions and keeps the records is the back end, and it runs on a server. They talk through an API: the front end sends a request, usually written in JSON, to an address called an endpoint, and gets a response back with a status code like 201 (it worked) or 409 (that time's taken). The back end reads and writes rows in a database. All of the code lives in a repo, and it gets deployed to environments, usually local, then staging, then production.

> [!TIP]
> **New to this? Let me break it down.**
> Picture Polish & Co. on a busy Saturday.
> - The **front end** is everything a customer sees: the menu on the wall and the booking iPad at the counter.
> - The **back end** is the back room, where the manager decides whether 2pm is free and what a gel pedicure costs.
> - The **API** is the receptionist walking a slip to the back room and coming back with an answer.
> - The **database** is the appointment book. If it isn't written in the book, it isn't booked.
> - **Production** is the salon on Saturday with real customers. **Staging** is a practice run on Monday when the doors are closed.
>
> That's the whole idea. The rest of this lesson is the real version.

**You'll need:**
- A computer with Chrome, Edge or Firefox for one hands-on step in Part 2. Everything else works on a phone.
- The [Polish & Co. running example](../example/) open in another tab
- A spreadsheet (Google Sheets, Excel or Numbers) for Part 3. No code needed.

**What you'll learn:**
- What the front end and back end each do, and which one gets the final say
- How to read an API request and response, including JSON and status codes
- How a database stores bookings as rows, and what reading and writing mean
- Where code lives and how a change gets from a laptop to real customers
- How to draw the full path of one tap, from the Book button to the database and back

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Front end and back end](part-1-front-end-and-back-end.md) | Follow one tap from the phone to the server | 10 min |
| [ ] | [APIs, JSON and status codes](part-2-apis-json-and-status-codes.md) | Read a request and response, then watch real ones | 15 min |
| [ ] | [Databases](part-3-databases.md) | Be the database for one booking | 15 min |
| [ ] | [Where code lives](part-4-where-code-lives.md) | Repos, environments and deploys | 10 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Supporting files:** [`services.csv`](services.csv) and [`appointments.csv`](appointments.csv), the salon's two database tables for Part 3.

**Optional, Advanced:** [Extra credit](extra-credit.md), what happens before the request, sign-in, and why retries can double-book.

**[Start Part 1 →](part-1-front-end-and-back-end.md)**
