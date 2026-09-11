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
- 100 seat capacity## Event listings to create in TruPortals (one per September event)
Each card in Email 1 links to its own event. Replace the four placeholders in `build_emails.py` (EVENT_LINKS) or find-and-replace in the HTML.

### 1. Alliance Performance Training Facility (placeholder `REPLACE-WITH-ALLIANCE-EVENT-LINK`)
- Date: Saturday, September 19, 2026, 8:00 AM to 1:00 PM ET
- Location: Banta Pl, Fair Lawn, NJ
- Price: TBD (free to attend if this is a tabling event)
- Description: Come see us at the Alliance community event. Herbal samples, education, and a chance to meet the team in person.

### 2. Liberty Science Center After Dark: 70s Boogie Nights (placeholder `REPLACE-WITH-LSC-EVENT-LINK`)
- Date: Thursday, September 24, 2026, 7:00 PM to 11:00 PM ET
- Location: Liberty State Park, Jersey City, NJ
- Price: TBD (LSC sells these tickets; if TPH is not selling, point the card at the LSC ticket page instead of a TruPortals event)
- Description: Adults only night at the Science Center. Disco, exhibits, and The People's Herbalist mocktail bar.

### 3. Pass the Mic: Comedy & Conversations (placeholder `REPLACE-WITH-COMEDY-EVENT-LINK`)
- Date: Friday, September 25, 2026, 7:00 PM to 9:00 PM ET (doors and holistic happy hour at 7:00, show at 8:00)
- Location: Williams Center Cultural Arts Center, Rutherford, NJ
- Price: $45 general admission (educator buy one get one, and $100 sponsor option, if confirmed)
- Capacity: 100
- Description: A night of laughs and real talk, alcohol free. Doors open at 7 for a holistic happy hour with herbal mocktails and DJ Santana. At 8, Danny takes the mic with headliner Monique Lettice for stand up, a talk show segment, and audience moments built around one theme: back in the day vs. now. Food trucks outside. Bring your people, seats are limited to 100.

### 4. Diabetes Resource Event (placeholder `REPLACE-WITH-DIABETES-EVENT-LINK`)
- Date: Saturday, September 26, 2026, 10:00 AM to 12:00 PM ET
- Location: 314 Hobson Street, Newark, NJ
- Price: TBD (free community event assumed)
- Description: Free community resource day. Learn how herbs, food, and daily habits can support healthy blood sugar.

After saving each event, copy its public link and paste it over the matching placeholder in both emails.
