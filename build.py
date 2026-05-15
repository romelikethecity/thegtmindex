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
    {"id": "ai-sdr", "title": "AI SDR & Outbound", "icon": "&#128233;", "description": "Autonomous AI SDRs, outbound engines, email personalization, and signal-based prospecting tools for modern B2B sales teams.", "niche": "ai-sdr"},
    {"id": "voice-ai", "title": "Voice AI Agents", "icon": "&#127908;", "description": "Voice AI platforms, conversational AI infrastructure, sales and customer service voice agents, and resources for builders and buyers of voice-native AI.", "niche": "voice-ai"},
    {"id": "ai-compliance", "title": "AI Compliance & Governance", "icon": "&#9878;", "description": "AI compliance automation, governance platforms, security tools, regulatory trackers, and frameworks for ISO 42001, NIST AI RMF, and EU AI Act readiness.", "niche": "ai-compliance"},
    {"id": "workflow-automation", "title": "AI Workflow Automation", "icon": "&#128268;", "description": "AI-native workflow platforms (Lindy, Gumloop, Relay), established automation tools (Zapier, Make, n8n), embedded iPaaS, and resources for ops teams.", "niche": "workflow-automation"},
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


# =============================================================================
# GUIDES — long-form articles
# =============================================================================

GUIDE_CSS_EXTRA = """
/* Guide article styles */
.guide-wrap { padding: 100px 24px 64px; max-width: 760px; margin: 0 auto; }
.guide-wrap h1 { font-size: clamp(28px, 4vw, 38px); font-weight: 700; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.5px; color: var(--text); }
.guide-meta { font-size: 13px; color: var(--text-muted); margin-bottom: 32px; }
.guide-meta a { color: var(--amber-dark); }
.guide-wrap h2 { font-size: 24px; font-weight: 700; margin: 40px 0 12px; color: var(--text); letter-spacing: -0.3px; }
.guide-wrap h3 { font-size: 18px; font-weight: 600; margin: 28px 0 10px; color: var(--text); }
.guide-wrap p { font-size: 16px; color: #374151; margin-bottom: 16px; line-height: 1.75; }
.guide-wrap ul, .guide-wrap ol { margin: 0 0 20px 22px; color: #374151; }
.guide-wrap li { font-size: 16px; line-height: 1.7; margin-bottom: 8px; }
.guide-wrap a { color: var(--amber-dark); text-decoration: underline; text-decoration-color: #FCD34D; text-underline-offset: 3px; }
.guide-wrap a:hover { color: var(--amber); }
.guide-wrap blockquote { border-left: 3px solid var(--amber); padding: 4px 18px; margin: 20px 0; color: var(--text-muted); font-size: 15px; }
.guide-table-wrap { overflow-x: auto; margin: 16px 0 24px; }
.guide-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.guide-table th, .guide-table td { padding: 10px 12px; border: 1px solid var(--border); text-align: left; vertical-align: top; }
.guide-table th { background: #F9FAFB; font-weight: 600; }
.guide-callout { background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 10px; padding: 20px 22px; margin: 24px 0; }
.guide-callout p { margin-bottom: 0; font-size: 15px; }
.guide-faq { margin-top: 32px; }
.guide-faq details { border: 1px solid var(--border); border-radius: 8px; padding: 14px 18px; margin-bottom: 10px; background: var(--bg-white); }
.guide-faq summary { font-weight: 600; cursor: pointer; font-size: 15px; color: var(--text); }
.guide-faq details[open] summary { margin-bottom: 8px; }
.guide-faq p { font-size: 15px; color: #4B5563; margin-bottom: 0; }
.guide-related { margin-top: 48px; padding: 28px; background: #F9FAFB; border-radius: 12px; border: 1px solid var(--border); }
.guide-related h2 { font-size: 18px; margin-top: 0; margin-bottom: 12px; }
.guide-related ul { list-style: none; margin: 0; padding: 0; }
.guide-related li { font-size: 14px; margin-bottom: 8px; }
.guide-related a { color: var(--amber-dark); text-decoration: none; font-weight: 500; }
.guide-related a:hover { text-decoration: underline; }
.guides-grid { padding: 64px 24px 80px; max-width: 1100px; margin: 0 auto; }
.guides-grid h1 { font-size: clamp(28px, 4vw, 38px); font-weight: 700; margin-bottom: 12px; letter-spacing: -0.5px; }
.guides-grid .sub { color: var(--text-muted); font-size: 16px; margin-bottom: 32px; }
.guides-list { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.guide-card { background: var(--bg-white); border: 1px solid var(--border); border-radius: 10px; padding: 24px; transition: border-color 200ms, box-shadow 200ms; display: block; }
.guide-card:hover { border-color: var(--amber); box-shadow: var(--shadow-hover); }
.guide-card h3 { font-size: 17px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
.guide-card p { font-size: 14px; color: var(--text-muted); line-height: 1.6; margin-bottom: 10px; }
.guide-card .date { font-size: 12px; color: var(--text-light); }
@media (max-width: 700px) { .guides-list { grid-template-columns: 1fr; } }
"""


GUIDES = [
    {
        "slug": "gtm-engineer-vs-revops",
        "title": "GTM Engineer vs RevOps: How These Two Roles Differ",
        "meta": "GTM Engineer vs RevOps, side by side. What each role owns, comp benchmarks, reporting lines, and which one your B2B SaaS team should hire first in 2026.",
        "summary": "What each role owns, where they overlap, what they get paid, and which to hire first.",
        "word_target": 1500,
        "date": "2026-05-14",
    },
    {
        "slug": "b2b-saas-gtm-org-chart",
        "title": "The Modern B2B SaaS GTM Org Chart: An ARR Stage Guide",
        "meta": "How a modern B2B SaaS go-to-market org is structured today. Reporting lines, team ratios, and headcount benchmarks at every ARR stage from seed to scale.",
        "summary": "Reporting lines, team ratios, and headcount benchmarks by ARR stage for B2B SaaS GTM organizations.",
        "word_target": 1600,
        "date": "2026-05-14",
    },
    {
        "slug": "se-to-ae-ratio-benchmarks",
        "title": "SE to AE Ratio Benchmarks for B2B SaaS Pre-Sales Teams",
        "meta": "SE to AE ratio benchmarks broken down by ACV, segment, and product complexity. How to size your B2B pre-sales team using Bridge Group and ICONIQ data.",
        "summary": "Benchmark SE to AE ratios by ACV, segment, and product complexity. When to add headcount and when to specialize.",
        "word_target": 1500,
        "date": "2026-05-14",
    },
    {
        "slug": "when-to-hire-fractional-gtm-leader",
        "title": "When to Hire a Fractional GTM Leader: A Founder Guide",
        "meta": "Signals it is time to hire a fractional CRO, CMO, or RevOps leader. Pricing benchmarks, scope templates, and how to evaluate fractional vs a full-time hire.",
        "summary": "Signals it is time to bring in a fractional GTM leader, what they cost, and how to scope the engagement.",
        "word_target": 1400,
        "date": "2026-05-14",
    },
    {
        "slug": "ai-impact-b2b-gtm-stack-2026",
        "title": "AI Impact on the B2B GTM Stack: 2026 State of the Market",
        "meta": "How AI is changing the B2B go-to-market stack in 2026. AI SDRs, voice agents, RevOps copilots, and the GTM tool categories most likely to consolidate.",
        "summary": "Where AI is replacing tools, where it is adding new layers, and which GTM categories will consolidate first.",
        "word_target": 1500,
        "date": "2026-05-14",
    },
]

# Import additional guide metadata and content
from _guides_extra import GUIDE_EXTRAS
from _guides_bodies import GUIDES_CONTENT
from _guides_bodies2 import GUIDES_CONTENT2
from _guides_bodies3 import GUIDES_CONTENT3

# Merge content dictionaries
_ALL_GUIDE_CONTENT = {}
_ALL_GUIDE_CONTENT.update(GUIDES_CONTENT)
_ALL_GUIDE_CONTENT.update(GUIDES_CONTENT2)
_ALL_GUIDE_CONTENT.update(GUIDES_CONTENT3)

# Extend GUIDES list with the new entries
GUIDES.extend(GUIDE_EXTRAS)


def _guide_head(g, schema_blocks):
    schema_script = ""
    for s in schema_blocks:
        schema_script += f'<script type="application/ld+json">\n{json.dumps(s, indent=2)}\n</script>\n'
    extra = f"<style>{GUIDE_CSS_EXTRA}</style>\n{schema_script}"
    return get_head(g["title"], g["meta"], f"/guides/{g['slug']}/", extra)


def _guide_schemas(g, faqs):
    canonical = f"{BASE_URL}/guides/{g['slug']}/"
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": g["title"],
        "description": g["meta"],
        "url": canonical,
        "datePublished": g["date"],
        "dateModified": g["date"],
        "author": {"@type": "Person", "name": "Rome Thorndike", "url": "https://www.linkedin.com/in/romethorndike/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": BASE_URL},
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{BASE_URL}/guides/"},
            {"@type": "ListItem", "position": 3, "name": g["title"], "item": canonical},
        ],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return [article, breadcrumb, faq]


def _render_faqs(faqs):
    html = '<div class="guide-faq">'
    for q, a in faqs:
        html += f'\n<details><summary>{q}</summary><p>{a}</p></details>'
    html += '\n</div>'
    return html


def _render_related(items):
    """items: list of (label, href) tuples."""
    lis = "\n".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)
    return f'<div class="guide-related"><h2>Keep reading</h2><ul>\n{lis}\n</ul></div>'


def _write_guide(g, body_html, faqs, related):
    schemas = _guide_schemas(g, faqs)
    html = _guide_head(g, schemas)
    pub_date = datetime.strptime(g["date"], "%Y-%m-%d").strftime("%B %-d, %Y")
    html += f"""
<body>
{get_header()}

<div class="guide-wrap">
  <nav class="rp-breadcrumb">
    <a href="/">Home</a> &rsaquo; <a href="/guides/">Guides</a> &rsaquo; <span>{g['title']}</span>
  </nav>

  <h1>{g['title']}</h1>
  <div class="guide-meta">By <a href="https://www.linkedin.com/in/romethorndike/" target="_blank" rel="noopener">Rome Thorndike</a> &middot; Published {pub_date}</div>

  {body_html}

  <h2>Frequently asked questions</h2>
  {_render_faqs(faqs)}

  {_render_related(related)}
</div>

{get_newsletter_section()}
{get_footer()}
</body>
</html>"""

    out_dir = os.path.join(SITE_DIR, "guides", g["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    # word count for logging
    import re as _re
    text = _re.sub(r"<[^>]+>", " ", body_html)
    words = len([w for w in text.split() if w.strip()])
    print(f"  Built: /guides/{g['slug']}/ ({words} words)")
    return words


def build_guide_from_content(slug):
    """Generic guide builder using _ALL_GUIDE_CONTENT."""
    g = next(x for x in GUIDES if x["slug"] == slug)
    body, faqs, related = _ALL_GUIDE_CONTENT[slug]
    return _write_guide(g, body, faqs, related)


def build_guide_gtm_engineer_vs_revops():
    g = next(x for x in GUIDES if x["slug"] == "gtm-engineer-vs-revops")
    body = """
<p>GTM engineers and revenue operations leaders both sit at the seam between sales, marketing, and the tools that power them. Both can write SQL. Both touch Salesforce, HubSpot, and the data warehouse. Both report into a revenue or marketing leader more often than into engineering. That overlap makes the roles easy to confuse, and easy to hire wrong.</p>

<p>The shortest distinction: a RevOps lead designs the revenue system. A GTM engineer builds inside it. RevOps owns process, planning, forecasting, and tool selection. A GTM engineer ships automations, enrichments, and integrations that move pipeline. Companies that treat them as interchangeable end up with a RevOps manager writing brittle Python scripts at midnight, or a GTM engineer asked to run a forecast call they were never trained for.</p>

<h2>What a RevOps lead owns</h2>

<p>The Pavilion State of RevOps and similar practitioner surveys put four responsibilities at the center of the function: planning, process, systems, and insights. In plain language, that means quota and territory design, the lead-to-cash process, the CRM and adjacent stack, and the dashboards leadership reads on Monday morning.</p>

<p>A senior RevOps leader spends their week on quarterly planning models, pipeline reviews, deal desk approvals, comp plan questions, and the small group of dashboards that anchor the forecast. They write SQL when needed, but they spend more time in spreadsheets, Salesforce reports, and meetings with sales and finance than they spend in code.</p>

<h2>What a GTM engineer owns</h2>

<p>The GTM engineer title only became common around 2023, popularized by writers like Mark Kosoglow and the team at Clay. The job is closer to a full-stack engineer who picked revenue as their problem space. Outbound automation, AI SDR plumbing, signal-based routing, custom enrichment pipelines, scraping, webhook glue, and the messy integration layer between RevOps tools all fall on this person.</p>

<p>A GTM engineer ships things. A typical week includes a new Clay table feeding an outbound sequence, a Cursor or Make scenario that pulls product usage data into a sales playbook, a Slack alert that fires when an account hits a high-intent signal, and one or two broken integrations to fix. Salary data from <a href="https://gtmepulse.com">GTME Pulse</a> tracks the comp curve, which has moved up sharply as AI-native outbound stacks have spread.</p>

<h2>Where they overlap</h2>

<p>Both roles read SQL fluently. Both can build a Salesforce report and both speak in funnel stages. The overlap is real, and at smaller companies a single hire often covers both. What sets them apart is the center of gravity.</p>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Dimension</th><th>RevOps</th><th>GTM Engineer</th></tr></thead>
<tbody>
<tr><td>Primary output</td><td>Plans, models, processes</td><td>Working automations and integrations</td></tr>
<tr><td>Tool depth</td><td>Salesforce, HubSpot, BI, planning tools</td><td>Clay, n8n, Make, scripts, APIs, AI agents</td></tr>
<tr><td>Time horizon</td><td>Quarterly and annual</td><td>Daily and weekly shipping</td></tr>
<tr><td>Stakeholder</td><td>CRO, CFO, VP Sales</td><td>VP Marketing, head of demand gen, RevOps lead</td></tr>
<tr><td>Reporting line</td><td>CRO or COO</td><td>CMO, VP Marketing, or RevOps</td></tr>
</tbody>
</table></div>

<h2>Comp benchmarks</h2>

<p>Pavilion, RepVue, and Bridge Group all publish RevOps benchmarks that put senior individual contributor base salaries in a similar band, with senior managers and directors taking a clear step up. Equity ranges widely depending on stage. The <a href="https://therevopsreport.com">RevOps Report</a> tracks the moving averages by title and segment.</p>

<p>GTM engineer comp is less mature as a benchmark category because the title is younger. Practitioner-led pay data from <a href="https://gtmepulse.com">GTME Pulse</a> shows base salaries similar to senior RevOps ICs at well-funded startups, with bonus and equity structures closer to a marketing or engineering role than to a sales role. The premium goes to engineers who can credibly build AI-native pipelines, since the role of <a href="/ai-sdr/">AI SDR systems</a> and <a href="/workflow-automation/">workflow automation</a> has expanded what a single engineer can ship in a quarter.</p>

<h2>Which one to hire first</h2>

<p>If you have nothing, hire RevOps first. A company under roughly $5M ARR without a clean CRM, a working forecast, or a defined lead-to-cash process needs the planner before it needs the builder. Without that foundation, a GTM engineer ends up automating broken process and shipping faster paths to bad data.</p>

<p>Once the system is in place, the math changes. Companies that already have a RevOps lead, a clean CRM, and an outbound motion get more return from a GTM engineer than from a second RevOps hire. The Bessemer and ICONIQ Growth benchmarks both point to the same conclusion in different words: at scale, the marginal hour of a planner gives back less pipeline than the marginal hour of a builder who can wire a new signal into a working sequence.</p>

<p>A third pattern is also common. Some companies hire one person with both skill sets and call them "RevOps engineer" or "head of revenue systems." That works when the candidate exists, which is rare. More often the title hides a tradeoff, and one half of the job goes unowned.</p>

<h2>Reporting structure</h2>

<p>RevOps usually reports to the CRO at companies past Series B, or to the CEO or COO earlier. The function is a cross-functional service, not a sales function, even when it lives under sales on the org chart. GTM engineers most often report into marketing, into RevOps, or into a head of growth, depending on where the highest-impact automations live. Some report directly to the CMO when paid acquisition and outbound are the main growth engines.</p>

<p>Neither role belongs in a generic engineering org. Both need daily contact with sellers and marketers to do their job well. The <a href="/revops/">RevOps directory</a> and <a href="/gtm-engineers/">GTM engineers directory</a> on this site collect the communities, newsletters, and tools each role draws on.</p>

<h2>Hiring signals to watch for</h2>

<p>For RevOps, look for evidence of building a forecast process from scratch, designing a comp plan, leading a CRM migration, and shipping a planning model that the CFO trusted. Ask about a quota or territory model they built and what changed after it shipped.</p>

<p>For a GTM engineer, look at the projects portfolio first. Ask for a walkthrough of a Clay table, a custom enrichment chain, or an outbound sequence with branching logic. Ask what they would do with a list of 5,000 accounts and one week. Strong candidates show you the system on screen instead of describing it.</p>

<h2>The headcount math</h2>

<p>A reasonable starting ratio in a SaaS company past $10M ARR is one senior RevOps lead per 30 to 60 quota-carrying reps, with one or two GTM engineers supporting the outbound and marketing motion underneath. Bridge Group SDR benchmarks and ICONIQ Growth reports converge on similar headcount math, with adjustments for ACV and segment.</p>

<p>The exact numbers matter less than the principle. RevOps headcount scales with the size of the sales team it supports. GTM engineering headcount scales with the volume and complexity of automated touches a company runs. A high-volume outbound program with three sequences and minimal signal triggers needs less GTM engineering than a signal-heavy program running across 12 plays and 30 sources.</p>

<h2>Common organizational mistakes</h2>

<p>Four mistakes recur in the hiring patterns published in Pavilion and OpenView surveys. The first is hiring a GTM engineer before the CRM is clean. Without a trusted data layer, every automation the engineer ships either breaks against bad records or amplifies bad routing.</p>

<p>The second is hiring a RevOps lead with no executive sponsor. RevOps work crosses sales, marketing, finance, and customer success, and an unsponsored RevOps hire ends up running tickets for whichever leader shouts loudest. The fix is to set the reporting line and the weekly executive standing meeting before the hire starts.</p>

<p>The third is treating GTM engineering as an extension of IT. A GTM engineer who reports to an IT or general engineering function will deliver against engineering priorities, not revenue priorities, and the planned outbound velocity rarely materializes. The fourth is hiring both roles into the same job description in the hope of saving headcount. The combined role attracts generalists who do neither half well.</p>

<h2>Career path differences</h2>

<p>The two roles also lead to different next jobs. RevOps senior managers move into director and VP RevOps roles, into chief of staff positions, or into VP Strategy roles at growth-stage companies. Some move into operations leadership at investment firms. The career path is well-defined and compensation curves are predictable.</p>

<p>GTM engineers tend to move along one of two paths. Some grow into heads of growth engineering or platform owners inside marketing or RevOps. Others move laterally into founding engineer roles at early-stage startups, since the skill set transfers cleanly to building zero-to-one revenue systems. The second path produces more equity outcomes. The first path produces more title progression.</p>
"""
    faqs = [
        ("Is GTM engineer a real job title or a rebrand of marketing ops?",
         "It is a distinct role. Marketing ops owns the marketing automation platform, lead scoring, and campaign infrastructure. A GTM engineer ships automations and integrations across sales and marketing, often using tools like Clay, n8n, and AI agents that marketing ops platforms do not cover."),
        ("Can one person do both RevOps and GTM engineering?",
         "At companies under about $5M ARR, often yes. Past that, the planning and process work in RevOps usually expands to fill a full role, and the engineering work expands to fill another. Hiring one person to do both at scale tends to leave one half of the job unowned."),
        ("Which role pays more?",
         "At similar seniority, base salaries are close. RevOps directors and VPs typically out-earn senior GTM engineers because the role carries broader scope. GTM engineers at AI-native outbound companies can match or exceed that comp when equity is included."),
        ("Does a GTM engineer need to know how to code?",
         "Yes. The role assumes fluency in SQL, comfort with APIs and webhooks, and at least intermediate Python or JavaScript. Strong candidates also ship in Clay, n8n, Make, or similar tools without writing code, but the engineering background is what makes the rest reliable."),
        ("Where does a GTM engineer report?",
         "Most often into marketing, RevOps, or a head of growth. Reporting to engineering is rare and usually creates friction because the work is paced by GTM priorities, not engineering sprints."),
    ]
    related = [
        ("RevOps tools, newsletters, and communities", "/revops/"),
        ("GTM engineers directory", "/gtm-engineers/"),
        ("AI SDR and outbound platforms", "/ai-sdr/"),
        ("Marketing operations resources", "/marketing-ops/"),
        ("RevOps Report (salary and tool reviews)", "https://therevopsreport.com"),
        ("GTME Pulse (GTM engineer salary data)", "https://gtmepulse.com"),
    ]
    return _write_guide(g, body, faqs, related)


def build_guide_b2b_saas_gtm_org_chart():
    g = next(x for x in GUIDES if x["slug"] == "b2b-saas-gtm-org-chart")
    body = """
<p>Every B2B SaaS company past seed stage runs some version of the same go-to-market org chart. The titles vary. The reporting lines move depending on who the CEO trusts. The basic shape, however, is stable enough that benchmark reports from Bessemer Venture Partners, ICONIQ Growth, OpenView, and SaaStr describe it in similar terms.</p>

<p>This guide walks through that shape stage by stage, from the first seller to the post-IPO org. It also points out where new roles have entered the picture in the past two years, including AI SDRs, GTM engineers, and platform-style RevOps teams.</p>

<h2>The three pillars</h2>

<p>A modern B2B SaaS GTM org sits on three pillars: a revenue pillar that closes business, a marketing pillar that creates demand, and a customer pillar that keeps and expands accounts. Each pillar has a leader, each leader reports into the CEO or into a single revenue officer, and each one carries its own operations function inside it or shares a central one.</p>

<p>The revenue pillar runs outbound, inbound conversion, and closing. It typically includes SDRs, AEs, sales engineers, and a sales leadership layer. The marketing pillar runs brand, product marketing, demand generation, content, and marketing operations. The customer pillar covers onboarding, customer success, support, and renewals or expansion. Larger orgs split renewals into a dedicated team. Sapphire Ventures and OpenView both publish detailed maps of the function at scale.</p>

<h2>Seed to $1M ARR</h2>

<p>At seed, the founder is the head of sales. There is usually one or two founding sellers, a head of marketing only if a marketing-led founder did not exist, and no formal customer success function. Onboarding is done by the founder or the seller who closed the deal.</p>

<p>The trap at this stage is over-hiring. ICONIQ and SaaStr data both show that the second seller hire is the highest-risk hire a young company makes, because the founder is often still the only person who can close repeatably. The fix is to hire a strong first AE who can also do discovery and to delay marketing leadership until product-market fit is clear enough to brief one.</p>

<h2>$1M to $5M ARR</h2>

<p>The first real sales leader joins, usually as a head of sales or director of sales, almost never yet a VP. SDR coverage starts to appear, often as one SDR per two or three AEs. A marketing leader joins, usually with a demand generation bias and a thin product marketing layer underneath them.</p>

<p>This is also when the first <a href="/revops/">RevOps</a> hire makes sense. Bridge Group benchmarks consistently show that the first RevOps hire pays back inside two quarters when sellers and the leadership team have lost confidence in the forecast. A first <a href="/customer-success/">CSM</a> usually joins around $2M to $3M ARR if the product is technical or has a renewal motion.</p>

<h2>$5M to $20M ARR</h2>

<p>The org doubles in shape. The head of sales becomes a VP Sales with two or three managers underneath. Marketing splits into product marketing, content, and demand generation as named functions. <a href="/presales/">Solutions engineering</a> appears, with the first SE often hired around $5M to $8M ARR when product complexity warrants it. Bridge Group SE benchmarks suggest one SE per three to five AEs at this stage in mid-market SaaS.</p>

<p>The customer team grows into a director or VP of customer success with two or three CSMs. RevOps grows from a single hire into a team of two to four. The first <a href="/sales-enablement/">sales enablement</a> hire often appears here, usually as a single program manager. Channel and <a href="/partner-channel/">partner</a> motions enter the picture if the product has a natural ecosystem.</p>

<h2>$20M to $50M ARR</h2>

<p>This is the stage where the CRO title becomes appropriate. The CRO oversees sales, customer success, and revenue operations, with marketing reporting either to the CRO or to the CEO depending on philosophy. Bessemer Cloud Index notes the split runs roughly even across public SaaS companies. The decision is less about correctness than about who the CEO trusts to align demand and revenue.</p>

<p>Inside sales, the org splits by segment, with separate teams for SMB, mid-market, and enterprise. Each segment usually has its own AE bench, SE coverage, and SDR pod. The CSM team splits along the same lines, often with a separate renewals function reporting to the CRO. Marketing adds a <a href="/abm/">field or ABM</a> function, a brand lead, and a growing <a href="/marketing-ops/">marketing operations</a> team.</p>

<h2>$50M to $200M ARR</h2>

<p>Headcount discipline becomes the central question. ICONIQ Growth data on public and late-stage private SaaS companies consistently shows GTM headcount as a percentage of total headcount in a 45 to 55 percent band at this stage. Companies above that band are usually fighting churn or a long sales cycle. Companies below it have either a low-touch motion or a problem the board is not yet seeing.</p>

<p>The CRO has a full bench: VP Sales, VP Customer Success, VP RevOps, and often a VP Sales Strategy or chief of staff. Marketing matches with a VP of demand, VP of product marketing, and a senior brand or communications leader. Operations functions consolidate. RevOps starts to look like a platform team that supports sales, marketing, and customer success with shared tooling and data.</p>

<h2>Where new roles fit</h2>

<p>Three roles have entered the standard org chart in the past two years. <a href="/gtm-engineers/">GTM engineers</a> sit inside marketing or RevOps and ship outbound automations, signal pipelines, and integration glue. <a href="/ai-sdr/">AI SDR</a> ownership lives inside either the SDR team itself or RevOps, depending on whether the company treats it as augmentation or replacement. <a href="/workflow-automation/">Workflow automation</a> owners often share a desk with RevOps and report into the same VP.</p>

<p>A fourth role, the head of <a href="/geo/">generative engine optimization</a>, has appeared at companies that depend on inbound. It usually lives inside content or demand generation rather than as a standalone function.</p>

<h2>Sample headcount ratios</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Function</th><th>$5M ARR</th><th>$20M ARR</th><th>$50M ARR</th></tr></thead>
<tbody>
<tr><td>AEs</td><td>4 to 6</td><td>12 to 20</td><td>30 to 50</td></tr>
<tr><td>SDRs</td><td>2 to 4</td><td>6 to 12</td><td>15 to 25</td></tr>
<tr><td>SEs</td><td>1 to 2</td><td>3 to 6</td><td>8 to 15</td></tr>
<tr><td>CSMs</td><td>2 to 3</td><td>6 to 10</td><td>15 to 25</td></tr>
<tr><td>RevOps</td><td>1</td><td>2 to 4</td><td>6 to 10</td></tr>
<tr><td>Marketing</td><td>3 to 5</td><td>8 to 15</td><td>20 to 35</td></tr>
</tbody>
</table></div>

<p>These ranges come from Bridge Group SDR and SE benchmarks, OpenView SaaS Benchmarks, and ICONIQ Growth Topline Growth reports. Local conditions move the numbers. ACV, segment, sales cycle, and product complexity all push the right answer up or down by 20 to 40 percent.</p>

<h2>Reporting line decisions that matter</h2>

<p>The hardest reporting line to get right is where marketing sits. A CMO who reports to the CEO and a CRO who owns sales and customer success can work, and so can a single CRO who oversees both. Bessemer notes both patterns in public S-1 filings. The decision usually breaks on whether the CEO has the bandwidth and operating experience to manage the marketing function directly.</p>

<p>The second hard decision is RevOps. RevOps under the CFO produces tighter numbers and slower change. RevOps under the CRO produces faster change and looser numbers. RevOps under the COO is the middle path and the most common at companies past $50M ARR.</p>

<p>For role-by-role hiring resources, see the directories for <a href="/revenue-leaders/">revenue leaders</a>, <a href="/sellers/">sellers</a>, <a href="/customer-success/">customer success</a>, and <a href="/demand-gen/">demand generation</a>.</p>
"""
    faqs = [
        ("When should a SaaS company hire its first CRO?",
         "Most B2B SaaS companies move from a VP Sales to a CRO somewhere between $20M and $50M ARR, when the role expands to cover sales, customer success, and revenue operations. Hiring a CRO before $10M ARR usually signals that the CEO wants distance from sales rather than a true scope expansion."),
        ("Does marketing report to the CRO or the CEO?",
         "Public SaaS companies split roughly evenly between the two patterns. The decision usually depends on whether the CEO has the bandwidth and experience to manage marketing directly, and how tightly the company wants demand and revenue aligned at the leadership layer."),
        ("Where do GTM engineers sit on the org chart?",
         "Most often inside marketing, RevOps, or a head of growth team. Reporting to engineering creates friction because the work is paced by GTM priorities, not product engineering sprints."),
        ("What is a normal SDR-to-AE ratio?",
         "Bridge Group benchmarks put SDR-to-AE coverage in the 1:2 to 1:3 range at most B2B SaaS companies, with enterprise-led motions running closer to 1:1 and high-volume SMB motions running closer to 1:4."),
        ("How big should RevOps be?",
         "A common ratio is one RevOps person per 30 to 60 quota-carrying reps, with the team specializing into systems, analytics, and process roles past about $50M ARR."),
    ]
    related = [
        ("Revenue leaders directory", "/revenue-leaders/"),
        ("RevOps directory", "/revops/"),
        ("Pre-sales and SE directory", "/presales/"),
        ("Customer success directory", "/customer-success/"),
        ("Demand generation directory", "/demand-gen/"),
        ("The CRO Report (compensation data)", "https://thecroreport.com"),
    ]
    return _write_guide(g, body, faqs, related)


def build_guide_se_to_ae_ratio_benchmarks():
    g = next(x for x in GUIDES if x["slug"] == "se-to-ae-ratio-benchmarks")
    body = """
<p>The SE to AE ratio is one of the most repeated benchmarks in B2B SaaS, and one of the least useful when used without context. A single number cannot capture how product complexity, average contract value, segment, and sales cycle length interact. What the benchmarks can do is anchor a budget conversation and flag when a number is out of band.</p>

<p>This guide collects what published practitioner data says about SE to AE coverage, breaks the numbers down by segment and ACV, and walks through how to size a pre-sales team without copying a ratio that does not match your motion.</p>

<h2>The headline benchmark</h2>

<p>Bridge Group's SaaS AE Metrics and Compensation Report and the PreSales Collective community surveys both put the median SE to AE ratio across B2B SaaS in roughly a 1:3 to 1:4 band. That number hides almost everything that matters. It mixes SMB and enterprise, low-complexity and high-complexity products, and US and international teams.</p>

<p>The same data, broken out by segment, looks very different. Enterprise-led motions cluster between 1:1 and 1:2. Mid-market motions sit between 1:3 and 1:5. SMB motions, when SEs exist at all, run wider than 1:5, often closer to a single SE supporting a pod of six to ten AEs on demo and technical questions.</p>

<h2>What moves the ratio</h2>

<p>Four factors move SE coverage more than anything else. ACV is the most reliable driver. Sapphire Ventures and ICONIQ Growth both show a clean curve: higher ACV equals more SE involvement per deal equals a tighter SE to AE ratio. A $250K ACV motion almost always justifies a 1:2 or 1:1 ratio. A $15K ACV motion rarely does.</p>

<p>Product complexity is the second driver. Infrastructure, security, and developer tools tend to need an SE on most calls. Horizontal SaaS, especially in marketing and HR, can often run with an SE only on opportunities above a certain ACV threshold. The third driver is sales cycle length. Long cycles concentrate technical work into discrete moments like architecture reviews and proof-of-concept builds, which makes pooled coverage workable. Short cycles spread technical work across many parallel deals and push toward dedicated coverage.</p>

<p>The fourth driver is segment specialization inside the AE team. If AEs cover dedicated patches and the product has meaningful technical depth, SE specialization usually follows. If AEs are generalists, SEs can pool across them.</p>

<h2>Benchmark ratios by motion</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Motion</th><th>Typical ACV</th><th>SE to AE ratio</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Enterprise (named accounts)</td><td>$150K+</td><td>1:1 to 1:2</td><td>Dedicated SE per AE, sometimes plus a solution architect</td></tr>
<tr><td>Commercial enterprise</td><td>$50K to $150K</td><td>1:2 to 1:3</td><td>Pooled SE coverage with named accounts</td></tr>
<tr><td>Mid-market</td><td>$20K to $50K</td><td>1:3 to 1:5</td><td>Pooled coverage, often by industry or product line</td></tr>
<tr><td>SMB</td><td>under $20K</td><td>1:6 to 1:10</td><td>Often handled by sales engineers or solution consultants on demand</td></tr>
<tr><td>Developer tools and infrastructure</td><td>varies</td><td>1:1 to 1:3</td><td>Higher SE intensity across all segments because of technical depth</td></tr>
</tbody>
</table></div>

<p>These ranges come from Bridge Group, PreSales Collective surveys, and the public 10-Ks of SaaS companies that disclose pre-sales headcount. The <a href="https://presalespulse.com">PreSales Pulse</a> site tracks more granular data by industry and stage.</p>

<h2>When to add the first SE</h2>

<p>Most B2B SaaS companies add their first SE between $5M and $8M ARR. Two signals usually trigger the hire. The first is AEs spending more than 25 percent of their time on technical scoping calls or POCs they cannot run themselves. The second is a win rate gap between deals that involved technical pre-sales support and deals that did not. When that gap reaches 10 percentage points or more, the SE hire pays back inside a quarter or two.</p>

<p>A common mistake is to delay the first SE hire until win rates have already dropped. The signal worth watching is AE time allocation, not lagging win rates. Bridge Group's quota attainment data shows that AEs who spend over 30 percent of their time on technical work consistently underperform peers by 15 to 20 percent on quota attainment.</p>

<h2>Specialization at scale</h2>

<p>Past $20M ARR, SE teams usually start to specialize. Three patterns dominate. The first is segment-based specialization, with SEs aligned to enterprise, mid-market, or SMB. The second is product-line specialization at multi-product companies. The third is industry vertical specialization, common in healthcare, financial services, and the public sector.</p>

<p>Each pattern has tradeoffs. Segment specialization scales most cleanly but produces SEs with shallow product depth across the catalog. Product-line specialization preserves depth but creates routing complexity when a deal crosses lines. Industry specialization tends to win the largest deals and lose the most candidates to attrition, since vertical SEs are heavily recruited.</p>

<h2>Pooled versus dedicated coverage</h2>

<p>Pooled SE coverage works when product complexity is moderate and the sales cycle is long enough that an SE can move between deals without losing context. Dedicated SE coverage works when the product is technically deep, the AE patch is large, and the SE can build account knowledge that translates into multi-year expansion. Most companies run a mix, with dedicated coverage for the top 20 percent of accounts and pooled coverage underneath.</p>

<p>One SE leader pattern that scales well is to set the dedicated coverage threshold at the same ACV that triggers an executive briefing or enterprise procurement process. That keeps the SE attention aligned with the deals that need it most.</p>

<h2>Where SE work is changing</h2>

<p>Two changes have shifted SE workload in the past three years. The first is the rise of AI-assisted demo environments and product tour tools, which have reduced the time a senior SE spends on first demos. The second is the growing surface area of integration and security questions, which has pulled SE time toward architecture reviews and security questionnaires. The net effect is that SE time per deal has held steady while the mix has shifted.</p>

<p>For platform and tool resources used by modern SE teams, see the <a href="/presales/">pre-sales directory</a>. For broader benchmarks on revenue team headcount, the <a href="/revenue-leaders/">revenue leaders directory</a> and <a href="https://thecroreport.com">CRO Report</a> publish updated data each quarter. The <a href="/sellers/">sellers directory</a> covers the AE side of the same coverage equation.</p>

<h2>How to use these benchmarks</h2>

<p>Pick the row that matches your motion, then adjust for product complexity and sales cycle. Companies that run technically deep products in mid-market should sit at the tight end of the mid-market range. Companies that run horizontal products in enterprise can usually live at the loose end of the enterprise range. If the resulting headcount feels off by more than 20 percent from where the benchmark lands, ask whether your motion is the one you assumed it was.</p>

<h2>SE compensation and quota structure</h2>

<p>SE compensation has converged across most B2B SaaS companies on a 70/30 or 80/20 base-to-variable split, with the variable portion tied to a mix of team quota attainment and individual deal contribution. Bridge Group and PreSales Collective surveys both put senior IC SE base salaries inside a clear band, with directors and VPs running a step up. Equity grants are common at venture-backed companies and rare at growth-stage and public companies.</p>

<p>The structural decision worth getting right is whether SEs carry an individual number or share a team number. Individual numbers create accountability and tension with AEs over deal allocation. Team numbers create alignment and reduce friction but blur attribution. Most companies past $20M ARR run team-based variable with individual modifiers for stretch performance.</p>

<h2>Adjacent roles to know</h2>

<p>Three SE-adjacent roles often appear at the same companies. Solution architects sit one level deeper on technical work and typically join larger deals after a discovery pass. Implementation engineers and post-sales technical owners pick up the work after close, and the handoff between SE and implementation is the most common operational pain point for SE leaders. Customer engineers, common in developer-tools companies, blur the line between pre-sales and customer-facing engineering and often report to product or engineering rather than sales.</p>

<p>Headcount math for these roles follows similar segment logic. Enterprise motions tend to have dedicated solution architects on the largest accounts. Mid-market motions pool the role. SMB motions typically do not have it at all.</p>
"""
    faqs = [
        ("What is a good SE to AE ratio in mid-market SaaS?",
         "Bridge Group and PreSales Collective survey data put mid-market SE to AE ratios in the 1:3 to 1:5 range, with the tighter end appropriate for technically deeper products and the looser end for horizontal applications."),
        ("When should a SaaS company hire its first SE?",
         "Most companies hire the first SE between $5M and $8M ARR, triggered by AEs spending more than 25 percent of their time on technical scoping or by a clear win rate gap between deals with and without technical pre-sales support."),
        ("Should SEs report to sales or product?",
         "Most B2B SaaS companies run SEs under sales, reporting to a VP Sales or a head of pre-sales who sits inside the revenue org. SEs under product is rare and usually creates friction with revenue forecasting and quota alignment."),
        ("Do SMB SaaS companies need SEs at all?",
         "Sometimes. SMB motions under $20K ACV often substitute scaled demos, in-product trials, and customer education for dedicated SE coverage. SEs appear when the product is technically deep enough that AEs cannot answer scoping questions in real time."),
        ("Has AI changed SE coverage ratios?",
         "Not yet in published benchmarks. AI tools have shifted the mix of SE work toward architecture review and security questionnaires, but the headcount math has held within historical bands."),
    ]
    related = [
        ("Pre-sales and SE directory", "/presales/"),
        ("B2B sellers directory", "/sellers/"),
        ("Sales enablement directory", "/sales-enablement/"),
        ("Revenue leaders directory", "/revenue-leaders/"),
        ("PreSales Pulse (SE comp and tools)", "https://presalespulse.com"),
        ("The Seller Report (AE comp benchmarks)", "https://thesellerreport.com"),
    ]
    return _write_guide(g, body, faqs, related)


def build_guide_when_to_hire_fractional_gtm_leader():
    g = next(x for x in GUIDES if x["slug"] == "when-to-hire-fractional-gtm-leader")
    body = """
<p>Fractional GTM leadership has gone from a niche offering to a real category in the past four years. Fractional CROs, CMOs, VPs of Sales, and RevOps leaders now show up in seed-stage hiring conversations as a default option rather than an exception. The market for these engagements has matured enough that <a href="/fractional/">fractional directories</a>, dedicated marketplaces, and standardized scope templates now exist.</p>

<p>The question is not whether fractional leadership works. It does, when applied to the right problem at the right stage. The question is when to use it, how to scope it, and how to evaluate a candidate against a full-time hire.</p>

<h2>The two signals that say fractional is the right move</h2>

<p>The first signal is uncertainty about the long-term shape of the role. If you do not know whether your company needs a sales-led, marketing-led, or product-led GTM motion in two years, a fractional leader gives you working senior thinking without locking in a full-time hire who matches one motion. This is the most common reason early-stage CEOs hire fractional CROs.</p>

<p>The second signal is a specific gap with a known endpoint. A fractional RevOps leader to design a comp plan and migrate a CRM. A fractional CMO to brief a new positioning effort and hand off to a director-level hire. A fractional VP Sales to build a hiring scorecard and onboard the first two AEs. These engagements work because both sides know what done looks like and when the engagement ends.</p>

<h2>When fractional is the wrong call</h2>

<p>Fractional leadership is the wrong call when the work requires full-time presence with the team. New AE coaching, daily forecast calls, large team management, and active deal participation all require enough hours that a fractional engagement either fails to deliver or expands until it costs more than a full-time hire.</p>

<p>It is also the wrong call when the underlying problem is product-market fit, pricing, or positioning. A fractional CRO cannot fix a product that does not retain customers. SaaStr and First Round have both written about the pattern where a fractional sales leader is hired to fix what is in fact a product problem, and the engagement ends with a sales process that works against a product that still does not.</p>

<h2>Pricing benchmarks</h2>

<p>Fractional engagements in the US tend to land in a few standard pricing brackets. Pavilion, BUILT IN, and the marketplaces tracked at <a href="https://fractionalpulse.com">Fractional Pulse</a> show consistent ranges.</p>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Role</th><th>Engagement size</th><th>Monthly retainer</th></tr></thead>
<tbody>
<tr><td>Fractional CRO</td><td>1 to 2 days per week</td><td>$10K to $25K</td></tr>
<tr><td>Fractional CMO</td><td>1 to 2 days per week</td><td>$8K to $20K</td></tr>
<tr><td>Fractional VP Sales</td><td>2 to 3 days per week</td><td>$10K to $20K</td></tr>
<tr><td>Fractional RevOps</td><td>1 to 2 days per week</td><td>$6K to $15K</td></tr>
<tr><td>Fractional head of demand</td><td>1 to 2 days per week</td><td>$8K to $18K</td></tr>
</tbody>
</table></div>

<p>Equity grants are uncommon at the lower end of the range and frequent at the upper end. Pavilion's fractional executive surveys show roughly a third of engagements above $15K monthly include a small equity component, usually between 0.10 and 0.50 percent, vesting over the term of the engagement.</p>

<h2>How to scope the engagement</h2>

<p>Three elements separate a working fractional engagement from a failed one. The first is a defined deliverable list. Generic monthly hours engagements fail more often than scoped ones because neither side ever agrees on what done looks like.</p>

<p>The second is a clear reporting cadence. Strong fractional engagements include a weekly working session with the CEO or the next functional leader, a monthly written update, and a quarterly review against the original scope. Looser cadences tend to drift into advisory mode, which costs more than it returns.</p>

<p>The third is a transition plan from day one. The best fractional engagements name the full-time hire they are setting up, even when that hire is six or twelve months out. A fractional CRO who is also defining the eventual full-time VP Sales scorecard returns more value than one who is operating in isolation.</p>

<h2>Where to find candidates</h2>

<p>Three channels produce most fractional placements. Founder and operator networks remain the highest signal source, especially for CRO and CMO roles where references matter more than resume scans. Pavilion's fractional pod and a small number of curated marketplaces produce the next tier of candidates. LinkedIn searches with the right boolean filters can produce the rest, though signal-to-noise gets worse there.</p>

<p>For role-specific resources and active communities, the <a href="/fractional/">fractional directory</a> on this site collects the better marketplaces and playbook resources. The <a href="/revenue-leaders/">revenue leaders directory</a> and <a href="/revops/">RevOps directory</a> cover the practitioner communities where many fractional candidates are active.</p>

<h2>Evaluation criteria</h2>

<p>Three questions sort strong fractional candidates from weak ones. First, ask for the last three engagements they ran and the outcomes. Strong candidates can name the deliverable, the timeline, and what shifted afterward. Weak candidates describe activities rather than outcomes.</p>

<p>Second, ask how they handle the handoff to a full-time hire. Strong candidates have a template, a scorecard, and a calibration process. Weak candidates plan to stay involved indefinitely.</p>

<p>Third, ask about a project that did not work. Fractional leaders who can name a failure and what they learned tend to be calibrated. Those who cannot are usually selling a generalized resume rather than a specific operator track record.</p>

<h2>Fractional versus interim</h2>

<p>The two terms get used interchangeably and should not be. A fractional leader operates part-time over a sustained period, often six to eighteen months, while a company decides on the full-time shape of the role. An interim leader operates full-time for a defined window, often three to nine months, between two full-time hires or during a leave.</p>

<p>Interim engagements look like a higher-cost retainer because they are full-time. Pricing for interim CROs and CMOs typically runs $25K to $50K monthly with a one to three month minimum, often plus a placement bonus on a successful full-time hire identified during the term. Pavilion and senior search firms both track this market separately from fractional.</p>

<h2>When the fractional engagement should end</h2>

<p>Two endings are healthy. The first is the planned handoff to a full-time hire who the fractional leader helped recruit and onboard. The second is the discovery that the work was either smaller than expected or already absorbed by other functions, with the engagement closed cleanly.</p>

<p>One ending is a warning sign. Fractional engagements that drift past eighteen months without a transition plan usually indicate either that the company is using fractional as a permanent solution for a full-time problem, or that the fractional leader has become operationally indispensable in a way that resists the original intent. The first case usually ends in a missed quarter. The second usually ends in a difficult separation.</p>

<h2>Common fractional engagement shapes</h2>

<p>Four shapes show up most often in the data tracked at <a href="https://fractionalpulse.com">Fractional Pulse</a> and in Pavilion's annual surveys. The first is the launch shape, a six-month engagement designed to stand up a function from scratch and hand it off. This is the most common fractional CMO and fractional RevOps pattern at seed and Series A.</p>

<p>The second is the bridge shape, three to six months covering a gap between a departed full-time leader and the replacement. The third is the advisor-plus shape, where a fractional leader runs a small number of strategic projects in parallel with light operational involvement, often paired with a board observer seat. The fourth is the playbook shape, where a fractional CRO or CMO designs a specific motion, like a new outbound program or a partner channel, with a defined go-live date.</p>

<h2>Common failure modes</h2>

<p>Three failure modes account for most fractional engagements that end poorly. The first is scope creep, where a clearly defined initial project absorbs operational responsibilities the company should have hired into directly. The fix is a written deliverable list reviewed every 30 days.</p>

<p>The second is misaligned hours. A two-day-per-week engagement that the company expects to behave like a full-time role produces frustration on both sides. The fix is to be explicit about what the fractional leader is not doing, including which meetings they will not attend and which decisions they will not own.</p>

<p>The third is the missing internal owner. Even strong fractional leaders need a counterpart inside the company who owns daily execution. Engagements without that counterpart turn into a one-person consulting project, with the company paying for ideas it has no path to implement.</p>
"""
    faqs = [
        ("How much does a fractional CRO cost?",
         "Most US fractional CRO engagements run $10K to $25K monthly for one to two days per week. Engagements above $15K monthly sometimes include a small equity grant in the 0.10 to 0.50 percent range, vesting over the term of the engagement."),
        ("When should I hire a fractional CRO instead of a full-time VP Sales?",
         "A fractional CRO is the right call when the long-term shape of the GTM motion is still uncertain, or when a specific scoped problem has a defined endpoint. A full-time VP Sales is the right call when daily team management, active deal participation, and continuous coaching are the core need."),
        ("What is the difference between fractional and interim?",
         "Fractional engagements are part-time and run six to eighteen months while a company decides on the full-time shape of the role. Interim engagements are full-time and cover a defined window, often three to nine months, between two full-time hires."),
        ("How long should a fractional engagement last?",
         "Most successful fractional engagements run six to twelve months, with the strongest ones ending in a planned handoff to a full-time hire the fractional leader helped recruit. Engagements past eighteen months without a transition plan tend to drift."),
        ("Do fractional leaders take equity?",
         "Sometimes. Pavilion data shows roughly a third of fractional engagements above $15K monthly include a small equity grant. Below that retainer level, equity is uncommon and the engagement runs on cash."),
    ]
    related = [
        ("Fractional executives directory", "/fractional/"),
        ("Revenue leaders directory", "/revenue-leaders/"),
        ("RevOps directory", "/revops/"),
        ("Demand generation directory", "/demand-gen/"),
        ("Fractional Pulse (marketplaces and pricing)", "https://fractionalpulse.com"),
        ("The CRO Report (compensation data)", "https://thecroreport.com"),
    ]
    return _write_guide(g, body, faqs, related)


def build_guide_ai_impact_b2b_gtm_stack_2026():
    g = next(x for x in GUIDES if x["slug"] == "ai-impact-b2b-gtm-stack-2026")
    body = """
<p>The B2B go-to-market stack has absorbed more change in the past 24 months than in the prior decade. Outbound, enrichment, scheduling, demo, forecasting, and customer success workflows all now have credible AI-native options. Some of those options replace incumbent tools. Some of them sit on top as a new layer. A few of them are still searching for product-market fit.</p>

<p>This guide is a snapshot of where AI has moved the GTM stack as of mid-2026, based on category-by-category public data, vendor disclosures, and practitioner surveys from Pavilion, ChiefMartec, and the team behind the <a href="https://theaimarketpulse.com">AI Market Pulse</a> tracker.</p>

<h2>Outbound and AI SDR</h2>

<p>Outbound is the category that has changed most. Two distinct patterns now exist in the market. The first is AI-augmented outbound, where a human SDR uses AI tools for research, drafting, and signal triage but still owns sequencing and call work. The second is AI SDR, where an autonomous agent handles research, drafting, sequencing, and reply handling end to end.</p>

<p>The augmented pattern has clearly worked at scale. The autonomous pattern has produced mixed results in published case studies, with strong outcomes in tightly defined segments and weaker outcomes in long-cycle or multi-stakeholder motions. The <a href="/ai-sdr/">AI SDR directory</a> tracks the active platforms in both categories.</p>

<p>The category most likely to consolidate in the next 18 months is mid-market outbound platforms that sit between AI SDR and traditional sequencing. Several vendors have already merged or pivoted in the past year, and Pavilion's RevOps surveys show buyer fatigue with the number of overlapping options.</p>

<h2>Enrichment and signal</h2>

<p>Data enrichment moved from a stable category dominated by ZoomInfo and Apollo to a more competitive one in 24 months. Clay, in particular, has changed the practitioner expectation that enrichment is a fixed schema rather than a programmable workflow. Newer entrants like Default, Persana, and a long tail of waterfall and signal-routing tools now compete with the incumbents on flexibility rather than data volume.</p>

<p>Signal data, distinct from firmographic enrichment, has matured into its own category. Intent, hiring signal, technographic, news, funding, and product usage data now all have dedicated vendors. The interesting move in 2026 is the convergence of signal data and AI sequencing, where signals trigger contextual outreach generated at write time rather than chosen from a sequence library. The <a href="/gtm-engineers/">GTM engineers directory</a> and <a href="https://gtmepulse.com">GTME Pulse</a> track this space closely.</p>

<h2>Voice and conversation</h2>

<p>Voice AI is the GTM category with the highest variance in maturity. Inbound voice agents handling SDR qualification and customer service triage have working production deployments at companies including several public software vendors. Outbound voice agents handling cold calling work in narrow scripts and fail outside them. The <a href="/voice-ai/">voice AI directory</a> tracks the active platforms and their use cases.</p>

<p>Two trends to watch. The first is the move from voice agents as a standalone product to voice as a feature of a broader CRM or engagement platform. The second is regulatory tightening on outbound voice, with several US states adding disclosure requirements in the past year. The market for outbound voice agents in B2B is real but will move slower than the marketing suggests.</p>

<h2>RevOps and forecasting</h2>

<p>RevOps tooling has absorbed AI features in a less disruptive pattern than outbound. CRM, forecasting, and pipeline management tools have added AI features rather than been replaced by AI-native challengers. Clari, Gong, Salesforce, and HubSpot have each shipped meaningful AI features in the past 18 months without losing core category share.</p>

<p>The new layer that has appeared is the RevOps copilot, a class of tools that sit on top of the CRM and data warehouse and answer ad hoc questions in natural language. These tools have replaced a portion of the manual analyst work that historically lived inside RevOps teams, though not the planning work. The <a href="/revops/">RevOps directory</a> tracks the active platforms.</p>

<h2>Workflow automation</h2>

<p>The line between iPaaS and AI workflow tools has blurred. Zapier, Make, and n8n have shipped AI features that compete directly with newer AI-native platforms like Lindy, Gumloop, and Relay. The <a href="/workflow-automation/">workflow automation directory</a> covers both categories.</p>

<p>The practical question for GTM teams is whether to standardize on a single platform or to pick best-in-class for each use case. Most teams above $20M ARR end up running two or three workflow tools, with a primary platform for general automation and one or two AI-native tools for specific high-value workflows like outbound research, lead routing, and reply handling.</p>

<h2>Compliance and governance</h2>

<p>The newest GTM-adjacent category is AI compliance and governance. ISO 42001, the NIST AI Risk Management Framework, and the EU AI Act have produced enough buyer demand that a real vendor market now exists. The <a href="/ai-compliance/">AI compliance directory</a> tracks the active platforms.</p>

<p>The category sits adjacent to GTM rather than inside it, but the demand often originates from sales and customer-facing teams answering enterprise security questionnaires. Pre-sales teams and SEs are the most common internal sponsor for compliance tooling purchases. The <a href="/presales/">pre-sales directory</a> covers the related platforms and communities.</p>

<h2>Customer success and expansion</h2>

<p>The customer success category has seen the slowest AI absorption among the major GTM functions. Health scoring, churn prediction, and renewal forecasting have had AI features for years, with mixed practitioner reviews on accuracy. The newer move is AI agents for onboarding and self-service expansion, which have produced strong outcomes at companies with high-volume motions and weaker outcomes at companies with relationship-driven enterprise motions.</p>

<p>The <a href="/customer-success/">customer success directory</a> tracks the active platforms and communities. The category likely to grow in 2026 is AI-assisted QBR and executive business review tooling, which has appeared at several vendors but has not yet consolidated.</p>

<h2>What this means for hiring</h2>

<p>Three role-level shifts have already shown up in published hiring data. The first is the rise of <a href="/gtm-engineers/">GTM engineers</a>, now a standard role at companies past $5M ARR. The second is the appearance of AI-specific roles inside marketing and RevOps teams, often titled "head of AI" or "growth engineer." The third is the slow flattening of mid-funnel SDR headcount at companies that have moved aggressively to AI outbound, paired with growth in senior SDR and AE roles that handle higher-touch follow-up.</p>

<p>For salary data and trend tracking by role, the role directories on this site link out to the dedicated content sites: <a href="https://gtmepulse.com">GTME Pulse</a> for GTM engineers, <a href="https://therevopsreport.com">The RevOps Report</a> for RevOps, <a href="https://thesellerreport.com">The Seller Report</a> for AEs and SDRs, and <a href="https://theaimarketpulse.com">AI Market Pulse</a> for AI-specific roles.</p>

<h2>Where the stack goes next</h2>

<p>Two predictions look safer than the rest. First, the AI SDR and AI outbound space will consolidate, with the survivors absorbing both the augmentation and autonomous patterns into a single platform per buyer segment. Second, the workflow automation and iPaaS space will continue to converge, with AI features becoming table stakes rather than a category boundary.</p>

<p>Less certain is whether voice AI will reach the production bar that text-based AI has cleared. The technology works in narrow cases. The question is whether the cases broaden fast enough to justify the category before buyer attention shifts to the next layer of the stack.</p>

<h2>Budget shifts inside the GTM stack</h2>

<p>Practitioner surveys from Pavilion, ChiefMartec, and the LeanData benchmark series show three budget shifts inside the GTM stack since 2024. The first is a consolidation of seat-based engagement tools, with companies cutting overlapping outreach licenses as AI-augmented sequencing has reduced the seller-per-tool requirement. The second is a rise in workflow and orchestration spend, with the AI agent and workflow category now taking a meaningful slice of budgets that previously went to data enrichment alone.</p>

<p>The third is a rise in data warehouse and reverse ETL spend tied to GTM use cases. Companies that built signal-heavy outbound programs in the past 18 months have pushed more data through Snowflake, BigQuery, and Hightouch than they did historically, with the marginal cost showing up in finance reviews rather than in the marketing tool budget line. The <a href="/data-stack/">data stack directory</a> tracks the platforms inside this category.</p>

<h2>What buyers should evaluate</h2>

<p>Three evaluation criteria separate durable AI GTM tools from short-lived ones. The first is whether the tool produces a measurable outcome that the buyer's team would have produced without it, given the same input data. Tools that only repackage existing data into a chat interface tend to lose budget inside a year. The second is whether the tool is integrated with the systems where the work happens. Standalone AI tools that require a new login and a new workflow rarely sustain usage past the first quarter. The third is whether the vendor has a credible answer for data privacy and security, since enterprise buyers now block any tool that cannot pass a basic AI risk review.</p>
"""
    faqs = [
        ("Has AI replaced human SDRs?",
         "Not at scale. AI augmentation tools have changed how human SDRs work and have flattened mid-funnel SDR headcount growth at some companies, but autonomous AI SDR deployments have produced mixed results outside tightly defined segments."),
        ("What GTM tools are most at risk of consolidation in 2026?",
         "Mid-market outbound platforms that sit between AI SDR and traditional sequencing are the most consolidation-prone category. Pavilion RevOps surveys show buyer fatigue with the number of overlapping options, and several vendors have already merged or pivoted."),
        ("Are AI voice agents working in B2B sales?",
         "Inbound qualification and triage agents are in production at several public software vendors. Outbound cold-calling voice agents work in narrow scripts and fail outside them. The category will likely move slower than the marketing suggests."),
        ("How is AI changing RevOps?",
         "RevOps tooling has absorbed AI features incrementally rather than being replaced by AI-native challengers. A new layer of RevOps copilots has appeared, replacing a portion of manual analyst work without changing the core planning function."),
        ("What new GTM roles has AI created?",
         "GTM engineers are the clearest new role, now standard at companies past $5M ARR. AI-specific roles inside marketing and RevOps, often titled head of AI or growth engineer, have also appeared at well-funded scale-ups."),
    ]
    related = [
        ("AI SDR and outbound directory", "/ai-sdr/"),
        ("Voice AI directory", "/voice-ai/"),
        ("Workflow automation directory", "/workflow-automation/"),
        ("AI compliance and governance", "/ai-compliance/"),
        ("GTM engineers directory", "/gtm-engineers/"),
        ("AI Market Pulse (salary and hiring data)", "https://theaimarketpulse.com"),
    ]
    return _write_guide(g, body, faqs, related)


def build_guides_index():
    """Index page for /guides/."""
    cards = ""
    for g in GUIDES:
        cards += f"""
    <a class="guide-card" href="/guides/{g['slug']}/">
      <h3>{g['title']}</h3>
      <p>{g['summary']}</p>
      <div class="date">Published {datetime.strptime(g['date'], '%Y-%m-%d').strftime('%B %-d, %Y')}</div>
    </a>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": f"Guides | {SITE_NAME}",
        "url": f"{BASE_URL}/guides/",
        "description": "Long-form guides on B2B go-to-market roles, org design, hiring benchmarks, and the AI tooling shift.",
        "hasPart": [
            {
                "@type": "Article",
                "headline": g["title"],
                "url": f"{BASE_URL}/guides/{g['slug']}/",
                "datePublished": g["date"],
            }
            for g in GUIDES
        ],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{BASE_URL}/guides/"},
        ],
    }

    extra = f"<style>{GUIDE_CSS_EXTRA}</style>\n"
    extra += f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>\n'
    extra += f'<script type="application/ld+json">\n{json.dumps(breadcrumb, indent=2)}\n</script>\n'

    desc = "Deep-dive guides on B2B GTM roles, org design, pre-sales ratios, fractional leadership, and how AI is reshaping the modern revenue stack."
    html = get_head("GTM Guides", desc, "/guides/", extra)
    html += f"""
<body>
{get_header()}

<section class="guides-grid">
  <nav class="rp-breadcrumb"><a href="/">Home</a> &rsaquo; <span>Guides</span></nav>
  <h1>GTM Guides</h1>
  <p class="sub">Deep-dive articles on go-to-market roles, hiring benchmarks, and the AI shift inside B2B revenue teams.</p>
  <div class="guides-list">
    {cards}
  </div>
</section>

{get_newsletter_section()}
{get_footer()}
</body>
</html>"""

    out_dir = os.path.join(SITE_DIR, "guides")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    print(f"  Built: /guides/ ({len(GUIDES)} guides)")


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
    urls.append({"loc": f"{BASE_URL}/guides/", "priority": "0.8"})
    for g in GUIDES:
        urls.append({"loc": f"{BASE_URL}/guides/{g['slug']}/", "priority": "0.8"})

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

    print("\n  Building guides...")
    build_guides_index()
    build_guide_gtm_engineer_vs_revops()
    build_guide_b2b_saas_gtm_org_chart()
    build_guide_se_to_ae_ratio_benchmarks()
    build_guide_when_to_hire_fractional_gtm_leader()
    build_guide_ai_impact_b2b_gtm_stack_2026()

    # Build all extended guides via generic builder
    for _slug in _ALL_GUIDE_CONTENT.keys():
        build_guide_from_content(_slug)

    print("")
    build_robots()
    build_sitemap()
    build_404()
    build_cname()

    print(f"\nDone. {len(DIRECTORIES)} directories built, {len(GUIDES)} guides built.")
