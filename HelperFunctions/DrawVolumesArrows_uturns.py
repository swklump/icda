def draw_volume_arrows_uturn(self, df, i,
                           ebentering_flow, wbentering_flow, nbentering_flow, sbentering_flow,
                           ebvol_entering, wbvol_entering, nbvol_entering, sbvol_entering,
                           ebu_flow, wbu_flow, nbu_flow, sbu_flow,
                           ebu_vol, wbu_vol, nbu_vol, sbu_vol,
                           kw, kw_red):

    from matplotlib.patches import FancyArrowPatch
    thru_arrow_length = 0.8

    # Draw EBU movements
    if df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to EBU east of intersection' or \
            df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to EBU east of intersection' or \
            df['Reroute-NBT'][i] == 'Prohibit NBT, reroute to EBU east of intersection':
        arrow_dict1 = {'x1': 5.2, 'y1': -0.25}
        text_dict1 = {'x1': 5.15, 'y1': 0.09}
        arrow_dict2 = {'x1': 6, 'y1': 0.45}
        text_dict2 = {'x1': 5.6, 'y1': 0.6}
        # Draw the arrows and text red if conflicting flows above user threshold.
        if wbentering_flow + ebu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], -arrow_dict1['y1']), connectionstyle="arc3,rad = 2", **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], '(uturn) ' + str(ebu_vol), horizontalalignment='right', weight='bold', fontsize=8,color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-thru_arrow_length, arrow_dict2['y1']), **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], wbvol_entering, horizontalalignment='center', weight='bold', fontsize=8, color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], -arrow_dict1['y1']), connectionstyle="arc3,rad = 2", **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], '(uturn) ' + str(ebu_vol), horizontalalignment='right', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']-thru_arrow_length, arrow_dict2['y1']), **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], wbvol_entering, horizontalalignment='center', weight='bold', fontsize=8)

    # Draw WBU movements
    if df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to WBU west of intersection' or df['Reroute-SBL'][
        i] == 'Prohibit SBL, reroute to WBU west of intersection' or df['Reroute-SBT'][
        i] == 'Prohibit SBT, reroute to WBU west of intersection':
        arrow_dict1 = {'x1': -5.2, 'y1': 0.25}
        text_dict1 = {'x1': -5.2, 'y1': -0.2}
        arrow_dict2 = {'x1': -6, 'y1': -0.45}
        text_dict2 = {'x1': -5.6, 'y1': -0.8}
        # Draw the arrows and text red if conflicting flows above user threshold.
        if ebentering_flow + wbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], -arrow_dict1['y1']), connectionstyle="arc3,rad = 2", **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], str(wbu_vol) + ' (uturn)', horizontalalignment='left', weight='bold', fontsize=8,color='red')
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+thru_arrow_length, arrow_dict2['y1']), **kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], ebvol_entering, horizontalalignment='center', weight='bold', fontsize=8,color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (arrow_dict1['x1'], -arrow_dict1['y1']), connectionstyle="arc3,rad = 2", **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], str(wbu_vol) + ' (uturn)', horizontalalignment='left', weight='bold', fontsize=8)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']), (arrow_dict2['x1']+thru_arrow_length, arrow_dict2['y1']), **kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], ebvol_entering, horizontalalignment='center', weight='bold', fontsize=8)

    # Draw NBU movements
    if df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to NBU north of intersection' or \
            df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to NBU north of intersection' or \
            df['Reroute-WBT'][i] == 'Prohibit WBT, reroute to NBU north of intersection':
        arrow_dict1 = {'x1': 0.25, 'y1': 4.25}
        text_dict1 = {'x1': 0, 'y1': 4.95}
        arrow_dict2 = {'x1': -0.45, 'y1': 5.05}
        text_dict2 = {'x1': -0.55, 'y1': 4.7}
        # Draw the arrows and text red if conflicting flows above user threshold.
        if sbentering_flow + nbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (-arrow_dict1['x1'], arrow_dict1['y1']),connectionstyle="arc3,rad = 2", **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], str(nbu_vol), verticalalignment='bottom', weight='bold',fontsize=8,color='red', rotation=90)
            self.canvas.axes.text(text_dict1['x1']+0.3, text_dict1['y1'], '(uturn)',verticalalignment='bottom', weight='bold', fontsize=8, color='red', rotation=90)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']),(arrow_dict2['x1'], arrow_dict2['y1'] - thru_arrow_length),**kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], sbvol_entering, horizontalalignment='right', weight='bold',fontsize=8,color='red')
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (-arrow_dict1['x1'], arrow_dict1['y1']),connectionstyle="arc3,rad = 2", **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], str(nbu_vol), verticalalignment='bottom', weight='bold',fontsize=8, rotation=90)
            self.canvas.axes.text(text_dict1['x1']+0.3, text_dict1['y1'], '(uturn)',verticalalignment='bottom', weight='bold', fontsize=8, rotation=90)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']),(arrow_dict2['x1'], arrow_dict2['y1'] - thru_arrow_length),**kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], sbvol_entering, horizontalalignment='right', weight='bold',fontsize=8)

    # Draw SBU movements
    if df['Reroute-SBL'][i] == 'Prohibit SBL, reroute to SBU south of intersection' or \
            df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to SBU south of intersection' or \
            df['Reroute-EBT'][i] == 'Prohibit EBT, reroute to SBU south of intersection':
        arrow_dict1 = {'x1': -0.25, 'y1': -4.25}
        text_dict1 = {'x1': -0.2, 'y1': -4.95}
        arrow_dict2 = {'x1': 0.45, 'y1': -5.05}
        text_dict2 = {'x1': 0.6, 'y1': -4.75}
        # Draw the arrows and text red if conflicting flows above user threshold.
        if nbentering_flow + sbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (-arrow_dict1['x1'], arrow_dict1['y1']),connectionstyle="arc3,rad = 2", **kw_red))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], '(uturn) '+str(sbu_vol), verticalalignment='top', weight='bold',fontsize=8,color="red", rotation=90)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']),(arrow_dict2['x1'], arrow_dict2['y1'] + thru_arrow_length),**kw_red))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], nbvol_entering, horizontalalignment='left', weight='bold',fontsize=8,color="red")
        else:
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict1['x1'], arrow_dict1['y1']), (-arrow_dict1['x1'], arrow_dict1['y1']),connectionstyle="arc3,rad = 2", **kw))
            self.canvas.axes.text(text_dict1['x1'], text_dict1['y1'], '(uturn) '+str(sbu_vol), verticalalignment='top', weight='bold',fontsize=8, rotation=90)
            self.canvas.axes.add_patch(FancyArrowPatch((arrow_dict2['x1'], arrow_dict2['y1']),(arrow_dict2['x1'], arrow_dict2['y1'] + thru_arrow_length),**kw))
            self.canvas.axes.text(text_dict2['x1'], text_dict2['y1'], nbvol_entering, horizontalalignment='left', weight='bold',fontsize=8)