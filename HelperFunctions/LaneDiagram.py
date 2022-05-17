def lane_diagrams(self, df, i, kw):
    from matplotlib.patches import FancyArrowPatch
    from matplotlib.pyplot import Rectangle

#### Main Intersection Lane Diagram
    coords = {'nbl': (-5.25, 3.75), 'nbt': (-4.95, 3.75), 'sbl': (-4.65, 6.55), 'sbt': (-4.95, 6.55),
              'ebl': (-6.55, 5.45), 'ebt': (-6.55, 5.15), 'wbl': (-3.35, 4.85), 'wbt': (-3.35, 5.15)}
    self.canvas.axes.text(-4.95, 7, 'Main Intx Lane Diagram', horizontalalignment='center', fontsize=8)
    rectangle = Rectangle((-3, 6.9), -3.9, -3.65, edgecolor='black', facecolor="none", linestyle="dotted")
    self.canvas.axes.add_patch(rectangle)

    # EB
    if df['Reroute-EBL'][i] != 'Prohibit EBL, reroute to EBU east of intersection' and \
            df['Reroute-EBL'][i] != 'Prohibit EBL, reroute to SBU south of intersection' and \
            df['Reroute-EBL'][i] != 'Displace EBL west of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['ebl'], (coords['ebl'][0] + 0.5, coords['ebl'][1] + 0.5),connectionstyle="arc3,rad = 0.6", **kw))
        self.canvas.axes.text(coords['ebl'][0] - 0.1, coords['ebl'][1] - 0.05, df['Max Lanes-EBL'][i], horizontalalignment='center',fontsize=8)
    if df['Reroute-EBT'][i] != 'Prohibit EBT, reroute to SBU south of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['ebt'], (coords['ebt'][0] + 0.75, coords['ebt'][1]), **kw))
        self.canvas.axes.text(coords['ebt'][0] - 0.1, coords['ebt'][1] - 0.1, df['Max Lanes-EBT'][i], horizontalalignment='center',fontsize=8)

    # WB
    if df['Reroute-WBL'][i] != 'Prohibit WBL, reroute to WBU west of intersection' and \
            df['Reroute-WBL'][i] != 'Prohibit WBL, reroute to NBU north of intersection' and \
            df['Reroute-WBL'][i] != 'Displace WBL east of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['wbl'], (coords['wbl'][0] - 0.5, coords['wbl'][1] - 0.5),connectionstyle="arc3,rad = 0.6", **kw))
        self.canvas.axes.text(coords['wbl'][0] + 0.05, coords['wbl'][1] - 0.1, df['Max Lanes-WBL'][i], horizontalalignment='center',fontsize=8)
    if df['Reroute-WBT'][i] != 'Prohibit WBT, reroute to NBU north of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['wbt'], (coords['wbt'][0] - 0.75, coords['wbt'][1]), **kw))
        self.canvas.axes.text(coords['wbt'][0] + 0.05, coords['wbt'][1] - 0.05, df['Max Lanes-WBT'][i],horizontalalignment='center', fontsize=8)

    # NB
    if df['Reroute-NBL'][i] != 'Prohibit NBL, reroute to NBU north of intersection' and \
            df['Reroute-NBL'][i] != 'Prohibit NBL, reroute to EBU east of intersection' and \
            df['Reroute-NBL'][i] != 'Displace NBL south of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['nbl'], (coords['nbl'][0] - 0.5, coords['nbl'][1] + 0.5),connectionstyle="arc3,rad = 0.6", **kw))
        self.canvas.axes.text(coords['nbl'][0], coords['nbl'][1] - 0.25, df['Max Lanes-NBL'][i],horizontalalignment='center', fontsize=8)
    if df['Reroute-NBT'][i] != 'Prohibit NBT, reroute to EBU east of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['nbt'], (coords['nbt'][0], coords['nbt'][1] + 0.75), **kw))
        self.canvas.axes.text(coords['nbt'][0], coords['nbt'][1] - 0.25, df['Max Lanes-NBT'][i],horizontalalignment='center', fontsize=8)

    # SB
    if df['Reroute-SBL'][i] != 'Prohibit SBL, reroute to SBU south of intersection' and \
            df['Reroute-SBL'][i] != 'Prohibit SBL, reroute to WBU west of intersection' and \
            df['Reroute-SBL'][i] != 'Displace SBL north of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['sbl'], (coords['sbl'][0] + 0.5, coords['sbl'][1] - 0.5),connectionstyle="arc3,rad = 0.6", **kw))
        self.canvas.axes.text(coords['sbl'][0], coords['sbl'][1] + 0.05, df['Max Lanes-SBL'][i],horizontalalignment='center', fontsize=8)
    if df['Reroute-SBT'][i] != 'Prohibit SBT, reroute to WBU west of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords['sbt'], (coords['sbt'][0], coords['sbt'][1] - 0.75), **kw))
        self.canvas.axes.text(coords['sbt'][0], coords['sbt'][1] + 0.05, df['Max Lanes-SBT'][i],horizontalalignment='center', fontsize=8)


####Uturn Lane Diagram
    coords_uturn = {'ebu': (6, 4.85), 'wbu': (3.9, 5.35), 'nbu': (5.2, 5.9), 'sbu': (4.7, 4.3)}

    self.canvas.axes.text(4.95, 7, 'Uturn Lane Diagram', horizontalalignment='center', fontsize=8)
    rectangle = Rectangle((6.9, 6.9), -3.9, -3.65, edgecolor='black', facecolor="none", linestyle="dotted")
    self.canvas.axes.add_patch(rectangle)

    # EBU
    if df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to EBU east of intersection' or \
            df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to EBU east of intersection' or \
            df['Reroute-NBT'][i] == 'Prohibit NBT, reroute to EBU east of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords_uturn['ebu'], (coords_uturn['ebu'][0], coords_uturn['ebu'][1]+0.5),connectionstyle="arc3,rad = 2", **kw))
        self.canvas.axes.text(coords_uturn['ebu'][0]-0.05, coords_uturn['ebu'][1]-0.1, df['Max Lanes-EBU'][i],horizontalalignment='right', fontsize=8)
        self.canvas.axes.add_patch(FancyArrowPatch((coords_uturn['ebu'][0] + 0.75, coords_uturn['ebu'][1]+0.65), (coords_uturn['ebu'][0], coords_uturn['ebu'][1]+0.65), **kw))
        self.canvas.axes.text(coords_uturn['ebu'][0]+0.5, coords_uturn['ebu'][1]+0.75, df['Max Lanes-WBT_Uturn'][i],horizontalalignment='center', fontsize=8)

    #WBU
    if df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to WBU west of intersection' or \
            df['Reroute-SBL'][i] == 'Prohibit SBL, reroute to WBU west of intersection' or \
            df['Reroute-SBT'][i] == 'Prohibit SBT, reroute to WBU west of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords_uturn['wbu'], (coords_uturn['wbu'][0], coords_uturn['wbu'][1]-0.5), connectionstyle="arc3,rad = 2", **kw))
        self.canvas.axes.text(coords_uturn['wbu'][0]+0.05, coords_uturn['wbu'][1]-0.1, df['Max Lanes-WBU'][i], horizontalalignment='left', fontsize=8)
        self.canvas.axes.add_patch(FancyArrowPatch((coords_uturn['wbu'][0] - 0.75, coords_uturn['wbu'][1]-0.65), (coords_uturn['wbu'][0], coords_uturn['wbu'][1]-0.65), **kw))
        self.canvas.axes.text(coords_uturn['wbu'][0]-0.5, coords_uturn['wbu'][1]-0.9, df['Max Lanes-EBT_Uturn'][i],horizontalalignment='center', fontsize=8)

    # NBU
    if df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to NBU north of intersection' or \
            df['Reroute-WBT'][i] == 'Prohibit WBT, reroute to NBU north of intersection' or \
            df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to NBU north of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords_uturn['nbu'], (coords_uturn['nbu'][0]-0.5, coords_uturn['nbu'][1]), connectionstyle="arc3,rad = 2", **kw))
        self.canvas.axes.text(coords_uturn['nbu'][0]-0.1, coords_uturn['nbu'][1]-0.25, df['Max Lanes-NBU'][i], horizontalalignment='left', fontsize=8)
        self.canvas.axes.add_patch(FancyArrowPatch((coords_uturn['nbu'][0]-0.65, coords_uturn['nbu'][1] + 0.75), (coords_uturn['nbu'][0]-0.65, coords_uturn['nbu'][1]), **kw))
        self.canvas.axes.text(coords_uturn['nbu'][0]-0.85, coords_uturn['nbu'][1]+0.5, df['Max Lanes-SBT_Uturn'][i],horizontalalignment='center', fontsize=8)

    # SBU
    if df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to SBU south of intersection' or \
            df['Reroute-EBT'][i] == 'Prohibit EBT, reroute to SBU south of intersection' or \
            df['Reroute-SBL'][i] == 'Prohibit SBL, reroute to SBU south of intersection':
        self.canvas.axes.add_patch(FancyArrowPatch(coords_uturn['sbu'], (coords_uturn['sbu'][0]+0.5, coords_uturn['sbu'][1]), connectionstyle="arc3,rad = 2", **kw))
        self.canvas.axes.text(coords_uturn['sbu'][0]+0.05, coords_uturn['sbu'][1]+0.05, df['Max Lanes-SBU'][i], horizontalalignment='right', fontsize=8)
        self.canvas.axes.add_patch(FancyArrowPatch((coords_uturn['sbu'][0]+0.65, coords_uturn['sbu'][1] - 0.75), (coords_uturn['sbu'][0]+0.65, coords_uturn['sbu'][1]), **kw))
        self.canvas.axes.text(coords_uturn['sbu'][0]+0.85, coords_uturn['sbu'][1]-0.6, df['Max Lanes-NBT_Uturn'][i],horizontalalignment='center', fontsize=8)