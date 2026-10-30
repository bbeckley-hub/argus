<div align="center">

# 👁️ ARGUS

### *Antimicrobial Resistance Genomic Unified Surveillance*

**The hundred-eyed giant of AMR surveillance — one species, one eye, at a time.**

[![Live Site](https://img.shields.io/badge/🌐_Live_Site-argus--db.org-0a1628?style=for-the-badge)](https://argus-db.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Pathogens](https://img.shields.io/badge/Pathogens-7%20ESKAPE-red?style=for-the-badge)](https://argus-db.org/)
[![Live Builds](https://img.shields.io/badge/Live_Builds-1-success?style=for-the-badge)](https://saurus-db.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](https://argus-db.org/)

[**🏛️ Home**](https://argus-db.org/) ·
[**🦖 SAURUS**](https://saurus-db.org/) ·
[**💻 SAURUS-CLI**](https://pypi.org/project/saurus-cli/) ·
[**🚧 Roadmap**](#-roadmap) ·
[**📚 Citation**](#-citation)

</div>

---

## 🧭 The Name

In Greek myth, **Argus Panoptes** — "the all-seeing" — was a giant with a hundred eyes. Even when he slept, half his eyes stayed open, watching without pause.

That is the metaphor we work from. **Antimicrobial resistance does not sleep.** It moves between hospitals, farms, continents, and species. The pathogens driving the AMR crisis — the **ESKAPE** group — are collectively responsible for the majority of healthcare-associated resistant infections worldwide. Yet surveillance of each has evolved in its own silo, with its own tools, its own data formats, and its own access barriers.

**ARGUS is our answer to the metaphor.** A unified, species-specific surveillance family where each pathogen gets its own open resource, its own community, and its own citable artifact — but they all share the same architectural DNA, so an advance in one is an advance in all.

---

## 🚨 The Problem — Fragmented Surveillance, Fragmented Access

We now have *millions* of public bacterial genomes. In *Staphylococcus aureus* alone, over 134,000 complete or draft assemblies are deposited in NCBI. The raw data exists. The annotations exist. The epidemiological metadata exists.

And yet the most routine question in genomic epidemiology still requires a script.

Ask for *"all MRSA ST5 bloodstream isolates from the United States between 2015 and 2023 carrying SCCmec II and capsule type 5"* and watch what happens:

- You download typing tables from one source.
- You download gene presence/absence from another.
- You download NCBI BioSample metadata from a third.
- You write custom Python to cross-reference accessions.
- You reconcile column names, accession formats, and version suffixes.
- You iterate until the join doesn't silently drop records.
- **Then** you get your accession list.

That is not a data problem. That is an **interface problem** — and it is why the majority of researchers, clinicians, and public health teams who *should* be doing genomic surveillance are locked out of it. The data is free; the workflow is not.

> **Domain-scale archives** (AllTheBacteria) solve the reprocessing problem — but they don't do species-specific typing or clinical metadata.
>
> **Bulk annotation databases** (Shelenkov et al.) solve the annotation problem — but they distribute static tables, not queryable interfaces.
>
> **Analysis pipelines** (Bactopia, StaphScope, Nullarbor) solve the "what is this genome?" problem — but not the "which genomes match these criteria?" problem.
>
> **ARGUS** solves the retrieval problem — the one every downstream tool depends on.

---

## 👁️ What ARGUS Is

**ARGUS** is a **family of independent, open genomic surveillance platforms** — one per ESKAPE pathogen. Each resource is:

- **Accession-first** — every page ends in a clean accession list ready for `datasets download genome accession`
- **Species-specific** — not a generic bacterial browser, but a purpose-built platform for one pathogen's typing, gene content, and epidemiology
- **Serverless** — static HTML/CSS/JS hosted entirely on GitHub Pages, with bundled data; no servers, no databases, no APIs, no rate limits
- **Packaged for every ecosystem** — each ARGUS resource ships as a web app, a pip package, a conda package, and a Docker image, with the full dataset bundled
- **Free and open** — no login, no API key, no cost, MIT-licensed

Every ARGUS resource shares the same architecture, so improvements in one propagate to all. When we add a new feature to SAURUS, we inherit it in ECLIPSE. When we publish a new release of the ARGUS generator scripts, every sibling benefits.

---

## 🗺️ The ARGUS Family

| Resource | Pathogen | Web | CLI | Status |
|---|---|---|---|---|
| 🦖 **SAURUS** | *Staphylococcus aureus* | [**saurus-db.org**](https://saurus-db.org/) | [**pip install saurus-cli**](https://pypi.org/project/saurus-cli/) | ✅ **Live** |
| 🌑 **ECLIPSE** | *Escherichia coli* | [bbeckley-hub.github.io/eclipse](https://bbeckley-hub.github.io/eclipse) | — | 🚧 **In progress** |
| 🌊 **ABYSS** | *Acinetobacter baumannii* | — | — | 🚧 **In progress** |
| 🏆 **KLEOS** | *Klebsiella pneumoniae* | — | — | 📋 Planned |
| 💧 **PSEUDA** | *Pseudomonas aeruginosa* | — | — | 📋 Planned |
| 👑 **EMPIRE** | *Enterococcus faecium* | — | — | 📋 Planned |
| 🌀 **ENTROPY** | *Enterobacter* spp. | — | — | 📋 Planned |

Each live resource will eventually have its own custom domain (`eclipse-db.org`, `abyss-db.org`, etc.) and its own peer-reviewed publication. Domains are being secured in priority order as the corresponding resource approaches release.

---

## 🦖 SAURUS — The Flagship Build

**SAURUS** (*Staphylococcus aureus* Unified Resource for Universal Surveillance) is the first and currently only fully live ARGUS resource. It launched as a proof of concept that the ARGUS architecture could deliver real surveillance value — and it has.

### What SAURUS delivers today

| Category | Coverage |
|---|---|
| **Unique genomes indexed** | **134,299** |
| **De novo typed genomes** | **98,138** |
| **MRSA rate across typed collection** | **59.2%** |
| **Countries represented** | **139** |
| **Unique sequence types** | **2,116** |
| **Unique spa types** | **3,932** |
| **Curated clonal complexes** | **~50** |

### Two interfaces, one dataset

| Interface | Access | Install |
|---|---|---|
| 🌐 **Web UI** | [**saurus-db.org**](https://saurus-db.org/) | None — runs in your browser |
| 💻 **SAURUS-CLI** | [**pypi.org/project/saurus-cli**](https://pypi.org/project/saurus-cli/) | `pip install saurus-cli` |

Both interfaces expose the same 11 modules, the same 134,299 genomes, the same epidemiological metadata — and both produce the same deliverable: **a clean accession list** ready to feed directly to `datasets download genome accession`.

### Try it in 30 seconds

```bash
pip install saurus-cli
saurus --lineage USA300 --country USA --source blood --count
# → 907
```

Or open [**saurus-db.org/pages/mrsa.html**](https://saurus-db.org/pages/mrsa.html), filter by `MRSA = MRSA`, `ST = 5`, `Country = USA`, `Source = blood`, and click **🧬 Accessions**.

Either way, you have your genome accessions in under a minute — filtered by **genotype, phenotype, and geography**.

**→ Full SAURUS details:** [saurus-db.org/about.html](https://saurus-db.org/about.html) · [README](https://github.com/bbeckley-hub/saurus)

---

## 🏗️ The Shared ARGUS Architecture

Every ARGUS resource — live, in progress, or planned — shares the same foundational design. This is what makes the family coherent and sustainable.

### 1. Serverless static-site generation

All pages are self-contained HTML documents with embedded CSS and JavaScript. Data is injected as JSON at build time by self-contained Python generators. The site is served from **GitHub Pages** over HTTPS.

**Why it matters:** No relational databases. No API rate limits. No server costs. No data decay. No security surface. If GitHub Pages is online, ARGUS is online.

### 2. Bundled-data packaging

Every ARGUS web resource ships with a companion CLI that **bundles the full dataset inside the installable artifact** — the pip wheel, conda package, and Docker image all contain the complete data, compressed as `.tsv.gz`. After installation, queries run locally with no network access.

**Why it matters:** Zero-configuration installs. No `saurus init`, no `ECLIPSE fetch`, no first-run downloads. The first query works in seconds. Version skew between code and data is impossible — they are the same artifact.

### 3. Accession-first export

Every page, every filter, every module ends in the same deliverable: **a clean list of genome accessions** ready for `datasets download genome accession --inputfile list.txt`. Multi-format export (TSV, CSV, JSON, accession list) is available everywhere, and multiple formats can be requested in a single CLI run.

**Why it matters:** The artifact downstream pipelines actually consume is a first-class citizen of the interface, not an afterthought. This is the single biggest design decision that distinguishes ARGUS from generic bacterial browsers.

### 4. Reproducibility as a design principle

- Web resources: static HTML that can be archived, DOI-minted, and re-served indefinitely
- CLI resources: JSON config files that capture query parameters byte-for-byte, and Docker images that pin an entire analysis environment
- Data: version-pinned release bundles, immutable and citable

**Why it matters:** Genomic surveillance is a *public health* activity. A query run today by a public health lab in Accra must be reproducible by a reviewer in Geneva six months from now. ARGUS makes this trivial instead of heroic.

---

## 🧬 The Species-Optimized Pipeline Ecosystem

The ARGUS family is built on a collection of species-optimized computational pipelines developed by our group at the University of Ghana Medical School. Each pipeline wraps the appropriate typing schemes, resistance-gene databases, and species-specific tools into a reproducible container, and each produces the per-sample summary tables that the ARGUS generator scripts consume without modification.

| Pipeline | Pathogen | Publication | Repository |
|---|---|---|---|
| **StaphScope** | *Staphylococcus aureus* | *BMC Genomics* 2026;27:261 | [github](https://github.com/bbeckley-hub/staphscope-typing-tool) |
| **EcoliTyper** | *Escherichia coli* | *BMC Bioinformatics* 2026;27(1):182 | [github](https://github.com/bbeckley-hub/ecolityper) |
| **AcinetoScope** | *Acinetobacter baumannii* | *Sci Rep* 2026 | [github](https://github.com/bbeckley-hub/acinetoscope) |

These pipelines are the analytical backbone of ARGUS. Because they output a common schema, extending ARGUS to a new pathogen is primarily an exercise in **curation and integration**, not algorithm development.

---

## 🚧 Roadmap

The ARGUS expansion proceeds in priority order, based on (1) public-health urgency of the pathogen, (2) availability of a mature species-optimized typing pipeline, and (3) existing data coverage in NCBI. The current plan:

| Phase | Resource | Pathogen | Prerequisite pipeline | ETA |
|---|---|---|---|---|
| **I** ✅ | **SAURUS** | *S. aureus* | StaphScope ✅ | **Live** |
| **II** 🚧 | **ECLIPSE** | *E. coli* | EcoliTyper ✅ | **In progress** |
| **III** | **ABYSS** | *A. baumannii* | AcinetoScope ✅ | Next |
| **IV** | **KLEOS** | *K. pneumoniae* | (Kleboscope) | 2027 |
| **V** | **PSEUDA** | *P. aeruginosa* | (PseudoScope) | 2027 |
| **VI** | **EMPIRE** | *E. faecium* | (Enteromark) | 2028 |
| **VII** | **ENTROPY** | *Enterobacter* spp. | (EnteroScope) | 2028 |

Each resource ships with its own DOI, its own CLI package, its own web domain, and its own peer-reviewed publication. The ARGUS initiative does not require a "big bang" release — it grows one pathogen at a time, each one a complete, citable contribution in its own right.

### Cross-species features (planned post-v1.0)

Once at least three ARGUS resources are live, we plan to introduce:

- **A unified ARGUS query interface** — filter by pathogen, lineage, gene content, and metadata across the entire family
- **An ARGUS-CLI umbrella** — a single `pip install argus-cli` that dispatches to the appropriate pathogen module
- **Cross-species comparative views** — e.g., *"show me all mecA-carrying genomes across all six ESKAPE pathogens in West Africa"*

These are deliberately deferred until the individual resources are mature. A unified interface built on top of two incomplete resources would be an illusion.

---

## 💰 Funding and Sustainability

**ARGUS is developed entirely without external grant funding.**

This is a grassroots initiative, developed in a resource-limited setting, to demonstrate that high-impact, world-class genomic surveillance can be achieved through resourceful engineering and open-source collaboration.

### How it is sustained

- **Infrastructure** — Custom web domains (`argus-db.org`, `saurus-db.org`) are registered for 10 years to guarantee permanent accessibility, and are generously supported by our collaborators and co-authors
- **Compute** — Large-scale genomic processing is performed on the **ZUPUTO High-Performance Computing cluster** at the University of Ghana
- **Distribution** — Packages are hosted on PyPI, Bioconda, and the GitHub Container Registry — all free infrastructure that does not depend on grant cycles
- **Code** — Every resource is MIT-licensed, forkable, and permanent. When a maintainer becomes unavailable, the resource continues to function because it has no moving parts to maintain

### Why this model matters

Traditional dynamic databases fail when grant funding ends: the servers are shut down, the databases go stale, and the community loses access. ARGUS is designed to be **immune to this failure mode**. A static site hosted on GitHub Pages will serve content as long as GitHub exists. A pip package published to PyPI will install as long as PyPI exists. There is no maintenance cost to ARGUS remaining online.

This is not just a cost optimization. It is a design choice that ensures ARGUS outlives any individual funding cycle, any institutional affiliation, and any individual maintainer.

---

## 📚 Citation

If you use any ARGUS resource in your research, please cite the corresponding resource publication, the underlying typing pipeline, and (where applicable) the source gene annotation dataset.

### ARGUS resources

> **SAURUS** — Beckley B, Olalekan A, Afeke I, Amarh V. SAURUS: an interactive web resource for typing-based genome retrieval in *Staphylococcus aureus*. *BMC Genom Data* [under review]. 2026.

> **SAURUS-CLI** — Beckley B. SAURUS-CLI: a reproducible command-line interface for typing-based genome retrieval in *Staphylococcus aureus*. *BMC Bioinformatics* [under review]. 2026.

### Typing pipelines

> **StaphScope** — Beckley B, Amarh V. StaphScope: a species-optimized computational pipeline for rapid and accessible *Staphylococcus aureus* genotyping and surveillance. *BMC Genomics*. 2026;27:261. [doi:10.1186/s12864-026-12609-x](https://doi.org/10.1186/s12864-026-12609-x)

> **EcoliTyper** — Beckley B, Amarh V. EcoliTyper: a species-optimized computational pipeline for comprehensive genotyping and surveillance of *Escherichia coli*. *BMC Bioinformatics*. 2026;27(1):182. [doi:10.1186/s12859-026-06529-6](https://doi.org/10.1186/s12859-026-06529-6)

> **AcinetoScope** — Beckley B, Amarh V, Lopes BS, et al. AcinetoScope: a computational pipeline for rapid, comprehensive *Acinetobacter baumannii* outbreak investigation and resistance gene tracking. *Sci Rep*. 2026. [doi:10.1038/s41598-026-70189-y](https://doi.org/10.1038/s41598-026-70189-y)

### Source gene annotations

> **Shelenkov et al.** — Shelenkov A, Slavokhotova A, Yunusova M, et al. Genomic typing, antimicrobial resistance gene, virulence factor and plasmid replicon database for the important pathogenic bacteria *Staphylococcus aureus*. *BMC Genom Data*. 2025;26(1):65. [doi:10.1186/s12863-025-01363-w](https://doi.org/10.1186/s12863-025-01363-w)


---

## 🤝 Contributing

The ARGUS initiative welcomes:

- 🐛 **Bug reports** — [open an issue](https://github.com/bbeckley-hub/argus/issues)
- 💡 **Feature suggestions** — [start a discussion](https://github.com/bbeckley-hub/argus/discussions)
- 🧬 **Species pipeline submissions** — if you maintain a species-optimized typing pipeline and would like to build an ARGUS resource on top of it, we would love to hear from you
- 🏛️ **Institutional partnerships** — for training, adoption, or collaborative surveillance work

Each ARGUS resource has its own contributing guide. For SAURUS, see [github.com/bbeckley-hub/saurus#-contributing](https://github.com/bbeckley-hub/saurus#-contributing).

---

## 📬 Contact

**Lead Developer:** Brown Beckley
**Affiliation:** Department of Medical Biochemistry, University of Ghana Medical School, Accra, Ghana
**Email:** [brownbeckley94@gmail.com](mailto:brownbeckley94@gmail.com)
**GitHub:** [@bbeckley-hub](https://github.com/bbeckley-hub)

---

## 📄 License

**MIT License** — free to use, modify, and redistribute. Attribution appreciated.

See [LICENSE](LICENSE) for details.

---

<div align="center">

**👁️ ARGUS** — *Antimicrobial Resistance Genomic Unified Surveillance*

*One pathogen at a time. One eye at a time.*

[**🏛️ argus-db.org**](https://argus-db.org/) ·
[**🦖 saurus-db.org**](https://saurus-db.org/) ·
[**💻 saurus-cli on PyPI**](https://pypi.org/project/saurus-cli/) ·
[**🐙 github.com/bbeckley-hub/argus**](https://github.com/bbeckley-hub/argus)

*Built with 🧬 at the University of Ghana Medical School.*

</div>
