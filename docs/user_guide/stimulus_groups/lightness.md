# Lightness stimuli

Lightness perception research is characterized by an extraordinary diversity of stimuli, with dozens of distinct illusions each highlighting different aspects of visual processing. Unlike other domains where a few canonical stimuli dominate, lightness research features many distinct illusions - from classic simultaneous brightness contrast to White's illusion, Cornsweet edges, and the Todorovic effect.

## Why so many different stimuli?

The variety is both interesting and a challenge. Each illusion reveals something different about how our visual system processes lightness, but it also means there's no standard set that everyone agrees on. Different labs tend to focus on different subsets of stimuli, which makes it tricky to compare results across studies.

## Stimupy's approach

We've tried to address this by collecting a wide range of lightness stimuli in one place. This stems partly from our own research interests in understanding these phenomena computationally. Here's what you'll find:

**Brightness contrast** (`sbcs`): Good old simultaneous brightness contrast - identical targets that look different depending on their backgrounds. We have basic rectangular versions, circular ones, and fancier multi-background setups.

**Brightness assimilation**: Including checkerboard variants (`checkerboards`) with contrast-contrast effects that demonstrate how local and global processing interact, and bullseye patterns (`bullseyes`) that show assimilation effects where targets shift toward the surrounding pattern.

**Cornsweet edges** (`cornsweets`): These create strong lightness differences using smooth gradients - great for studying how the visual system enhances edges.

**Lightness inducing patterns**: The famous White's illusion (`whites`) from 1979 that shook up lightness theory by showing that what matters isn't just what surrounds a target, but what it's connected to. Also includes things like Benary's cross (`benarys`), the Todorovic illusion (`todorovics`), the dungeon illusion (`dungeons`) with its diamond targets on grids, and grating effects (`gratings`) that show how layout and connectivity really matter for lightness.

## Benchmark stimulus sets

Even though there's no universal standard, a few collections have become popular reference points:

**Robinson, Hammon & de Sa (2007)** (`RHS2007`): A comprehensive collection that includes many classic lightness illusions in standardized formats. This set has been particularly influential in computational modeling of lightness perception and provides a good starting point for researchers wanting to test models across multiple phenomena.

**Individual paper collections**: We also include stimulus sets from influential individual studies, such as White (1981, 1985), Domijan (2015), and others, allowing researchers to replicate specific experimental conditions exactly.

## Getting started

If you're looking to explore lightness illusions, test a model, or set up new experiments, you'll find the tools here. Everything comes with lots of parameter options so you can tweak things however you need for your particular research question.