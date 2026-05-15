"""
Guide body content. Each entry: slug -> (body_html, faqs, related)
Style rules enforced: no em dashes, no banned words, no AI tells.
"""

GUIDES_CONTENT = {}


# =============================================================================
# 1) sdr-vs-bdr-which-role
# =============================================================================
GUIDES_CONTENT["sdr-vs-bdr-which-role"] = (
"""
<p>SDR and BDR are the two most common titles for the role that opens pipeline at the top of the funnel. At many B2B SaaS companies the two titles are used as synonyms. At others, they map to a real split between inbound and outbound work. The confusion is old enough that hiring managers, recruiters, and reps themselves often disagree on what each title means.</p>

<p>The shortest answer is that the title split is mostly historical, but the work split inside teams is real. This guide walks through where the labels diverge, where they overlap, and how to decide which one fits your pipeline motion.</p>

<h2>The original split</h2>

<p>The Sales Development Representative title popularized at Salesforce in the mid-2000s referred to inbound qualification: triaging marketing-sourced leads, running first-call discovery, and routing qualified opportunities to account executives. The Business Development Representative title, used earlier at companies like Oracle and IBM, referred to outbound prospecting: cold outreach into named accounts to source new logos.</p>

<p>Bridge Group SDR surveys from the past decade show the split has blurred. Roughly two-thirds of teams use one of the titles for both functions, with the choice driven by founder preference rather than scope. The remaining third still uses SDR for inbound and BDR for outbound, with separate teams and separate managers.</p>

<h2>What inbound reps do</h2>

<p>Inbound development reps own the response to marketing-sourced leads, content downloads, demo requests, and product signups. The work is paced by the volume of inbound the marketing team produces. A typical inbound rep handles 40 to 80 leads per week, runs a short first-call discovery, and books qualified meetings for an account executive.</p>

<p>The metrics that matter are speed to lead, qualified meeting rate, and downstream pipeline conversion. The best inbound reps live in the inbound queue, are measured on response time in minutes, and rarely run multi-touch sequences. The work overlaps with the <a href="/sellers/">B2B sellers</a> directory and the practitioner content at <a href="https://thesellerreport.com">The Seller Report</a>.</p>

<h2>What outbound reps do</h2>

<p>Outbound development reps own cold prospecting into named accounts. The work is paced by the size of the territory and the depth of the named account list. A typical outbound rep runs sequences against 80 to 200 accounts at any time, builds out contacts across each account, and books first meetings with new logos.</p>

<p>The metrics that matter are accounts touched, meetings sourced, and pipeline created. Modern outbound teams also track quality signals like account fit, multi-thread depth, and reply rates. The role increasingly overlaps with <a href="/gtm-engineers/">GTM engineers</a> on the tooling side and with <a href="/ai-sdr/">AI SDR</a> systems on the automation side, with platform data tracked at <a href="https://gtmepulse.com">GTME Pulse</a>.</p>

<h2>Compensation</h2>

<p>Bridge Group and RepVue data converge on similar comp bands for both titles when work is held constant. On-target earnings for a first-year SDR or BDR at a venture-backed B2B SaaS company typically sit between 60 and 85 thousand US dollars, with a 65 to 75 percent base and the rest tied to meetings or qualified opportunities. Senior reps approaching promotion to AE earn closer to the top of that band.</p>

<p>The pay band itself does not move much by title. Where comp diverges is by motion: enterprise outbound roles tend to pay 5 to 15 percent higher than inbound SMB roles at the same company, because the cycle is longer and the named account work is harder to learn. The breakdown is tracked in detail at <a href="https://thesellerreport.com">The Seller Report</a>.</p>

<h2>Reporting structure</h2>

<p>Both titles most often report into a manager of sales development, who in turn reports to a VP Sales, head of sales development, or VP Marketing depending on the company. Reporting into marketing tends to correlate with an inbound-heavy motion. Reporting into sales tends to correlate with an outbound-heavy motion. Reporting into RevOps is rare and usually a transitional setup at companies that have just hired their first <a href="/revops/">RevOps</a> lead.</p>

<h2>Headcount ratios</h2>

<p>Bridge Group benchmarks place the SDR-to-AE ratio in B2B SaaS in a 1:2 to 1:3 band for most companies. Enterprise-led motions run closer to 1:1, with one or two named-account BDRs per enterprise AE. High-volume SMB motions run closer to 1:4, with a single inbound rep covering multiple closers.</p>

<p>The ratio matters more than the title. A team with three SDRs and one AE in a high-velocity SMB motion looks different from a team with one BDR and one AE in an enterprise motion, regardless of which label the team uses. The <a href="/b2b-saas-gtm-org-chart/" >B2B SaaS GTM org chart</a> guide walks through how the ratios shift by ARR stage.</p>

<h2>Career path</h2>

<p>The next step from either title is AE in roughly 70 percent of cases, based on a mix of Bridge Group and RepVue surveys. Other paths include moves into sales enablement, marketing operations, customer success, or RevOps. The <a href="/sellers/">sellers directory</a> and <a href="/sales-enablement/">sales enablement directory</a> cover the resources for each of those moves.</p>

<p>Tenure to promotion is more predictive than title. The median time from SDR or BDR to AE sits around 18 to 24 months at well-managed teams, with the top quartile promoting at 12 to 15 months and the bottom quartile lingering past 30 months. The <a href="/guides/when-to-promote-an-sdr-to-ae/">SDR to AE promotion</a> guide covers the signals to use.</p>

<h2>Which title to use</h2>

<p>If the role you are hiring for is primarily inbound, calling it SDR aligns with industry convention and makes the JD easier to read for candidates. If the role is primarily outbound, BDR is the more conventional label, especially for enterprise named-account work. If the role does both, pick the title that matches the dominant motion and document the scope in the job description so candidates know what they are signing up for.</p>

<p>The mistake to avoid is using the title split as a signaling tool to imply seniority. Some teams use BDR to mean a more senior SDR, which only works inside the company and confuses external candidates. If you need a senior tier, create a Senior SDR or Senior BDR title with its own scorecard, comp band, and promotion criteria.</p>

<h2>Common org mistakes</h2>

<p>Three patterns recur in the hiring reviews published by Pavilion and Bridge Group. The first is splitting inbound and outbound across two titles without splitting the management, which produces a manager who only knows one half of the job well. The second is pairing one SDR or BDR with multiple AEs across very different segments, which spreads the rep too thin to specialize. The third is over-investing in outbound headcount before the inbound funnel is converting, which masks weak marketing with raw activity.</p>

<p>The fix to all three is to write the scope before the title. The label can be SDR, BDR, or something else. What matters is whether the rep, the manager, and the AE all describe the role the same way on day 60.</p>
""",
[
    ("Is SDR or BDR more senior?",
     "Neither is senior in industry convention. Some companies use BDR to imply seniority over SDR, but the practice is inconsistent and confuses external candidates. If you need a senior tier, create a Senior SDR or Senior BDR with its own scorecard rather than relying on the title split."),
    ("Which title is used for outbound work?",
     "BDR is the more common label for outbound named-account prospecting, especially at enterprise B2B companies. SDR is more common for inbound qualification work, though about two-thirds of teams use a single title for both motions."),
    ("Do SDRs and BDRs get paid differently?",
     "At the same company and same motion, comp bands are similar. Where pay diverges is by segment: enterprise outbound roles tend to pay 5 to 15 percent more than inbound SMB roles because the cycle is longer and the prospecting work is harder to learn."),
    ("How many SDRs per AE is normal?",
     "Bridge Group benchmarks put the ratio in a 1:2 to 1:3 band at most B2B SaaS companies. Enterprise motions run closer to 1:1 and high-volume SMB motions run closer to 1:4. The ratio is more about the motion than the title."),
    ("Should SDRs report into sales or marketing?",
     "Both patterns are common. Reporting into marketing correlates with inbound-heavy motions. Reporting into sales correlates with outbound-heavy motions. The function lives well in either place as long as the manager owns the metrics that match the team's actual work."),
],
[
    ("B2B sellers directory", "/sellers/"),
    ("Sales enablement directory", "/sales-enablement/"),
    ("AI SDR and outbound directory", "/ai-sdr/"),
    ("RevOps directory", "/revops/"),
    ("The Seller Report (comp and tools)", "https://thesellerreport.com"),
    ("GTME Pulse (GTM engineer salary data)", "https://gtmepulse.com"),
]
)


# =============================================================================
# 2) inside-sales-vs-field-sales
# =============================================================================
GUIDES_CONTENT["inside-sales-vs-field-sales"] = (
"""
<p>Inside sales and field sales used to describe two clearly separate motions. Inside meant the seller worked from a desk, used the phone, ran demos over web conferencing, and closed remotely. Field meant the seller worked from a territory, visited customers in person, ran on-site discovery, and closed face to face.</p>

<p>That clean split is mostly gone. Hybrid motions, post-pandemic remote work, and AI-augmented outbound have produced a middle ground where most enterprise sellers run a mix of remote and on-site work, and most SMB sellers never visit a customer in person. This guide walks through how the math has shifted and where the labels still mean something.</p>

<h2>What inside sales means today</h2>

<p>Inside sales today refers to a seller who runs the entire sales cycle remotely, from prospecting to discovery to demo to close. The motion runs on video, phone, and email. Travel is rare. The seller often handles a high volume of accounts in a defined territory, with deals closing in 30 to 90 days for mid-market and longer for enterprise hybrid work.</p>

<p>Bridge Group inside sales benchmarks place quotas in a 600K to 1.4M annual band for mid-market AEs, with on-target earnings between 200K and 320K US dollars at most well-funded B2B SaaS companies. The <a href="/sellers/">sellers directory</a> and <a href="https://thesellerreport.com">The Seller Report</a> track comp by segment.</p>

<h2>What field sales means today</h2>

<p>Field sales today refers to a seller assigned to a geographic or vertical territory who spends meaningful time on-site with customers. The motion still uses video and phone, but the seller travels for major-account meetings, executive briefings, conferences, and key-decision moments. Deal cycles are longer, typically 6 to 18 months for enterprise software.</p>

<p>Field AE quotas in B2B SaaS run in a 1.4M to 3M annual band at most companies, with on-target earnings between 280K and 450K US dollars. The pay premium reflects the longer cycle, the larger deal size, and the operational cost of running a territory. The <a href="/revenue-leaders/">revenue leaders directory</a> and <a href="https://thecroreport.com">The CRO Report</a> publish the benchmark data by segment.</p>

<h2>Hybrid motions and the messy middle</h2>

<p>Most B2B SaaS companies today run a hybrid motion that does not fit either label cleanly. Mid-market AEs might travel for two to four deals a quarter. Enterprise AEs might run 60 percent of their work remotely. The label that fits is the dominant mode, not the only mode.</p>

<p>The shift accelerated during the pandemic and has held since. ICONIQ Growth surveys from 2024 and 2025 show enterprise software buyers now expect at least 30 percent of seller interactions to be remote, even on six-figure deals. The same surveys show field travel did not collapse to zero. Customers still want on-site executive presence for major decisions, on-site discovery for complex deployments, and on-site QBRs for strategic accounts.</p>

<h2>Comp structure differences</h2>

<p>Inside and field AEs are compensated on similar curves but with different absolute levels. Both use a base plus commission structure, with commission tied to quota attainment and accelerators above plan. Field AEs typically earn a smaller percentage of base from commission because the deal size is larger and the cycle is longer, which would create too much pay variance under a pure commission structure.</p>

<p>The other structural difference is non-recoverable draw and territory ramp. Field AEs almost always get a 90 to 180 day non-recoverable draw and a defined ramp period of 9 to 12 months. Inside AEs get a similar structure but with a shorter ramp, typically 4 to 6 months, because the cycle compresses.</p>

<h2>Headcount math by segment</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Segment</th><th>Typical ACV</th><th>Quota Band</th><th>Cycle</th><th>Motion</th></tr></thead>
<tbody>
<tr><td>SMB</td><td>5K to 25K</td><td>500K to 900K</td><td>14 to 45 days</td><td>Inside</td></tr>
<tr><td>Mid-market</td><td>25K to 100K</td><td>700K to 1.4M</td><td>45 to 120 days</td><td>Inside, light field</td></tr>
<tr><td>Enterprise</td><td>100K to 500K</td><td>1.2M to 2.5M</td><td>4 to 12 months</td><td>Hybrid</td></tr>
<tr><td>Strategic</td><td>500K plus</td><td>2M to 4M</td><td>6 to 18 months</td><td>Field</td></tr>
</tbody>
</table></div>

<h2>Pre-sales support</h2>

<p>The <a href="/presales/">pre-sales</a> ratio differs by motion. Inside SMB sellers rarely get a dedicated SE. Mid-market inside sellers often share one SE across three to five AEs. Enterprise hybrid sellers typically have one SE per two to three AEs. Field strategic sellers run with one or even two SEs per AE on the largest accounts. The <a href="/guides/se-to-ae-ratio-benchmarks/">SE to AE ratio</a> guide breaks down the math.</p>

<h2>Where AI has changed the picture</h2>

<p>AI tooling has compressed inside sales workflows more than field sales workflows. <a href="/ai-sdr/">AI SDR</a> systems and modern outbound platforms cover much of the prospecting and qualification work that inside reps used to do manually. AI-assisted research, call recording analysis, and CRM auto-update tools have reduced the time inside AEs spend on administrative work.</p>

<p>Field sales has absorbed AI more slowly. The work is relationship-driven, multi-stakeholder, and dependent on on-site signal that AI tools cannot read well. Field AEs benefit from AI on the back end, in call summaries and account research, but the front end of the role still depends on human judgment and presence.</p>

<h2>Which motion fits which company</h2>

<p>The choice between inside and field is structurally determined by ACV and cycle, not by preference. A company with a 15K ACV cannot afford a field motion. A company with a 250K ACV cannot win competitive enterprise deals without on-site presence at key moments. The middle range is where the decision matters, and most B2B SaaS companies between 50K and 150K ACV run a hybrid motion by default.</p>

<p>Pavilion and OpenView benchmarks both show that companies trying to run a pure inside motion at high ACV lose deals to competitors who travel. Companies trying to run a pure field motion at low ACV bleed margin and cannot scale headcount past a single quarter. The hybrid pattern wins because it matches investment to deal value.</p>

<h2>Common mistakes</h2>

<p>The three recurring mistakes in this category are easy to spot. The first is hiring a field AE profile for an inside role and paying them like a field rep, which produces an AE who does not run enough volume to hit quota. The second is the reverse, hiring an inside AE for a field role and underfunding their travel budget, which produces an AE who never visits accounts and loses competitive cycles to a competitor who does.</p>

<p>The third is treating the motion as fixed rather than evolving. Companies that grow ACV from SMB into enterprise need to convert at least part of their AE bench to hybrid or field over 12 to 24 months. Companies that move down-market need to convert in the other direction. Either way, the seller profile, ramp, comp, and quota model all need to move together.</p>
""",
[
    ("Is field sales still relevant in B2B SaaS?",
     "Yes, for deals above roughly 100K ACV. ICONIQ Growth surveys show enterprise buyers still expect on-site executive presence at key decision moments, even though 30 to 60 percent of seller interactions now happen remotely. The hybrid motion is the new default at most B2B SaaS companies past mid-market."),
    ("What is the quota difference between inside and field AEs?",
     "Bridge Group benchmarks put mid-market inside AE quotas in a 600K to 1.4M annual band, while enterprise field AE quotas run 1.4M to 3M. The differential reflects the larger deal size, longer cycle, and higher seller cost of a field motion."),
    ("Do inside sales reps make less money?",
     "OTE bands are lower on absolute dollars for inside than for field at the same company, but the ramp is shorter and the quota is more predictable. Top inside AEs at high-ACV mid-market companies can match or exceed field AE comp at slower-growing companies."),
    ("How has remote work changed the split?",
     "It collapsed the clean separation. Most enterprise sellers now run a hybrid motion with two to four travel trips per quarter rather than weekly territory travel. The label of inside or field is shorthand for the dominant mode, not the only mode."),
    ("When should a company switch from inside to field?",
     "When ACV crosses roughly 100K and competitive enterprise deals are being lost to vendors who travel. The transition is gradual, with mid-market AEs taking on hybrid coverage of larger accounts before a dedicated field bench is built out."),
],
[
    ("B2B sellers directory", "/sellers/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("Pre-sales and SE directory", "/presales/"),
    ("AI SDR and outbound directory", "/ai-sdr/"),
    ("The Seller Report (comp data)", "https://thesellerreport.com"),
    ("The CRO Report (leadership comp)", "https://thecroreport.com"),
]
)


# =============================================================================
# 3) demand-gen-vs-growth-marketing
# =============================================================================
GUIDES_CONTENT["demand-gen-vs-growth-marketing"] = (
"""
<p>Demand generation and growth marketing are two of the most commonly confused functions in B2B SaaS. Some teams use the titles as synonyms. Other teams treat them as separate functions reporting to different VPs. The lack of consistent definitions across the industry has produced real confusion in hiring, scoping, and headcount planning.</p>

<p>The clearest distinction is that demand gen owns the pipeline number for the sales team. Growth marketing owns experiments and product-driven acquisition that may or may not produce sales-ready pipeline. The functions overlap on tactics but answer to different success metrics.</p>

<h2>What demand gen owns</h2>

<p>Demand gen owns the pipeline number. The function builds and runs the programs that produce marketing-qualified leads, opportunities, and pipeline dollars at a measurable cost per stage. Paid acquisition, content syndication, email nurture, webinars, field events, and partner-sourced pipeline all live inside demand gen at most B2B SaaS companies.</p>

<p>The function is paced by the sales pipeline coverage target, usually 3x to 4x the quarterly bookings goal. Demand gen leaders spend their week on funnel conversion analysis, channel mix decisions, lead handoff with sales, and pipeline forecast reviews. The <a href="/demand-gen/">demand gen directory</a> and <a href="https://demandgeninsider.com">Demand Gen Insider</a> track the resources practitioners use.</p>

<h2>What growth marketing owns</h2>

<p>Growth marketing owns the experimentation and product-driven acquisition motion. The function runs A/B tests on landing pages, signup flows, pricing pages, and product-led growth surfaces. At companies with a free trial or freemium tier, growth marketing also owns activation, conversion to paid, and the early stages of expansion that happen inside the product.</p>

<p>The function is paced by experiment velocity and learning rate rather than by pipeline coverage. Growth marketing leaders spend their week on experiment design, statistical analysis, and product partnerships with engineering and product. The role has roots in consumer growth teams at Facebook, Dropbox, and Pinterest, and most senior growth marketers came up through those motions before moving to B2B.</p>

<h2>The handoff problem</h2>

<p>The hardest scope question is what happens to inbound product signups. At companies with a clean PLG motion, growth marketing owns the signup flow, activation, and conversion to paid. At companies with a hybrid PLG plus sales-led motion, the handoff between growth-driven activation and sales-driven expansion lives in a gray zone. The <a href="/guides/product-led-growth-vs-sales-led-growth/">PLG vs SLG</a> guide walks through how teams resolve it.</p>

<p>The cleanest resolution is to assign accounts above a usage or fit threshold to sales, with growth marketing keeping ownership of the long tail and the activation surfaces. The messier resolution is to share ownership across both functions, which works for two quarters and then breaks under attribution disputes. The best version of this assignment is documented in a shared playbook between the VP Marketing or CMO and the head of growth.</p>

<h2>Comp benchmarks</h2>

<p>OpenView, Pavilion, and ICONIQ Growth benchmarks place senior demand gen IC base salaries in a 140K to 200K US dollar band at venture-backed B2B SaaS companies, with directors at 180K to 240K and VPs at 230K to 320K. Bonus structures typically tie 15 to 25 percent of total comp to pipeline and bookings goals.</p>

<p>Growth marketing comp runs slightly higher at senior levels at companies with a real PLG motion, where the function carries direct revenue accountability. At sales-led companies without a strong product growth surface, growth marketing comp tends to align with demand gen. The benchmark data is tracked at <a href="https://demandgeninsider.com">Demand Gen Insider</a> and across the <a href="/demand-gen/">demand gen</a> directory.</p>

<h2>Reporting structure</h2>

<p>Demand gen almost always reports to the CMO or VP Marketing. Some early-stage companies place it under a head of growth or head of revenue, but the standard at scale is inside marketing. Growth marketing splits more, with some companies placing it inside marketing under the CMO, others inside product under the CPO, and a few inside revenue under the CRO at companies with strong PLG-to-sales handoff.</p>

<p>Bessemer Cloud Index and ChiefMartec data show the reporting line for growth marketing tracks the strength of the company's product-led motion. Companies with a strong PLG motion put growth marketing closer to product. Companies with weak PLG and strong sales put growth marketing inside marketing.</p>

<h2>Hiring order</h2>

<p>Most B2B SaaS companies hire demand gen first. The first demand gen hire typically arrives at 1M to 3M ARR, runs the inbound and outbound paid mix, and produces measurable pipeline within two quarters. The first growth marketing hire arrives later, usually at 5M to 15M ARR, and only at companies with a real product signup surface.</p>

<p>Companies that hire growth marketing before demand gen often regret it. The growth function struggles to produce pipeline without a working marketing engine to layer on, and the first growth hire ends up doing demand gen work under a different title. The reverse mistake, hiring demand gen first and then expecting them to also run product experiments, often works in the short term and then breaks at scale.</p>

<h2>Tool stack differences</h2>

<p>The two functions share a marketing automation platform, a CRM, and a CDP at most companies. Where the stacks diverge is in the experimentation and product analytics layer. Growth marketing depends on tools like Amplitude, Mixpanel, and Heap for product analytics, on Statsig or Optimizely for experimentation, and on tight integration with the engineering org. Demand gen depends on tools like LinkedIn, paid search platforms, ABM platforms, and the <a href="/marketing-ops/">marketing operations</a> stack.</p>

<p>The overlap is the marketing automation platform and the CRM, which both functions need access to. The split is everything below those two systems. The <a href="https://mopsreport.com">MOPs Report</a> tracks the marketing operations side of the stack in detail.</p>

<h2>Common org mistakes</h2>

<p>Three patterns recur. The first is treating growth marketing as a label upgrade for demand gen, which produces a team paid like growth that delivers demand gen results, and a CMO who cannot tell which function is underperforming. The second is splitting demand gen and growth across two reporting lines without a shared funnel definition, which produces attribution disputes and a sales team that does not know who to call.</p>

<p>The third is hiring a senior growth marketer at a company without a PLG surface, which leaves the new hire running experiments that have no path to revenue. The fix to all three is to write the funnel definition, the channel ownership matrix, and the experiment-to-revenue path before posting the role. The label can be either one. What matters is whether the team can describe what they own without overlapping with each other.</p>

<h2>Where the two functions are converging</h2>

<p>AI tooling has narrowed the gap between demand gen and growth marketing in the past 18 months. AI-assisted landing page generation, automated A/B testing, and conversion analysis tools have lowered the cost of experimentation enough that demand gen teams can run growth-style work without a dedicated growth hire. At the same time, growth marketing teams now use paid acquisition tools that look identical to the ones demand gen has always used.</p>

<p>The functions are unlikely to merge into one, because the reporting line and the success metric still differ. They are likely to share more day-to-day tooling and to overlap more on tactical execution, while continuing to answer to different KPIs.</p>
""",
[
    ("Are demand gen and growth marketing the same thing?",
     "No. Demand gen owns the pipeline number for the sales team. Growth marketing owns experimentation and product-driven acquisition. The tactics overlap, but the success metrics differ: demand gen reports on pipeline and bookings, growth marketing reports on experiment velocity and product revenue."),
    ("Which function should a B2B SaaS company hire first?",
     "Demand gen. The first demand gen hire typically arrives at 1M to 3M ARR and produces pipeline within two quarters. Growth marketing only makes sense once there is a real product signup or PLG surface to optimize, usually past 5M ARR."),
    ("Where does growth marketing report?",
     "It depends on the strength of the company's PLG motion. Companies with a strong product-led motion place growth inside product under the CPO. Companies with weak PLG place growth inside marketing under the CMO. A small number of companies place growth inside revenue under the CRO."),
    ("How is growth marketing compensated differently?",
     "At PLG companies with direct revenue accountability, senior growth marketers earn more than senior demand gen ICs. At sales-led companies, the two roles compensate similarly. Bonus structures also differ, with demand gen tied to pipeline and growth tied to experiment-driven revenue."),
    ("Has AI changed the split between the two roles?",
     "AI tooling has narrowed the day-to-day tactical overlap, with demand gen teams now able to run growth-style experiments at low cost. The strategic distinction in reporting line and success metric still holds, and most B2B SaaS companies keep both functions even as the tooling converges."),
],
[
    ("Demand generation directory", "/demand-gen/"),
    ("Marketing operations directory", "/marketing-ops/"),
    ("ABM platforms and resources", "/abm/"),
    ("RevOps directory", "/revops/"),
    ("Demand Gen Insider (benchmarks)", "https://demandgeninsider.com"),
    ("MOPs Report (marketing ops salary)", "https://mopsreport.com"),
]
)


# =============================================================================
# 4) demand-gen-vs-product-marketing
# =============================================================================
GUIDES_CONTENT["demand-gen-vs-product-marketing"] = (
"""
<p>Demand generation and product marketing are the two halves of a working B2B marketing org. The functions are often confused by people outside marketing, which leads to mis-hiring and to muddled handoffs between the team building messaging and the team running campaigns.</p>

<p>The simplest split is that product marketing owns what the company says and demand gen owns who hears it. Product marketers build the positioning, the messaging framework, the launch plan, and the sales enablement assets. Demand generation runs the channels, the campaigns, and the pipeline coverage that turn those assets into measurable revenue.</p>

<h2>What product marketing owns</h2>

<p>Product marketing owns the answer to four questions: who buys this product, why they buy, what the product is at a positioning level, and how to talk about it. The function builds the messaging framework, the buyer personas, the competitive positioning, the launch plan for new product releases, and most of the sales-facing content.</p>

<p>Senior product marketers run the launch process for new features and new product lines. They write the homepage. They own the pricing page. They build the sales pitch deck. They run the win-loss program. Pavilion and the Product Marketing Alliance both publish surveys that converge on this scope at companies past 10M ARR.</p>

<h2>What demand gen owns</h2>

<p>Demand gen owns the pipeline coverage number. The function builds and runs the programs that produce marketing-qualified leads, opportunities, and pipeline dollars. Paid acquisition, content syndication, webinars, nurture campaigns, and field events all live inside <a href="/demand-gen/">demand generation</a>.</p>

<p>Demand gen leaders spend their week on channel mix, funnel conversion analysis, pipeline coverage reviews, and the handoff with sales. The work is paced by quarterly pipeline goals. The function depends on product marketing for the messaging and positioning that the campaigns deploy.</p>

<h2>Where the handoff lives</h2>

<p>The handoff is the campaign brief. Product marketing writes the positioning and the messaging framework. Demand gen writes the campaign brief that translates the framework into channel-specific assets, then runs the campaign. The brief is the artifact that both functions share, and the quality of the brief is the strongest predictor of campaign performance at most B2B SaaS companies.</p>

<p>Mature marketing orgs document the brief format and review it jointly before any campaign launch. Less mature orgs let product marketing throw assets over the wall and let demand gen wing the channel execution, which produces campaigns that miss the positioning and positioning that never reaches the market.</p>

<h2>Tool stack differences</h2>

<p>The two functions share the marketing automation platform, the CRM, and the CDP. Where the stacks diverge is in the content and competitive intelligence layer. Product marketing depends on tools like Klue, Crayon, or Klozer for competitive intel, on win-loss platforms like Clozd, and on internal tools for messaging documentation.</p>

<p>Demand gen depends on paid acquisition platforms, ABM tools, and the <a href="/marketing-ops/">marketing operations</a> stack underneath the marketing automation platform. The <a href="https://demandgeninsider.com">Demand Gen Insider</a> and <a href="https://mopsreport.com">MOPs Report</a> sites track the stack in detail.</p>

<h2>Comp benchmarks</h2>

<p>OpenView and Pavilion benchmarks place senior product marketing manager base salaries in a 150K to 200K US dollar band at venture-backed B2B SaaS companies, with directors at 180K to 240K and VPs at 230K to 300K. Bonus structures are lighter than in demand gen because the role does not carry direct pipeline accountability.</p>

<p>Senior demand gen IC comp runs in a similar band, but bonus structures tie 15 to 25 percent of total comp to pipeline and bookings goals. The result is similar OTE at senior IC levels and slightly higher OTE for demand gen at director and VP levels at companies that hit their pipeline targets.</p>

<h2>Hiring order</h2>

<p>Most B2B SaaS companies hire demand gen first. A first demand gen hire arrives around 1M to 3M ARR. A first product marketing hire arrives later, usually around 3M to 8M ARR, often when the product portfolio expands beyond a single use case.</p>

<p>Companies that hire product marketing before demand gen sometimes do it because the founder is messaging-driven and wants the positioning right before scaling acquisition. The pattern works at companies with a clear product-market fit and a founder-driven sales motion, and breaks at companies that hire a senior product marketer expecting them to also run paid acquisition. The reverse is more common and tends to work: hire demand gen first to produce pipeline, then layer in product marketing once the messaging needs to be consistent across multiple channels and segments.</p>

<h2>Reporting structure</h2>

<p>Both functions report into the CMO or VP Marketing at most B2B SaaS companies. Product marketing reporting into product happens at some PLG-heavy companies, but it is the minority pattern. Demand gen reporting outside of marketing is rare and usually a transitional setup.</p>

<p>The most common organizational tension between the two functions is the role of the head of revenue. CROs often want product marketing to report into the revenue org because they consume the sales-facing content. CMOs argue that product marketing is the strategic core of the marketing org and should not be split off. Bessemer and ICONIQ data show the CMO usually wins this argument at companies past 20M ARR.</p>

<h2>Day-to-day collaboration</h2>

<p>Effective marketing teams run a weekly working session between the head of demand gen and the head of product marketing. The agenda covers upcoming launches, campaign briefs in flight, messaging tests in market, and sales feedback on the latest assets. The session is half operational planning and half strategic alignment, and the quality of the relationship between these two leaders is one of the strongest predictors of marketing team performance at the VP level.</p>

<p>The other operational mechanism is the launch checklist. Product marketing owns the launch plan. Demand gen owns the campaign execution that turns the launch into pipeline. The launch checklist documents the handoff in enough detail that both functions can run the launch without negotiating scope each time.</p>

<h2>Common mistakes</h2>

<p>Four patterns recur. The first is splitting the two functions across two reporting lines without a shared funnel definition, which produces attribution disputes and a sales team that does not know who to call. The second is hiring a senior product marketer to also run demand gen, which produces a team that does either of the two roles well but rarely both.</p>

<p>The third is treating product marketing as a content function rather than a strategic function, which underuses the senior hire and turns the role into a writer for landing pages. The fourth is treating demand gen as a channel function rather than a pipeline function, which produces a team that hits leading indicators without producing closed revenue.</p>

<p>The fix to all four is the same: write the funnel definition, the brief format, and the launch checklist before scaling the team. The roles can be filled in any order. The artifacts are what hold the operating model together.</p>

<h2>Where the lines blur</h2>

<p>At companies with a strong PLG motion, the line between product marketing, demand gen, and growth marketing blurs further. The <a href="/guides/demand-gen-vs-growth-marketing/">demand gen vs growth marketing</a> guide walks through how those three functions divide work. The short version is that product marketing still owns the positioning, demand gen still owns the pipeline number, and growth marketing owns the experimentation and product surface conversion that sits in between.</p>
""",
[
    ("What does product marketing do?",
     "Product marketing owns the positioning, messaging framework, buyer personas, competitive intelligence, launch plans for new features, and most of the sales-facing content. The function is strategic rather than channel-driven and supplies the assets that demand gen and sales deploy in market."),
    ("Should we hire demand gen or product marketing first?",
     "Most B2B SaaS companies hire demand gen first, usually at 1M to 3M ARR, because the function produces pipeline directly. Product marketing typically arrives at 3M to 8M ARR, often when the product portfolio expands beyond a single use case or when launches become a regular operating cadence."),
    ("Do product marketers carry a pipeline number?",
     "Not directly. Product marketing typically carries goals tied to launch outcomes, win rate, and content adoption rather than pipeline coverage. The function influences pipeline through positioning and messaging quality, but the pipeline number lives with demand gen."),
    ("Where should product marketing report?",
     "Most B2B SaaS companies place it inside marketing under the CMO. A small number of PLG-heavy companies place it inside product under the CPO. The CRO sometimes argues for it to report into revenue, but at companies past 20M ARR the CMO almost always retains the function."),
    ("What is the most common mistake in this split?",
     "Treating product marketing as a content function rather than a strategic function. The senior product marketer hire only pays back when the role owns positioning, win-loss, and the launch process. Pure content production is a junior role that does not require senior product marketing experience."),
],
[
    ("Demand generation directory", "/demand-gen/"),
    ("Marketing operations directory", "/marketing-ops/"),
    ("ABM platforms and resources", "/abm/"),
    ("Sales enablement directory", "/sales-enablement/"),
    ("Demand Gen Insider (benchmarks)", "https://demandgeninsider.com"),
    ("MOPs Report (marketing ops salary)", "https://mopsreport.com"),
]
)


# =============================================================================
# 5) marketing-ops-vs-revops
# =============================================================================
GUIDES_CONTENT["marketing-ops-vs-revops"] = (
"""
<p>Marketing operations and revenue operations both sit at the operations layer underneath the revenue org. Both own data, both own systems, and both work cross-functionally. The titles are sometimes used as if they were tiers of the same role, with RevOps being treated as the senior version of MOps. That framing is wrong and produces hiring mistakes.</p>

<p>MOps and RevOps are distinct functions with overlapping toolsets. MOps owns the marketing automation platform, lead lifecycle, and the systems and reporting under the marketing org. RevOps owns the cross-functional revenue process across sales, marketing, and customer success, the CRM, the planning models, and the forecast.</p>

<h2>What marketing ops owns</h2>

<p>Marketing ops owns the marketing automation platform, the lead lifecycle, lead scoring, lead routing, attribution, and the campaign infrastructure that demand gen depends on. The function lives inside marketing and reports to the CMO or VP Marketing in almost all B2B SaaS companies.</p>

<p>Senior MOps leaders run the lead-to-revenue process from form fill through MQL to sales acceptance. They own Marketo, HubSpot, Pardot, or whatever marketing automation platform the company runs on. They own the attribution model and the marketing source reporting. The <a href="/marketing-ops/">marketing operations directory</a> and <a href="https://mopsreport.com">MOPs Report</a> track the platforms and practitioner communities.</p>

<h2>What RevOps owns</h2>

<p>RevOps owns the revenue process across sales, marketing, and customer success. The function owns the CRM, quarterly planning, quota and territory design, the lead-to-cash process, the forecast, and the cross-functional reporting that leadership consumes. The function reports to the CRO at companies past Series B, or to the CEO or COO earlier.</p>

<p>A senior RevOps leader runs the planning models, the forecast call, the deal desk, the comp plan analysis, and the cross-functional dashboards that anchor the revenue function. The <a href="/revops/">RevOps directory</a> and <a href="https://therevopsreport.com">The RevOps Report</a> track the function in detail.</p>

<h2>Where the overlap lives</h2>

<p>The overlap is the handoff between marketing and sales. Both functions touch the lead lifecycle. Both functions touch the attribution model. Both functions need clean data flowing from the marketing automation platform into the CRM. The two functions either work well together or fight constantly over data ownership and reporting interpretations.</p>

<p>The cleanest division is to have MOps own everything inside the marketing automation platform and the lead routing rules, with RevOps owning everything inside the CRM and the cross-functional process. The handoff lives in the field mapping and the data sync between the two systems. When that handoff is well documented and stable, the two functions cooperate. When it is unstable, the two functions blame each other.</p>

<h2>Reporting structure</h2>

<p>MOps reports to marketing in 90 percent of cases. RevOps reports to revenue or operations. The two functions do not typically share a manager, which is a feature rather than a bug. A shared manager would force one function to subordinate to the other and would lose the cross-functional perspective that RevOps brings.</p>

<p>The exception is small companies where one person covers both functions. A single ops hire at 3M to 5M ARR often runs both the marketing automation platform and the CRM. The setup works for a year or two and then breaks under workload, at which point the company hires a second person and the two functions split formally.</p>

<h2>Comp benchmarks</h2>

<p>Pavilion and RepVue data place senior MOps manager base salaries in a 130K to 180K US dollar band at venture-backed B2B SaaS companies, with directors at 160K to 220K and VPs at 200K to 280K. RevOps salaries run slightly higher at the same seniority because the scope is broader. Senior RevOps managers earn 140K to 200K base, directors 170K to 240K, and VPs 240K to 350K.</p>

<p>The pay differential is real but smaller than the title would suggest. The bigger differential is in equity, where RevOps leaders tend to earn more because the scope influences the planning models and forecast that the board reviews.</p>

<h2>Hiring order</h2>

<p>The hiring order depends on company motion. PLG-led companies usually hire MOps first because the marketing automation platform is the central system. Sales-led companies usually hire RevOps first because the CRM and forecast are the central systems. Companies with balanced motions often hire both within a year of each other, typically at 3M to 8M ARR.</p>

<p>A common founder mistake is hiring a RevOps lead and expecting them to also run the marketing automation platform. The senior RevOps profile rarely has deep Marketo or HubSpot configuration experience. The mistake produces a brittle marketing automation setup and a frustrated RevOps lead doing work outside their scope.</p>

<h2>Tool stack ownership</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>System</th><th>MOps</th><th>RevOps</th></tr></thead>
<tbody>
<tr><td>Marketing automation</td><td>Owner</td><td>Consumer</td></tr>
<tr><td>CRM</td><td>Consumer</td><td>Owner</td></tr>
<tr><td>Lead scoring and routing</td><td>Owner</td><td>Process partner</td></tr>
<tr><td>Attribution model</td><td>Joint, MOps leads</td><td>Joint, RevOps reviews</td></tr>
<tr><td>Forecast and planning</td><td>Consumer</td><td>Owner</td></tr>
<tr><td>Quota and territory</td><td>Consumer</td><td>Owner</td></tr>
<tr><td>Quarterly business review</td><td>Marketing portion</td><td>Revenue portion</td></tr>
<tr><td>Data warehouse and BI</td><td>Marketing surfaces</td><td>Revenue and cross-functional</td></tr>
</tbody>
</table></div>

<h2>Common mistakes</h2>

<p>Four patterns recur in MOps and RevOps hiring. The first is the title creep mistake, where a company hires a MOps manager and renames them RevOps without expanding scope. The new title sets expectations the role cannot meet and produces a planning gap at the CRO level.</p>

<p>The second is the reverse: hiring a RevOps lead and assigning them MOps work because the CMO has not hired a MOps person yet. The RevOps lead does the MOps work poorly and resents the assignment, and the actual RevOps work goes unowned. The third is letting both functions report into the same VP at scale, which produces a single point of failure and limits the cross-functional perspective.</p>

<p>The fourth is treating the attribution model as a MOps deliverable rather than a joint output. Attribution is the artifact where the two functions either align or fight. Treating it as a single-owner output produces an attribution view that one function trusts and the other rejects.</p>

<h2>Career path differences</h2>

<p>The two roles also lead to different next jobs. Senior MOps leaders move into VP Marketing or head of revenue operations roles, with the latter being a real scope expansion. RevOps leaders move into VP RevOps, chief of staff, COO, and head of strategy roles. Some RevOps leaders move into VP Sales roles, though the move is less common than the reverse.</p>

<p>The <a href="/guides/path-to-vp-revops/">path to VP RevOps</a> guide covers the career steps in detail. The <a href="https://mopsreport.com">MOPs Report</a> tracks the marketing ops side of the career market.</p>
""",
[
    ("Is RevOps the senior version of marketing ops?",
     "No. The two are distinct functions with different scope and reporting lines. RevOps covers the cross-functional revenue process across sales, marketing, and customer success. MOps covers the marketing automation platform, lead lifecycle, and marketing systems. Treating one as a tier of the other produces hiring mistakes."),
    ("Where should marketing ops report?",
     "Inside marketing, to the CMO or VP Marketing, in roughly 90 percent of cases. Reporting MOps into RevOps or into IT happens at some companies, but the work is paced by marketing campaigns and tends to suffer outside the marketing reporting line."),
    ("Who owns the attribution model?",
     "Both functions touch it. The cleanest setup is for MOps to own the model construction inside the marketing automation platform, with RevOps reviewing and signing off on the cross-functional view. Single-owner attribution tends to produce a number that one function trusts and the other rejects."),
    ("Can one person do both MOps and RevOps?",
     "At companies under about 5M ARR, often yes. A single ops hire usually handles both the marketing automation platform and the CRM. The setup breaks under workload past that ARR band, at which point the company hires a second person and splits the functions formally."),
    ("Which function pays more?",
     "At similar seniority, RevOps base salaries run 10 to 20 percent higher than MOps because the scope is broader. The equity differential at director and VP levels is larger, because RevOps influences the planning models and forecast that the board reviews."),
],
[
    ("Marketing operations directory", "/marketing-ops/"),
    ("RevOps directory", "/revops/"),
    ("Demand generation directory", "/demand-gen/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("MOPs Report (MOps salary data)", "https://mopsreport.com"),
    ("The RevOps Report (RevOps benchmarks)", "https://therevopsreport.com"),
]
)


# =============================================================================
# 6) revops-vs-sales-ops
# =============================================================================
GUIDES_CONTENT["revops-vs-sales-ops"] = (
"""
<p>The RevOps title has largely replaced sales ops at venture-backed B2B SaaS companies in the past five years. The question for founders and hiring managers is whether that replacement is a real scope expansion or a cosmetic rename. The honest answer is that it depends on the company.</p>

<p>At well-run companies, RevOps is a real expansion. The function covers sales operations, marketing operations partnerships, customer success operations, the forecast, and the cross-functional planning that touches all three pillars. At less mature companies, RevOps is sales ops with a new title and the same scope. The difference shows up in the hiring profile, the reporting line, and what the role owns on the operating cadence.</p>

<h2>What sales ops historically owned</h2>

<p>Sales ops, as the function existed at most B2B SaaS companies through 2018, owned the sales side of the operations stack. CRM administration, sales reporting, quota and territory design, commission and comp administration, deal desk support, and pipeline reporting all sat inside sales ops.</p>

<p>The function reported to the head of sales or to the CFO and was paced by quarterly sales cycles. Sales ops leaders ran the forecast call, kept the CRM clean, and produced the dashboards that VP Sales and the CFO consumed. The function was tactical and execution-focused.</p>

<h2>What RevOps adds</h2>

<p>RevOps, in its modern form, adds three things to the historical sales ops scope. The first is cross-functional partnership with marketing and customer success on the lead-to-cash process. The second is strategic planning at the company level, including the annual operating plan, segmentation analysis, and capacity planning. The third is the data layer that sits underneath all three functions, including the data warehouse, BI tooling, and cross-functional attribution.</p>

<p>The <a href="/revops/">RevOps directory</a> and <a href="https://therevopsreport.com">The RevOps Report</a> track how the function operates at companies that have made the shift. Pavilion's State of RevOps surveys put strategic planning at the center of the role at companies past 20M ARR.</p>

<h2>Where the rebrand is real</h2>

<p>The rebrand is real when three things happen. First, the function reports to the CRO or CEO rather than to the VP Sales. Second, the function covers marketing ops or partners with it on the lead-to-cash process. Third, the function owns the annual operating plan and the cross-functional segmentation work, not just the sales forecast.</p>

<p>At companies where all three are true, the senior hire is a meaningful step up from a sales ops director. The candidate profile is different, the comp is higher, and the operating cadence is different. The function influences the board deck and the CFO's planning model in ways that pure sales ops never did.</p>

<h2>Where the rebrand is cosmetic</h2>

<p>The rebrand is cosmetic when the function still reports to the VP Sales, still owns only the sales side of operations, and still spends most of its time on CRM administration and pipeline reporting. The new title attracts senior candidates who then discover the scope is smaller than the title implied. The mismatch produces turnover within 12 to 18 months.</p>

<p>Founders make this mistake when they want the RevOps brand without the cross-functional reporting line. The fix is to either expand the scope to match the title, or to keep the sales ops title and hire for the actual scope.</p>

<h2>Hiring profile differences</h2>

<p>A senior sales ops director has 7 to 12 years of sales operations experience, deep Salesforce or HubSpot administration skills, fluency with quota and territory design, and a track record of running the forecast. The role is closer to a sales leader than to a finance lead in operating posture.</p>

<p>A senior RevOps leader has the same operational foundation but adds three things: a track record of cross-functional planning, fluency with marketing ops and customer success ops, and a strategic posture that lets them sit in a CRO planning meeting and contribute beyond pipeline. The senior RevOps candidate often has consulting, finance, or chief of staff experience in addition to ops experience.</p>

<h2>Comp benchmarks</h2>

<p>Pavilion and RepVue data place senior sales ops manager base salaries in a 130K to 175K US dollar band, with directors at 160K to 220K and VPs at 200K to 280K. RevOps salaries at the same seniority run 10 to 20 percent higher, with senior managers at 140K to 200K, directors at 170K to 240K, and VPs at 240K to 350K.</p>

<p>The differential is real but small. The bigger differential is in equity at director and VP levels, where RevOps leaders earn more because the scope influences strategic outcomes the board reviews directly.</p>

<h2>Reporting line shifts</h2>

<p>Sales ops historically reported to the VP Sales, with a dotted line to the CFO. RevOps in its modern form reports to the CRO, the CEO, or the COO depending on the company. Reporting to the CFO is common at companies where finance owns capacity planning and revenue modeling, but it tends to slow the function down on operational execution.</p>

<p>Bessemer and ICONIQ Growth data both show that companies with RevOps reporting to the CRO tend to ship faster on operational changes and run looser on financial discipline. Companies with RevOps reporting to the CFO tend to ship slower and run tighter. The COO middle path is the most common at companies past 50M ARR.</p>

<h2>When to make the shift</h2>

<p>Most B2B SaaS companies make the shift between 10M and 30M ARR. Below 10M, the function does not have enough scope to justify the RevOps brand and the senior hire it implies. Above 30M, the function almost always needs to be cross-functional and strategic, regardless of what title it carries.</p>

<p>The signal that the shift is overdue is when the head of sales ops is being pulled into marketing planning, customer success planning, or annual operating plan work that the title does not cover. Either expand the scope and rename, or hire a second leader to cover the cross-functional work, depending on the existing leader's profile.</p>

<h2>What the future of the function looks like</h2>

<p>Three trends are visible in the past 24 months. The first is the appearance of GTM engineering as an adjacent function, often reporting into the same VP RevOps. The <a href="/guides/gtm-engineer-vs-revops/">GTM engineer vs RevOps</a> guide walks through the split. The second is the emergence of RevOps copilots, AI-native tools that automate a portion of the manual analyst work that historically sat inside RevOps.</p>

<p>The third is the deepening of strategic finance partnerships. RevOps leaders at companies past 50M ARR increasingly partner with finance teams on capacity planning, segmentation, and pricing decisions. The function is moving closer to the chief of staff role at some companies and closer to a strategic operations role at others.</p>

<h2>Common mistakes</h2>

<p>Three patterns recur. The first is the cosmetic rebrand without scope expansion, which produces a senior hire mismatch and turnover. The second is hiring a RevOps lead with no executive sponsor, which produces a leader who runs tickets for whichever VP shouts loudest. The third is treating RevOps as an extension of finance, which produces strong reporting and slow operational execution.</p>

<p>The fix to all three is to write the scope, the reporting line, and the operating cadence before the hire starts. The label can be either sales ops or RevOps. What matters is whether the role is set up to deliver the work that the company needs.</p>
""",
[
    ("Is RevOps just a new name for sales ops?",
     "Sometimes. At mature companies, RevOps is a real scope expansion covering sales, marketing, and customer success operations plus cross-functional planning. At less mature companies, RevOps is sales ops with a new title. The difference shows up in the reporting line, the hiring profile, and what the role owns on the operating cadence."),
    ("When should a company make the shift from sales ops to RevOps?",
     "Most B2B SaaS companies make the shift between 10M and 30M ARR. Below 10M, the function does not have enough cross-functional scope. Above 30M, the function almost always needs to be cross-functional, regardless of title. The trigger is when the existing leader is doing cross-functional work the sales ops title does not cover."),
    ("Where should RevOps report?",
     "Most commonly to the CRO, with COO and CFO as common alternatives. Reporting to the CRO produces faster operational execution and looser financial discipline. Reporting to the CFO produces tighter discipline and slower execution. The COO middle path is the most common at companies past 50M ARR."),
    ("How is the hiring profile different?",
     "A senior RevOps leader has the same operational foundation as a senior sales ops director but adds cross-functional planning experience, fluency with marketing and customer success ops, and a strategic posture suited to executive planning meetings. Consulting, finance, or chief of staff experience is common in the RevOps candidate pool."),
    ("Does RevOps pay more than sales ops?",
     "Yes, but the differential is smaller than the title implies. Senior RevOps base salaries run 10 to 20 percent above sales ops at the same seniority. The bigger differential is in equity at director and VP levels, where RevOps leaders earn more because the scope influences board-reviewed strategic outcomes."),
],
[
    ("RevOps directory", "/revops/"),
    ("Marketing operations directory", "/marketing-ops/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("GTM engineers directory", "/gtm-engineers/"),
    ("The RevOps Report (benchmarks)", "https://therevopsreport.com"),
    ("The CRO Report (leadership comp)", "https://thecroreport.com"),
]
)


# =============================================================================
# 7) customer-success-vs-account-management
# =============================================================================
GUIDES_CONTENT["customer-success-vs-account-management"] = (
"""
<p>Customer success and account management cover the post-sale relationship at B2B SaaS companies. Both functions own retention. Both touch expansion. Both report into the revenue or customer org at most companies. The titles are sometimes used as synonyms and sometimes treated as separate functions with different scopes.</p>

<p>The cleanest distinction is that customer success owns adoption, value realization, and renewal. Account management owns commercial expansion and quota-carrying upsell. Some companies blend the two into a single role. Others split them deliberately and staff both. The choice depends on motion, segment, and how much expansion the product naturally produces.</p>

<h2>What customer success owns</h2>

<p>Customer success owns the work that keeps customers using the product and getting value from it. The function runs onboarding, adoption tracking, health scoring, executive business reviews, and the renewal conversation. The CSM role is typically not commission-paid on net new revenue, though variable comp tied to renewal rate is common.</p>

<p>The function reports to a VP Customer Success who reports to the CRO at most B2B SaaS companies past Series B. Pavilion, the CS Pulse, and the Gainsight Pulse surveys all converge on a similar scope at companies between 10M and 100M ARR.</p>

<h2>What account management owns</h2>

<p>Account management owns the commercial expansion of existing accounts. The function runs upsell, cross-sell, and price increases at renewal. AMs carry quota and earn commission on expansion bookings. The role is structurally closer to a sales role than to a customer-facing role, though the day-to-day work involves more relationship management than new logo selling.</p>

<p>The function reports either to the head of sales or to the head of customer success, depending on the company. Reporting into sales tends to align with companies that treat expansion as a sales motion. Reporting into customer success tends to align with companies that treat expansion as a service motion.</p>

<h2>The blended model</h2>

<p>At companies with a strong PLG motion or with low-touch SMB customers, customer success and account management are often the same role. A single CSM owns adoption, renewal, and expansion, with quota tied to net retention rather than to new bookings. The blended model works at low ACV with high volume.</p>

<p>The blended model breaks at higher ACV. Once accounts are large enough that adoption work and commercial work each fill a person's time, the two roles need to split. Bessemer and ICONIQ data show the split usually happens around 50K to 100K ACV at most B2B SaaS companies. Below that band, one CSM can plausibly own both. Above it, the workload exceeds a single role.</p>

<h2>Comp benchmarks</h2>

<p>Pavilion, Gainsight, and RepVue data place senior CSM base salaries in a 110K to 150K US dollar band at venture-backed B2B SaaS companies, with directors at 150K to 200K and VPs at 200K to 280K. Variable comp ties 15 to 30 percent of total OTE to retention and adoption metrics.</p>

<p>Account manager OTE runs higher because the role carries quota. Senior AMs earn 160K to 220K OTE, with a 50/50 or 60/40 base-to-variable split that mirrors AE comp structures. Senior AMs at companies with strong expansion motions often out-earn AEs in absolute dollars because the renewal cycle and expansion are more predictable than new logo selling.</p>

<h2>Headcount math</h2>

<p>CSM coverage ratios depend heavily on ACV. SMB CSMs typically cover 100 to 300 accounts each on a pooled model. Mid-market CSMs cover 30 to 80 accounts each. Enterprise CSMs cover 8 to 20 accounts. Strategic CSMs cover 1 to 5 accounts.</p>

<p>Account manager ratios run lower because the role is commercial. Senior AMs typically cover 10 to 30 accounts at most companies. The <a href="/customer-success/">customer success directory</a> and <a href="https://thecspulse.com">The CS Pulse</a> track the benchmark data by segment and motion.</p>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Segment</th><th>CSM Accounts</th><th>AM Accounts</th><th>Common Setup</th></tr></thead>
<tbody>
<tr><td>SMB (under 25K ACV)</td><td>100 to 300</td><td>Blended</td><td>Single role</td></tr>
<tr><td>Mid-market (25K to 100K)</td><td>30 to 80</td><td>50 to 100</td><td>Split or blended</td></tr>
<tr><td>Enterprise (100K to 500K)</td><td>8 to 20</td><td>15 to 40</td><td>Always split</td></tr>
<tr><td>Strategic (500K plus)</td><td>1 to 5</td><td>3 to 10</td><td>Always split, often dual coverage</td></tr>
</tbody>
</table></div>

<h2>Reporting structure</h2>

<p>Customer success almost always reports to the CRO or to the VP Customer Success who reports to the CRO. Reporting to the COO or CEO happens at smaller companies but converges on the CRO model past Series B.</p>

<p>Account management splits more. Some companies place AMs inside customer success, sharing a VP. Others place AMs inside sales, sharing the VP Sales and the same forecast cadence as AEs. Both patterns work. The choice depends on whether the company sees expansion as a service-led motion or a sales-led motion.</p>

<h2>Compensation philosophy</h2>

<p>The compensation philosophy difference between the two roles is the cleanest way to see the underlying difference in function. CSMs are compensated for adoption and retention. The bonus pool ties to product adoption metrics, NPS, renewal rate, and gross retention. AMs are compensated for revenue expansion. The bonus pool ties to net new bookings from existing accounts, upsell ARR, and net retention.</p>

<p>When the two roles share a single compensation philosophy, the role tends to drift toward whichever metric is easier to influence. Pure retention-driven comp produces CSMs who avoid hard pricing conversations. Pure expansion-driven comp produces CSMs who under-invest in adoption. The split exists in part to avoid that drift.</p>

<h2>Career path differences</h2>

<p>CSM senior leaders move into VP Customer Success, head of professional services, head of customer experience, or COO roles. Some move into customer marketing or product roles. The <a href="/guides/path-to-vp-customer-success/">path to VP Customer Success</a> guide covers the career steps.</p>

<p>Account manager senior leaders move into VP Account Management, VP Sales, or head of enterprise sales roles. The career path is closer to a sales career path than to a customer career path, and senior AMs at enterprise SaaS companies often move into AE leadership rather than CS leadership.</p>

<h2>Common mistakes</h2>

<p>Four patterns recur in CSM and AM scoping. The first is the blended role at high ACV, where one person tries to do both adoption and commercial work and does neither well. The second is treating account management as a renewal function, which produces AMs who do not aggressively push expansion and miss the upsell cycle.</p>

<p>The third is putting CSMs on quota for new logo expansion. The role is not structured to source new buying centers inside an existing account and tends to underperform on that metric. The fourth is splitting the roles without aligning the comp plan, which produces conflicting incentives between the CSM and the AM covering the same account.</p>

<p>The fix to all four is to write the scope, the comp plan, and the account coverage model together. The split between CSM and AM works when the two roles operate from a shared playbook with non-overlapping success metrics. It breaks when the comp plan, the scope, or the coverage assignment is left ambiguous.</p>
""",
[
    ("What is the difference between CSM and account manager?",
     "CSMs own adoption, value realization, and renewal. Account managers own commercial expansion and carry quota on upsell bookings. At low ACV with high volume, the two roles often blend into a single position. Above roughly 50K ACV, the workload exceeds a single role and the two functions split."),
    ("Does customer success carry quota?",
     "CSMs typically carry retention and adoption goals rather than new bookings quota. Variable comp ties 15 to 30 percent of total OTE to renewal rate, gross retention, and adoption metrics. Companies that put CSMs on a new bookings quota usually see the role drift toward sales work and away from adoption."),
    ("Where does account management report?",
     "Both inside customer success and inside sales are common patterns. Reporting into sales tends to align with companies that treat expansion as a sales motion. Reporting into customer success tends to align with companies that treat expansion as a service motion. Either pattern works with the right comp plan and coverage model."),
    ("When should a SaaS company split CS and AM into separate roles?",
     "When ACV crosses roughly 50K to 100K and the workload for adoption work and commercial work each fill a person's time. Below that ACV band, a blended role works. Above it, the two functions need to split to prevent the role from drifting toward whichever metric is easier to influence."),
    ("Who owns the renewal conversation?",
     "Both functions touch it. The cleanest setup is for the CSM to own the strategic renewal conversation and the AM to own the commercial terms and pricing. At companies with a blended model, the CSM owns both. At companies that split, the AM closes the renewal and the CSM influences it through the year's adoption work."),
],
[
    ("Customer success directory", "/customer-success/"),
    ("B2B sellers directory", "/sellers/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("Sales enablement directory", "/sales-enablement/"),
    ("The CS Pulse (CS comp data)", "https://thecspulse.com"),
    ("The CRO Report (leadership comp)", "https://thecroreport.com"),
]
)


# =============================================================================
# 8) account-manager-vs-account-executive
# =============================================================================
GUIDES_CONTENT["account-manager-vs-account-executive"] = (
"""
<p>Account manager and account executive sit at opposite ends of the same revenue motion. AEs close new business. AMs grow it. The titles are sometimes confused, especially at companies where both roles carry quota and both manage book of business relationships. The work, the cycle, and the seller profile differ.</p>

<p>The shortest distinction is that AEs hunt and AMs farm. AEs source new logos, run the deal cycle from first meeting to close, and earn commission on net new bookings. AMs own existing accounts, run renewals and expansion conversations, and earn commission on upsell and renewal premium.</p>

<h2>What account executives own</h2>

<p>Account executives own the new logo motion. The role runs the deal cycle from sales-accepted lead to closed-won, owns the multi-stakeholder negotiation, and carries a new bookings quota. The cycle time varies by segment: 14 to 45 days for SMB, 45 to 120 days for mid-market, and 4 to 12 months for enterprise.</p>

<p>AE comp is structured with a 50/50 or 60/40 base-to-variable split, with accelerators above plan. Bridge Group and RepVue data place mid-market AE OTE between 200K and 320K US dollars at venture-backed B2B SaaS companies, with enterprise AE OTE running 280K to 450K. The <a href="/sellers/">sellers directory</a> and <a href="https://thesellerreport.com">The Seller Report</a> track the benchmarks.</p>

<h2>What account managers own</h2>

<p>Account managers own the existing book of business. The role runs renewal cycles, identifies expansion opportunities, executes upsell and cross-sell motions, and manages the multi-stakeholder relationship across long-term accounts. AMs typically cover fewer accounts than AEs cover in pipeline at any given time, but the relationship depth is greater.</p>

<p>AM comp is structured similarly to AE comp at most B2B SaaS companies, with a 50/50 or 60/40 split between base and variable. The variable component ties to a mix of expansion bookings, renewal premium, and net retention. Senior AM OTE runs 180K to 280K at most venture-backed companies, slightly below AE OTE because the cycle is more predictable.</p>

<h2>Where the roles overlap</h2>

<p>The overlap is the cross-sell motion at expanding accounts. An AM who closes a new buying center inside an existing account is doing AE work, and an AE who closes a multi-year deal with built-in expansion is doing AM work. The cleanest companies define a clear rule for which role handles which case, usually based on whether the expansion crosses a department, a product line, or an executive sponsor boundary.</p>

<p>The companies that struggle with this overlap leave it ambiguous and let the two roles negotiate. The result is internal politics and lost deals. The fix is to write the rule into the account assignment model and the comp plan, with the deal desk arbitrating edge cases.</p>

<h2>Cycle differences</h2>

<p>The AE cycle starts with discovery and ends with a signed contract. The AM cycle starts with a signed contract and ends with renewal or churn. The two cycles run on different rhythms. AEs run quarterly, with a strong push at end of quarter. AMs run on the renewal calendar of each account, with churn risk peaking at the 90-day window before renewal.</p>

<p>The seller profile differs as a result. AEs tend toward urgency, deal-closing instincts, and competitive deal management. AMs tend toward patience, relationship depth, and strategic account planning. The two profiles can overlap in one person, but most senior reps in either role have a clear dominant tendency.</p>

<h2>Segment fit</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Segment</th><th>AE Focus</th><th>AM Focus</th><th>Typical Setup</th></tr></thead>
<tbody>
<tr><td>SMB</td><td>Net new logos, high volume</td><td>Often blended into CSM or AE</td><td>One role covers both</td></tr>
<tr><td>Mid-market</td><td>Net new logos, hybrid coverage</td><td>Dedicated AM at expanding accounts</td><td>Split with handoff at year one</td></tr>
<tr><td>Enterprise</td><td>Net new logos, multi-quarter cycles</td><td>Dedicated AM, often paired with CSM</td><td>Always split</td></tr>
<tr><td>Strategic</td><td>Dedicated AE, single account or pod</td><td>Multi-person AM coverage</td><td>Always split, dual coverage</td></tr>
</tbody>
</table></div>

<h2>Handoff timing</h2>

<p>The handoff from AE to AM is one of the most underdocumented operational moments in B2B SaaS. The cleanest companies define the handoff to happen 60 to 90 days after contract signature, after onboarding is complete and the CSM has a working adoption motion. The AE retains the relationship through the handoff window and then transfers to the AM with documented account history.</p>

<p>Companies that skip the handoff documentation lose deal context, lose customer relationships, and produce AMs who arrive at year two without knowing why the deal closed. The <a href="/guides/customer-success-vs-account-management/">CSM vs AM</a> guide walks through where customer success fits inside the same handoff.</p>

<h2>Comp comparison</h2>

<p>AE and AM OTE bands overlap at most companies, with AE comp running slightly higher because the new logo cycle is harder to predict. The most important comp structure difference is the accelerator design. AE accelerators kick in above plan and scale aggressively at 150 to 200 percent of quota. AM accelerators tend to be flatter because the underlying revenue base is more predictable and the upside is structurally smaller.</p>

<p>Strategic AMs at large enterprise SaaS companies sometimes earn more than AEs at the same company in absolute dollars, because the strategic account book carries massive expansion potential. The differential at most companies, however, runs in favor of the AE.</p>

<h2>Reporting structure</h2>

<p>AEs almost always report to a sales manager who reports to a VP Sales who reports to the CRO. AMs sometimes report into the same sales line and sometimes report into customer success. The choice depends on whether the company treats expansion as a sales motion or a service motion.</p>

<p>Bessemer and ICONIQ data show roughly 60 percent of B2B SaaS companies place AMs under sales and 40 percent under customer success. The split has held for the past five years and is largely driven by leadership philosophy rather than by motion economics.</p>

<h2>Career paths</h2>

<p>AEs move into senior AE, sales manager, director of sales, and VP Sales roles. Some move into solutions consulting or revenue enablement. The <a href="/guides/path-from-ae-to-sales-leader/">AE to sales leader</a> guide covers the path.</p>

<p>AMs move into senior AM, AM team lead, head of account management, and VP Account Management roles. Some move into customer success leadership or strategic accounts. The path is less standardized than the AE path because the function is younger as a named title at most companies.</p>

<h2>Common mistakes</h2>

<p>Four patterns recur. The first is treating AM as a junior AE role, with junior comp, junior accounts, and no real career path. The setup loses senior AM talent and produces an AM bench that cannot run expansion at scale. The second is loading AMs with retention work that belongs to CSMs, which produces AMs who do service work without the comp structure to match.</p>

<p>The third is asking AEs to also farm their accounts post-sale, which produces AEs who under-invest in net new pipeline because the existing book pays better. The fourth is splitting AE and AM without clear handoff documentation, which produces lost context and customer frustration. The fix to all four is the same: write the scope, the comp plan, and the handoff model before scaling either role.</p>
""",
[
    ("What is the difference between an AE and an AM?",
     "AEs close new logos and carry a net new bookings quota. AMs grow existing accounts and carry an expansion and renewal quota. The cycles, the seller profiles, and the comp structures all differ. AEs run quarterly with strong end-of-quarter pushes. AMs run on each account's renewal calendar."),
    ("Should an AE also manage their own renewals?",
     "Not in most B2B SaaS companies past SMB. AEs who farm their own accounts post-sale tend to under-invest in net new pipeline because the existing book pays better. The cleaner setup is to hand off to an AM 60 to 90 days after contract signature, once onboarding is complete."),
    ("Do AMs earn less than AEs?",
     "On average, yes. AE OTE runs slightly higher because the new logo cycle is harder to predict and the accelerators are steeper. Strategic AMs at large enterprise SaaS companies sometimes earn more than AEs in absolute dollars because the expansion potential of a strategic account book is massive."),
    ("Where should account management report?",
     "Roughly 60 percent of B2B SaaS companies place AMs under sales and 40 percent under customer success. Reporting into sales aligns with companies that treat expansion as a sales motion. Reporting into customer success aligns with companies that treat expansion as a service motion. Either pattern works with the right comp plan."),
    ("What is the most common mistake in this split?",
     "Treating AM as a junior AE role with junior accounts and no career path. The setup loses senior AM talent and produces an AM bench that cannot run expansion at scale. Companies that take expansion seriously hire AMs with comp, scope, and career paths that match the strategic value of the existing book."),
],
[
    ("B2B sellers directory", "/sellers/"),
    ("Customer success directory", "/customer-success/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("Sales enablement directory", "/sales-enablement/"),
    ("The Seller Report (comp data)", "https://thesellerreport.com"),
    ("The CS Pulse (CS comp)", "https://thecspulse.com"),
]
)


# =============================================================================
# 9) vp-sales-vs-cro
# =============================================================================
GUIDES_CONTENT["vp-sales-vs-cro"] = (
"""
<p>The shift from VP Sales to CRO is one of the most consequential title changes a B2B SaaS company makes. The CRO title implies a broader scope, a different operating cadence, and a different relationship with the CEO and the board. The shift is often made at the wrong time, for the wrong reasons, and with the wrong candidate.</p>

<p>The shortest distinction is that a VP Sales runs the sales team. A CRO runs the revenue function across sales, customer success, revenue operations, and often marketing. The first is a functional leader. The second is a cross-functional executive.</p>

<h2>What a VP Sales owns</h2>

<p>A VP Sales owns the sales team. The role manages sales managers, owns the new bookings number, runs the forecast call, hires and ramps AEs, and partners with marketing on pipeline. The function is paced by the quarterly sales cycle and lives inside a defined operating cadence: weekly pipeline reviews, monthly forecast, quarterly business reviews.</p>

<p>The role reports to the CEO at most companies under 30M ARR. The compensation is structured with a 50/50 or 60/40 base-to-variable split. RepVue and Pavilion data place senior VP Sales OTE between 350K and 600K at venture-backed B2B SaaS companies, with significant variance by segment and stage.</p>

<h2>What a CRO owns</h2>

<p>A CRO owns the revenue function. The scope covers sales, customer success, revenue operations, and at many companies marketing. The role reports to the CEO and partners with the CFO on capacity planning, with the board on revenue strategy, and with the product team on go-to-market for new releases.</p>

<p>The function is paced by the annual operating plan, not by the quarterly cycle. CRO compensation is structured similarly to VP Sales but with a lower variable percentage because the scope cannot be tied to a single quarter's bookings. RepVue and The CRO Report place senior CRO OTE between 500K and 900K at venture-backed B2B SaaS companies, with equity often dominating total comp at well-funded scale-ups. The <a href="https://thecroreport.com">CRO Report</a> tracks the benchmark data.</p>

<h2>When the shift makes sense</h2>

<p>The shift from VP Sales to CRO makes sense at most B2B SaaS companies somewhere between 20M and 50M ARR. The trigger is when the scope of the role naturally expands to cover customer success, RevOps, and cross-functional planning. Below 20M, the scope rarely justifies the title. Above 50M, the function almost always needs to be cross-functional, regardless of what title it carries.</p>

<p>Bessemer Cloud Index and ICONIQ Growth data both show the median move happens around 30M ARR at well-run companies. Companies that make the move earlier often do it for symbolic reasons rather than scope reasons, which produces a CRO title without the cross-functional reporting line.</p>

<h2>When the shift is premature</h2>

<p>The shift is premature when three conditions are present. The first is that the company is below 15M ARR and the sales team is small enough that the VP Sales is still running deals directly. The second is that customer success and RevOps still report to the CEO or COO rather than into the revenue function. The third is that the board is pushing for a CRO hire as a signal to investors rather than as a scope expansion.</p>

<p>Companies that make the shift prematurely produce a CRO title with the scope of a VP Sales role. The candidate they hire arrives expecting the full scope and either expands it informally or leaves within 12 to 18 months. The fix is to wait until the scope justifies the title.</p>

<h2>The internal promotion question</h2>

<p>The hardest decision is whether to promote an existing VP Sales into the CRO role or to hire externally. The promotion path works when the incumbent has cross-functional credibility, has built strong partnerships with marketing and customer success, and is ready to delegate the daily sales operation to a new VP Sales.</p>

<p>The external hire path works when the company has hit a growth wall, when the incumbent VP Sales is not the right profile for a scaled role, or when the board has identified a specific gap in operating experience. Bessemer and OpenView surveys show roughly 60 percent of CRO hires at venture-backed companies are external, with 40 percent internal promotions.</p>

<h2>Reporting line decisions</h2>

<p>The two hardest reporting line decisions at the CRO transition are marketing and customer success. Marketing reporting to the CRO works when the CEO is operationally focused on product and engineering rather than on go-to-market. Marketing reporting to the CEO works when the CEO has strong marketing instincts or when product marketing is a strategic priority for the company.</p>

<p>Customer success reporting to the CRO is the standard pattern past Series B. Reporting to the CEO or COO is more common at smaller companies and at companies with a strong product-led motion. The <a href="/revenue-leaders/">revenue leaders directory</a> and <a href="https://thecroreport.com">The CRO Report</a> track the patterns at venture-backed companies.</p>

<h2>Comp structure</h2>

<p>VP Sales comp is heavily commission-driven, with 40 to 50 percent of OTE in variable tied to the quarterly bookings number. The structure works for a functional role with quarterly accountability.</p>

<p>CRO comp tends to be more weighted toward base and equity, with 25 to 40 percent of OTE in variable. The variable component ties to annual revenue, net retention, and a small set of strategic metrics rather than to quarterly bookings alone. The shift in comp structure follows the shift in operating cadence from quarterly to annual.</p>

<h2>Equity differences</h2>

<p>The equity differential between VP Sales and CRO is real but smaller than the title would suggest at most companies. The bigger differential is in the equity package timing. CROs hired into a real cross-functional scope at growth-stage companies often negotiate equity refresh grants tied to revenue milestones, which can dwarf the base and variable components over a four-year vesting period.</p>

<p>The Pavilion executive compensation surveys and the ICONIQ Growth scale-up surveys both show the CRO equity package at companies past 50M ARR running 0.5 to 2 percent of fully diluted equity, with the band depending heavily on whether the hire is the first CRO or a replacement.</p>

<h2>Common mistakes</h2>

<p>Four patterns recur in the VP Sales to CRO transition. The first is the symbolic title change without scope expansion, which produces an internal promotion that confuses the rest of the org. The second is hiring an external CRO without a clear scope decision on marketing, which produces an immediate conflict between the new CRO and the existing CMO.</p>

<p>The third is hiring a CRO with deep enterprise sales experience for a company that runs a mid-market or SMB motion, which produces a strategic mismatch and a slow ramp. The fourth is firing the existing VP Sales when the CRO arrives, which loses operating context and produces a sales execution gap during the most fragile period of the transition.</p>

<p>The fix to all four is to write the scope, the reporting line, and the success criteria before posting the role. The CEO and the board should align on the answer before any hiring conversation. The <a href="/guides/path-to-cro/">path to CRO</a> guide covers the candidate side of the same transition.</p>
""",
[
    ("When should a SaaS company make the VP Sales to CRO shift?",
     "Most B2B SaaS companies make the shift between 20M and 50M ARR, with the median at well-run companies around 30M. The trigger is when the scope naturally expands to cover customer success, RevOps, and cross-functional planning. Below 20M, the scope rarely justifies the title."),
    ("Should marketing report to the CRO?",
     "Both patterns are common at scale, splitting roughly evenly across public B2B SaaS companies. Marketing reporting to the CRO works when the CEO is operationally focused on product and engineering. Marketing reporting to the CEO works when the CEO has strong marketing instincts or when product marketing is a strategic priority."),
    ("Is internal promotion or external hire more common for the first CRO?",
     "External hires are more common, running roughly 60 percent of first CRO appointments at venture-backed companies. Internal promotion works when the incumbent VP Sales has cross-functional credibility and is ready to delegate the daily sales operation to a new VP Sales."),
    ("How does CRO comp differ from VP Sales comp?",
     "CRO comp is more weighted toward base and equity, with 25 to 40 percent of OTE in variable tied to annual revenue and strategic metrics. VP Sales comp runs 40 to 50 percent in variable tied to quarterly bookings. The shift in structure follows the shift in operating cadence from quarterly to annual."),
    ("What is the most common CRO hiring mistake?",
     "Hiring a CRO with enterprise sales experience for a company that runs a mid-market or SMB motion. The strategic mismatch produces a slow ramp and often a mutual exit within 12 to 18 months. The fix is to align the candidate profile to the actual motion before the search starts."),
],
[
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("RevOps directory", "/revops/"),
    ("Customer success directory", "/customer-success/"),
    ("B2B sellers directory", "/sellers/"),
    ("The CRO Report (CRO comp data)", "https://thecroreport.com"),
    ("The RevOps Report (RevOps benchmarks)", "https://therevopsreport.com"),
]
)


# =============================================================================
# 10) solutions-engineer-vs-sales-engineer
# =============================================================================
GUIDES_CONTENT["solutions-engineer-vs-sales-engineer"] = (
"""
<p>Solutions engineer and sales engineer are two of the most interchangeably used titles in B2B SaaS. Some companies use one or the other exclusively. Others use both for different tiers or for different segments. A handful of companies use the titles for distinct functions.</p>

<p>The honest answer is that the labels are almost interchangeable at most companies. The work is technical pre-sales: scoping, demo, proof of concept, integration architecture, and the technical conversation that supports the AE through the sales cycle. This guide walks through where the titles diverge, where they overlap, and how to think about hiring.</p>

<h2>What the titles share</h2>

<p>Both solutions engineers and sales engineers run the technical conversation inside a sales cycle. The work includes discovery on the customer's technical environment, demo customization, proof of concept design and execution, integration architecture, security and compliance question handling, and the technical relationship with the buyer's engineering or operations team.</p>

<p>Both roles report into a manager of pre-sales who reports to the VP Sales or, at larger companies, to a VP of Pre-Sales who reports to the CRO. The function lives inside the revenue org at most B2B SaaS companies. The <a href="/presales/">pre-sales directory</a> and <a href="https://presalespulse.com">PreSales Pulse</a> track the practitioner communities and resources.</p>

<h2>Where the titles diverge</h2>

<p>The clearest divergence happens at companies that use both titles. In those cases, the typical split is:</p>

<ul>
<li>Sales engineer covers the bulk of pre-sales work for mid-market and SMB segments, with a demo-and-POC focus.</li>
<li>Solutions engineer covers enterprise pre-sales with a focus on architecture, integration design, and multi-system deployment planning. The role is more consultative.</li>
</ul>

<p>The split is not industry standard. Some companies reverse the labels. Some companies use solutions architect as the senior title above sales engineer. The <a href="/guides/solutions-architect-vs-sales-engineer/">solutions architect vs sales engineer</a> question is its own scope discussion.</p>

<h2>Title use by company</h2>

<p>Pavilion and Bridge Group SE surveys show that solutions engineer is the more common title at enterprise SaaS companies and at companies founded after 2018. Sales engineer is the older title and remains more common at hardware-adjacent companies, infrastructure companies, and B2B SaaS companies founded before 2015.</p>

<p>The choice of title at the individual company is usually driven by founder preference or by a hiring leader's prior experience. The work is similar enough that the title difference does not move the candidate pool much. The <a href="https://presalespulse.com">PreSales Pulse</a> tracks the title distribution by company segment.</p>

<h2>Comp benchmarks</h2>

<p>Bridge Group SE benchmarks place senior pre-sales OTE between 220K and 340K US dollars at venture-backed B2B SaaS companies, with mid-market roles at the lower end and enterprise roles at the upper end. The variable component is typically 25 to 35 percent of OTE, tied to the revenue closed on deals the SE supported.</p>

<p>The title difference does not produce a material comp difference at most companies. The bigger drivers of comp variance are segment, ACV, and seniority. Senior enterprise SEs supporting multi-million ACV deals out-earn mid-market SEs at the same company by 30 to 60 percent.</p>

<h2>Reporting structure and ratios</h2>

<p>SE to AE ratios depend on segment and product complexity. Bridge Group benchmarks place mid-market SE to AE ratios in a 1:3 to 1:5 band, with enterprise ratios at 1:2 to 1:3 and strategic ratios at 1:1 or even 2:1 for the largest deals. The <a href="/guides/se-to-ae-ratio-benchmarks/">SE to AE ratio</a> guide walks through the math.</p>

<p>The function reports to a manager of pre-sales, who reports to the VP Sales or to a VP of Pre-Sales at companies with a dedicated pre-sales leadership layer. The VP Pre-Sales title is common at enterprise SaaS companies past 50M ARR and rare at SMB-focused companies.</p>

<h2>Specialization at scale</h2>

<p>At companies past 20M ARR, the pre-sales function typically specializes. Common specialization patterns include:</p>

<ul>
<li>Industry specialization, with dedicated SEs for financial services, healthcare, or manufacturing.</li>
<li>Product specialization, with SEs assigned to specific product lines or use cases.</li>
<li>Segment specialization, with separate benches for SMB, mid-market, enterprise, and strategic.</li>
<li>Architecture specialization, with a dedicated solutions architect team handling complex deployment design.</li>
</ul>

<p>The specialization pattern depends on the company's product portfolio and customer mix. Companies with broad portfolios specialize by product. Companies with deep vertical exposure specialize by industry. Most companies past 50M ARR specialize on at least two axes.</p>

<h2>Career path</h2>

<p>Pre-sales career paths run in three directions. The first is into pre-sales leadership: manager, director, and VP Pre-Sales. The second is into adjacent technical roles: solutions architecture, customer success engineering, or technical account management. The third is laterally into product or engineering, particularly into developer relations or product management roles at API-first companies.</p>

<p>The <a href="https://presalespulse.com">PreSales Pulse</a> career section tracks the moves practitioners make. The most common next role from senior SE is either pre-sales manager or solutions architect, with a smaller subset moving into product management.</p>

<h2>Common mistakes</h2>

<p>Three patterns recur in pre-sales hiring. The first is treating the SE as a demo-builder rather than a technical seller, which underuses senior talent and produces SEs who never develop the consultative skills that close enterprise deals. The second is under-staffing pre-sales relative to the AE bench, which produces AEs who run technical conversations they are not equipped for and lose competitive deals as a result.</p>

<p>The third is treating SE and AE as adversaries rather than partners, which produces an organizational dynamic where the AE owns the deal and the SE owns nothing. The cleanest companies pair SE and AE with shared success criteria, shared comp on the deals they jointly closed, and a shared QBR cadence. The fix is to write the partnership model into the operating cadence rather than leaving it to individual personalities.</p>

<h2>The AI impact on pre-sales</h2>

<p>AI tooling has changed the pre-sales day-to-day in two ways. The first is on the demo side, where AI-assisted demo generation and automated environment provisioning have reduced the time SEs spend building bespoke demo environments. The second is on the technical research side, where AI-assisted reading of customer documentation and configuration files has compressed discovery work.</p>

<p>The function as a whole has not been replaced or displaced by AI. The relationship-driven, multi-stakeholder, architecture-heavy work that defines senior pre-sales remains human work. The <a href="/guides/ai-impact-b2b-gtm-stack-2026/">AI impact on the B2B GTM stack</a> guide covers the broader trends.</p>
""",
[
    ("Are solutions engineer and sales engineer the same title?",
     "At most B2B SaaS companies, yes. The work is technical pre-sales: scoping, demo, POC, architecture, and technical buyer relationship. Where the titles diverge inside the same company, sales engineer often covers mid-market and SMB while solutions engineer covers enterprise with a more consultative scope."),
    ("Which title is more common at enterprise companies?",
     "Solutions engineer is the more common title at enterprise SaaS companies and at companies founded after 2018. Sales engineer remains more common at older B2B SaaS companies, infrastructure companies, and hardware-adjacent companies. Both titles are widely used."),
    ("Do the two titles pay differently?",
     "Not materially at the same company. Comp variance is driven by segment, ACV, and seniority. Senior enterprise SEs supporting multi-million ACV deals out-earn mid-market SEs at the same company by 30 to 60 percent, regardless of which title they carry."),
    ("What is a normal SE to AE ratio?",
     "Bridge Group benchmarks place mid-market ratios in a 1:3 to 1:5 band, enterprise ratios at 1:2 to 1:3, and strategic ratios at 1:1 or higher. The ratio depends on segment, product complexity, and ACV more than on the SE title in use."),
    ("Where does pre-sales report?",
     "Inside the revenue org, to a manager of pre-sales who reports to the VP Sales. At enterprise SaaS companies past 50M ARR, a dedicated VP Pre-Sales role often exists and reports to the CRO. Reporting outside the revenue org is rare and usually a transitional setup."),
],
[
    ("Pre-sales and SE directory", "/presales/"),
    ("B2B sellers directory", "/sellers/"),
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("Sales enablement directory", "/sales-enablement/"),
    ("PreSales Pulse (SE benchmarks)", "https://presalespulse.com"),
    ("The Seller Report (sales comp)", "https://thesellerreport.com"),
]
)


# =============================================================================
# 11) chief-revenue-officer-vs-chief-sales-officer
# =============================================================================
GUIDES_CONTENT["chief-revenue-officer-vs-chief-sales-officer"] = (
"""
<p>Chief revenue officer and chief sales officer are two C-level titles that sometimes describe the same role and sometimes describe different scopes. The choice of one title over the other reveals how the CEO and the board think about the revenue function and what they expect from the executive.</p>

<p>The shortest distinction is that a CRO owns the entire revenue function, while a CSO owns only sales. The CRO title appeared at venture-backed SaaS companies in the late 2010s and has become the standard at scaling B2B SaaS companies. The CSO title persists at some companies and signals a deliberate choice to keep sales separate from marketing and customer success at the executive level.</p>

<h2>What a CRO owns</h2>

<p>A CRO owns the revenue function across sales, customer success, revenue operations, and sometimes marketing. The role reports to the CEO and partners with the CFO on capacity planning, with the board on revenue strategy, and with the product team on go-to-market for new releases.</p>

<p>The CRO operating cadence is annual rather than quarterly. The function owns the annual operating plan, the segmentation strategy, the comp plan design, the territory model, and the cross-functional reporting that anchors board reviews. Pavilion executive surveys put CRO OTE at venture-backed B2B SaaS companies between 500K and 900K US dollars, with equity dominating total comp at well-funded scale-ups. The <a href="https://thecroreport.com">CRO Report</a> tracks the benchmarks.</p>

<h2>What a CSO owns</h2>

<p>A CSO owns sales. The scope covers the AE bench, sales management, sales development, and pre-sales. Customer success and marketing report separately, usually to a chief customer officer and a CMO respectively. Revenue operations sometimes report to the CSO and sometimes to the COO or CFO.</p>

<p>The CSO operating cadence is quarterly, paced by the bookings cycle. The function is functionally narrower than CRO but operationally deeper inside sales execution. CSO OTE runs in a similar band to VP Sales OTE at most companies, with the title difference signaling scope rather than scale. The <a href="/guides/vp-sales-vs-cro/">VP Sales vs CRO</a> guide walks through the related transition.</p>

<h2>Why a company picks one over the other</h2>

<p>The choice usually reflects three things. The first is whether the company wants cross-functional alignment under a single revenue executive or wants to keep sales, marketing, and customer success as distinct executive functions. The second is the CEO's operating background. The third is the maturity of the marketing and customer success functions.</p>

<p>Companies with strong, independent marketing and customer success leaders often pick CSO because the cross-functional integration happens at the CEO level rather than under a CRO. Companies that want a single revenue executive to own the full funnel pick CRO. Both patterns work. The choice is structural rather than universally correct.</p>

<h2>Reporting structure differences</h2>

<div class="guide-table-wrap"><table class="guide-table">
<thead><tr><th>Function</th><th>Under CRO</th><th>Under CSO</th></tr></thead>
<tbody>
<tr><td>Sales (AEs, SDRs, managers)</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Pre-sales (SEs)</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Customer success</td><td>Usually</td><td>Reports to CCO or CEO</td></tr>
<tr><td>Marketing</td><td>Sometimes</td><td>Reports to CMO</td></tr>
<tr><td>Revenue operations</td><td>Yes</td><td>Sometimes to COO or CFO</td></tr>
<tr><td>Partner and channel</td><td>Yes</td><td>Sometimes split</td></tr>
</tbody>
</table></div>

<h2>Comp comparison</h2>

<p>CRO comp at venture-backed B2B SaaS companies runs slightly higher than CSO comp at the same company stage, mostly because the scope is broader. The differential at the executive level is real but smaller than the title would suggest. Pavilion and ICONIQ data place the median CRO OTE roughly 15 to 25 percent above the median CSO OTE at growth-stage companies.</p>

<p>The equity differential is larger and tied to the scope of the operating plan. CROs with full responsibility for the revenue function typically negotiate equity grants tied to revenue milestones, which can dwarf the base and variable components over a four-year vesting period. CSOs negotiate equity tied more narrowly to sales execution.</p>

<h2>Industry patterns</h2>

<p>The CRO title is more common at SaaS, fintech, and software-adjacent B2B companies. The CSO title persists at hardware companies, traditional enterprise software, and companies with a strong channel motion where sales and channel partnerships sit together. Some financial services and professional services companies also retain the CSO title.</p>

<p>The Bessemer Cloud Index of public SaaS companies shows a clear preference for CRO at companies founded after 2015 and a more mixed picture at older companies. The trend is toward CRO over the past five years, with the share of public B2B SaaS companies using the CRO title growing year over year.</p>

<h2>The role of the CMO</h2>

<p>The most operationally important difference between a CRO and a CSO is the relationship with marketing. Under a CRO, marketing either reports to the CRO or partners closely with the CRO on the revenue plan. Under a CSO, marketing operates as a distinct executive function reporting to the CEO.</p>

<p>Both models work. The CRO model produces tighter funnel alignment and faster cross-functional decision-making. The CSO model produces stronger marketing independence and often a more strategic marketing voice at the executive level. The choice usually depends on whether the CEO trusts the CMO to operate independently or wants the CRO to own the cross-functional alignment.</p>

<h2>The hire decision</h2>

<p>Companies hiring for either title should write the scope decision before posting the role. The most common mistake is posting a CRO role with a CSO scope, which attracts candidates expecting cross-functional ownership and produces a mismatch within the first year. The reverse mistake, posting a CSO role with a CRO scope, attracts candidates with narrow sales experience and produces a strategic gap at the executive level.</p>

<p>The fix is to align the CEO and the board on the scope decision before any candidate conversation. The scope decision drives the candidate profile, the comp band, the equity grant, and the success criteria. Without that alignment, the hire is set up to fail.</p>

<h2>Title transitions over time</h2>

<p>Some companies transition from CSO to CRO as the scope expands. The transition is usually triggered when customer success, RevOps, or marketing scope migrates under the existing CSO. The title change formalizes a scope expansion that has already happened.</p>

<p>The reverse transition, from CRO to CSO, is rare and usually signals a deliberate restructuring of the executive function. The most common case is a company where a new CEO wants to separate sales, marketing, and customer success at the executive level, which can produce a CRO exit and a new CSO hire as part of the restructuring.</p>

<h2>Common mistakes</h2>

<p>Three patterns recur. The first is treating the CRO title as a recruiting tool rather than a scope decision, which produces a candidate mismatch within the first year. The second is hiring a CRO and then keeping the CMO and the head of customer success as direct CEO reports, which removes the cross-functional scope the title implied.</p>

<p>The third is hiring a CSO and expecting them to run cross-functional alignment without the scope to do so, which produces an executive who lacks the authority to make the operational changes the role requires. The fix to all three is to align the title with the scope before the hire starts. The <a href="https://thecroreport.com">CRO Report</a> tracks how successful companies handle this alignment.</p>
""",
[
    ("Is a CRO the same as a CSO?",
     "No. A CRO owns the entire revenue function across sales, customer success, revenue operations, and often marketing. A CSO owns only sales, with the other functions reporting separately to the CEO or to other executives. The choice of title signals how the company structures its revenue org at the executive level."),
    ("Which title is more common in B2B SaaS today?",
     "CRO is more common at companies founded after 2015 and is the standard at venture-backed scale-ups. CSO persists at hardware companies, traditional enterprise software, and some financial services companies. The trend over the past five years has been toward CRO."),
    ("Does a CRO earn more than a CSO?",
     "On average, yes. The differential is 15 to 25 percent in OTE at the median, with a larger gap in equity at growth-stage companies. The pay reflects the broader scope of the CRO role, not the title itself. A CSO with effectively CRO scope earns CRO comp at most well-run companies."),
    ("Why would a company pick CSO over CRO?",
     "Companies with strong, independent marketing and customer success leaders sometimes prefer CSO because the cross-functional integration happens at the CEO level. The pattern preserves executive independence for marketing and customer success and produces a more focused sales executive."),
    ("What is the most common mistake in this title decision?",
     "Posting a CRO role with a CSO scope. The mismatch attracts candidates expecting cross-functional ownership and produces a poor fit within the first year. The fix is to align CEO and board on the scope decision before any candidate conversation, then post the role with the title that matches the actual scope."),
],
[
    ("Revenue leaders directory", "/revenue-leaders/"),
    ("B2B sellers directory", "/sellers/"),
    ("Customer success directory", "/customer-success/"),
    ("RevOps directory", "/revops/"),
    ("The CRO Report (CRO comp data)", "https://thecroreport.com"),
    ("The Seller Report (sales comp)", "https://thesellerreport.com"),
]
)
