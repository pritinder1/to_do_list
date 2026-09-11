# TPH September 2026 email queue

Sub-account: The People's Herbalist (TruPortals location `K03NyY3QgvKM66LM0Bl7`)
Sender name: Danny | The People's Herbalist
Sender email: danny@thepeoplesherbalist.com (domain reply.thepeoplesherbalist.com auto-selects)
Test email: hello@trucreatives.com
Timezone: America/New_York

## Links to set before pasting (top of build_emails.py or find-and-replace in the HTML)
| Placeholder | Replace with |
|---|---|
| `https://REPLACE-WITH-COMEDY-EVENT-LINK` | TruPortals event link for the Sept 25 comedy show |
| `https://app.thepeoplesherbalist.com/events` | All-events page (confirm the URL from the events section) |
| `https://REPLACE-WITH-WHATSAPP-GROUP-LINK` | The People's Herbal Circle WhatsApp invite link |
| `FLYER_IMG` (optional) | Hosted URL of the September calendar flyer if you want the image above the list |

## Email 1: Comedy show push + September calendar
- File: `01-comedy-show-september-calendar.html`
- Send: Tue Sept 15, 10:00 AM ET
- Subject: Comedy, mocktails and a DJ. Sept 25 is our night 🎤
- Preview: Danny hosts Pass the Mic at the Williams Center. Plus every September event in one place.
- Resend to unopened after 12h, subject: Still thinking about Sept 25? Seats are going.
- Track clicks ON, UTM ON

## Email 2: Final call
- File: `02-comedy-show-final-call.html`
- Send: Wed Sept 23, 10:00 AM ET (or Tue Sept 22 if the Thursday LSC event is also being pushed)
- Subject: This Friday: Pass the Mic. Last call for seats 🎤
- Preview: Holistic happy hour at 7, show at 8, food trucks outside. Grab your ticket before Friday.
- Resend to unopened after 12h, subject: Tomorrow night. Are you coming?
- Track clicks ON, UTM ON

## Facts in the copy to confirm with Danny before sending
- Headliner name spelling: "Monique Lettice" (meeting notes also show "Latisse")
- Ticket price $45 and the educator buy one get one offer
- Times: flyer says 7:00 to 9:00 PM; Sept 1 meeting notes say happy hour 7 to 8, show at 8
- Food trucks (wood fired pizza and dessert) were "pending" as of Sept 1
- 100 seat capacity

## Logo
- `assets/tph-logo.png` is the brand logo with the white background removed (transparent PNG, 642x238).
- The emails currently load it from this repo's raw GitHub URL. Upload it to the TruPortals media library and swap `LOGO` in `build_emails.py` (or find-and-replace in the HTML) so the email does not depend on this branch.
- Never embed the logo as a base64 data URI: Gmail does not render those.

## Event listing to create in TruPortals (Communities / Events)
- Title: Pass the Mic: Comedy & Conversations
- Date: Friday, September 25, 2026
- Time: 7:00 PM to 9:00 PM ET (doors and holistic happy hour at 7:00, show at 8:00)
- Location: Williams Center Cultural Arts Center, Rutherford, NJ
- Ticket: $45 general admission (educator buy one get one, if confirmed)
- Capacity: 100
- Cover image: the calendar flyer or the comedy show graphic
- Description:
  A night of laughs and real talk, alcohol free. Doors open at 7 for a holistic happy hour with herbal mocktails and DJ Santana. At 8, Danny takes the mic with headliner Monique Lettice for stand up, a talk show segment, and audience moments built around one theme: back in the day vs. now. Food trucks outside. Bring your people, seats are limited to 100.
- After saving, copy the event's public link and paste it over `https://REPLACE-WITH-COMEDY-EVENT-LINK` in both emails.
