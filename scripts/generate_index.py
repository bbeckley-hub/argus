#!/usr/bin/env python3
"""generate_index.py — ARGUS landing page. Writes docs/index.html."""

import argparse, json
from pathlib import Path
from argus_common import wrap_html
from argus_data import PLATFORMS, SCIENCE_QUOTES


def build_platform_cards():
    cards = []
    for p in PLATFORMS:
        status = p["status"]
        status_label = {"live": "Live", "progress": "Preview", "planned": "Planned"}[status]
        is_clickable = status in ("live", "progress")
        card_cls = "platform-card live reveal" if is_clickable else "platform-card planned"
        href = p["url"] if is_clickable else "#"
        target = 'target="_blank" rel="noopener"' if is_clickable else ''
        tag = "a" if is_clickable else "div"
        extra_attr = f'href="{href}" {target}' if is_clickable else 'role="link" aria-disabled="true"'
        genomes_html = ""
        if p.get("genomes"):
            genomes_html = f'<span style="font-size:0.72em;color:var(--fg-3);font-weight:600;">{p["genomes"]} genomes</span>'
        cards.append(f'''
        <{tag} {extra_attr} class="{card_cls}" style="--pc: {p['color']};">
            <div class="pc-head">
                <span class="pc-emoji">{p['emoji']}</span>
                <div>
                    <div class="pc-name">{p['name']}</div>
                    <div class="pc-species">{p['species']}</div>
                </div>
            </div>
            <div class="pc-desc">{p['desc']}</div>
            <div class="pc-footer">
                <span class="pc-status {status}">{status_label}</span>
                {genomes_html}
                <span class="pc-arrow">{'→' if is_clickable else '·'}</span>
            </div>
        </{tag}>''')
    return "\n".join(cards)


BODY = f'''
<header class="hero">
    <div class="hero-inner">
        <span class="hero-badge">Open Genomic Surveillance</span>
        <h1>Welcome to <span>ARGUS</span></h1>
        <p class="tagline">One family. Seven priority pathogens. One accession-first workflow.</p>
        <p style="font-size:1.1em;color:var(--fg-3);margin-bottom:24px;font-weight:500;">
            <strong style="color:var(--gold);font-size:1.3em;">134,160</strong> genomes under surveillance &middot;
            <strong style="color:var(--gold);font-size:1.3em;">2</strong> platforms live &middot;
            <strong style="color:var(--gold);font-size:1.3em;">5</strong> planned
        </p>
        <p class="desc">
            An open, serverless genomic surveillance platform for the WHO priority ESKAPE pathogens.
            No installation. No login. No API key. Just filter, verify, and export your accession list.
        </p>
        <div class="hero-ctas">
            <a class="btn btn-primary" href="#family">Explore the family →</a>
            <a class="btn btn-secondary" href="vision.html">Read our vision</a>
            <a class="btn btn-secondary" href="resources.html">Resources &amp; citation</a>
        </div>
    </div>
</header>

<section class="quote-banner" id="quote-banner">
    <div class="quote-inner">
        <div class="quote-mark">"</div>
        <p class="quote-text" id="quote-text">Loading inspiration…</p>
        <p class="quote-author" id="quote-author"></p>
    </div>
    <div class="quote-dots" id="quote-dots"></div>
</section>

<section class="section reveal" id="problem">
    <div class="section-inner">
        <span class="section-eyebrow">The bottleneck</span>
        <h2>Finding the right genomes should not be this hard.</h2>
        <p class="section-sub">
            The exponential growth of publicly available pathogen genomes has created an
            unprecedented opportunity for genomic epidemiology. Yet a persistent bottleneck
            remains: retrieving a defined subset of genomes that match specific genotypic
            or epidemiological criteria.
        </p>

        <div class="compare-grid">
            <div class="compare-col old">
                <h3><span class="pill">Old way</span> Hours of scripting before science</h3>
                <ul>
                    <li>Download static compressed TSVs from five different sources</li>
                    <li>Manually join tables by accession — mismatch errors guaranteed</li>
                    <li>Write Python scripts to filter genotype and metadata separately</li>
                    <li>Debug the pipeline when a column name changes</li>
                    <li>Query again from scratch for each new criterion</li>
                    <li>Duplicate data across tools and pipelines</li>
                </ul>
            </div>
            <div class="compare-col new">
                <h3><span class="pill">ARGUS way</span> Minutes from query to accession list</h3>
                <ul>
                    <li>Open one interactive browser page — no install, no login</li>
                    <li>Stack filters across genotype, geography, and metadata in one query</li>
                    <li>Watch matching counts update live as you narrow the search</li>
                    <li>Export a clean plain-text accession list with one click</li>
                    <li>Feed directly into NCBI Datasets for genome retrieval</li>
                    <li>Every annotation, every metadata field — one architecture</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="section alt reveal">
    <div class="section-inner">
        <span class="section-eyebrow">The solution</span>
        <h2>Four steps from query to genome.</h2>
        <p class="section-sub">
            Every ARGUS platform is built around the same workflow — the actual downstream
            deliverable, a clean accession list, sits at the centre of the interface.
        </p>
        <div class="steps">
            <div class="step"><span class="step-num">1</span><h4>Filter</h4><p>Stack filters across genotype, geography, and metadata. Sequence type, resistance gene, country, source, year — all in one place.</p></div>
            <div class="step"><span class="step-num">2</span><h4>Verify</h4><p>See live counts, distribution charts, and lineage context before you download anything. Confirm the query returns what you need.</p></div>
            <div class="step"><span class="step-num">3</span><h4>Export</h4><p>One click downloads a plain-text accession list. No scripting. No API keys. No CSV wrangling. Just one ID per line.</p></div>
            <div class="step"><span class="step-num">4</span><h4>Download</h4><p>Feed the list to NCBI Datasets and retrieve the underlying assemblies. Every platform is designed around this final step.</p></div>
        </div>
    </div>
</section>

<section class="section reveal" id="family">
    <div class="section-inner">
        <span class="section-eyebrow">The family</span>
        <h2>Seven ESKAPE pathogens. One architecture.</h2>
        <p class="section-sub">
            Each platform is a species-specific resource with its own name, its own DOI,
            its own release cycle, and its own community of users — but they all share
            the same accession-first, serverless, metadata-integrated foundation.
        </p>
        <div class="family-grid">
            {build_platform_cards()}
        </div>
    </div>
</section>

<section class="section alt reveal">
    <div class="section-inner">
        <div class="cite">
            <h3>📚 Please cite the platforms you use</h3>
            <p>
                Each platform carries its own citation block on its landing page and its own
                Zenodo DOI on release. Full citation lists for every platform are on the
                <a href="resources.html">Resources page</a>.
            </p>
        </div>
    </div>
</section>
'''

EXTRA_JS = f'<script>window.__ARGUS_QUOTES__ = {json.dumps(SCIENCE_QUOTES, ensure_ascii=False)};</script>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="docs/index.html")
    args = ap.parse_args()

    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    html = wrap_html(
        title="ARGUS — ESKAPE Genomic Surveillance",
        description="ARGUS — one family, seven ESKAPE pathogens. An open, serverless, accession-first genomic surveillance platform.",
        body_html=BODY,
        active_key="platforms",
        extra_js=EXTRA_JS,
    )
    out.write_text(html, encoding="utf-8")
    print(f"✅ Written: {out} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
