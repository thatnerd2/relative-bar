# Relative Bar Graph Generator

Bar graphs usually have static statistics.  I thought it might be interesting to have a bar graph in which each bar depended on the other bars, and each bar was adjustable.  One might think of a spreadsheet, where changing one cell causes other formula-based cells to change.

Upon fiddling with it for a few hours, I discovered that for full range of motion, for any n bars, 2*n bars would have to be shown - n bars to play with the formulas directly, and n bars to adjust the variables.  Adjusting a single variable would adjust the appropriate number of formulas, and adjusting a formula would adjust the appropriate number of bars.  This is interesting, but not as interesting as the original concept I had in mind, so I'm shelving this project for now.

I used Phaser's game engine to render the bars as bitmaps - I planned to transition to something more raw later, but this was a great setup for prototyping.
