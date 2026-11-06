<sub>Lesson 1, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll see what happens before the request leaves the phone, how the back end knows who's asking, and why tapping **Book** twice can make two bookings. It's optional. Skip it if you're done for now.

<details open>
<summary><strong>Go deeper (before the request: DNS and HTTPS)</strong></summary>

In Part 1 the request "travels to the back end". Two things happen first.
1. **DNS turns the name into an address.** Computers find each other by IP address, not by names like `api.polishandco.example`. The phone asks the Domain Name System which address that name points to, a lot like looking up a contact before you call. Julia Evans' [Mess With DNS](https://messwithdns.net/) lets you play with real DNS records safely.
2. **HTTPS sets up a private, checked connection.** The phone and the server agree on encryption, and the phone checks the server's certificate to make sure it's really the salon's server. After that, nobody on the café Wi-Fi can read Sam's phone number.

Then the HTTP request from Part 2 goes through that connection. [What happens when...](https://github.com/alex/what-happens-when) walks through every step in detail.
</details>

<details open>
<summary><strong>Go deeper (sign-in: who's asking, and are they allowed?)</strong></summary>

The status codes `401` and `403` map onto two separate questions:
- **Authentication (authn)** is "who are you?" Sam signs in, and the server gives her phone a token, a long random string that proves she signed in. The phone sends it with every request, usually in an `Authorization` header.
- **Authorization (authz)** is "are you allowed to do this?" Sam can cancel `bk_1042`. She can't cancel Tasha's `bk_1035`, even though she's signed in.

Most serious bugs here are authorization bugs: someone's signed in properly and can see or change something that isn't theirs. Test them from a normal customer's account. An admin account can see everything, so it hides exactly the bug you're looking for.
</details>

<details open>
<summary><strong>Go deeper (retries, idempotency and the coat check)</strong></summary>

Phones lose signal. Say Sam taps **Book**, the request reaches the server and the booking is saved, but the response gets lost on the way back. Her screen spins, so she taps again. Now there are two bookings.

The fix is **idempotency**: making it safe to send the same request twice. Think of a coat check ticket. If you hand over the same ticket twice, you get the same coat, not two coats.

In practice, the front end makes up a unique key when Sam first taps **Book** and sends it with the request, and with any retry. The back end remembers the key. If it sees the same key again, it sends back the first booking instead of making a new one. Stripe's docs explain the pattern well:

> "The API supports idempotency for safely retrying requests without accidentally performing the same operation twice."
> [Stripe, Idempotent requests](https://docs.stripe.com/api/idempotent_requests)

That's also why `POST` isn't idempotent on its own, which you saw in MDN's table in Part 2.
</details>

<details open>
<summary><strong>Go deeper (two systems, and nothing ties them together)</strong></summary>

Now say the salon starts charging the $20 deposit by card when Sam books. That's two systems: the salon's database and the payment provider. There's no single switch that saves the booking and charges the card together.

So things can half happen:
- The booking saved and the charge failed. Ama's slot is held with no deposit.
- The charge went through and the booking didn't save. Sam paid for nothing.

Teams handle this a few ways:
1. **Do things in a careful order**, and undo the first step if the second fails. Only undo what this request created, nothing else.
2. **Retry safely**, using the idempotency key above.
3. **Reconcile.** Regularly compare the payment provider's records with the bookings table, like counting the till at the end of the night, and fix what doesn't match.

You don't need to design this yourself. You do need to ask "what happens if it fails halfway?" in planning, because that question usually finds the bug before customers do.
</details>

---

[Back to the lesson](README.md) | [Part 5 (Wrap up)](part-5-wrap-up.md)
