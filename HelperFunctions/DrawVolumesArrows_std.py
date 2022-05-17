def draw_volume_arrows_std(self, df, i, ebt_flow, wbt_flow, nbt_flow, sbt_flow,
                       ebl_flow, wbl_flow, nbl_flow, sbl_flow,
                       kw, kw_red):

    from matplotlib.patches import FancyArrowPatch

    # Define functions for drawing arrows
    def left_arrow(arrow_coord1, arrow_coord2, arrow_type, text_coord1, text_coord2, text_val, alg_type, justification, rot, text_color):
        self.canvas.axes.add_patch(FancyArrowPatch(arrow_coord1, arrow_coord2, connectionstyle="arc3,rad = 0.6", **arrow_type))
        if alg_type == 'horizontalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, horizontalalignment=justification, weight='bold',fontsize=8,
                 rotation=rot, color=text_color)
        elif alg_type == 'verticalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, verticalalignment=justification, weight='bold', fontsize=8,
                 rotation=rot, color=text_color)

    def right_arrow(arrow_coord1, arrow_coord2, text_coord1, text_coord2, text_val, alg_type, justification, rot):
        self.canvas.axes.add_patch(FancyArrowPatch(arrow_coord1, arrow_coord2, connectionstyle="arc3,rad = -0.6", **kw))
        if alg_type == 'horizontalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, horizontalalignment=justification, weight='bold',fontsize=8,
                 rotation=rot)
        elif alg_type == 'verticalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, verticalalignment=justification, weight='bold', fontsize=8,
                 rotation=rot)

    def thru_arrow(arrow_coord1, arrow_coord2, arrow_type, text_coord1, text_coord2, text_val, alg_type, justification, rot, text_color):
        self.canvas.axes.add_patch(FancyArrowPatch(arrow_coord1, arrow_coord2, **arrow_type))
        if alg_type == 'horizontalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, horizontalalignment=justification, weight='bold',fontsize=8,
                 rotation=rot, color=text_color)
        elif alg_type == 'verticalalignment':
            self.canvas.axes.text(text_coord1, text_coord2, text_val, verticalalignment=justification, weight='bold', fontsize=8,
                 rotation=rot, color=text_color)


##### Draw EB movements
    x_align_eb = -2.25
    y_align_eb = -0.9
    coords = {'ebl': (x_align_eb, y_align_eb+0.4), 'ebt':(x_align_eb, y_align_eb), 'ebr':(x_align_eb, y_align_eb-0.4)}

    coords_ebl = [coords['ebl'], (coords['ebl'][0]+0.5, coords['ebl'][1]+0.5)]
    coords_ebl_text = [coords['ebl'][0], coords['ebl'][1] - 0.05]

    coords_ebt = [coords['ebt'], (coords['ebt'][0]+0.75, coords['ebt'][1])]
    coords_ebt_text = [coords['ebt'][0], coords['ebt'][1]-0.05]

    coords_ebr = [coords['ebr'], (coords['ebr'][0]+0.5, coords['ebr'][1]-0.5)]
    coords_ebr_text = [coords['ebr'][0], coords['ebr'][1]-0.05]

    # Only draw if the EBL exists
    if df['Reroute-EBL'][i] in ('Prohibit EBL, reroute to EBU east of intersection',
                                'Prohibit EBL, reroute to SBU south of intersection',
                                'Displace EBL west of intersection'):
        pass

    else:
        #Draw the arrows and text red if conflicting flows above user threshold.
        if wbt_flow + ebl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            left_arrow(coords_ebl[0], coords_ebl[1], kw_red, coords_ebl_text[0], coords_ebl_text[1], df['EBL'][i], 'horizontalalignment',
                       'right', 0, 'red')
        else:
            left_arrow(coords_ebl[0], coords_ebl[1], kw, coords_ebl_text[0], coords_ebl_text[1], df['EBL'][i],'horizontalalignment','right', 0, 'black')
    # Only draw if the EBT exists
    if df['Reroute-EBT'][i] == 'Prohibit EBT, reroute to SBU south of intersection':
        pass
    else:
        # If conflicting movements above max flow rate, draw red, else black
        if df['Reroute-WBL'][i] == 'No change' and ebt_flow + wbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            thru_arrow(coords_ebt[0], coords_ebt[1], kw_red, coords_ebt_text[0], coords_ebt_text[1], df['EBT'][i], 'horizontalalignment','right', 0, 'red')
        else:
            thru_arrow(coords_ebt[0], coords_ebt[1], kw, coords_ebt_text[0], coords_ebt_text[1], df['EBT'][i], 'horizontalalignment','right', 0, 'black')
    # Draw the EBR
    right_arrow(coords_ebr[0],coords_ebr[1], coords_ebr_text[0], coords_ebr_text[1], df['EBR'][i], 'horizontalalignment', 'right', 0)


##### Draw WB movements
    x_align_wb = x_align_eb * -1
    y_align_wb = y_align_eb * -1
    coords = {'wbl': (x_align_wb, y_align_wb - 0.4), 'wbt': (x_align_wb, y_align_wb), 'wbr': (x_align_wb, y_align_wb + 0.4)}

    coords_wbl = [coords['wbl'], (coords['wbl'][0]-0.5, coords['wbl'][1]-0.5)]
    coords_wbl_text = [coords['wbl'][0], coords['wbl'][1]-0.05]

    coords_wbt = [coords['wbt'], (coords['wbt'][0]-0.75, coords['wbt'][1])]
    coords_wbt_text = [coords['wbt'][0], coords['wbt'][1]-0.05]

    coords_wbr = [coords['wbr'], (coords['wbr'][0]-0.5, coords['wbr'][1]+0.5)]
    coords_wbr_text = [coords['wbr'][0], coords['wbr'][1]-0.05]
    
    if df['Reroute-WBL'][i] in ('Prohibit WBL, reroute to WBU west of intersection',
                                'Prohibit WBL, reroute to NBU north of intersection',
                                'Displace WBL east of intersection'):
        pass
    else:
        # Draw the arrows and text red if conflicting flows above user threshold.
        if ebt_flow + wbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            left_arrow(coords_wbl[0], coords_wbl[1], kw_red, coords_wbl_text[0], coords_wbl_text[1], df['WBL'][i],'horizontalalignment','left', 0, 'red')
        else:
            left_arrow(coords_wbl[0], coords_wbl[1], kw, coords_wbl_text[0], coords_wbl_text[1], df['WBL'][i],'horizontalalignment', 'left', 0, 'black')
    if df['Reroute-WBT'][i] == 'Prohibit WBT, reroute to NBU north of intersection':
        pass
    else:
        if df['Reroute-EBL'][i] == 'No change' and wbt_flow + ebl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            thru_arrow(coords_wbt[0], coords_wbt[1], kw_red, coords_wbt_text[0], coords_wbt_text[1], df['WBT'][i], 'horizontalalignment','left', 0, 'red')
        else:
            thru_arrow(coords_wbt[0], coords_wbt[1], kw, coords_wbt_text[0], coords_wbt_text[1], df['WBT'][i], 'horizontalalignment','left', 0, 'black')
    right_arrow(coords_wbr[0], coords_wbr[1], coords_wbr_text[0], coords_wbr_text[1], df['WBR'][i],'horizontalalignment', 'left', 0)

##### Draw NB movements
    x_align_nb = 1
    y_align_nb = -2
    coords = {'nbl': (x_align_nb-0.4, y_align_nb), 'nbt': (x_align_nb, y_align_nb), 'nbr': (x_align_nb+0.4, y_align_nb)}
    
    coords_nbl = [coords['nbl'], (coords['nbl'][0]-0.5, coords['nbl'][1]+0.5)]
    coords_nbl_text = [coords['nbl'][0]-0.05, coords['nbl'][1]]

    coords_nbt = [coords['nbt'], (coords['nbt'][0], coords['nbt'][1]+0.75)]
    coords_nbt_text = [coords['nbt'][0]-0.05, coords['nbt'][1]]

    coords_nbr = [coords['nbr'], (coords['nbr'][0]+0.5, coords['nbr'][1]+0.5)]
    coords_nbr_text = [coords['nbr'][0]-0.05, coords['nbr'][1]]
    
    if df['Reroute-NBL'][i] in ('Prohibit NBL, reroute to NBU north of intersection',
                                'Prohibit NBL, reroute to EBU east of intersection',
                                'Displace NBL south of intersection'):
        pass
    else:
        # Draw the arrows and text red if conflicting flows above user threshold.
        if sbt_flow + nbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            left_arrow(coords_nbl[0], coords_nbl[1], kw_red, coords_nbl_text[0], coords_nbl_text[1], df['NBL'][i],'verticalalignment', 'top', 90, 'red')
        else:
            left_arrow(coords_nbl[0], coords_nbl[1], kw, coords_nbl_text[0], coords_nbl_text[1], df['NBL'][i],'verticalalignment', 'top', 90, 'black')
    if df['Reroute-NBT'][i] == 'Prohibit NBT, reroute to EBU east of intersection':
        pass
    else:
        if df['Reroute-SBL'][i] == 'No change' and nbt_flow + sbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            thru_arrow(coords_nbt[0], coords_nbt[1], kw_red, coords_nbt_text[0], coords_nbt_text[1], df['NBT'][i], 'verticalalignment','top', 90, 'red')
        else:
            thru_arrow(coords_nbt[0], coords_nbt[1], kw, coords_nbt_text[0], coords_nbt_text[1], df['NBT'][i], 'verticalalignment','top', 90, 'black')
    right_arrow(coords_nbr[0], coords_nbr[1], coords_nbr_text[0], coords_nbr_text[1], df['NBR'][i],'verticalalignment', 'top', 90)

#### Draw SB movements
    x_align_sb = x_align_nb * -1
    y_align_sb = y_align_nb * -1
    coords = {'sbl': (x_align_sb + 0.4, y_align_sb), 'sbt': (x_align_sb, y_align_sb),
              'sbr': (x_align_sb - 0.4, y_align_sb)}
    coords_sbl = [coords['sbl'], (coords['sbl'][0]+0.5, coords['sbl'][1]-0.5)]
    coords_sbl_text = [coords['sbl'][0]-0.05, coords['sbl'][1]+0.05]

    coords_sbt = [coords['sbt'], (coords['sbt'][0], coords['sbt'][1]-0.75)]
    coords_sbt_text = [coords['sbt'][0]-0.05, coords['sbt'][1]+0.05]

    coords_sbr = [coords['sbr'], (coords['sbr'][0]-0.5, coords['sbr'][1]-0.5)]
    coords_sbr_text = [coords['sbr'][0]-0.05, coords['sbr'][1]+0.05]
    
    if df['Reroute-SBL'][i] in ('Prohibit SBL, reroute to SBU south of intersection',
                                'Prohibit SBL, reroute to WBU west of intersection',
                                'Displace SBL north of intersection'):
        pass
    else:
        # Draw the arrows and text red if conflicting flows above user threshold.
        if nbt_flow + sbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            left_arrow(coords_sbl[0], coords_sbl[1], kw_red, coords_sbl_text[0], coords_sbl_text[1], df['SBL'][i],'verticalalignment', 'bottom', 90, 'red')
        else:
            left_arrow(coords_sbl[0], coords_sbl[1], kw, coords_sbl_text[0], coords_sbl_text[1], df['SBL'][i],'verticalalignment', 'bottom', 90, 'black')
    if df['Reroute-SBT'][i] == 'Prohibit SBT, reroute to WBU west of intersection':
        pass
    else:
        if df['Reroute-NBL'][i] == 'No change' and sbt_flow + nbl_flow / df['LT_UT Volume Factor'][i] > int(df['Max Sum Conf Flow Rates'][i]):
            thru_arrow(coords_sbt[0], coords_sbt[1], kw_red, coords_sbt_text[0], coords_sbt_text[1], df['SBT'][i],'verticalalignment', 'bottom', 90, 'red')
        else:
            thru_arrow(coords_sbt[0], coords_sbt[1], kw, coords_sbt_text[0], coords_sbt_text[1], df['SBT'][i],'verticalalignment', 'bottom', 90, 'black')
    right_arrow(coords_sbr[0], coords_sbr[1], coords_sbr_text[0], coords_sbr_text[1], df['SBR'][i], 'verticalalignment','bottom', 90)