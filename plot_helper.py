from matplotlib.pyplot import close
from pandas import options
from io import BytesIO
import win32clipboard

from HelperFunctions.Centerlines import centerlines
from HelperFunctions.DrawVolumesArrows_displacedlefts import draw_volume_arrows_displacedlefts
from HelperFunctions.DrawVolumesArrows_std import draw_volume_arrows_std
from HelperFunctions.DrawVolumesArrows_uturns import draw_volume_arrows_uturn
from HelperFunctions.FlaggedConflicts import flagged_conflicts
from HelperFunctions.LaneDiagram import lane_diagrams

# Suppress warnings for copying slices
options.mode.chained_assignment = None
from PIL import Image


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def plot_helper(self, df, save_yn, savelocation):

    kw = dict(arrowstyle="Simple,tail_width=0.3,head_width=3,head_length=8", color="k")
    kw_red = dict(arrowstyle="Simple,tail_width=0.3,head_width=3,head_length=8", color="r")

    i = 0

    # Run for how many plots are to be made
    while i < len(df['Scenario Name']):
        # Error for left turn ratio over 1.o
        if df['LT_UT Volume Factor'][i] > 1:
            self.messagebox.setText("The left turn volume factor ('LT_UT Volume Factor' in template) cannot be greater "
                                    "than 1.00. Please enter a factor less than 1.00.")
            self.messagebox.setStyleSheet("color: red;")
            close()
            return
        nbu_vol = 0
        sbu_vol = 0
        ebu_vol = 0
        wbu_vol = 0

        # Move and recalculate volumes
        if df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to EBU east of intersection':
            df['EBT'][i] += df['EBL'][i]
            ebu_vol += df['EBL'][i]
            df['WBR'][i] += df['EBL'][i]
            df['EBL'][i] = 0
        elif df['Reroute-EBL'][i] == 'Prohibit EBL, reroute to SBU south of intersection':
            df['EBR'][i] += df['EBL'][i]
            sbu_vol += df['EBL'][i]
            df['NBT'][i] += df['EBL'][i]
            df['EBL'][i] = 0
        elif df['Reroute-EBL'][i] == 'Displace EBL west of intersection':
            pass
        if df['Reroute-EBT'][i] == 'Prohibit EBT, reroute to SBU south of intersection':
            df['EBR'][i] += df['EBT'][i]
            sbu_vol += df['EBT'][i]
            df['NBR'][i] += df['EBT'][i]
            df['EBT'][i] = 0

        if df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to WBU west of intersection':
            df['WBT'][i] += df['WBL'][i]
            wbu_vol += df['WBL'][i]
            df['EBR'][i] += df['WBL'][i]
            df['WBL'][i] = 0
        elif df['Reroute-WBL'][i] == 'Prohibit WBL, reroute to NBU north of intersection':
            df['WBR'][i] += df['WBL'][i]
            nbu_vol += df['WBL'][i]
            df['SBT'][i] += df['WBL'][i]
            df['WBL'][i] = 0
        elif df['Reroute-WBL'][i] == 'Displace WBL east of intersection':
            pass
        if df['Reroute-WBT'][i] == 'Prohibit WBT, reroute to NBU north of intersection':
            df['WBR'][i] += df['WBT'][i]
            nbu_vol += df['WBT'][i]
            df['SBR'][i] += df['WBT'][i]
            df['WBT'][i] = 0

        if df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to NBU north of intersection':
            df['NBT'][i] += df['NBL'][i]
            nbu_vol += df['NBL'][i]
            df['SBR'][i] += df['NBL'][i]
            df['NBL'][i] = 0
        elif df['Reroute-NBL'][i] == 'Prohibit NBL, reroute to EBU east of intersection':
            df['NBR'][i] += df['NBL'][i]
            ebu_vol += df['NBL'][i]
            df['WBT'][i] += df['NBL'][i]
            df['NBL'][i] = 0
        elif df['Reroute-NBL'][i] == 'Displace NBL south of intersection':
            pass
        if df['Reroute-NBT'][i] == 'Prohibit NBT, reroute to EBU east of intersection':
            df['NBR'][i] += df['NBT'][i]
            ebu_vol += df['NBT'][i]
            df['WBR'][i] += df['NBT'][i]
            df['NBT'][i] = 0

        if df['Reroute-SBL'][i] == 'Prohibit SBL, reroute to SBU south of intersection':
            df['SBT'][i] += df['SBL'][i]
            sbu_vol += df['SBL'][i]
            df['NBR'][i] += df['SBL'][i]
            df['SBL'][i] = 0
        elif df['Reroute-SBL'][i] == 'Prohibit SBL, reroute to WBU west of intersection':
            df['SBR'][i] += df['SBL'][i]
            wbu_vol += df['SBL'][i]
            df['EBT'][i] += df['SBL'][i]
            df['SBL'][i] = 0
        elif df['Reroute-SBL'][i] == 'Displace SBL north of intersection':
            pass
        if df['Reroute-SBT'][i] == 'Prohibit SBT, reroute to WBU west of intersection':
            df['SBR'][i] += df['SBT'][i]
            wbu_vol += df['SBT'][i]
            df['EBR'][i] += df['SBT'][i]
            df['SBT'][i] = 0

        ebvol_entering = df['EBL'][i] + df['EBT'][i] + df['EBR'][i] - wbu_vol
        wbvol_entering = df['WBL'][i] + df['WBT'][i] + df['WBR'][i] - ebu_vol
        nbvol_entering = df['NBL'][i] + df['NBT'][i] + df['NBR'][i] - sbu_vol
        sbvol_entering = df['SBL'][i] + df['SBT'][i] + df['SBR'][i] - nbu_vol

        ebvol_exiting = df['NBR'][i] + df['EBT'][i] + df['SBL'][i]
        wbvol_exiting = df['SBR'][i] + df['WBT'][i] + df['NBL'][i]
        nbvol_exiting = df['WBR'][i] + df['NBT'][i] + df['EBL'][i]
        sbvol_exiting = df['EBR'][i] + df['SBT'][i] + df['WBL'][i]

        # Calculate the flow
        ebt_flow = int(df['EBT'][i] / df['Max Lanes-EBT'][i])
        wbt_flow = int(df['WBT'][i] / df['Max Lanes-WBT'][i])
        nbt_flow = int(df['NBT'][i] / df['Max Lanes-NBT'][i])
        sbt_flow = int(df['SBT'][i] / df['Max Lanes-SBT'][i])
        ebl_flow = int(df['EBL'][i] / df['Max Lanes-EBL'][i])
        wbl_flow = int(df['WBL'][i] / df['Max Lanes-WBL'][i])
        nbl_flow = int(df['NBL'][i] / df['Max Lanes-NBL'][i])
        sbl_flow = int(df['SBL'][i] / df['Max Lanes-SBL'][i])
        ebu_flow = int(ebu_vol / df['Max Lanes-EBU'][i])
        wbu_flow = int(wbu_vol / df['Max Lanes-WBU'][i])
        nbu_flow = int(nbu_vol / df['Max Lanes-NBU'][i])
        sbu_flow = int(sbu_vol / df['Max Lanes-SBU'][i])

        ebentering_flow = int(ebvol_entering / df['Max Lanes-EBT_Uturn'][i])
        wbentering_flow = int(wbvol_entering / df['Max Lanes-WBT_Uturn'][i])
        nbentering_flow = int(nbvol_entering / df['Max Lanes-NBT_Uturn'][i])
        sbentering_flow = int(sbvol_entering / df['Max Lanes-SBT_Uturn'][i])

        ebexiting_flow = int(ebvol_exiting / df['Max Lanes-EBT'][i])
        wbexiting_flow = int(wbvol_exiting / df['Max Lanes-WBT'][i])
        nbexiting_flow = int(nbvol_exiting / df['Max Lanes-NBT'][i])
        sbexiting_flow = int(sbvol_exiting / df['Max Lanes-SBT'][i])

        # Set up plots
        self.canvas.axes.cla()
        self.canvas.axes.set_xlim(xmin=-7, xmax=7)
        self.canvas.axes.set_ylim(ymin=-7, ymax=7)
        self.canvas.axes.xaxis.set_ticks([])
        self.canvas.axes.yaxis.set_ticks([])
        self.canvas.axes.spines['top'].set_visible(False)
        self.canvas.axes.spines['right'].set_visible(False)
        self.canvas.axes.spines['bottom'].set_visible(False)
        self.canvas.axes.spines['left'].set_visible(False)

        # Add text for street names and headings for conflicts
        self.canvas.axes.text(0, 7, 'Scenario Name', horizontalalignment='center', fontsize=9, weight='bold')
        self.canvas.axes.text(0, 6.7, df['Scenario Name'][i], horizontalalignment='center', fontsize=8)
        self.canvas.axes.text(-2.5, 1.9, df['East West Street Name'][i], horizontalalignment='right', fontsize=8)
        self.canvas.axes.text(1.9, -2.5, df['North-South Street Name'][i], verticalalignment='top', rotation=-90,fontsize=8)
        self.canvas.axes.text(-7, -3.7, 'Conflicts: Main Intersection', horizontalalignment='left', fontsize=10)
        self.canvas.axes.text(-7, -5.5, 'Conflicts: U-turns', horizontalalignment='left', fontsize=10)
        self.canvas.axes.text(7, -5.5, 'Conflicts: Displaced Lefts', horizontalalignment='right', fontsize=10)

        # Draw lane diagram
        lane_diagrams(self, df, i, kw)

        # Draw road centerlines
        centerlines(self)

        # Draw arrows, standard
        draw_volume_arrows_std(self, df, i, ebt_flow, wbt_flow, nbt_flow, sbt_flow, ebl_flow, wbl_flow, nbl_flow,
                               sbl_flow, kw, kw_red)

        # Draw arrows, uturns
        draw_volume_arrows_uturn(self, df, i,
                                 ebentering_flow, wbentering_flow, nbentering_flow, sbentering_flow,
                                 ebvol_entering, wbvol_entering, nbvol_entering, sbvol_entering,
                                 ebu_flow, wbu_flow, nbu_flow, sbu_flow,
                                 ebu_vol, wbu_vol, nbu_vol, sbu_vol,
                                 kw, kw_red)

        # Draw arrows, displaced lefts
        draw_volume_arrows_displacedlefts(self, df, i,
                                          ebexiting_flow, wbexiting_flow, nbexiting_flow, sbexiting_flow,
                                          ebvol_exiting, wbvol_exiting, nbvol_exiting, sbvol_exiting,
                                          ebl_flow, wbl_flow, nbl_flow, sbl_flow,
                                          kw, kw_red)

        # Add text for flagged conflicts
        flagged_conflicts(self, df, i,
                          ebexiting_flow, wbexiting_flow, nbexiting_flow, sbexiting_flow,
                          ebt_flow, wbt_flow, nbt_flow, sbt_flow,
                          ebl_flow, wbl_flow, nbl_flow, sbl_flow,
                          ebu_flow, wbu_flow, nbu_flow, sbu_flow,
                          ebentering_flow, wbentering_flow, nbentering_flow, sbentering_flow)

        if save_yn == "Yes":
            if savelocation == '':
                self.messagebox.setText("Please select a save location (Step 7).")
                self.messagebox.setStyleSheet("color: red;")
                return
            else:
                if len(df['Scenario Name']) == 1:
                    filepath = savelocation + '/saved_figure.png'
                    # Save plot to path
                    self.canvas.print_figure(filepath)

                    #Copy plot to clipboard
                    image = Image.open(filepath)
                    output = BytesIO()
                    image.convert("RGB").save(output, "BMP")
                    data = output.getvalue()[14:]
                    output.close()
                    send_to_clipboard(win32clipboard.CF_DIB, data)
                else:
                    self.canvas.print_figure(savelocation + '/' + df['Scenario Name'][i] + '.png')

        self.canvas.draw()
        self.messagebox.setText("Plots created!")
        self.messagebox.setStyleSheet("color: green;")


        i += 1
