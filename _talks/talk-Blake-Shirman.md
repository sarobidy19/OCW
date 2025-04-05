--- 
name: Embedding decision trees to solve bivariate recurrence relations 
speakers: 
 - Blake Shirman
categories:
 - Contributed
--- 
 
We start by showing how repeated iterations of Pascal's recurrence can generate a binary decision tree.  Embedding this tree into the integer lattice in a particular way reveals the familiar grid of NE (North, East) lattice paths.  While this is not a novel transformation, it begs the question: what other recurrence relations can be similarly transformed into a lattice grid?  We begin our search, appropriately, with a small modification of NE lattice paths.  We rotate our grid clockwise by 45 degrees and only count those paths that reach a certain high-point, but no higher.  Counting these "high-point paths" we see a similar recurrence to Pascal's, but more resistant to other methods of analysis.  After repeating our decision-tree-embedding method on this new recurrence, we only need to perform a reflection and rotation to see our familiar NE lattice, deriving a nice closed form for the number of high-point paths!  We close by considering some other bivariate sequences to see which might be amenable to our method.  Results on high-point paths comes from work on a recent publication by Acton, Petersen, Shirman, and Tenner (https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i1p15).