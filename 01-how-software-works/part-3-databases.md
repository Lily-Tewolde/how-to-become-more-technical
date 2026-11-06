<sub>Lesson 1, Part 3 of 5 · about 15 min</sub>

# Databases

**In this part,** you'll open the salon's two database tables, do the back end's job by hand to check whether a time is free, and write a new booking as a row.

## Why this matters

The database is the app's memory. If the screen says "You're booked!" but there's no row in the appointments table, she isn't booked.

It's also where almost every number you care about as a PM comes from. "How many no-shows last month?" and "which service makes the most money?" are both questions about rows in tables. If you can read a table, you can check a dashboard yourself instead of taking it on faith.

## How it works

PostgreSQL is one of the most widely used databases, and its docs describe tables plainly:

> "Each table is a named collection of *rows*. Each row of a given table has the same set of named *columns*, and each column is of a specific data type."
> [PostgreSQL, Concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html)

If you've used a spreadsheet, you already have the picture:

| Database word | Spreadsheet version | At the salon |
|---|---|---|
| **Table** | One tab | `appointments` |
| **Row** | One line | One appointment |
| **Column** | One header | `start_time` |
| **ID** | A unique label in the first column | `bk_1035` |

Tables point at each other using IDs. Each appointment has a `service_id` like `gel-pedicure`, and that matches a row in the `services` table where the price lives. That's why it's called a **relational** database.

There are only two things you do with a database:
1. **Read.** Look things up without changing them. "Is 3pm free?"
2. **Write.** Add, change or remove rows. "Save this booking."

Reads are low risk. Writes are where the bugs that hurt customers live, because a bad write stays in the book until someone fixes it.

### 7. Open the salon's two tables

**Import both CSV files into a spreadsheet, one tab each.** Download [`services.csv`](services.csv) and [`appointments.csv`](appointments.csv). In Google Sheets, go to **File**, then **Import**, and choose **Insert new sheet** so each file gets its own tab.

Take a minute to look around:
- `services` has seven rows. Each one has an `id`, a `name`, a `price` and how many `minutes` it takes.
- `appointments` has eleven bookings for Saturday, November 14, across two nail techs, Ama and Jo.
- Each appointment has a `status`. Most are `confirmed`. One is `cancelled`.

A real salon would also have a customers table for phone numbers and emails. I've left it out to keep this small.

<details>
<summary><strong>Stuck?</strong></summary>

- **"GitHub shows the file as a table, not a download."** Click the **Raw** button, then save the page, or use the download icon above the file.
- **"The times turned into weird numbers."** Your spreadsheet tried to be helpful and converted them. Format the column as plain text, or just read them as they are.
</details>

### 8. Check if Saturday at 2pm is free

**Check the appointments table the way the back end would.** A customer wants a gel pedicure on Saturday at 2pm. Look at `services` first. A gel pedicure takes 60 minutes, so she needs a tech from 2:00 to 3:00.

An existing appointment clashes if **it starts before the new one ends, and it ends after the new one starts**. Skip any row that's cancelled.

Check each tech:
1. **Ama.** Is there a confirmed row for Ama that starts before 3:00 and ends after 2:00?
2. **Jo.** Same question for Jo.

<details>
<summary>Answer</summary>

Both are busy.
- Ama has `bk_1035`, an acrylic full set from 1:30 to 3:00.
- Jo has `bk_1036`, a classic pedicure from 2:00 to 2:50.

The back end would send back a `409 Conflict`, and the front end should offer another time.
</details>

Now try 3pm, which needs a tech from 3:00 to 4:00.

<details>
<summary>Answer</summary>

Ama is free, and Jo isn't.
- Ama's `bk_1035` ends at exactly 3:00. Back to back is fine, because it doesn't end *after* 3:00.
- Ama's `bk_1037` at 3:00 is `cancelled`, so it doesn't count.
- Jo has `bk_1038`, a classic manicure from 3:00 to 3:45.

So the back end books Ama.
</details>

Those two traps, the exact 3:00 finish and the cancelled row, are exactly the kind of thing a developer has to get right in code. They're also great test cases when you get to [Evals 101](../06-evals-101/) and [Evals in CI](../09-evals-in-ci/).

### 9. Save the booking

**Add the new appointment as a row.** This is the write from Step 4 in Part 1. Add this line at the bottom of `appointments`:

| id | service_id | tech | customer_name | start_time | end_time | status | price | deposit |
|---|---|---|---|---|---|---|---|---|
| bk_1042 | gel-pedicure | Ama | Sam L. | 2026-11-14 15:00 | 2026-11-14 16:00 | confirmed | 60 | 20 |

Check two things before you call it done:
1. **The price came from `services`.** $60 for a gel pedicure. It didn't come from the customer.
2. **The deposit follows the rule.** The FAQ says a $20 deposit holds any appointment over $50. $60 is over $50, so it's 20.

Notice the deposit rule isn't a column in `services`. It lives in the back end's code. Some rules live in data and some live in code, and it's worth asking which is which, because data can be changed by the salon in an admin screen while code needs a developer and a deploy.

**You're done when** you can say why 2pm was refused, why Ama got 3pm, and where the $60 and the $20 came from.

<details>
<summary><strong>Go deeper (the same thing in SQL)</strong></summary>

**SQL** is the language most databases use for reading and writing. This read finds anything that clashes with a 3:00 to 4:00 booking:

```sql
SELECT tech, id, start_time, end_time
FROM appointments
WHERE status = 'confirmed'
  AND start_time < '2026-11-14 16:00'
  AND end_time   > '2026-11-14 15:00';
```

It returns one row, Jo's `bk_1038`. Any tech who isn't in the result is free.

This write saves the booking:

```sql
INSERT INTO appointments
  (id, service_id, tech, customer_name, start_time, end_time, status, price, deposit)
VALUES
  ('bk_1042', 'gel-pedicure', 'Ama', 'Sam L.', '2026-11-14 15:00', '2026-11-14 16:00', 'confirmed', 60, 20);
```

A few things engineers worry about that you'll hear in planning:
- **Two customers tap at once.** If both check 3pm, both see it free and both write, Ama's double-booked. Databases have tools for this, like constraints that refuse a clashing row and transactions that make the check and the write happen as one step. The losing customer gets the `409`.
- **Why the price is copied into the booking.** If the salon raises the gel pedicure to $65 next month, Sam's booking should still say $60. Copying it at booking time keeps history honest.
- **Why cancelled rows aren't deleted.** Keeping the row with `status = cancelled` means you can still count cancellations and handle the deposit rule. Deleting it would erase that history.

Want to practise? [SQLBolt](https://sqlbolt.com/) has short interactive SQL lessons that run in your browser.
</details>

## Quick check

<details>
<summary>1. A row for Jo runs from 1:00 to 2:00. Does it clash with a new 2:00 to 3:00 booking?</summary>

No. It ends at exactly 2:00, which isn't after the new one starts. Back to back is fine.
</details>

<details>
<summary>2. What's the difference between a read and a write?</summary>

A read looks things up without changing anything. A write adds, changes or removes rows. Writes are riskier because a bad one stays in the database until someone fixes it.
</details>

---

**Next: [Part 4 (Where code lives)](part-4-where-code-lives.md)** | [Back to the lesson](README.md)
