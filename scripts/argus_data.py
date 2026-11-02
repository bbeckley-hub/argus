#!/usr/bin/env python3
"""
argus_data.py — All ARGUS data structures (platforms, quotes, citations, roadmap).
"""

PLATFORMS = [
    {"name": "SAURUS",  "emoji": "🦖", "species": "Staphylococcus aureus",
     "color": "#3b82f6", "status": "live",
     "desc": "Typing, gene retrieval, and metadata for public S. aureus genomes.",
     "genomes": "134,160",
     "url": "https://saurus-db.org/"},
    {"name": "ECLIPSE", "emoji": "🌑", "species": "Escherichia coli",
     "color": "#7c3aed", "status": "live",
     "desc": "MLST, phylogroups, serotypes, and CHTyper for public E. coli genomes.",
     "genomes": "450+",
     "url": "https://bbeckley-hub.github.io/eclipse/"},
    {"name": "ABYSS",   "emoji": "🌊", "species": "Acinetobacter baumannii",
     "color": "#0d9488", "status": "progress",
     "desc": "Pasteur MLST, IC1–IC12, KL/OCL capsules, OXA-51, and carbapenemase tracking.",
     "url": "https://bbeckley-hub.github.io/abyss/"},
    {"name": "KLEOS",   "emoji": "🏆", "species": "Klebsiella pneumoniae",
     "color": "#dc2626", "status": "planned",
     "desc": "Pasteur ST, wzi capsular typing, carbapenemases, and hypervirulence markers.",
     "url": "https://github.com/bbeckley-hub/kleos"},
    {"name": "PSEUDA",  "emoji": "💧", "species": "Pseudomonas aeruginosa",
     "color": "#06b6d4", "status": "planned",
     "desc": "MLST, O-antigen typing, intrinsic resistance, and T3SS virulence effectors.",
     "url": "https://github.com/bbeckley-hub/pseuda"},
    {"name": "EMPIRE",  "emoji": "👑", "species": "Enterococcus faecium",
     "color": "#f59e0b", "status": "planned",
     "desc": "MLST, vanA/vanB typing, and surface protein epidemiology for VRE.",
     "url": "https://github.com/bbeckley-hub/empire"},
    {"name": "ENTROPY", "emoji": "🌀", "species": "Enterobacter spp.",
     "color": "#475569", "status": "planned",
     "desc": "Species-level ST typing, AmpC variants, and carbapenemase tracking.",
     "url": "https://github.com/bbeckley-hub/entropy"},
]

SCIENCE_QUOTES = [
    {"text": "Imagination is more important than knowledge.", "author": "Albert Einstein"},
    {"text": "Nothing in life is to be feared, it is only to be understood.", "author": "Marie Curie"},
    {"text": "Somewhere, something incredible is waiting to be known.", "author": "Carl Sagan"},
    {"text": "Extraordinary claims require extraordinary evidence.", "author": "Carl Sagan"},
    {"text": "The first principle is that you must not fool yourself — and you are the easiest person to fool.", "author": "Richard Feynman"},
    {"text": "If I have seen further, it is by standing on the shoulders of giants.", "author": "Isaac Newton"},
    {"text": "Chance favors the prepared mind.", "author": "Louis Pasteur"},
    {"text": "The microbe is nothing; the terrain is everything.", "author": "Louis Pasteur"},
    {"text": "One sometimes finds what one is not looking for.", "author": "Alexander Fleming"},
    {"text": "It is not the strongest of the species that survives, but the one most responsive to change.", "author": "Charles Darwin"},
    {"text": "Argus Panoptes never slept. Neither should surveillance.", "author": "Brown Beckley"},
    {"text": "One pathogen at a time is how surveillance fails. Seven at once is how it works.", "author": "Brown Beckley"},
    {"text": "Open data saves lives. Surveillance belongs to everyone.", "author": "Brown Beckley"},
    {"text": "Where a pathogen comes from is half the story of where it goes next.", "author": "Brown Beckley"},
]

CITATIONS = [
    {"platform": "SAURUS", "emoji": "🦖", "color": "#3b82f6", "role": "Pipeline",
     "ref": "Beckley B, Amarh V. StaphScope: a species-optimized computational pipeline for rapid and accessible Staphylococcus aureus genotyping and surveillance. BMC Genomics. 2026;27:261.",
     "doi": "10.1186/s12864-026-12609-x",
     "url": "https://doi.org/10.1186/s12864-026-12609-x"},
    {"platform": "SAURUS", "emoji": "🦖", "color": "#3b82f6", "role": "Gene data",
     "ref": "Shelenkov A, Slavokhotova A, Yunusova M, et al. Genomic typing, antimicrobial resistance gene, virulence factor and plasmid replicon database for the important pathogenic bacteria Staphylococcus aureus. BMC Genom Data. 2025;26:65.",
     "doi": "10.1186/s12863-025-01363-w",
     "url": "https://doi.org/10.1186/s12863-025-01363-w"},
    {"platform": "ECLIPSE", "emoji": "🌑", "color": "#7c3aed", "role": "Pipeline",
     "ref": "Beckley B, Amarh V. EcoliTyper: a species-optimized computational pipeline for comprehensive genotyping and surveillance of Escherichia coli. BMC Bioinformatics. 2026;27(1):182.",
     "doi": "10.1186/s12859-026-06529-6",
     "url": "https://doi.org/10.1186/s12859-026-06529-6"},
    {"platform": "ABYSS", "emoji": "🌊", "color": "#0d9488", "role": "Pipeline",
     "ref": "Beckley B, Amarh V, Lopes BS, et al. AcinetoScope: a computational pipeline for rapid, comprehensive Acinetobacter baumannii outbreak investigation and resistance gene tracking. Scientific Reports. 2026.",
     "doi": "10.1038/s41598-026-70189-y",
     "url": "https://doi.org/10.1038/s41598-026-70189-y"},
    {"platform": "ABYSS", "emoji": "🌊", "color": "#0d9488", "role": "Gene data",
     "ref": "Shelenkov A, Mikhaylova Y, Akimkin V. Genomic Epidemiology Dataset for the Important Nosocomial Pathogenic Bacterium Acinetobacter baumannii. Data. 2024;9(2):22.",
     "doi": "10.3390/data9020022",
     "url": "https://doi.org/10.3390/data9020022"},
]

REPOS = [
    {"name": "ARGUS (this portal)", "url": "https://github.com/bbeckley-hub/argus"},
    {"name": "SAURUS",              "url": "https://github.com/bbeckley-hub/saurus"},
    {"name": "ECLIPSE",             "url": "https://github.com/bbeckley-hub/eclipse"},
    {"name": "ABYSS",               "url": "https://github.com/bbeckley-hub/abyss"},
    {"name": "KLEOS",               "url": "https://github.com/bbeckley-hub/kleos"},
    {"name": "PSUEDA",              "url": "https://github.com/bbeckley-hub/pseuda"},
    {"name": "EMPIRE",              "url": "https://github.com/bbeckley-hub/empire"},
    {"name": "ENTROPY",             "url": "https://github.com/bbeckley-hub/entropy"},
]

ROADMAP = [
    {"name": "SAURUS",  "emoji": "🦖", "species": "S. aureus",         "color": "#3b82f6", "current": "v0.8 (Live)", "next": "v1.0.0", "milestone": "134,160 typed · Zenodo DOI · Database manuscript"},
    {"name": "ECLIPSE", "emoji": "🌑", "species": "E. coli",           "color": "#7c3aed", "current": "v0.1 (Dev)", "next": "v0.3",   "milestone": "Full RefSeq typing · AMR/VFDB/Plasmid"},
    {"name": "ABYSS",   "emoji": "🌊", "species": "A. baumannii",      "color": "#0d9488", "current": "v0.1 (Dev)",  "next": "v0.2",   "milestone": "Statistics · Lineages · Downloads"},
    {"name": "KLEOS",   "emoji": "🏆", "species": "K. pneumoniae",     "color": "#dc2626", "current": "Planned",     "next": "v0.1",   "milestone": "Pasteur ST + wzi capsular + carbapenemases"},
    {"name": "PSEUDA",  "emoji": "💧", "species": "P. aeruginosa",     "color": "#06b6d4", "current": "Planned",     "next": "v0.1",   "milestone": "MLST + O-antigen + T3SS effectors"},
    {"name": "EMPIRE",  "emoji": "👑", "species": "E. faecium",        "color": "#f59e0b", "current": "Planned",     "next": "v0.1",   "milestone": "MLST + vanA/vanB + surface proteins"},
    {"name": "ENTROPY", "emoji": "🌀", "species": "Enterobacter spp.", "color": "#475569", "current": "Planned",     "next": "v0.1",   "milestone": "MLST + AmpC + carbapenemases"},
]
