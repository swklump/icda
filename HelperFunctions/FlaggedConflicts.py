def flagged_conflicts(self, df, i,
                      ebexiting_flow, wbexiting_flow, nbexiting_flow, sbexiting_flow,
                      ebt_flow, wbt_flow, nbt_flow, sbt_flow,
                      ebl_flow, wbl_flow, nbl_flow, sbl_flow,
                      ebu_flow, wbu_flow, nbu_flow, sbu_flow,
                      ebentering_flow, wbentering_flow, nbentering_flow, sbentering_flow):

    # Conflicts within intersection
    y_pos = -4
    y_diff = 0.3
    x_pos = -7
    if df['Reroute-EBL'][i] == 'No change' and wbt_flow + ebl_flow / df['LT_UT Volume Factor'][i] > \
            int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Eastbound Left/Westbound Thru', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if df['Reroute-WBL'][i] == 'No change' and ebt_flow + wbl_flow / df['LT_UT Volume Factor'][i] > \
            int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Westbound Left/Eastbound Thru', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if df['Reroute-NBL'][i] == 'No change' and sbt_flow + nbl_flow / df['LT_UT Volume Factor'][i] > \
            int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Northbound Left/Southbound Thru', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if df['Reroute-SBL'][i] == 'No change' and nbt_flow + sbl_flow / df['LT_UT Volume Factor'][i] > \
            int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Southbound Left/Northbound Thru', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if y_pos == -4:
        self.canvas.axes.text(x_pos, y_pos, 'None', horizontalalignment='left', fontsize=8)

    # Conflicts at u-turns
    y_pos = -5.8
    y_diff = 0.3
    x_pos = -7
    if ('EBU' in df['Reroute-EBL'][i] or 'EBU' in df['Reroute-NBL'][i] or 'EBU' in df['Reroute-NBT'][i]) and \
            wbentering_flow + ebu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Eastbound U-turn/Westbound Entering', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if ('WBU' in df['Reroute-WBL'][i] or 'WBU' in df['Reroute-SBL'][i] or 'WBU' in df['Reroute-SBT'][i]) and \
            ebentering_flow + wbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Westbound U-turn/Eastbound Entering', horizontalalignment='left', fontsize=8, color='red')
        y_pos -= y_diff
    if ('NBU' in df['Reroute-NBL'][i] or 'NBU' in df['Reroute-WBL'][i] or 'NBU' in df['Reroute-WBT'][i]) and \
            sbentering_flow + nbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Northbound U-turn/Southbound Entering', horizontalalignment='left', fontsize=8,color='red')
        y_pos -= y_diff
    if ('SBU' in df['Reroute-SBL'][i] or 'SBU' in df['Reroute-EBL'][i] or 'SBU' in df['Reroute-EBT'][i]) and \
            nbentering_flow + sbu_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Southbound U-turn/Northbound Entering', horizontalalignment='left', fontsize=8,color='red')
        y_pos -= y_diff
    if y_pos == -5.8:
        self.canvas.axes.text(x_pos, y_pos, 'None', horizontalalignment='left', fontsize=8)

    # Conflicts at displaced lefts
    y_pos = -5.8
    y_diff = 0.3
    x_pos = 7
    if df['Reroute-EBL'][i] == 'Displace EBL west of intersection' and wbexiting_flow + ebl_flow / \
            df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Disp. Eastbound Left/Westbound Exiting', horizontalalignment='right', fontsize=8,color='red')
        y_pos -= y_diff
    if df['Reroute-WBL'][i] == 'Displace WBL east of intersection' and ebexiting_flow + wbl_flow / \
            df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Disp. Westbound Left/Eastbound Exiting', horizontalalignment='right', fontsize=8,color='red')
        y_pos -= y_diff
    if df['Reroute-NBL'][i] == 'Displace NBL south of intersection' and sbexiting_flow + nbl_flow / \
            df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Disp. Northboud Left/Southbound Exiting', horizontalalignment='right', fontsize=8,color='red')
        y_pos -= y_diff
    if df['Reroute-SBL'][i] == 'Displace SBL north of intersection' and nbexiting_flow + sbl_flow / \
            df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
        self.canvas.axes.text(x_pos, y_pos, 'Disp. Southbound Left/Northbound Exiting', horizontalalignment='right', fontsize=8,color='red')
        y_pos -= y_diff
    if y_pos == -5.8:
        self.canvas.axes.text(x_pos, y_pos, 'None', horizontalalignment='right', fontsize=8)