def centerlines(self):

    from matplotlib.patches import FancyArrowPatch

    # Centerlines
    self.canvas.axes.add_patch(FancyArrowPatch((-3, 0), (3, 0), alpha=0.5, color='black', linewidth=0.5))
    self.canvas.axes.add_patch(FancyArrowPatch((0, -3), (0, 3), alpha=0.5, color='black', linewidth=0.5))

    # Curb Returns
    #Top left
    self.canvas.axes.add_patch(FancyArrowPatch((-3.2, 1.7), (-1.7, 3.2), connectionstyle="arc3,rad = 0.6", alpha=0.5, color='black',linewidth=0.5))
    #Top right
    self.canvas.axes.add_patch(FancyArrowPatch((3.2, 1.7), (1.7, 3.2), connectionstyle="arc3,rad = -0.6", alpha=0.5, color='black',linewidth=0.5))
    #Bottom right
    self.canvas.axes.add_patch(FancyArrowPatch((3.2, -1.7), (1.7, -3.2), connectionstyle="arc3,rad = 0.6", alpha=0.5, color='black',linewidth=0.5))
    #Bottom left
    self.canvas.axes.add_patch(FancyArrowPatch((-3.2, -1.7), (-1.7, -3.2), connectionstyle="arc3,rad = -0.6", alpha=0.5, color='black',linewidth=0.5))