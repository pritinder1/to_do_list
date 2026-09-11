#!/usr/bin/env python3
"""Builds the two TPH September 2026 emails (comedy show push + calendar)."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
# Hosted logo. Gmail does not render base64 data-URI images, so the logo must be a hosted HTTPS URL.
# Swap for a TruPortals media-library URL once uploaded (assets.cdn.filesafe.space/K03NyY3QgvKM66LM0Bl7/...).
LOGO = "https://storage.googleapis.com/content-assistant-images-persistent/0ebfceed-98ea-47c4-b4b9-02afb316765a.png"  # transparent PNG (assets/tph-logo.png) on permanent Google Cloud Storage via SearchAtlas

# ---- ONE PLACE TO SET LINKS -------------------------------------------------
COMEDY_LINK = "https://REPLACE-WITH-COMEDY-EVENT-LINK"          # TruPortals event link (Sept 25)
# One TruPortals event link per September event. Replace each placeholder once the events exist.
EVENT_LINKS = {
    "19": "https://REPLACE-WITH-ALLIANCE-EVENT-LINK",
    "24": "https://REPLACE-WITH-LSC-EVENT-LINK",
    "25": COMEDY_LINK,
    "26": "https://REPLACE-WITH-DIABETES-EVENT-LINK",
}
EVENT_CTA = {"19": "Details &amp; RSVP", "24": "Get Tickets", "25": "Get Tickets", "26": "Details &amp; RSVP"}
EVENTS_LINK = "https://app.thepeoplesherbalist.com/events"       # all-events page (confirm)
SHOP_LINK = "https://thepeoplesherbalist.com"
RADIO_LINK = "https://whcr.org"
WHATSAPP_LINK = "https://REPLACE-WITH-WHATSAPP-GROUP-LINK"       # The People's Herbal Circle
FLYER_IMG = ""  # optional: hosted URL of the September calendar flyer. Leave blank to skip.

STYLE = """<style type="text/css">
    body,table,td,a{-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}
    table,td{mso-table-lspace:0pt;mso-table-rspace:0pt;}
    table{border-collapse:collapse!important;}
    img{-ms-interpolation-mode:bicubic;border:0;outline:none;text-decoration:none;display:block;}
    body{margin:0!important;padding:0!important;width:100%!important;background:#e8ecdf;}
    a{text-decoration:none;}
    .container{width:100%;max-width:620px;}
    .brand-logo{width:300px;max-width:90%;height:auto;margin:0 auto;}
    .fluid-image{display:block;width:100%;max-width:620px;height:auto;margin:0 auto;}

    .date-cell{width:96px;}
    @media only screen and (max-width:640px){
      .container{width:100%!important;max-width:100%!important;}
      .outer-pad{padding:0!important;}
      .mobile-pad{padding-left:18px!important;padding-right:18px!important;text-align:center!important;}
      .hero-pad{padding:28px 20px 34px!important;}
      .headline{font-size:33px!important;line-height:38px!important;letter-spacing:-.5px!important;}
      .section-title{font-size:27px!important;line-height:32px!important;}
      .brand-logo{width:240px!important;max-width:90%!important;height:auto!important;margin:0 auto!important;}

      .fluid-image{width:100%!important;max-width:100%!important;height:auto!important;margin:0 auto!important;}
      .fact-cell{display:block!important;width:100%!important;max-width:100%!important;box-sizing:border-box!important;padding:6px 0!important;text-align:center!important;}
      .date-cell{width:84px!important;}
      .event-wrap{padding-left:16px!important;padding-right:16px!important;}
    }
  </style>"""

def button(href, label, bg="#3b4c2d", color="#ffffff"):
    """Bulletproof table button: fill comes from bgcolor + background-color on the td."""
    return (f'<table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin:0 auto;">'
            f'<tr><td align="center" bgcolor="{bg}" style="background-color:{bg};border-radius:999px;mso-padding-alt:16px 34px;">'
            f'<a href="{href}" target="_blank" style="display:inline-block;min-width:200px;padding:16px 34px;color:{color};font-family:Arial,Helvetica,sans-serif;'
            f'font-size:12px;line-height:15px;font-weight:900;letter-spacing:.8px;text-transform:uppercase;text-align:center;text-decoration:none;border-radius:999px;">'
            f'<font color="{color}">{label}</font></a></td></tr></table>')

def bulletproof(html):
    """Clients like the Gmail iOS app strip the background shorthand and <style>. Add bgcolor attrs and longhand background-color."""
    import re
    def fix(m):
        tag, before, color = m.group(1), m.group(2), m.group(3)
        return f'<{tag}{before}bgcolor="{color}" style="background-color:{color};'
    html = re.sub(r'<(td|table)([^>]*?)style="background:(#[0-9a-fA-F]{6});', fix, html)
    return html

def head(title, preheader):
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="x-apple-disable-message-reformatting">
  <title>{title}</title>
  {STYLE}
</head>
<body style="margin:0;padding:0;background:#e8ecdf;">
<div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">{preheader}</div>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#e8ecdf">
  <tr>
    <td class="outer-pad" align="center" style="padding:28px 10px;">
      <!--[if mso]><table role="presentation" width="620" cellspacing="0" cellpadding="0" border="0" align="center"><tr><td><![endif]-->
      <table role="presentation" class="container" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" bgcolor="#ffffff" style="width:100%;max-width:620px;background-color:#ffffff;box-shadow:0 18px 55px rgba(47,61,37,.14);margin:0 auto;">
"""

def brand_hero(kicker, headline, sub):
    return f"""
        <!-- BRAND HERO -->
        <tr>
          <td class="mobile-pad hero-pad" align="center" style="background:#ffffff;padding:30px 28px 36px;text-align:center;font-family:Arial,Helvetica,sans-serif;border-bottom:1px solid #e2e2e2;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" style="max-width:540px;margin:0 auto;">
              <tr>
                <td align="center" style="padding:0 0 22px;">
                  <a href="{SHOP_LINK}" target="_blank" style="display:inline-block;">
                    <img class="brand-logo" src="{LOGO}" width="300" alt="The People's Herbalist" style="display:block;width:300px;max-width:90%;height:auto;margin:0 auto;">
                  </a>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:0;">
                  <p style="margin:0 0 10px;color:#596b4b;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">{kicker}</p>
                  <h1 class="headline" style="margin:0 0 12px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:34px;line-height:40px;font-weight:700;letter-spacing:-.5px;">{headline}</h1>
                  <p style="margin:0 auto;max-width:480px;color:#4d5946;font-size:15px;line-height:24px;">{sub}</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
"""

def comedy_spotlight(intro_kicker, intro_title, intro_copy, cta_label, urgency_line=""):
    urgency = f'<p style="margin:14px auto 0;max-width:420px;color:#8a5a32;font-size:12px;line-height:18px;font-weight:900;letter-spacing:.6px;text-transform:uppercase;">{urgency_line}</p>' if urgency_line else ""
    return f"""
        <!-- COMEDY SHOW SPOTLIGHT -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#1f2818;padding:38px 32px 40px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 8px;color:#e6c781;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">{intro_kicker}</p>
            <h2 class="section-title" style="margin:0 0 6px;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:34px;line-height:40px;font-weight:700;">{intro_title}</h2>
            <p style="margin:0 0 22px;color:#e6c781;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:26px;font-style:italic;">Friday, September 25 &middot; Williams Center, Rutherford NJ</p>
            <p style="margin:0 auto 26px;max-width:470px;color:#d6dfcc;font-size:15px;line-height:24px;">{intro_copy}</p>

            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" style="max-width:520px;margin:0 auto 26px;">
              <tr>
                <td class="fact-cell" width="33%" valign="top" align="center" style="padding:0 6px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#2f3d25;border-radius:16px;">
                    <tr><td align="center" style="padding:16px 10px;">
                      <p style="margin:0 0 4px;color:#e6c781;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Doors</p>
                      <p style="margin:0;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:24px;font-weight:700;">7:00 PM</p>
                      <p style="margin:4px 0 0;color:#aeb99e;font-size:12px;line-height:17px;">Holistic happy hour<br>with DJ Santana</p>
                    </td></tr>
                  </table>
                </td>
                <td class="fact-cell" width="33%" valign="top" align="center" style="padding:0 6px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#2f3d25;border-radius:16px;">
                    <tr><td align="center" style="padding:16px 10px;">
                      <p style="margin:0 0 4px;color:#e6c781;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Showtime</p>
                      <p style="margin:0;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:24px;font-weight:700;">8:00 PM</p>
                      <p style="margin:4px 0 0;color:#aeb99e;font-size:12px;line-height:17px;">Comedy, talk show<br>and open mic</p>
                    </td></tr>
                  </table>
                </td>
                <td class="fact-cell" width="33%" valign="top" align="center" style="padding:0 6px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#2f3d25;border-radius:16px;">
                    <tr><td align="center" style="padding:16px 10px;">
                      <p style="margin:0 0 4px;color:#e6c781;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Tickets</p>
                      <p style="margin:0;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:20px;line-height:24px;font-weight:700;">$45</p>
                      <p style="margin:4px 0 0;color:#aeb99e;font-size:12px;line-height:17px;">Educators: buy one,<br>get one free</p>
                    </td></tr>
                  </table>
                </td>
              </tr>
            </table>

            {button(COMEDY_LINK, cta_label, "#e6c781", "#26321f")}
            {urgency}
          </td>
        </tr>
"""

def what_to_expect():
    return f"""
        <!-- WHAT TO EXPECT -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#ffffff;padding:36px 32px 10px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 7px;color:#596b4b;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">What The Night Looks Like</p>
            <h2 class="section-title" style="margin:0 0 10px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:31px;line-height:36px;font-weight:700;">Back in the day vs. now.</h2>
            <p style="margin:0 auto 22px;max-width:490px;color:#4d5946;font-size:14px;line-height:22px;">Danny hosts. Headliner Monique Lettice brings the laughs. In between, real conversation about how we grew up, how we live now, and what wellness looks like for our community. Think 70s, 80s and 90s energy, alcohol free.</p>
          </td>
        </tr>
        <tr>
          <td class="mobile-pad" align="center" style="background:#ffffff;padding:0 32px 36px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" style="max-width:540px;margin:0 auto;">
              <tr>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="left" style="padding:18px 20px;">
                      <p style="margin:0 0 4px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Holistic Happy Hour</p>
                      <p style="margin:0;color:#2f3d25;font-size:14px;line-height:21px;">Herbal mocktails made with real botanicals, a DJ set, and time to meet the people behind the brand.</p>
                    </td></tr>
                  </table>
                </td>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="left" style="padding:18px 20px;">
                      <p style="margin:0 0 4px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Live Comedy</p>
                      <p style="margin:0;color:#2f3d25;font-size:14px;line-height:21px;">Stand up, a talk show segment, and audience moments where you might end up part of the bit.</p>
                    </td></tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="left" style="padding:18px 20px;">
                      <p style="margin:0 0 4px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Food Trucks</p>
                      <p style="margin:0;color:#2f3d25;font-size:14px;line-height:21px;">Come hungry. Wood fired pizza and dessert trucks are lined up outside the venue.</p>
                    </td></tr>
                  </table>
                </td>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="left" style="padding:18px 20px;">
                      <p style="margin:0 0 4px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Bring Your People</p>
                      <p style="margin:0;color:#2f3d25;font-size:14px;line-height:21px;">Seats are limited to 100. Grab tickets for your crew now so you can sit together.</p>
                    </td></tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
"""

EVENTS = [
    ("SAT", "SEP", "19", "#2f6b3a", "Alliance Performance Training Facility", "Come see us at the Alliance community event. Samples, herbal education, and a chance to say hello in person.", "Banta Pl, Fair Lawn, NJ", "8:00 AM to 1:00 PM"),
    ("THU", "SEP", "24", "#1f3f7a", "Liberty Science Center After Dark: 70s Boogie Nights", "Adults only night at the Science Center. Disco, exhibits, and our herbal mocktail bar.", "Liberty State Park, Jersey City, NJ", "7:00 PM to 11:00 PM"),
    ("FRI", "SEP", "25", "#b58a1e", "Pass the Mic: Comedy &amp; Conversations", "Our big night. Holistic happy hour at 7, show at 8. Hosted by Danny with headliner Monique Lettice.", "Williams Center Cultural Arts Center, Rutherford, NJ", "7:00 PM to 9:00 PM"),
    ("SAT", "SEP", "26", "#8a4a22", "Diabetes Resource Event", "Free community resource day. Learn how herbs, food, and daily habits can support healthy blood sugar.", "314 Hobson Street, Newark, NJ", "10:00 AM to 12:00 PM"),
]

def event_row(day, mon, num, color, title, copy, place, time, highlight=False):
    bg = "#fbf6e6" if highlight else "#ffffff"
    border = "#e6c781" if highlight else "#dbe2d4"
    cta = f'<p style="margin:10px 0 0;"><a href="{EVENT_LINKS[num]}" target="_blank" style="color:#8a5a32;font-size:12px;line-height:18px;font-weight:900;letter-spacing:.6px;text-transform:uppercase;text-decoration:underline;">{EVENT_CTA[num]} &rsaquo;</a></p>'
    return f"""
              <tr>
                <td style="padding:0 0 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:{bg};border:1px solid {border};border-radius:18px;">
                    <tr>
                      <td class="date-cell" width="96" valign="top" align="center" style="padding:16px 8px 16px 16px;">
                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:{color};border-radius:14px;">
                          <tr><td align="center" style="padding:12px 4px;">
                            <p style="margin:0;color:#ffffff;font-family:Arial,Helvetica,sans-serif;font-size:10px;line-height:13px;font-weight:900;letter-spacing:1.4px;">{day}</p>
                            <p style="margin:0;color:#ffffff;font-family:Arial,Helvetica,sans-serif;font-size:10px;line-height:13px;font-weight:700;letter-spacing:1.4px;">{mon}</p>
                            <p style="margin:2px 0 0;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:30px;line-height:32px;font-weight:700;">{num}</p>
                          </td></tr>
                        </table>
                      </td>
                      <td valign="top" align="left" style="padding:16px 18px 16px 8px;font-family:Arial,Helvetica,sans-serif;">
                        <h3 style="margin:0 0 5px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:24px;font-weight:700;">{title}</h3>
                        <p style="margin:0 0 8px;color:#596356;font-size:13px;line-height:20px;">{copy}</p>
                        <p style="margin:0;color:#2f3d25;font-size:12px;line-height:18px;font-weight:700;">&#128205; {place}</p>
                        <p style="margin:0;color:#2f3d25;font-size:12px;line-height:18px;font-weight:700;">&#128337; {time}</p>
                        {cta}
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>"""

def calendar_section():
    rows = "".join(event_row(*e, highlight=(e[2] == "25")) for e in EVENTS)
    flyer = f"""
        <tr>
          <td align="center" style="background:#dde8d5;padding:0 30px 18px;font-size:0;line-height:0;">
            <a href="{EVENTS_LINK}" target="_blank" style="display:inline-block;"><img class="fluid-image" src="{FLYER_IMG}" width="540" alt="The People's Herbalist September 2026 Calendar of Events" style="display:block;width:100%;max-width:540px;height:auto;margin:0 auto;border-radius:18px;"></a>
          </td>
        </tr>""" if FLYER_IMG else ""
    return f"""
        <!-- SEPTEMBER CALENDAR -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#dde8d5;padding:34px 32px 18px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 7px;color:#596b4b;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">September 2026 Calendar of Events</p>
            <h2 class="section-title" style="margin:0 0 9px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:31px;line-height:36px;font-weight:700;">Where to find us this month.</h2>
            <p style="margin:0 auto;max-width:470px;color:#4d5946;font-size:14px;line-height:22px;">Connect. Community. Wellness. Nature. Four stops across New Jersey, and we would love to see you at any of them.</p>
          </td>
        </tr>{flyer}
        <tr>
          <td class="mobile-pad event-wrap" align="center" style="background:#dde8d5;padding:0 30px 8px;font-family:Arial,Helvetica,sans-serif;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" style="max-width:540px;margin:0 auto;">{rows}
            </table>
          </td>
        </tr>
        <tr>
          <td class="mobile-pad" align="center" style="background:#dde8d5;padding:8px 32px 34px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            {button(EVENTS_LINK, "See All Events", "#3b4c2d", "#ffffff")}
          </td>
        </tr>
"""

def radio_and_circle():
    return f"""
        <!-- RADIO + WHATSAPP -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#ffffff;padding:34px 32px 34px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center" style="max-width:540px;margin:0 auto;">
              <tr>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="center" style="padding:20px 18px;">
                      <p style="margin:0 0 6px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Every Wednesday &middot; 7 to 8 AM</p>
                      <p style="margin:0 0 6px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:24px;font-weight:700;">The People's Healing Hour</p>
                      <p style="margin:0 0 12px;color:#596356;font-size:13px;line-height:20px;">Live on 90.3 FM and WHCR.org. Call in at <a href="tel:12126506903" style="color:#2f3d25;font-weight:700;text-decoration:underline;">212-650-6903</a> and let your voice be heard.</p>
                      <a href="{RADIO_LINK}" target="_blank" style="color:#3b4c2d;font-size:12px;line-height:18px;font-weight:900;letter-spacing:.6px;text-transform:uppercase;text-decoration:underline;">Listen Live &rsaquo;</a>
                    </td></tr>
                  </table>
                </td>
                <td class="fact-cell" width="50%" valign="top" style="padding:0 6px 12px;">
                  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#f7f3e9;border:1px solid #e5dccb;border-radius:16px;">
                    <tr><td align="center" style="padding:20px 18px;">
                      <p style="margin:0 0 6px;color:#8a5a32;font-size:10px;line-height:14px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;">Stay Connected</p>
                      <p style="margin:0 0 6px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:19px;line-height:24px;font-weight:700;">The People's Herbal Circle</p>
                      <p style="margin:0 0 12px;color:#596356;font-size:13px;line-height:20px;">Our WhatsApp group for updates, event reminders, herbal tips and more.</p>
                      <a href="{WHATSAPP_LINK}" target="_blank" style="color:#3b4c2d;font-size:12px;line-height:18px;font-weight:900;letter-spacing:.6px;text-transform:uppercase;text-decoration:underline;">Join The Group &rsaquo;</a>
                    </td></tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
"""

def closing_cta(title, copy, cta_label):
    return f"""
        <!-- CLOSING CTA -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#2f3d25;padding:38px 32px 40px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 8px;color:#e6c781;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">Friday, September 25</p>
            <h2 class="section-title" style="margin:0 0 10px;color:#ffffff;font-family:Georgia,'Times New Roman',serif;font-size:31px;line-height:36px;font-weight:700;">{title}</h2>
            <p style="margin:0 auto 24px;max-width:460px;color:#d6dfcc;font-size:14px;line-height:22px;">{copy}</p>
            {button(COMEDY_LINK, cta_label, "#e6c781", "#26321f")}
            <p style="margin:18px 0 0;color:#aeb99e;font-size:12px;line-height:18px;">Rooted in community. Growing wellness. Naturally.</p>
          </td>
        </tr>
"""

FOOTER = """
        <!-- FOOTER -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#1f2818;padding:26px 32px 30px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 7px;color:#d6dfcc;font-size:11px;line-height:17px;font-weight:900;letter-spacing:1px;">The People's Herbalist &middot; New Jersey</p>
            <p style="margin:0 0 9px;color:#aeb99e;font-size:10px;line-height:16px;">Herbal products and educational content are for general wellness purposes and are not intended to diagnose, treat, cure, or prevent disease. Individual responses vary. If you are pregnant, nursing, taking medication, or managing a health condition, speak with a qualified healthcare professional before adding new herbs to your routine.</p>
            <p style="margin:0;font-size:10px;line-height:16px;"><a href="{{unsubscribe_link}}" style="color:#d6dfcc;text-decoration:underline;">Unsubscribe</a></p>
          </td>
        </tr>

      </table>
      <!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
</table>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# EMAIL 1: Comedy show push + September calendar
# ---------------------------------------------------------------------------
E1_SUBJECT = "Comedy, mocktails and a DJ. Sept 25 is our night 🎤"
E1_PREVIEW = "Danny hosts Pass the Mic at the Williams Center. Plus every September event in one place."
E1_RESEND_SUBJECT = "Still thinking about Sept 25? Seats are going."

email1 = head("Pass the Mic: Comedy & Conversations | The People's Herbalist", E1_PREVIEW)
email1 += brand_hero(
    "You Are Invited",
    "Save your Friday night. We planned a good one.",
    "Hey {{contact.first_name}}, Danny here. On September 25 we are turning the Williams Center into a holistic happy hour and comedy show, and I want you in the room.",
)
email1 += comedy_spotlight(
    "Pass The Mic",
    "Comedy &amp; Conversations",
    "One night. Real laughs, real conversation, herbal mocktails in your hand, and a room full of people who get it. No hangover in the morning.",
    "Get My Tickets",
    "Only 100 seats. Once they are gone, they are gone.",
)
email1 += what_to_expect()
email1 += calendar_section()
email1 += radio_and_circle()
email1 += closing_cta(
    "Come laugh with us.",
    "Grab your ticket, text a friend, and give yourself a Friday night that is actually worth looking forward to.",
    "Reserve My Seat",
)
email1 += FOOTER

# ---------------------------------------------------------------------------
# EMAIL 2: Final call reminder (send Tue Sept 22 or Wed Sept 23)
# ---------------------------------------------------------------------------
E2_SUBJECT = "This Friday: Pass the Mic. Last call for seats 🎤"
E2_PREVIEW = "Holistic happy hour at 7, show at 8, food trucks outside. Grab your ticket before Friday."
E2_RESEND_SUBJECT = "Tomorrow night. Are you coming?"

email2 = head("This Friday: Pass the Mic | The People's Herbalist", E2_PREVIEW)
email2 += brand_hero(
    "This Friday",
    "Last call for Friday night.",
    "{{contact.first_name}}, quick one from Danny. The comedy show is this Friday and the room is filling up. If you have been meaning to grab a ticket, this is the nudge.",
)
email2 += comedy_spotlight(
    "Pass The Mic",
    "Comedy &amp; Conversations",
    "Danny hosts. Monique Lettice headlines. DJ Santana opens the night with a holistic happy hour, and the food trucks are parked outside. Bring your people.",
    "Grab My Ticket Now",
    "Doors 7:00 PM. Show 8:00 PM. Limited seats left.",
)
email2 += what_to_expect()
email2 += f"""
        <!-- QUICK SEPTEMBER REMINDER -->
        <tr>
          <td class="mobile-pad" align="center" style="background:#dde8d5;padding:32px 32px 30px;text-align:center;font-family:Arial,Helvetica,sans-serif;">
            <p style="margin:0 0 7px;color:#596b4b;font-size:10px;line-height:14px;font-weight:900;letter-spacing:2.2px;text-transform:uppercase;">Also This Week</p>
            <h2 class="section-title" style="margin:0 0 10px;color:#1f2818;font-family:Georgia,'Times New Roman',serif;font-size:27px;line-height:32px;font-weight:700;">Make it a full week with us.</h2>
            <p style="margin:0 auto 6px;max-width:470px;color:#2f3d25;font-size:14px;line-height:22px;"><strong>Thu, Sept 24:</strong> Liberty Science Center After Dark, 70s Boogie Nights, 7 to 11 PM, Jersey City.</p>
            <p style="margin:0 auto 6px;max-width:470px;color:#2f3d25;font-size:14px;line-height:22px;"><strong>Fri, Sept 25:</strong> Pass the Mic Comedy &amp; Conversations, 7 to 9 PM, Rutherford.</p>
            <p style="margin:0 auto 18px;max-width:470px;color:#2f3d25;font-size:14px;line-height:22px;"><strong>Sat, Sept 26:</strong> Diabetes Resource Event, 10 AM to 12 PM, Newark.</p>
            <a href="{EVENTS_LINK}" target="_blank" style="color:#3b4c2d;font-size:12px;line-height:18px;font-weight:900;letter-spacing:.6px;text-transform:uppercase;text-decoration:underline;">See The Full September Calendar &rsaquo;</a>
          </td>
        </tr>
"""
email2 += closing_cta(
    "See you Friday?",
    "Two minutes to grab a ticket. Then all you have to do is show up and enjoy the night.",
    "Get My Tickets",
)
email2 += FOOTER

os.makedirs(OUT, exist_ok=True)
email1 = bulletproof(email1)
email2 = bulletproof(email2)
open(os.path.join(OUT, "01-comedy-show-september-calendar.html"), "w").write(email1)
open(os.path.join(OUT, "02-comedy-show-final-call.html"), "w").write(email2)
open(os.path.join(OUT, "SEND-SETTINGS.md"), "w").write(f"""# TPH September 2026 email queue

Sub-account: The People's Herbalist (TruPortals location `K03NyY3QgvKM66LM0Bl7`)
Sender name: Danny | The People's Herbalist
Sender email: danny@thepeoplesherbalist.com (domain reply.thepeoplesherbalist.com auto-selects)
Test email: hello@trucreatives.com
Timezone: America/New_York

## Links to set before pasting (top of build_emails.py or find-and-replace in the HTML)
| Placeholder | Replace with |
|---|---|
| `{COMEDY_LINK}` | TruPortals event link for the Sept 25 comedy show |
| `{EVENTS_LINK}` | All-events page (confirm the URL from the events section) |
| `{WHATSAPP_LINK}` | The People's Herbal Circle WhatsApp invite link |
| `FLYER_IMG` (optional) | Hosted URL of the September calendar flyer if you want the image above the list |

## Email 1: Comedy show push + September calendar
- File: `01-comedy-show-september-calendar.html`
- Send: Tue Sept 15, 10:00 AM ET
- Subject: {E1_SUBJECT}
- Preview: {E1_PREVIEW}
- Resend to unopened after 12h, subject: {E1_RESEND_SUBJECT}
- Track clicks ON, UTM ON

## Email 2: Final call
- File: `02-comedy-show-final-call.html`
- Send: Wed Sept 23, 10:00 AM ET (or Tue Sept 22 if the Thursday LSC event is also being pushed)
- Subject: {E2_SUBJECT}
- Preview: {E2_PREVIEW}
- Resend to unopened after 12h, subject: {E2_RESEND_SUBJECT}
- Track clicks ON, UTM ON

## Facts in the copy to confirm with Danny before sending
- Headliner name spelling: "Monique Lettice" (meeting notes also show "Latisse")
- Ticket price $45 and the educator buy one get one offer
- Times: flyer says 7:00 to 9:00 PM; Sept 1 meeting notes say happy hour 7 to 8, show at 8
- Food trucks (wood fired pizza and dessert) were "pending" as of Sept 1
- 100 seat capacity
""")
print("wrote", OUT)
