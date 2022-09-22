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

## Activity 4.1: Exploring ChimeraX

### Description

In this exercise, you will explore some proteins from RCSB using chimeraX.

### Steps

1. Open ChimeraX and run the following commands in the 'Command' box at the bottom of the screen (you will explain what each command does as part of this report):
   1. `open 4jjx`
   2. `color bychain`
   3. `select #1/A` # Look for the green outline around parts of the protein after you run this command
   4. `rainbow sel`
   5. `select ~sel`
   6. `delete sel`
   7. `surface`
   8. `color byhetero` # Hover your mouse over the newly colored atoms, What do the colors denote? Red,Blue, Yellow? 
   9. `~surface` # What does the '~' tilde character mean? This is the second time we have used it
   10. `distance #1/A:0@CA #1/A:171@CA` # What value does this compute? (Clue it is a parameter from our structures lecture this week)
   11. `hbonds reveal true` # What does this show? What can you conclude about the relationship between hydrogen bonds and the secondary structures (helices and sheets)?
2. Rotate your protein to showcase the distance and save this as a png file.
3. Write a report to explain what each of these commands AND answer the questions for each command.
4. Upload the mini-report (including the explanation of commands, image and image caption) to Canvas

---

## Activity 4.2: Homology Modelling with Swiss Model

### Background

Homology modelling attempts to predict the structure of a query primary sequence by comparison to a database of known structures. 

### Description

In this exercise, you will use the Swiss Model server to predict the structure of a protein already in the RCSB.  Effectively this is a positive control on the approach since we know an existing experimental structure exists for comparison.

### Steps

1. Navigate to the [RCSB](https://www.rcsb.org/)
2. Obtain the fasta sequence for the entry with RCSB accession ID: '4hjy' (this can be obtained from the 'Download Files' dropdown menu on the right hand side of the 4HJY entry page)
3. Navigate to the [Swiss Model website](https://swissmodel.expasy.org/interactive)
4. Paste in the contents or upload the fasta file as the input
5. Add an email and project name, while both are optional, it is often advised to include them, especially when a server job may take a while to complete
6. Start the modelling by clicking 'Build Model'
7. This server takes around ~15 minutes to complete
8. Once finished, you should have two models built.
9. Using the documentation: https://swissmodel.expasy.org/docs/help
10. Report the following for each model
    1.  The template used
    2.  The sequence identity
    3.  Coverage (the range modelled of the full query sequence)
    4.  GMQE
    5.  QMEANDisCo Global
    6.  Your conclusion on whether the model is reliable and why?
11. For the best model, we will now check against the actual '4hjy' structure.
    1.  Download the pdb file for the model![](images/SwissModel.PNG)
    2.  Load the pdb file into ChimeraX along with 4hjy
    3.  Perform a matchmaker between the model and the experimental structure
        1.  Note: the model is only one chain of the two chain protein so you should see the model superimpose onto one of the two chains
    4.  Export an image and answer the following question
        1.  Does the model appear to be largely consistent with the experimental structure why or why not?
12. Upload the writeup, figure and figure caption to Canvas

---

## Activity 4.3: Docking using Swiss Dock

### Background

Energetics drive the folding of molecules. In this activity you will explore the relationship between energetics and structure using a simple model system,a short RNA sequence.

### Description

TODO: once test files generated from Swiss Dock
   
---

## Activity 4.4: Interpreting Molecular Dynamics Plots

### Background

Molecular dynamics (MD) output a series of positions and velocities for an input set of atoms over the course a simulation.  Plots serve as a powerful means of conveying the stability of the simulated complex at a whole molecule and specific residue view.

For this activity, you will explore an article presenting MD plots and a manual for an MD library.  The manual includes example figures and you will interpret these plots.

### Description

1. Use Figure 5 from understanding-thermal-and-organic-solvent-stability-of-thermoalkalophilic-lipases-insights-from-computational-predictions-and-experiments.pdf Article (on Canvas)
   1. In the 450K simulation when did the stability of the Open State form start to degrade in Methanol? Explain how you reached this conclusion
   2. Imagine you ran 20 ns simulations for this same set of conditions, what is a risk very short simulations?
   3. At 450K, is the effect of simulation solvent dependent on the protein form (i.e. open or closed), why or why not? Speculate on a reason for this depedency or lack of dependency.
2. Navigate to https://cran.r-project.org/web/packages/MDplot/vignettes/publication.pdf
3. Answer the following questions for Figure 11.
   1. Does this plot convey information about the whole system or specific residues in the system?
   2. What was the approximate simulation time?
   3. Comparing WildType(WT) and Mutant, suppose the researcher was designing a mutation that was with the goal of destabilizing the protein.  Based on this plot, was is this mutation likely to destabilize the protein? Why or why not?
4. Answer the following questions for Figure 13.
   1. Does this plot convey information about the whole system or specific residues in the system?
   2. What regions of the molecule are relatively stable? What regions are relatively unstable?
5. Upload the writeup to Canvas