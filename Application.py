import matplotlib
import sys
import time

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from HelperFunctions.Application_helperfunctions import window_defaults
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QLabel, QProgressBar, QFileDialog
from PyQt5.QtGui import QPixmap, QIntValidator, QDesktopServices
from PyQt5.QtCore import QUrl
from decimal import Decimal
from pandas import DataFrame, read_excel
from plot_helper import plot_helper
from matplotlib.pyplot import close
from os import makedirs
import warnings

warnings.filterwarnings("ignore")

# Global variables for Module 1 class
inputfilepath = ''
savelocation = ''

appname = 'Intersection Concept Development App'
icon_path = 'PNG_files/icon.ico'


class Master():
    def backto_mainmenu(self):
        self.close()
        close()
        HomePage().exec_()

    # Function for the hyperlink
    def link(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))

    # Set up progress bar
    def setup_prog_bar(self):
        # Progress bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(250, 310, 250, 20)
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)

    # Run progress bar
    def run_prog_bar(self):
        seconds = 3
        self.completed = 0
        self.progress.setFormat('0%')
        self.progress.setValue(self.completed)
        while self.completed < 100:
            self.progress.setFormat(str(self.completed) + '%')
            self.progress.setValue(self.completed)
            self.completed += 100

            time.sleep(1)
            if seconds == 2:
                self.progress.setFormat('Program running!')
                self.progress.setValue(self.completed)
            else:
                self.progress.setFormat(str(self.completed) + '%')
                self.progress.setValue(self.completed)

            seconds -= 1

    def reset_prog_bar(self):
        # Reset progress bar
        self.completed = 0
        self.progress.setValue(self.completed)
        self.progress.setFormat('0%')


# Homepage
class HomePage(QDialog, Master):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi('UI_files/HomePage.ui', self)

        # Apply defaults
        window_defaults(self, appname, icon_path)

        label = QLabel(self)
        pixmap = QPixmap('PNG_files/HDRlogo.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        label.move(375, 260)

        # Run functions when buttons clicked
        self.overview_button.clicked.connect(self.ApplicationOverview)
        self.singleplot_button.clicked.connect(self.SinglePlot)
        self.batchplot_button.clicked.connect(self.BatchPlot)

    def ApplicationOverview(self):
        self.close()
        ApplicationOverview().exec_()

    def SinglePlot(self):
        self.close()
        SinglePlot().exec_()

    def BatchPlot(self):
        self.close()
        BatchPlot().exec_()


# Application Overview Module
class ApplicationOverview(QDialog, Master):
    def __init__(self):
        super(ApplicationOverview, self).__init__()
        loadUi('UI_files/ApplicationOverview.ui', self)

        # Apply defaults
        window_defaults(self, appname, icon_path)

        # Main menu
        self.mainmenu.clicked.connect(self.backto_mainmenu)

# For embedding mpl figure in PyQT UI
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)

# Single Plot Module
class SinglePlot(QDialog, Master):
    def __init__(self):
        super(SinglePlot, self).__init__()
        self.ui = uic.loadUi('UI_files/SinglePlot.ui', self)

        # Apply defaults
        window_defaults(self, appname, icon_path)

        self.canvas = MplCanvas(self, width=7, height=7, dpi=100)
        self.canvas.axes.xaxis.set_ticks([])
        self.canvas.axes.yaxis.set_ticks([])
        self.ui.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        self.reference_plot = None

        # Batch plot Excel template link
        self.label_template.linkActivated.connect(self.link)
        self.label_template.setText(
            '<a href="https://teams.microsoft.com/_#/files/General?threadId=19%3A8c6de16249154ae19a67a4ab643f3b61%40thread.skype&ctx=channel&context=Intersection%2520Concept%2520Development%2520App&rootfolder=%252Fteams%252FConceptDevelopmentPracticeGroup%252FShared%2520Documents%252FGeneral%252FIntersection%2520Concept%2520Development%2520App">here.</a>')

        # Restrict volume entries to integers, set default values
        volume_entries = [self.ebl_vol, self.ebt_vol, self.ebr_vol,
                          self.wbl_vol, self.wbt_vol, self.wbr_vol,
                          self.nbl_vol, self.nbt_vol, self.nbr_vol,
                          self.sbl_vol, self.sbt_vol, self.sbr_vol,
                          self.ebl_vol_pm, self.ebt_vol_pm, self.ebr_vol_pm,
                          self.wbl_vol_pm, self.wbt_vol_pm, self.wbr_vol_pm,
                          self.nbl_vol_pm, self.nbt_vol_pm, self.nbr_vol_pm,
                          self.sbl_vol_pm, self.sbt_vol_pm, self.sbr_vol_pm,
                          self.row_select]

        for v in volume_entries:
            v.setValidator(QIntValidator())
            v.setText('1')

        lane_entries = [self.ebt_lanes, self.wbt_lanes, self.nbt_lanes, self.sbt_lanes,
                        self.ebl_lanes, self.wbl_lanes, self.nbl_lanes, self.sbl_lanes,
                        self.ebt_lanes_u, self.wbt_lanes_u, self.nbt_lanes_u, self.sbt_lanes_u,
                        self.ebu_lanes, self.wbu_lanes, self.nbu_lanes, self.sbu_lanes]

        for v in lane_entries:
            v.setValidator(QIntValidator())
            v.setText('1')

        self.scenario_name.setMaxLength(40)
        self.ew_street.setMaxLength(15)
        self.ns_street.setMaxLength(15)
        self.max_conflict_flow.setValidator(QIntValidator())
        self.leftturnflow_box.setInputMask('0.00')

        self.max_conflict_flow.setText("1500")
        self.leftturnflow_box.setText('0.80')

        self.messagebox.setReadOnly(True)
        self.save_namebox.setReadOnly(True)

        # Attaching functions to the push buttons
        self.showplot.clicked.connect(self.update_plot)
        self.showplot.setDefault(True)
        self.savepathbox.clicked.connect(self.selectsavelocation)
        self.mainmenu.clicked.connect(self.backto_mainmenu)
        self.reset_button.clicked.connect(self.reset)
        self.uploadfile.clicked.connect(self.selectinputfile)
        self.importinputs_box.clicked.connect(self.importinputs)

    # Reset
    def reset(self):
        close()
        self.close()
        SinglePlot().exec_()

    # User selects save location for plot
    def selectsavelocation(self):
        global savelocation
        self.messagebox.setText('')
        savelocation = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
        self.save_namebox.setText(savelocation)

    # User uploads input file
    def selectinputfile(self):
        global inputfilepath
        self.messagebox.setText('')
        filename = QFileDialog.getOpenFileName()
        inputfilepath = filename[0]
        self.filenamebox.setText(inputfilepath)

    # User uploads input file
    def importinputs(self):
        try:
            df = read_excel(inputfilepath)
        except Exception:
            self.messagebox.setText("The uploaded file (Step 1) must be the standard Excel template. Please see the "
                                    "Sharepoint site for the Excel template.")
            self.messagebox.setStyleSheet("color: red;")
            return
        try:
            row_selection = int(self.row_select.text())
        except Exception:
            self.messagebox.setText("Enter a row number to import.")
            self.messagebox.setStyleSheet("color: red;")
            return

        if row_selection < 1:
            self.messagebox.setText("Enter a row number of 1 or greater.")
            self.messagebox.setStyleSheet("color: red;")
            return
        elif row_selection > len(df):
            self.messagebox.setText("The row number entered exceeds the number of rows in the input file.")
            self.messagebox.setStyleSheet("color: red;")
            return

        dict_input = {self.ebl_vol: 'EBL', self.ebt_vol: 'EBT', self.ebr_vol: 'EBR',
                      self.wbl_vol: 'WBL', self.wbt_vol: 'WBT', self.wbr_vol: 'WBR',
                      self.nbl_vol: 'NBL', self.nbt_vol: 'NBT', self.nbr_vol: 'NBR',
                      self.sbl_vol: 'SBL', self.sbt_vol: 'SBT', self.sbr_vol: 'SBR',
                      self.ebt_lanes: 'Max Lanes-EBT', self.wbt_lanes: 'Max Lanes-WBT', self.nbt_lanes: 'Max Lanes-NBT',
                      self.sbt_lanes: 'Max Lanes-SBT',
                      self.ebl_lanes: 'Max Lanes-EBL', self.wbl_lanes: 'Max Lanes-WBL', self.nbl_lanes: 'Max Lanes-NBL',
                      self.sbl_lanes: 'Max Lanes-SBL',
                      self.ebt_lanes_u: 'Max Lanes-EBT_Uturn', self.wbt_lanes_u: 'Max Lanes-WBT_Uturn', self.nbt_lanes_u: 'Max Lanes-NBT_Uturn',
                      self.sbt_lanes_u: 'Max Lanes-SBT_Uturn',
                      self.ebu_lanes: 'Max Lanes-EBU', self.wbu_lanes: 'Max Lanes-WBU', self.nbu_lanes: 'Max Lanes-NBU',
                      self.sbu_lanes: 'Max Lanes-SBU'}

        for k, v in dict_input.items():
            k.setText(str(df[v][row_selection-1]))
        self.ew_street.setText(str(df['East West Street Name'][row_selection-1]))
        self.ns_street.setText(str(df['North-South Street Name'][row_selection - 1]))

        self.ebl_reroute.setCurrentText(df['Reroute-EBL'][row_selection - 1])
        self.ebt_reroute.setCurrentText(df['Reroute-EBT'][row_selection - 1])
        self.wbl_reroute.setCurrentText(df['Reroute-WBL'][row_selection - 1])
        self.wbt_reroute.setCurrentText(df['Reroute-WBT'][row_selection - 1])
        self.nbl_reroute.setCurrentText(df['Reroute-NBL'][row_selection - 1])
        self.nbt_reroute.setCurrentText(df['Reroute-NBT'][row_selection - 1])
        self.sbl_reroute.setCurrentText(df['Reroute-SBL'][row_selection - 1])
        self.sbt_reroute.setCurrentText(df['Reroute-SBT'][row_selection - 1])

        self.max_conflict_flow.setText(str(df['Max Sum Conf Flow Rates'][row_selection - 1]))
        self.leftturnflow_box.setText(str(df['LT_UT Volume Factor'][row_selection - 1]))

    def update_plot(self):
        self.messagebox.setText("")
        self.canvas.axes.cla()

        # Step 1 vals
        name_scenario = self.scenario_name.text()
        ew_street = self.ew_street.text()
        ns_street = self.ns_street.text()

        # Step 7 val
        am_pm = self.am_pm_box.currentText()

        # Step 8 value
        save_yn = self.save_yn.currentText()
        save_yn_inputs = self.save_yn_inputs.currentText()

        # Get volumes and lanes from UI, store in dict
        if am_pm == "AM":
            try:
                vol_dict = {'ebl_vol': int(self.ebl_vol.text()), 'ebt_vol': int(self.ebt_vol.text()),
                            'ebr_vol': int(self.ebr_vol.text()),
                            'wbl_vol': int(self.wbl_vol.text()), 'wbt_vol': int(self.wbt_vol.text()),
                            'wbr_vol': int(self.wbr_vol.text()),
                            'nbl_vol': int(self.nbl_vol.text()), 'nbt_vol': int(self.nbt_vol.text()),
                            'nbr_vol': int(self.nbr_vol.text()),
                            'sbl_vol': int(self.sbl_vol.text()), 'sbt_vol': int(self.sbt_vol.text()),
                            'sbr_vol': int(self.sbr_vol.text())}
            except ValueError:
                self.messagebox.setText("Missing AM volumes! Please enter a number for every entry.")
                self.messagebox.setStyleSheet("color: red;")
                close()
                return
            else:
                pass
        elif am_pm == "PM":
            try:
                vol_dict_pm = {'ebl_vol_pm': int(self.ebl_vol_pm.text()), 'ebt_vol_pm': int(self.ebt_vol_pm.text()),
                               'ebr_vol_pm': int(self.ebr_vol_pm.text()),
                               'wbl_vol_pm': int(self.wbl_vol_pm.text()), 'wbt_vol_pm': int(self.wbt_vol_pm.text()),
                               'wbr_vol_pm': int(self.wbr_vol_pm.text()),
                               'nbl_vol_pm': int(self.nbl_vol_pm.text()), 'nbt_vol_pm': int(self.nbt_vol_pm.text()),
                               'nbr_vol_pm': int(self.nbr_vol_pm.text()),
                               'sbl_vol_pm': int(self.sbl_vol_pm.text()), 'sbt_vol_pm': int(self.sbt_vol_pm.text()),
                               'sbr_vol_pm': int(self.sbr_vol_pm.text())}
            except ValueError:
                self.messagebox.setText("Missing PM volumes! Please enter a number for every entry.")
                self.messagebox.setStyleSheet("color: red;")
                close()
                return
            else:
                pass
        # Get number of lanes, conflict flow rate, and lt ratio from UI
        try:
            lanes_dict = {'ebt_lanes': int(self.ebt_lanes.text()), 'wbt_lanes': int(self.wbt_lanes.text()),
                          'nbt_lanes': int(self.nbt_lanes.text()), 'sbt_lanes': int(self.sbt_lanes.text()),
                          'ebl_lanes': int(self.ebl_lanes.text()), 'wbl_lanes': int(self.wbl_lanes.text()),
                          'nbl_lanes': int(self.nbl_lanes.text()), 'sbl_lanes': int(self.sbl_lanes.text()),
                          'ebt_lanes_u': int(self.ebt_lanes_u.text()), 'wbt_lanes_u': int(self.wbt_lanes_u.text()),
                          'nbt_lanes_u': int(self.nbt_lanes_u.text()), 'sbt_lanes_u': int(self.sbt_lanes_u.text()),
                          'ebu_lanes': int(self.ebu_lanes.text()), 'wbu_lanes': int(self.wbu_lanes.text()),
                          'nbu_lanes': int(self.nbu_lanes.text()), 'sbu_lanes': int(self.sbu_lanes.text())}
            conflict_flow = self.max_conflict_flow.text()
            conflict_flow = int(conflict_flow)
            lt_ratio = self.leftturnflow_box.text()
            lt_ratio = Decimal(lt_ratio.strip(' "'))
        except Exception:
            self.messagebox.setText("Missing lanes, conflict flow rate, and/or left turn ratio! "
                                    "Please enter a number for every entry.")
            self.messagebox.setStyleSheet("color: red;")
            close()
            return
        else:
            pass

        for v in lanes_dict.values():
            if v < 1:
                self.messagebox.setText("Number of lanes cannot be less than one (Step 4).")
                self.messagebox.setStyleSheet("color: red;")
                close()
                return

        # Check that vols are not less than zero
        if am_pm == "AM":
            for v in vol_dict.values():
                if v < 0:
                    self.messagebox.setText(
                        "Volumes cannot be less than zero! Please enter a volume of zero or greater.")
                    self.messagebox.setStyleSheet("color: red;")
                    return
        elif am_pm == "PM":
            for v in vol_dict_pm.values():
                if v < 0:
                    self.messagebox.setText(
                        "Volumes cannot be less than zero! Please enter a volume of zero or greater.")
                    self.messagebox.setStyleSheet("color: red;")
                    return

        # Get reroutes from UI and store in dictionary
        reroute_dict = {'ebl_reroute': self.ebl_reroute.currentText(), 'ebt_reroute': self.ebt_reroute.currentText(),
                        'wbl_reroute': self.wbl_reroute.currentText(), 'wbt_reroute': self.wbt_reroute.currentText(),
                        'nbl_reroute': self.nbl_reroute.currentText(), 'nbt_reroute': self.nbt_reroute.currentText(),
                        'sbl_reroute': self.sbl_reroute.currentText(), 'sbt_reroute': self.sbt_reroute.currentText()}

        # Compile all data for data frame
        data_values = [name_scenario, ns_street, ew_street]
        if am_pm == "AM":
            for v in vol_dict.values():
                data_values.append(v)
        elif am_pm == "PM":
            for v in vol_dict_pm.values():
                data_values.append(v)
        for v in reroute_dict.values():
            data_values.append(v)
        for v in lanes_dict.values():
            data_values.append(v)
        data_values.append(int(conflict_flow))
        data_values.append(lt_ratio)

        # Create data frame
        col_headers = ['Scenario Name', 'North-South Street Name', 'East West Street Name',
                       'EBL', 'EBT', 'EBR', 'WBL', 'WBT', 'WBR',
                       'NBL', 'NBT', 'NBR', 'SBL', 'SBT', 'SBR',
                       'Reroute-EBL', 'Reroute-EBT', 'Reroute-WBL', 'Reroute-WBT',
                       'Reroute-NBL', 'Reroute-NBT', 'Reroute-SBL', 'Reroute-SBT',
                       'Max Lanes-EBT', 'Max Lanes-WBT', 'Max Lanes-NBT', 'Max Lanes-SBT',
                       'Max Lanes-EBL', 'Max Lanes-WBL', 'Max Lanes-NBL', 'Max Lanes-SBL',
                       'Max Lanes-EBT_Uturn', 'Max Lanes-WBT_Uturn', 'Max Lanes-NBT_Uturn', 'Max Lanes-SBT_Uturn',
                       'Max Lanes-EBU', 'Max Lanes-WBU', 'Max Lanes-NBU', 'Max Lanes-SBU',
                       'Max Sum Conf Flow Rates', 'LT_UT Volume Factor']

        single_plot_df = DataFrame([data_values], columns=col_headers)

        # Save inputs
        if save_yn_inputs == "Yes":
            if savelocation == '':
                self.messagebox.setText("Please select a save location (Step 7).")
                self.messagebox.setStyleSheet("color: red;")
                return
            else:
                # Create excel
                outputname = savelocation + '\\' + 'saved_inputs.xlsx'
                writer = (outputname)
                single_plot_df.to_excel(writer, index=False)

        plot_helper(self, single_plot_df, save_yn, savelocation)

# Batch Plot Module
class BatchPlot(QDialog, Master):
    def __init__(self):
        super(BatchPlot, self).__init__()
        self.ui = uic.loadUi('UI_files/BatchPlot.ui', self)

        # Apply defaults
        window_defaults(self, appname, icon_path)

        # Set up canvas
        self.canvas = MplCanvas(self, width=7, height=7, dpi=100)
        self.canvas.axes.xaxis.set_ticks([])
        self.canvas.axes.yaxis.set_ticks([])
        self.ui.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)
        self.reference_plot = None

        self.row_select.setValidator(QIntValidator())
        self.row_select.setText('1')

        # Batch plot Excel template link
        self.label.linkActivated.connect(self.link)
        self.label.setText(
            '<a href="https://teams.microsoft.com/_#/files/General?threadId=19%3A8c6de16249154ae19a67a4ab643f3b61%40thread.skype&ctx=channel&context=Intersection%2520Concept%2520Development%2520App&rootfolder=%252Fteams%252FConceptDevelopmentPracticeGroup%252FShared%2520Documents%252FGeneral%252FIntersection%2520Concept%2520Development%2520App">here.</a>')

        self.messagebox.setReadOnly(True)
        self.filenamebox.setReadOnly(True)
        self.filenamebox_2.setReadOnly(True)

        # Attaching functions to the push buttons
        self.mainmenu.clicked.connect(self.backto_mainmenu)
        self.uploadfile.clicked.connect(self.selectinputfile)
        self.savepathbox.clicked.connect(self.selectsavelocation)
        self.createplotbox.clicked.connect(self.runapp)
        self.createplotbox.setDefault(True)

        # Set up progress bar
        self.setup_prog_bar()

    # User selects excel file
    def selectinputfile(self):
        global inputfilepath
        self.messagebox.setText('')
        filename = QFileDialog.getOpenFileName()
        inputfilepath = filename[0]
        self.filenamebox.setText(inputfilepath)

    # User selects save location for plots
    def selectsavelocation(self):
        global savelocation
        self.messagebox.setText('')
        savelocation = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
        self.filenamebox_2.setText(savelocation)

    # User clicks "Create Plots"
    def runapp(self):
        self.messagebox.setText('')
        self.canvas.axes.cla()

        row_show = int(self.row_select.text())
        foldername = self.savefoldername.text()

        # Exception for no input file selected
        if inputfilepath == '':
            self.messagebox.setText('No file selected! Please upload a .csv file to create diagrams.')
            self.messagebox.setStyleSheet("color: red;")
            return

        # Exception for blank save location
        if savelocation == '':
            self.messagebox.setText('No save location selected! Please select a location to save the plots.')
            self.messagebox.setStyleSheet("color: red;")
            return

        # Exception for folder already exists
        if foldername != '':
            try:
                makedirs(savelocation + "/" + foldername)
            except Exception:
                self.messagebox.setText('Directory already exists or the folder name is not allowed! '
                                        'Please choose a different folder name.')
                self.messagebox.setStyleSheet("color: red;")
                return
            else:
                pass

        # Exception for wrong template file
        try:
            df = read_excel(inputfilepath)
        except Exception:
            self.messagebox.setText("The uploaded file (Step 1) must be the standard Excel template. Please see the "
                                    "Sharepoint site for the Excel template.")
            self.messagebox.setStyleSheet("color: red;")
            return

        # Run progress bar
        self.run_prog_bar()

        # Create plots
        save_yn = "Yes"
        savelocation1 = savelocation + '/' + foldername
        # try:
        plot_helper(self, df, save_yn, savelocation1)
        # except Exception:
        #     self.messagebox.setText("The uploaded file (Step 1) must be the standard Excel template. Please see the "
        #                             "Sharepoint site for the Excel template.")
        #     self.messagebox.setStyleSheet("color: red;")
        #     return
        save_yn = "No"
        plot_helper(self, df.iloc[0:row_show], save_yn, savelocation)
        # Reset progress bar
        self.reset_prog_bar()

        self.messagebox.setText('Diagrams created!')
        self.messagebox.setStyleSheet("color: green;")

app = QtWidgets.QApplication(sys.argv)
mainWindow = HomePage()
mainWindow.show()
sys.exit(app.exec_())
