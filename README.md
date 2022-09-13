# Note on Submission<!-- omit from toc --> 

- You should submit to Canvas this week for this activity set.

---

- [Activity 3.1: Blast](#activity-31-blast)
  - [Background](#background)
  - [Description](#description)
  - [Steps](#steps)
- [Activity 3.2: RCSB Entry Exploration](#activity-32-rcsb-entry-exploration)
  - [Background](#background-1)
  - [Description](#description-1)
  - [Steps](#steps-1)
- [Activity 3.3: RNA Model System on MFOld](#activity-33-rna-model-system-on-mfold)
  - [Background](#background-2)
  - [Description](#description-2)

## Activity 3.1: Blast

### Background

Basic Local Alignment Search Tool (Blast) is used to search for similar biological sequences (protein and nucleotide).  The impact of this tool on science cannot be understated.  NCBI hosts a web server for Blast making the tool accessible to the wider research community.

### Description

In this exercise, you will find an interesting protein using the NCBI protein database.  You will then blastp the sequence of the protein against two databases Finally, you will write a mini-report for this exercise.

### Steps

1. Navigate to the NCBI protein database
   1. https://www.ncbi.nlm.nih.gov/protein
2. Query a protein of interest by topic name or gene name. E.g. "CRISPR or Foxp2"
3. Download or copy the Fasta record (this contains the sequence data as well as a header description of the record)
4. Blastp the sequence against the nr database
   1. Note: if you get less than 3 results for this database, choose another sequence and rerun
5. Blastp the sequence against the pdb database
   1. NOTE: it is **okay** if you get zero results for this database.
6. Examine results and write a mini-report with the following sections and answered questions:
   1. Method
      1. What was the query sequence? (A link to the NCBI entry or accession ID are both reasonable options)
      2. When did you run blastp?
         1. Why is this information important to track for blast in the context of the query database?
      3. What parameters did you use? (Use the "search summary" tab on the results page)
   2. Discussion
      1. How should the statistics be interpreted?
         1. Score
         2. E-value
         3. Identity, Positives, Gaps
      2. How does the nr vs pdb database query compare? How do they contrast?
   3. Conclusion
      1. Based on the graphic summary, what regions of the protein are possibly important to protein function? What regions are possibly not required for protein function?
7. Upload the mini-report to Canvas


---

## Activity 3.2: RCSB Entry Exploration

### Background

The RCSB database includes protein structures derived from both experiment and now computationally modelled ones.  This database includes both the files as well as numerous annotations and cross referencing tools.

ChimeraX is a molecular structure tool useful for visualization and other molecular analyses.  It includes plugins that connect it to other uses of molecular structures including modelling, alignment (sequence and structure), and docking.

### Description

In this exercise, you will explore the RCSB to find an experimentally determined protein structure of interest.  You will describe the protein and use the RCSB structure similarity search tool to find a structurally similar protein and perform a pairwise sequence alignment.  Finally, you will install and generate a visualization of the structure using ChimeraX.


### Steps

1. Navigate to the [RCSB](https://www.rcsb.org/)
2. Query a protein of interest (I recommend something somewhat common like "Haemoglobin" to make the downstream steps a bit easier)
3. Select an RCSB entry that is experimentally determined.
4. Record the experimental information  (Use the Experimental Data Snapshot portion of the main page):
   1. How should the values be interpreted?
   2. This glossary may be useful: https://www.rcsb.org/docs/general-help/glossary
5. In the macromolecules box, find "Find similar proteins by" "3D Structure"
6. Select a structurally similar protein entry from another organism.
7. Perform a pairwise alignment using a tool on EMBL-EBI: https://www.ebi.ac.uk/services/data-resources-and-tools
   1. Record the following:
      1. Method Section for pairwise alignment
         1. At this juncture, you should have a good idea what aspects should be recorded for reproducibility sake. (But you can always ask your instructor/peers if unsure.)
      2. Pairwise alignment result
8. Install ChimeraX
   1. https://www.cgl.ucsf.edu/chimerax/
9. Start the program and follow the quick start tutorial
   1.  Help -> Quick Start Guide (This will open a new window)
   2.  Complete the section "Example Atomic-Structure Commands" as a tutorial
10. Open the two structures you found previously and run the a structural superimposition as follows:
    1.  Tools -> Structure Analysis -> Matchmaker
11. Move the view using your mouse to showcase the overlapping region
12. Convert to a publication style preset as follows:
    1.  Presets -> Publication
13. Save as a png as follows:
    1.  File -> Save... (Select png format and name appropriately)
14. Write a figure caption (make sure to name the proteins, what the image depicts)
15. Upload the writeup, figure and figure caption to Canvas

---

## Activity 3.3: RNA Model System on MFOld

### Background

Energetics drive the folding of molecules. In this activity you will explore the relationship between energetics and structure using a simple model system,a short RNA sequence.

### Description

1. For the activity use the sequence from the slides.
2. Navigate to http://www.unafold.org/mfold/applications/rna-folding-form.php
3. Confirm you can reproduce the results from the slides.
4. Next perform the following two things:
   1. Use your own constraints
      2. Include the results, the constraint parameter (i.e. "F 20 0 1")
      3. Describe what the constraint does? (i.e. ensures the 1 and 20th bases are paired together)
   2. Replace one letter of the query sequence to generate a structure with better energetics than the original sequence.
      1. Describe the results and why the change makes the structure more stable.
5. Upload the writeup to Canvas