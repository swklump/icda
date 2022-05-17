Explanation of files

The app uses PyQT, QT Designer for the GUI, matplotlib for the plotting, and pandas for data manipulation.
The app is turned into an exe with "pyinstaller --onefile --windowed --icon=PNG_files/icon.ico Application.spec" run in command line.

1. "Application.py"
	This file is the main script to run the app. To run, in CMD type "python Application.py".
	Each class in the script is for running modules seen from the home page. When first running the app, the HomePage class is activated (line 537-540). From the homepage, you can see 
buttons for "Application Overview", "Single Plot", and "Batch Plot". When each of these buttons is clicked, the corresponding class runs (lines 93-95).
	The "MplCanvas" class is for embedding the matplotlib plot within the PyQT GUI.

2. "Application.spec" specifies how to package the app. 

3. "plot_helper.py" does the legwork of creating the plots. It runs on a loop depending on how many plots need to be made. This runs processes for both the Single Plot and Batch Plot modules.
	The script starts off by moving and relocating volumes based on user selections. For instance, if "Prohibit EBL, reroute to EBU east of intersection" is selected, the EBL volume gets added
to the EBT volume, then the EBU volume, then the WBR volume, and the EBL volume goes to zero (lines 47-51).
	Then volumes are calculated for entering and exiting intersection. These volumes conflict with uturns (entering) and displaced lefts (exiting).
	Then flow rates are calculated by dividng the volumes by number of lanes.
	Then plots are set up (lines 154 onward). Plots are set up by dividing the work between functions in other files (LaneDiagram.py, FlaggedConflicts.py, etc).
	Finally, the plots are saved (optional) and shown (lines 206-229).
	All the data are stored in pandas dataframes for ease of access.


4. "Application_helperfunctions.py" is one function for implementing GUI defaults, like adding the icon in the top left of each window and adding the minimize window button.

5. "Centerlines.py" draws the centerlines of the major and minor road in the intersection plot, and the curb returns.

6. "DrawVolumesArrows_std.py" draws arrows for standard movements on the plots. Coordinates are stored in dictionaries for ease of manipulation. Draws red arrows and text if conflicting flow 
rates are above user specified threshold.

7. "DrawVolumesArrows_uturns.py" draws arrows for uturns on the plots.

8. "DrawVolumesArrows_displacedlefts.py" draws arrows for displaced lefts on the plots. 

9. "FlaggedConflicts.py" displaced the text in the bottom left and right corners of the plots, for when conflicting flow rates are above user specified thresholds.

10. "LaneDiagram.py" shows lane diagrams in top left and right corners of the plots. Just shows number of lanes for applicable movements.

11. "UI_files" folder has the QT Designer UI files. With QT Designer, UIs are edited with drag and drop.

12. "PNG_files" has the icon that are shown in the UI.

13. "Batchplot_template.xlsx" is the template file users upload for the Batch Plot module.

14. "Dist" folder is where the exe goes after you run the command to convert to and exe.



