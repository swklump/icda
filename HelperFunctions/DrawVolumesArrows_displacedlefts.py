def draw_volume_arrows_displacedlefts(self, df, i,
                             ebexiting_flow, wbexiting_flow, nbexiting_flow, sbexiting_flow,
                             ebvol_exiting, wbvol_exiting, nbvol_exiting, sbvol_exiting,
                             ebl_flow, wbl_flow, nbl_flow, sbl_flow,
                             kw, kw_red):

    from matplotlib.patches import FancyArrowPatch
    thru_arrow_length = 0.8
    left_arrow_length = 0.5

    # Draw EBL displaced left
    arrow_dict1 = {'x1': -3, 'y1': 0.75}
    text_dict1 = {'x1': -3.4, 'y1': 0.9}
    arrow_dict2 = {'x1': -4.3, 'y1': 0.25}
    text_dict2 = {'x1': -3.9, 'y1': 0.6}

    if df['Reroute-EBL'][i] == 'Displace EBL west of intersection':
        #Draw the arrows and text red if conflicting flows above user threshold.
        if wbexiting_flow + ebl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1']-thru_arrow_length, arrow_dict1['y1']), **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], wbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8, color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+left_arrow_length, arrow_dict2['y1']+left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], '(disp.left) ' + str(df['EBL'][i]), horizontalalignment='right', weight='bold',fontsize=8, color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1']-thru_arrow_length, arrow_dict1['y1']), **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], wbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+left_arrow_length, arrow_dict2['y1']+left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], '(disp.left) ' + str(df['EBL'][i]), horizontalalignment='right', weight='bold',fontsize=8)

    # Draw WBL displaced left
    arrow_dict1 = {'x1': 3, 'y1': -0.75}
    text_dict1 = {'x1': 3.4, 'y1': -1.1}
    arrow_dict2 = {'x1': 4.3, 'y1': -0.25}
    text_dict2 = {'x1': 3.9, 'y1': -0.7}
    if df['Reroute-WBL'][i] == 'Displace WBL east of intersection':
        # Draw the arrows and text red if conflicting flows above user threshold.
        if ebexiting_flow + wbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1']+thru_arrow_length, arrow_dict1['y1']), **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], ebvol_exiting, horizontalalignment='center', weight='bold', fontsize=8, color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-left_arrow_length, arrow_dict2['y1']-left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], str(df['WBL'][i]) + ' (disp.left)', horizontalalignment='left', weight='bold',fontsize=8, color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1']+thru_arrow_length, arrow_dict1['y1']), **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], ebvol_exiting, horizontalalignment='center', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-left_arrow_length, arrow_dict2['y1']-left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], str(df['WBL'][i]) + ' (disp.left)', horizontalalignment='left', weight='bold',fontsize=8)

    # Draw NBL displaced left
    arrow_dict1 = {'x1': -1, 'y1': -2.6}
    text_dict1 = {'x1': -1, 'y1': -2.55}
    arrow_dict2 = {'x1': -0.5, 'y1': -3.85}
    text_dict2 = {'x1': -0.4, 'y1': -3.75}
    if df['Reroute-NBL'][i] == 'Displace NBL south of intersection':
        if sbexiting_flow + nbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            # Draw the arrows and text red if conflicting flows above user threshold.
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], arrow_dict1['y1']-thru_arrow_length), **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], sbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8, color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-left_arrow_length, arrow_dict2['y1']+left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], str(df['NBL'][i]) + ' (disp.left)', horizontalalignment='left', weight='bold',fontsize=8, color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], arrow_dict1['y1']-thru_arrow_length), **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], sbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-left_arrow_length, arrow_dict2['y1']+left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], str(df['NBL'][i]) + ' (disp.left)', horizontalalignment='left', weight='bold',fontsize=8)

    # Draw SBL displaced left
    arrow_dict1 = {'x1': 1, 'y1': 2.6}
    text_dict1 = {'x1': 1, 'y1': 2.4}
    arrow_dict2 = {'x1': 0.5, 'y1': 3.9}
    text_dict2 = {'x1': 0.45, 'y1': 3.5}
    if df['Reroute-SBL'][i] == 'Displace SBL north of intersection':
        # Draw the arrows and text red if conflicting flows above user threshold.
        if nbexiting_flow + sbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], arrow_dict1['y1']+thru_arrow_length), **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], nbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8, color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+left_arrow_length, arrow_dict2['y1']-left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], '(disp.left) ' + str(df['SBL'][i]), horizontalalignment='right', weight='bold',fontsize=8, color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], arrow_dict1['y1']+thru_arrow_length), **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], nbvol_exiting, horizontalalignment='center', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+left_arrow_length, arrow_dict2['y1']-left_arrow_length), connectionstyle="arc3,rad = 0.6", **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], '(disp.left) ' + str(df['SBL'][i]), horizontalalignment='right', weight='bold',fontsize=8)