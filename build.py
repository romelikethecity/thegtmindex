#!/usr/bin/env python3
"""
Build script for The GTM Index (thegtmindex.com).
Hub site with 18 internal resource directory pages.
Authority brand: Navy + Amber, Inter font, light mode.
"""

import os
import sys
import json
from datetime import datetime

SITE_NAME = "The GTM Index"
BASE_URL = "https://thegtmindex.com"
SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
YEAR = datetime.now().year

# Import resource data from shared file
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _build_all_resources import RESOURCE_DATA

# =============================================================================
# CONTENT SITE MAP — maps each niche to its dedicated content site
# =============================================================================

CONTENT_SITES = {
    "gtm-engineers": {"name": "GTME Pulse", "url": "https://gtmepulse.com", "desc": "GTM engineer salary data, tools, and career intelligence"},
    "presales": {"name": "PreSales Pulse", "url": "https://presalespulse.com", "desc": "Solutions engineer salary benchmarks, tools, and career resources"},
    "fractional": {"name": "Fractional Pulse", "url": "https://fractionalpulse.com", "desc": "Fractional executive marketplaces, tax guides, and career playbooks"},
    "revops": {"name": "The RevOps Report", "url": "https://therevopsreport.com", "desc": "RevOps salary data, tool comparisons, and operations insights"},
    "revenue-leaders": {"name": "The CRO Report", "url": "https://thecroreport.com", "desc": "CRO and VP Sales compensation data, job market intel, and leadership resources"},
    "b2b-sales": {"name": "B2B Sales Tools", "url": "https://b2bsalestools.com", "desc": "Opinionated reviews of sales software for prospecting, engagement, and closing"},
    "data-stack": {"name": "DataStack Guide", "url": "https://datastackguide.com", "desc": "200+ data tool reviews, architecture guides, and stack comparisons"},
    "ai-careers": {"name": "AI Market Pulse", "url": "https://theaimarketpulse.com", "desc": "AI engineer salary premiums, skill demand, and career trajectory data"},
    "medical-devices": {"name": "Device Pulse", "url": "https://thedevicepulse.com", "desc": "Medical device cost intelligence and physician community resources"},
    "saas-reviews": {"name": "Sultan of SaaS", "url": "https://sultanofsaas.com", "desc": "Honest SaaS reviews and comparison guides for SMB buyers"},
    "fde": {"name": "FDE Pulse", "url": "https://fdepulse.com", "desc": "Forward deployed engineer jobs, salary benchmarks, and market intelligence"},
    "marketing-ops": {"name": "MOPs Report", "url": "https://mopsreport.com", "desc": "Marketing ops salary data, automation tool reviews, and career resources"},
    "demand-gen": {"name": "Demand Gen Insider", "url": "https://demandgeninsider.com", "desc": "Demand generation salary benchmarks, tool reviews, and pipeline strategy"},
    "abm": {"name": "The ABM Pulse", "url": "https://theabmpulse.com", "desc": "Account-based marketing salary data, platform reviews, and practitioner insights"},
    "customer-success": {"name": "The CS Pulse", "url": "https://thecspulse.com", "desc": "Customer success salary benchmarks, tool reviews, and career intelligence"},
    "sellers": {"name": "The Seller Report", "url": "https://thesellerreport.com", "desc": "Sales career intelligence for SDRs and AEs — comp data, tools, and market trends"},
    "partner-channel": {"name": "Partner Channels", "url": "https://partnerchannels.com", "desc": "Channel sales and partner program directories, strategy resources, and community hubs"},
    "sales-enablement": {"name": "SE Nablers", "url": "https://senablers.com", "desc": "Sales enablement platform reviews, career resources, and practitioner communities"},
    "product-launches": {"name": "The Launch Index", "url": "https://thelaunchindex.com", "desc": "Product launch data and market trends from 42,000+ launches tracked since 2021"},
}

# =============================================================================
# DIRECTORY DATA — all links are internal now
# =============================================================================

DIRECTORIES = [
    {"id": "gtm-engineers", "title": "GTM Engineers", "icon": "&#9889;", "description": "Newsletters, tools, and communities for technical revenue builders who wire together the systems that drive pipeline.", "niche": "gtm-engineers"},
    {"id": "presales", "title": "Pre-Sales / SEs", "icon": "&#128161;", "description": "Blogs, demo platforms, and community hubs for solutions engineers and technical sellers.", "niche": "presales"},
    {"id": "fractional", "title": "Fractional Executives", "icon": "&#128188;", "description": "Job boards, communities, and playbooks for fractional CROs, CMOs, CTOs, and CFOs.", "niche": "fractional"},
    {"id": "revops", "title": "RevOps", "icon": "&#9881;", "description": "Revenue operations tools, newsletters, and career resources for ops professionals.", "niche": "revops"},
    {"id": "revenue-leaders", "title": "Revenue Leaders", "icon": "&#128640;", "description": "CRO and VP Sales resources. Compensation data, market intel, and peer communities.", "niche": "revenue-leaders"},
    {"id": "b2b-sales", "title": "B2B Sales", "icon": "&#128202;", "description": "Sales tools, prospecting resources, and career content for account executives and SDRs.", "niche": "b2b-sales"},
    {"id": "data-stack", "title": "Data Stack", "icon": "&#128451;", "description": "Data engineering tools, architecture guides, and community resources for the modern data stack.", "niche": "data-stack"},
    {"id": "ai-careers", "title": "AI Careers", "icon": "&#129302;", "description": "AI engineering job boards, salary data, newsletters, and career resources.", "niche": "ai-careers"},
    {"id": "geo", "title": "GEO & AEO", "icon": "&#128270;", "description": "Tools, newsletters, and communities for getting your brand cited in ChatGPT, Perplexity, Claude, and Google AI Overviews.", "niche": "geo"},
    {"id": "medical-devices", "title": "Medical Devices", "icon": "&#127973;", "description": "Equipment intelligence, cost guides, and physician communities for capital device purchasing.", "niche": "medical-devices"},
    {"id": "saas-reviews", "title": "SaaS Reviews", "icon": "&#11088;", "description": "Opinionated SaaS review sites, comparison tools, and software evaluation resources.", "niche": "saas-reviews"},
    {"id": "fde", "title": "Forward Deployed Engineers", "icon": "&#128296;", "description": "Job boards, salary benchmarks, and community resources for forward deployed engineers.", "niche": "fde"},
    {"id": "marketing-ops", "title": "Marketing Ops", "icon": "&#128231;", "description": "MOPs newsletters, automation tools, and career resources for marketing operations professionals.", "niche": "marketing-ops"},
    {"id": "demand-gen", "title": "Demand Gen", "icon": "&#128200;", "description": "Demand generation blogs, ABM tools, and community resources for pipeline builders.", "niche": "demand-gen"},
    {"id": "abm", "title": "Account-Based Marketing", "icon": "&#127919;", "description": "ABM platforms, playbooks, and community resources for account-based practitioners.", "niche": "abm"},
    {"id": "customer-success", "title": "Customer Success", "icon": "&#129309;", "description": "CS newsletters, career resources, and community hubs for customer success professionals.", "niche": "customer-success"},
    {"id": "sellers", "title": "B2B Sellers", "icon": "&#128176;", "description": "Prospecting tools, sales newsletters, and career resources for individual contributors in sales.", "niche": "sellers"},
    {"id": "partner-channel", "title": "Partner & Channel", "icon": "&#129309;", "description": "Partner program directories, channel strategy resources, and ecosystem community hubs.", "niche": "partner-channel"},
    {"id": "sales-enablement", "title": "Sales Enablement", "icon": "&#128218;", "description": "Enablement platforms, content management tools, and community resources for enablement pros.", "niche": "sales-enablement"},
    {"id": "product-launches", "title": "Product Launches", "icon": "&#128506;", "description": "Launch trackers, market intelligence tools, and communities for product researchers and GTM teams.", "niche": "product-launches"},
]

# =============================================================================
# CSS
# =============================================================================

CSS = """
:root {
    --navy: #1B2838;
    --navy-deep: #0F1923;
    --amber: #F59E0B;
    --amber-light: #FBBF24;
    --amber-dark: #D97706;
    --bg: #FAFAFA;
    --bg-white: #FFFFFF;
    --text: #1F2937;
    --text-muted: #6B7280;
    --text-light: #94A3B8;
    --border: #E5E7EB;
    --icon-bg: #FEF3C7;
    --radius: 10px;
    --shadow: 0 1px 3px rgba(0,0,0,0.08);
    --shadow-hover: 0 4px 12px rgba(245,158,11,0.12);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

a { color: inherit; text-decoration: none; }

/* Header */
.header {
    background: var(--navy);
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
}
.header__inner {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.logo { font-size: 18px; font-weight: 700; color: var(--amber); }
.logo span { color: #fff; }
.nav { display: flex; gap: 24px; align-items: center; }
.nav a { color: var(--text-light); font-size: 14px; font-weight: 500; transition: color 150ms; }
.nav a:hover { color: #fff; }

.menu-toggle { display: none; background: none; border: none; cursor: pointer; padding: 8px; }
.menu-toggle span { display: block; width: 22px; height: 2px; background: #fff; margin: 5px 0; transition: 150ms; }

/* Hero */
.hero {
    padding: 140px 24px 80px;
    text-align: center;
    background: linear-gradient(180deg, var(--navy) 0%, var(--navy-deep) 100%);
}
.hero h1 { font-size: clamp(28px, 5vw, 44px); font-weight: 700; color: #fff; margin-bottom: 16px; letter-spacing: -0.5px; line-height: 1.15; }
.hero h1 em { color: var(--amber); font-style: normal; }
.hero p { font-size: 18px; color: var(--text-light); max-width: 600px; margin: 0 auto 32px; line-height: 1.6; }
.hero .cta { display: inline-block; background: var(--amber); color: var(--navy); padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 15px; transition: background 150ms; }
.hero .cta:hover { background: var(--amber-light); }

/* Stats */
.stats { display: flex; justify-content: center; gap: 48px; margin-top: 48px; }
.stat { text-align: center; }
.stat__number { font-size: 32px; font-weight: 700; color: var(--amber); }
.stat__label { font-size: 13px; color: var(--text-light); margin-top: 4px; }

/* Cards Grid */
.directories { padding: 64px 24px 80px; max-width: 1100px; margin: 0 auto; }
.directories h2 { font-size: 24px; font-weight: 700; margin-bottom: 8px; color: var(--text); }
.directories .subtitle { color: var(--text-muted); margin-bottom: 32px; font-size: 15px; }
.card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.card { background: var(--bg-white); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; transition: border-color 200ms, box-shadow 200ms; display: flex; flex-direction: column; }
.card:hover { border-color: var(--amber); box-shadow: var(--shadow-hover); }
.card__icon { width: 42px; height: 42px; background: var(--icon-bg); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin-bottom: 16px; }
.card h3 { font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
.card p { font-size: 13px; color: var(--text-muted); line-height: 1.55; margin-bottom: 16px; flex: 1; }
.card__link { font-size: 13px; color: var(--amber-dark); font-weight: 600; }
.card__link:hover { color: var(--amber); }

/* Newsletter CTA */
.newsletter { padding: 64px 24px; text-align: center; background: var(--bg-white); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.newsletter h2 { font-size: 24px; font-weight: 700; margin-bottom: 8px; }
.newsletter p { color: var(--text-muted); margin-bottom: 24px; font-size: 15px; }
.newsletter-form { display: flex; max-width: 440px; margin: 0 auto; gap: 8px; }
.newsletter-form input { flex: 1; padding: 12px 16px; border: 1px solid var(--border); border-radius: 8px; font-size: 14px; font-family: inherit; outline: none; }
.newsletter-form input:focus { border-color: var(--amber); }
.newsletter-form button { background: var(--amber); color: var(--navy); padding: 12px 24px; border: none; border-radius: 8px; font-weight: 600; font-size: 14px; cursor: pointer; font-family: inherit; transition: background 150ms; white-space: nowrap; }
.newsletter-form button:hover { background: var(--amber-light); }
.newsletter .msg { margin-top: 12px; font-size: 13px; }
.newsletter .msg.success { color: #059669; }
.newsletter .msg.error { color: #DC2626; }

/* Footer */
.footer { background: var(--navy); color: var(--text-light); padding: 48px 24px 32px; }
.footer__inner { max-width: 1100px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
.footer__brand { font-size: 16px; font-weight: 700; color: var(--amber); }
.footer__brand span { color: #fff; }
.footer__copy { font-size: 13px; color: rgba(255,255,255,0.4); }

/* About + Resource pages */
.page { padding: 100px 24px 64px; max-width: 760px; margin: 0 auto; }
.page h1 { font-size: 32px; font-weight: 700; margin-bottom: 20px; line-height: 1.2; letter-spacing: -0.5px; }
.page p { font-size: 16px; color: var(--text-muted); margin-bottom: 16px; line-height: 1.7; }
.page h2 { font-size: 20px; font-weight: 600; margin: 32px 0 12px; }
.page a { color: var(--amber-dark); }
.page a:hover { color: var(--amber); }

/* Resource page specific */
.rp-breadcrumb { font-size: 13px; color: var(--text-muted); margin-bottom: 24px; }
.rp-breadcrumb a { text-decoration: none; color: var(--amber-dark); }
.rp-intro { margin-bottom: 40px; }
.rp-intro p { font-size: 16px; color: #4B5563; line-height: 1.7; margin-bottom: 12px; }
.rp-section { margin-bottom: 48px; }
.rp-section-title { font-size: 22px; font-weight: 700; margin-bottom: 20px; padding-bottom: 8px; border-bottom: 2px solid #F3F4F6; color: var(--text); }
.rp-item { margin-bottom: 24px; }
.rp-item-title { font-size: 16px; font-weight: 600; margin-bottom: 4px; }
.rp-item-title a { text-decoration: underline; text-decoration-color: var(--border); text-underline-offset: 3px; color: var(--text); }
.rp-item-title a:hover { text-decoration-color: var(--text-muted); }
.rp-item-desc { font-size: 14px; color: var(--text-muted); line-height: 1.6; }
.rp-badge { display: inline-block; background: var(--icon-bg); color: #92400E; font-size: 11px; padding: 2px 8px; border-radius: 4px; font-weight: 600; vertical-align: middle; margin-left: 4px; }
.rp-curation { margin-top: 48px; padding: 32px; background: #F9FAFB; border-radius: 12px; border: 1px solid var(--border); }
.rp-curation h2 { font-size: 18px; font-weight: 600; margin-bottom: 12px; color: var(--text); }
.rp-curation p { font-size: 14px; color: var(--text-muted); line-height: 1.7; }
.rp-back { display: inline-block; margin-top: 32px; font-size: 14px; color: var(--amber-dark); font-weight: 500; }

/* Mobile */
.mobile-nav { display: none; position: fixed; top: 0; right: -100%; width: 260px; height: 100vh; background: var(--navy-deep); z-index: 200; padding: 80px 24px 24px; transition: right 250ms; }
.mobile-nav.active { right: 0; }
.mobile-nav a { display: block; color: var(--text-light); font-size: 16px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.06); }
.mobile-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 199; }
.mobile-overlay.active { display: block; }

@media (max-width: 900px) { .card-grid { grid-template-columns: repeat(2, 1fr); } .stats { gap: 32px; } }
@media (max-width: 640px) { .card-grid { grid-template-columns: 1fr; } .nav { display: none; } .menu-toggle { display: block; } .hero { padding: 120px 20px 60px; } .hero p { font-size: 16px; } .stats { flex-direction: column; gap: 16px; } .newsletter-form { flex-direction: column; } .footer__inner { flex-direction: column; gap: 12px; text-align: center; } .page { padding: 80px 16px 48px; } .page h1 { font-size: 26px; } }
.footer ul li a { color: rgba(255,255,255,0.5); text-decoration: none; font-size: 13px; transition: color 150ms; }
.footer ul li a:hover { color: var(--amber); }
@media (max-width: 768px) { .footer div[style*="grid-template-columns"] { grid-template-columns: repeat(2, 1fr) !important; } }
@media (max-width: 480px) { .footer div[style*="grid-template-columns"] { grid-template-columns: 1fr !important; } }
"""

# =============================================================================
# HTML COMPONENTS
# =============================================================================

def get_head(title, description, canonical_path="/", extra_head=""):
    full_title = f"{title} | {SITE_NAME}" if title != SITE_NAME else title
    canonical = f"{BASE_URL}{canonical_path}"
    desc = description[:160]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-V2GCLCTZHE"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-V2GCLCTZHE');
</script>
{extra_head}
</head>"""


def get_header():
    return """
<header class="header">
  <div class="header__inner">
    <a href="/" class="logo">The GTM <span>Index</span></a>
    <nav class="nav">
      <a href="/#directories">Browse</a>
      <a href="/about/">About</a>
      <a href="/#subscribe">Newsletter</a>
    </nav>
    <button class="menu-toggle" onclick="document.querySelector('.mobile-nav').classList.toggle('active');document.querySelector('.mobile-overlay').classList.toggle('active');" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="mobile-overlay" onclick="this.classList.remove('active');document.querySelector('.mobile-nav').classList.remove('active');"></div>
<nav class="mobile-nav">
  <a href="/#directories">Browse</a>
  <a href="/about/">About</a>
  <a href="/#subscribe">Newsletter</a>
</nav>"""


def get_footer():
    # Build site links grouped into columns
    col1_sites = ["revenue-leaders", "revops", "b2b-sales", "sellers", "presales", "sales-enablement"]
    col2_sites = ["gtm-engineers", "fde", "ai-careers", "data-stack", "marketing-ops", "demand-gen"]
    col3_sites = ["fractional", "abm", "customer-success", "partner-channel", "medical-devices", "saas-reviews", "product-launches"]

    def site_links(keys):
        links = ""
        for k in keys:
            s = CONTENT_SITES.get(k)
            if s:
                links += f'<li><a href="{s["url"]}">{s["name"]}</a></li>\n'
        return links

    return f"""
<footer class="footer" style="padding:48px 24px 32px;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:32px;margin-bottom:32px;font-size:13px;">
      <div>
        <div class="footer__brand" style="margin-bottom:16px;">The GTM <span>Index</span></div>
        <p style="color:rgba(255,255,255,0.5);font-size:12px;line-height:1.5;">Curated directories for every go-to-market role.</p>
      </div>
      <div>
        <div style="color:#fff;font-weight:600;margin-bottom:12px;font-size:13px;">Sales & Revenue</div>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
          {site_links(col1_sites)}
        </ul>
      </div>
      <div>
        <div style="color:#fff;font-weight:600;margin-bottom:12px;font-size:13px;">Engineering & Data</div>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
          {site_links(col2_sites)}
        </ul>
      </div>
      <div>
        <div style="color:#fff;font-weight:600;margin-bottom:12px;font-size:13px;">Strategy & Growth</div>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;">
          {site_links(col3_sites)}
        </ul>
      </div>
    </div>
    <div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:16px;display:flex;justify-content:space-between;align-items:center;">
      <div class="footer__copy">&copy; {YEAR} {SITE_NAME}. All rights reserved.</div>
      <div style="font-size:12px;color:rgba(255,255,255,0.4);"><a href="/about/" style="color:rgba(255,255,255,0.5);">About</a></div>
    </div>
  </div>
</footer>"""


def get_newsletter_section():
    return """
<section class="newsletter" id="subscribe">
  <h2>Stay Updated</h2>
  <p>Get notified when we add new directories or update existing ones.</p>
  <form class="newsletter-form" id="signup-form" onsubmit="return handleSignup(event)">
    <input type="email" name="email" placeholder="you@company.com" required>
    <button type="submit">Subscribe</button>
  </form>
  <div class="msg" id="signup-msg"></div>
</section>
<script>
async function handleSignup(e) {
  e.preventDefault();
  const form = e.target;
  const email = form.email.value;
  const btn = form.querySelector('button');
  const msg = document.getElementById('signup-msg');
  btn.disabled = true;
  btn.textContent = 'Sending...';
  try {
    const res = await fetch('https://newsletter-subscribe.rome-workers.workers.dev/subscribe', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email, list: 'gtm-index'})
    });
    const data = await res.json();
    if (data.ok) {
      msg.className = 'msg success';
      msg.textContent = 'You\\'re in. We\\'ll keep you posted.';
      form.email.value = '';
    } else {
      throw new Error(data.error || 'Something went wrong');
    }
  } catch(err) {
    msg.className = 'msg error';
    msg.textContent = err.message;
  }
  btn.disabled = false;
  btn.textContent = 'Subscribe';
}
</script>"""


# =============================================================================
# PAGE GENERATORS
# =============================================================================

def build_homepage():
    """Generate the landing page with internal directory links."""
    total_resources = sum(
        sum(len(s["items"]) for s in RESOURCE_DATA.get(d["niche"], {}).get("sections", []))
        for d in DIRECTORIES
    )

    cards_html = ""
    for d in DIRECTORIES:
        data = RESOURCE_DATA.get(d["niche"], {})
        count = sum(len(s["items"]) for s in data.get("sections", []))
        cards_html += f"""
    <a href="/{d['id']}/" class="card">
      <div class="card__icon">{d['icon']}</div>
      <h3>{d['title']}</h3>
      <p>{d['description']}</p>
      <div class="card__link">{count} resources curated &rarr;</div>
    </a>"""

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": BASE_URL,
        "description": "Hand-curated directories of the best newsletters, tools, communities, and content for every go-to-market role.",
        "publisher": {"@type": "Organization", "name": SITE_NAME}
    }, indent=2)

    html = get_head(SITE_NAME, "Hand-curated newsletters, tools, communities, and content for every go-to-market role. Organized by function.", "/", f'<script type="application/ld+json">\n{schema}\n</script>')
    html += f"""
<body>
{get_header()}

<section class="hero">
  <h1>Best resources for <em>go-to-market</em>.</h1>
  <p>Hand-curated newsletters, tools, communities, and content. Organized by function.</p>
  <a href="#directories" class="cta">Browse All Directories</a>
  <div class="stats">
    <div class="stat">
      <div class="stat__number">{len(DIRECTORIES)}</div>
      <div class="stat__label">Directories</div>
    </div>
    <div class="stat">
      <div class="stat__number">{total_resources}+</div>
      <div class="stat__label">Resources Curated</div>
    </div>
    <div class="stat">
      <div class="stat__number">6</div>
      <div class="stat__label">Categories per Directory</div>
    </div>
  </div>
</section>

<section class="directories" id="directories">
  <h2>Browse by Role</h2>
  <p class="subtitle">Each directory covers newsletters, blogs, tools, communities, podcasts, and courses.</p>
  <div class="card-grid">
    {cards_html}
  </div>
</section>

{get_newsletter_section()}
{get_footer()}
</body>
</html>"""

    os.makedirs(SITE_DIR, exist_ok=True)
    with open(os.path.join(SITE_DIR, "index.html"), "w") as f:
        f.write(html)
    print(f"  Built: index.html ({len(DIRECTORIES)} directories, {total_resources} resources)")


def build_resource_page(directory):
    """Generate a single resource directory page."""
    niche = directory["niche"]
    data = RESOURCE_DATA.get(niche)
    if not data or not any(s["items"] for s in data.get("sections", [])):
        print(f"  Skipped: /{directory['id']}/ (no data)")
        return

    slug = directory["id"]
    title = data["title"]
    description = data["description"]
    canonical = f"/{slug}/"

    # Build intro
    intro_html = "\n".join(f"        <p>{p.strip()}</p>" for p in data["intro"].split("\n\n") if p.strip())

    # Build sections
    sections_html = ""
    schema_items = []
    position = 1

    for section in data["sections"]:
        if not section["items"]:
            continue

        items_html = ""
        for i, item in enumerate(section["items"], 1):
            badge = ' <span class="rp-badge">OUR PICK</span>' if item.get("owned") else ""
            items_html += f"""
          <div class="rp-item">
            <h3 class="rp-item-title">
              {i}. <a href="{item['url']}" target="_blank" rel="noopener">{item['name']}</a>{badge}
            </h3>
            <p class="rp-item-desc">{item['desc']}</p>
          </div>"""
            schema_items.append({"@type": "ListItem", "position": position, "name": item["name"], "url": item["url"]})
            position += 1

        sections_html += f"""
      <section class="rp-section">
        <h2 class="rp-section-title">{section['title']}</h2>
        {items_html}
      </section>"""

    schema = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "ItemList", "name": title, "description": description, "numberOfItems": len(schema_items), "itemListElement": schema_items},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": title, "item": f"{BASE_URL}{canonical}"}
            ]},
            {
                "@type": "Article",
                "headline": title,
                "description": description,
                "url": f"{BASE_URL}{canonical}",
                "datePublished": "2026-04-13",
                "dateModified": "2026-04-28",
                "author": {
                    "@type": "Person",
                    "name": "Rome Thorndike",
                    "url": "https://www.linkedin.com/in/romethorndike/"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": SITE_NAME,
                    "url": BASE_URL
                }
            }
        ]
    }, indent=2)

    html = get_head(title, description, canonical, f'<script type="application/ld+json">\n{schema}\n</script>')
    html += f"""
<body>
{get_header()}

<div class="page">
  <nav class="rp-breadcrumb">
    <a href="/">Home</a> &rsaquo; <span>{directory['title']}</span>
  </nav>

  <h1>{title}</h1>
  <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px;">By <a href="https://www.linkedin.com/in/romethorndike/" target="_blank" rel="noopener" style="color: var(--amber-dark); text-decoration: none;">Rome Thorndike</a></div>

  <div class="rp-intro">
    {intro_html}
  </div>

  {sections_html}

  <div class="rp-curation">
    <h2>How We Curated This List</h2>
    <p>Three criteria. First, does this resource teach you something you can't learn from a Google search? Second, is it actively maintained and producing new content? Third, do practitioners in the role actually recommend it to peers? We don't accept payment for listings. We review and update this page quarterly.</p>
  </div>

  {f'<div class="rp-curation" style="margin-top:24px;border-left:3px solid var(--amber);"><h2>Go Deeper: {CONTENT_SITES[niche]["name"]}</h2><p>{CONTENT_SITES[niche]["desc"]}. Visit <a href="{CONTENT_SITES[niche]["url"]}">{CONTENT_SITES[niche]["name"]}</a> for the full picture.</p></div>' if niche in CONTENT_SITES else ''}

  <a href="/" class="rp-back">&larr; Browse all directories</a>
</div>

{get_newsletter_section()}
{get_footer()}
</body>
</html>"""

    page_dir = os.path.join(SITE_DIR, slug)
    os.makedirs(page_dir, exist_ok=True)
    with open(os.path.join(page_dir, "index.html"), "w") as f:
        f.write(html)
    print(f"  Built: /{slug}/ ({len(schema_items)} resources)")


def build_about():
    html = get_head("About", f"How {SITE_NAME} curates the best resources for every go-to-market function.", "/about/")
    html += f"""
<body>
{get_header()}

<div class="page">
  <h1>About The GTM Index</h1>

  <p>Every go-to-market role has its own ecosystem of newsletters, tools, communities, and content. The problem is finding the good stuff. Most "best of" lists are sponsored placements or SEO-driven filler.</p>

  <p>The GTM Index is different. We hand-curate every directory by talking to practitioners, reading the newsletters ourselves, and testing the tools. If something makes the list, it's because it's worth your time.</p>

  <h2>What We Cover</h2>

  <p>We maintain curated directories for {len(DIRECTORIES)} go-to-market functions, from GTM engineers and RevOps to fractional executives and customer success. Each directory covers six categories: newsletters, blogs and websites, communities, tools, podcasts, and courses.</p>

  <h2>How We Curate</h2>

  <p>Three criteria. First, does this resource teach you something you can't learn from a Google search? Second, is it actively maintained and producing new content? Third, do practitioners in the role actually recommend it to peers?</p>

  <p>We don't accept payment for listings. If a resource stops being useful, it comes off the list. We review and update every directory quarterly.</p>

  <h2>Who's Behind This</h2>

  <p>The GTM Index is built by operators who've worked across sales, marketing, data, and engineering. We got tired of bookmark folders with 200 dead links and decided to build something better.</p>

  <p>Questions or suggestions? Email <a href="mailto:hello@thegtmindex.com">hello@thegtmindex.com</a>.</p>
</div>

{get_newsletter_section()}
{get_footer()}
</body>
</html>"""

    about_dir = os.path.join(SITE_DIR, "about")
    os.makedirs(about_dir, exist_ok=True)
    with open(os.path.join(about_dir, "index.html"), "w") as f:
        f.write(html)
    print("  Built: /about/")


def build_robots():
    with open(os.path.join(SITE_DIR, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml")
    print("  Built: robots.txt")


def build_sitemap():
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [{"loc": f"{BASE_URL}/", "priority": "1.0"}, {"loc": f"{BASE_URL}/about/", "priority": "0.8"}]
    for d in DIRECTORIES:
        urls.append({"loc": f"{BASE_URL}/{d['id']}/", "priority": "0.9"})

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f'  <url>\n    <loc>{u["loc"]}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{u["priority"]}</priority>\n  </url>\n'
    xml += '</urlset>'
    with open(os.path.join(SITE_DIR, "sitemap.xml"), "w") as f:
        f.write(xml)
    print(f"  Built: sitemap.xml ({len(urls)} URLs)")


def build_404():
    html = get_head("Page Not Found", "The page you're looking for doesn't exist.", "/404.html")
    html += f"""
<body>
{get_header()}
<div class="page" style="text-align:center;padding-top:160px;">
  <h1>404</h1>
  <p>This page doesn't exist. <a href="/">Browse all directories</a>.</p>
</div>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "404.html"), "w") as f:
        f.write(html)
    print("  Built: 404.html")


def build_cname():
    with open(os.path.join(SITE_DIR, "CNAME"), "w") as f:
        f.write("thegtmindex.com")
    print("  Built: CNAME")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print(f"\nBuilding {SITE_NAME}...")
    print(f"Output: {SITE_DIR}\n")

    build_homepage()
    build_about()

    print("\n  Building resource pages...")
    for d in DIRECTORIES:
        build_resource_page(d)

    print("")
    build_robots()
    build_sitemap()
    build_404()
    build_cname()

    print(f"\nDone. {len(DIRECTORIES)} directories built.")
