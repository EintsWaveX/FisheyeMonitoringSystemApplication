# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpinBox, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModal)
        Widget.setEnabled(True)
        Widget.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setCursor(QCursor(Qt.ArrowCursor))
        Widget.setMouseTracking(False)
        Widget.setContextMenuPolicy(Qt.NoContextMenu)
        Widget.setAcceptDrops(False)
#if QT_CONFIG(tooltip)
        Widget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Widget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Widget.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        Widget.setLayoutDirection(Qt.LeftToRight)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 79)\n"
"}")
        self.MainFrame = QFrame(Widget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(20, 20, 1240, 660))
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.MainFrame.setFrameShape(QFrame.Box)
        self.MainFrame.setFrameShadow(QFrame.Plain)
        self.MainApplicationTitle = QLabel(self.MainFrame)
        self.MainApplicationTitle.setObjectName(u"MainApplicationTitle")
        self.MainApplicationTitle.setGeometry(QRect(20, 2, 1200, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display"])
        font.setPointSize(24)
        self.MainApplicationTitle.setFont(font)
        self.MainApplicationTitle.setScaledContents(False)
        self.MainApplicationTitle.setWordWrap(False)
        self.LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator = QFrame(self.MainFrame)
        self.LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator.setObjectName(u"LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator")
        self.LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator.setGeometry(QRect(20, 50, 1201, 16))
        self.LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator.setFrameShape(QFrame.HLine)
        self.LineXAxisMainApplicationTitleAndButtonsOfParametersSeparator.setFrameShadow(QFrame.Sunken)
        self.ImageProcessingButton = QPushButton(self.MainFrame)
        self.ImageProcessingButton.setObjectName(u"ImageProcessingButton")
        self.ImageProcessingButton.setGeometry(QRect(20, 70, 80, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Display"])
        font1.setBold(True)
        font1.setItalic(False)
        self.ImageProcessingButton.setFont(font1)
        self.ImageProcessingButton.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(220, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(185, 85, 0);\n"
"}")
        self.ImageProcessingButton.setCheckable(False)
        self.ImageProcessingButton.setAutoDefault(False)
        self.ImageProcessingButton.setFlat(False)
        self.VideoProcessingButton = QPushButton(self.MainFrame)
        self.VideoProcessingButton.setObjectName(u"VideoProcessingButton")
        self.VideoProcessingButton.setGeometry(QRect(105, 70, 80, 30))
        self.VideoProcessingButton.setFont(font1)
        self.VideoProcessingButton.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(220, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(185, 85, 0);\n"
"}")
        self.VideoProcessingButton.setCheckable(False)
        self.VideoProcessingButton.setAutoDefault(False)
        self.VideoProcessingButton.setFlat(False)
        self.StreamingButton = QPushButton(self.MainFrame)
        self.StreamingButton.setObjectName(u"StreamingButton")
        self.StreamingButton.setGeometry(QRect(190, 70, 110, 30))
        self.StreamingButton.setFont(font1)
        self.StreamingButton.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(220, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(185, 170, 0);\n"
"}")
        self.StreamingButton.setCheckable(False)
        self.StreamingButton.setAutoDefault(False)
        self.StreamingButton.setFlat(False)
        self.RecordingButton = QPushButton(self.MainFrame)
        self.RecordingButton.setObjectName(u"RecordingButton")
        self.RecordingButton.setGeometry(QRect(305, 70, 110, 30))
        self.RecordingButton.setFont(font1)
        self.RecordingButton.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(220, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(185, 170, 0);\n"
"}")
        self.RecordingButton.setCheckable(False)
        self.RecordingButton.setAutoDefault(False)
        self.RecordingButton.setFlat(False)
        self.LineXAxisIVSRAndSPSeparator = QFrame(self.MainFrame)
        self.LineXAxisIVSRAndSPSeparator.setObjectName(u"LineXAxisIVSRAndSPSeparator")
        self.LineXAxisIVSRAndSPSeparator.setGeometry(QRect(421, 65, 5, 40))
        self.LineXAxisIVSRAndSPSeparator.setFrameShape(QFrame.VLine)
        self.LineXAxisIVSRAndSPSeparator.setFrameShadow(QFrame.Sunken)
        self.SaveParametersButton = QPushButton(self.MainFrame)
        self.SaveParametersButton.setObjectName(u"SaveParametersButton")
        self.SaveParametersButton.setGeometry(QRect(431, 70, 160, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.SaveParametersButton.setFont(font2)
        self.SaveParametersButton.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 220, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 185, 127);\n"
"}")
        self.SaveParametersButton.setCheckable(False)
        self.SaveParametersButton.setAutoRepeat(True)
        self.SaveParametersButton.setAutoDefault(False)
        self.SaveParametersButton.setFlat(False)
        self.LineXAxisButtonsOfParametersSeparator = QFrame(self.MainFrame)
        self.LineXAxisButtonsOfParametersSeparator.setObjectName(u"LineXAxisButtonsOfParametersSeparator")
        self.LineXAxisButtonsOfParametersSeparator.setGeometry(QRect(20, 105, 1201, 16))
        self.LineXAxisButtonsOfParametersSeparator.setFrameShape(QFrame.HLine)
        self.LineXAxisButtonsOfParametersSeparator.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.MainFrame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 120, 1201, 331))
        self.CameraFieldViewLayout = QGridLayout(self.gridLayoutWidget)
        self.CameraFieldViewLayout.setObjectName(u"CameraFieldViewLayout")
        self.CameraFieldViewLayout.setContentsMargins(0, 0, 0, 0)
        self.FCFV_OriginalView = QGraphicsView(self.gridLayoutWidget)
        self.FCFV_OriginalView.setObjectName(u"FCFV_OriginalView")
        self.FCFV_OriginalView.setFrameShape(QFrame.Box)
        self.FCFV_OriginalView.setFrameShadow(QFrame.Plain)

        self.CameraFieldViewLayout.addWidget(self.FCFV_OriginalView, 1, 0, 1, 1)

        self.FCFV_SecondZoneView = QGraphicsView(self.gridLayoutWidget)
        self.FCFV_SecondZoneView.setObjectName(u"FCFV_SecondZoneView")
        self.FCFV_SecondZoneView.setFrameShape(QFrame.Box)
        self.FCFV_SecondZoneView.setFrameShadow(QFrame.Plain)

        self.CameraFieldViewLayout.addWidget(self.FCFV_SecondZoneView, 1, 2, 1, 1)

        self.NormalFisheyeCameraFieldView_FirstZoneLabel = QLabel(self.gridLayoutWidget)
        self.NormalFisheyeCameraFieldView_FirstZoneLabel.setObjectName(u"NormalFisheyeCameraFieldView_FirstZoneLabel")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Display"])
        font3.setPointSize(11)
        self.NormalFisheyeCameraFieldView_FirstZoneLabel.setFont(font3)
        self.NormalFisheyeCameraFieldView_FirstZoneLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(150, 85, 255);\n"
"}")
        self.NormalFisheyeCameraFieldView_FirstZoneLabel.setAlignment(Qt.AlignCenter)

        self.CameraFieldViewLayout.addWidget(self.NormalFisheyeCameraFieldView_FirstZoneLabel, 0, 1, 1, 1)

        self.NormalFisheyeCameraFieldView_SecondZoneLabel = QLabel(self.gridLayoutWidget)
        self.NormalFisheyeCameraFieldView_SecondZoneLabel.setObjectName(u"NormalFisheyeCameraFieldView_SecondZoneLabel")
        self.NormalFisheyeCameraFieldView_SecondZoneLabel.setFont(font3)
        self.NormalFisheyeCameraFieldView_SecondZoneLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(150, 85, 255);\n"
"}")
        self.NormalFisheyeCameraFieldView_SecondZoneLabel.setAlignment(Qt.AlignCenter)

        self.CameraFieldViewLayout.addWidget(self.NormalFisheyeCameraFieldView_SecondZoneLabel, 0, 2, 1, 1)

        self.NormalFisheyeCameraFieldView_OriginalLabel = QLabel(self.gridLayoutWidget)
        self.NormalFisheyeCameraFieldView_OriginalLabel.setObjectName(u"NormalFisheyeCameraFieldView_OriginalLabel")
        self.NormalFisheyeCameraFieldView_OriginalLabel.setFont(font3)
        self.NormalFisheyeCameraFieldView_OriginalLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.NormalFisheyeCameraFieldView_OriginalLabel.setFrameShape(QFrame.NoFrame)
        self.NormalFisheyeCameraFieldView_OriginalLabel.setFrameShadow(QFrame.Plain)
        self.NormalFisheyeCameraFieldView_OriginalLabel.setAlignment(Qt.AlignCenter)

        self.CameraFieldViewLayout.addWidget(self.NormalFisheyeCameraFieldView_OriginalLabel, 0, 0, 1, 1)

        self.FCFV_OriginalOperationField = QGridLayout()
        self.FCFV_OriginalOperationField.setObjectName(u"FCFV_OriginalOperationField")
        self.FCFV_OOF_RotateLabel = QLabel(self.gridLayoutWidget)
        self.FCFV_OOF_RotateLabel.setObjectName(u"FCFV_OOF_RotateLabel")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Display"])
        self.FCFV_OOF_RotateLabel.setFont(font4)
        self.FCFV_OOF_RotateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_RotateLabel, 0, 0, 1, 1)

        self.FCFV_OOF_ViewFirstZoneRadioButton = QRadioButton(self.gridLayoutWidget)
        self.FCFV_OOF_ViewFirstZoneRadioButton.setObjectName(u"FCFV_OOF_ViewFirstZoneRadioButton")
        self.FCFV_OOF_ViewFirstZoneRadioButton.setFont(font1)
        self.FCFV_OOF_ViewFirstZoneRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(85, 135, 255);\n"
"}")

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_ViewFirstZoneRadioButton, 0, 3, 1, 1)

        self.FCFV_OOF_RotateSpinBox = QSpinBox(self.gridLayoutWidget)
        self.FCFV_OOF_RotateSpinBox.setObjectName(u"FCFV_OOF_RotateSpinBox")
        font5 = QFont()
        font5.setFamilies([u"Fira Code"])
        self.FCFV_OOF_RotateSpinBox.setFont(font5)
        self.FCFV_OOF_RotateSpinBox.setMaximum(360)

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_RotateSpinBox, 0, 1, 1, 1)

        self.FCFV_OOF_ViewSecondZoneRadioButton = QRadioButton(self.gridLayoutWidget)
        self.FCFV_OOF_ViewSecondZoneRadioButton.setObjectName(u"FCFV_OOF_ViewSecondZoneRadioButton")
        self.FCFV_OOF_ViewSecondZoneRadioButton.setFont(font1)
        self.FCFV_OOF_ViewSecondZoneRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(255, 150, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(255, 115, 255);\n"
"}")

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_ViewSecondZoneRadioButton, 1, 3, 1, 1)

        self.FCFV_OOF_LineYAxis01Separator = QFrame(self.gridLayoutWidget)
        self.FCFV_OOF_LineYAxis01Separator.setObjectName(u"FCFV_OOF_LineYAxis01Separator")
        self.FCFV_OOF_LineYAxis01Separator.setFrameShape(QFrame.VLine)
        self.FCFV_OOF_LineYAxis01Separator.setFrameShadow(QFrame.Sunken)

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_LineYAxis01Separator, 0, 2, 1, 1)

        self.FCFV_OOF_LineYAxis02Separator = QFrame(self.gridLayoutWidget)
        self.FCFV_OOF_LineYAxis02Separator.setObjectName(u"FCFV_OOF_LineYAxis02Separator")
        self.FCFV_OOF_LineYAxis02Separator.setFrameShape(QFrame.VLine)
        self.FCFV_OOF_LineYAxis02Separator.setFrameShadow(QFrame.Sunken)

        self.FCFV_OriginalOperationField.addWidget(self.FCFV_OOF_LineYAxis02Separator, 1, 2, 1, 1)


        self.CameraFieldViewLayout.addLayout(self.FCFV_OriginalOperationField, 2, 0, 1, 1)

        self.FCFV_FirstZoneView = QGraphicsView(self.gridLayoutWidget)
        self.FCFV_FirstZoneView.setObjectName(u"FCFV_FirstZoneView")
        self.FCFV_FirstZoneView.setFrameShape(QFrame.Box)
        self.FCFV_FirstZoneView.setFrameShadow(QFrame.Plain)

        self.CameraFieldViewLayout.addWidget(self.FCFV_FirstZoneView, 1, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.MainFrame)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(20, 455, 1201, 156))
        self.PlateDetectionLayout = QGridLayout(self.gridLayoutWidget_4)
        self.PlateDetectionLayout.setObjectName(u"PlateDetectionLayout")
        self.PlateDetectionLayout.setContentsMargins(0, 0, 0, 0)
        self.PlateDetectionFirstZoneLabel = QLabel(self.gridLayoutWidget_4)
        self.PlateDetectionFirstZoneLabel.setObjectName(u"PlateDetectionFirstZoneLabel")
        self.PlateDetectionFirstZoneLabel.setFont(font3)
        self.PlateDetectionFirstZoneLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(150, 85, 255);\n"
"}")
        self.PlateDetectionFirstZoneLabel.setAlignment(Qt.AlignCenter)

        self.PlateDetectionLayout.addWidget(self.PlateDetectionFirstZoneLabel, 0, 1, 1, 1)

        self.PDZ02GraphicalFieldView = QGraphicsView(self.gridLayoutWidget_4)
        self.PDZ02GraphicalFieldView.setObjectName(u"PDZ02GraphicalFieldView")
        self.PDZ02GraphicalFieldView.setFrameShape(QFrame.Box)
        self.PDZ02GraphicalFieldView.setFrameShadow(QFrame.Plain)

        self.PlateDetectionLayout.addWidget(self.PDZ02GraphicalFieldView, 1, 2, 1, 1)

        self.PlateDetectionOriginalLabel = QLabel(self.gridLayoutWidget_4)
        self.PlateDetectionOriginalLabel.setObjectName(u"PlateDetectionOriginalLabel")
        self.PlateDetectionOriginalLabel.setFont(font3)
        self.PlateDetectionOriginalLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.PlateDetectionOriginalLabel.setAlignment(Qt.AlignCenter)

        self.PlateDetectionLayout.addWidget(self.PlateDetectionOriginalLabel, 0, 0, 1, 1)

        self.PlateDetectionSecondZoneLabel = QLabel(self.gridLayoutWidget_4)
        self.PlateDetectionSecondZoneLabel.setObjectName(u"PlateDetectionSecondZoneLabel")
        self.PlateDetectionSecondZoneLabel.setFont(font3)
        self.PlateDetectionSecondZoneLabel.setStyleSheet(u"QLabel {\n"
"	font-family: \"Segoe UI Variable Display\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(150, 85, 255);\n"
"}")
        self.PlateDetectionSecondZoneLabel.setAlignment(Qt.AlignCenter)

        self.PlateDetectionLayout.addWidget(self.PlateDetectionSecondZoneLabel, 0, 2, 1, 1)

        self.PDOGraphicalFieldView = QGraphicsView(self.gridLayoutWidget_4)
        self.PDOGraphicalFieldView.setObjectName(u"PDOGraphicalFieldView")
        self.PDOGraphicalFieldView.setFrameShape(QFrame.Box)
        self.PDOGraphicalFieldView.setFrameShadow(QFrame.Plain)

        self.PlateDetectionLayout.addWidget(self.PDOGraphicalFieldView, 1, 0, 1, 1)

        self.PlateDetectionFirstZoneLayout = QHBoxLayout()
        self.PlateDetectionFirstZoneLayout.setObjectName(u"PlateDetectionFirstZoneLayout")
        self.CountDetectedPDZ01Label = QLabel(self.gridLayoutWidget_4)
        self.CountDetectedPDZ01Label.setObjectName(u"CountDetectedPDZ01Label")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Variable Display"])
        font6.setPointSize(8)
        self.CountDetectedPDZ01Label.setFont(font6)
        self.CountDetectedPDZ01Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.PlateDetectionFirstZoneLayout.addWidget(self.CountDetectedPDZ01Label)

        self.CountDetectedPDZ01LineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.CountDetectedPDZ01LineEdit.setObjectName(u"CountDetectedPDZ01LineEdit")
        sizePolicy.setHeightForWidth(self.CountDetectedPDZ01LineEdit.sizePolicy().hasHeightForWidth())
        self.CountDetectedPDZ01LineEdit.setSizePolicy(sizePolicy)
        self.CountDetectedPDZ01LineEdit.setFont(font5)
        self.CountDetectedPDZ01LineEdit.setReadOnly(True)

        self.PlateDetectionFirstZoneLayout.addWidget(self.CountDetectedPDZ01LineEdit)

        self.PredictionPDZ02Label_2 = QLabel(self.gridLayoutWidget_4)
        self.PredictionPDZ02Label_2.setObjectName(u"PredictionPDZ02Label_2")
        self.PredictionPDZ02Label_2.setFont(font6)
        self.PredictionPDZ02Label_2.setAlignment(Qt.AlignCenter)

        self.PlateDetectionFirstZoneLayout.addWidget(self.PredictionPDZ02Label_2)

        self.PredictionPDZ01LineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.PredictionPDZ01LineEdit.setObjectName(u"PredictionPDZ01LineEdit")
        sizePolicy.setHeightForWidth(self.PredictionPDZ01LineEdit.sizePolicy().hasHeightForWidth())
        self.PredictionPDZ01LineEdit.setSizePolicy(sizePolicy)
        self.PredictionPDZ01LineEdit.setFont(font5)
        self.PredictionPDZ01LineEdit.setReadOnly(True)

        self.PlateDetectionFirstZoneLayout.addWidget(self.PredictionPDZ01LineEdit)

        self.SaveButtonPDZ01 = QPushButton(self.gridLayoutWidget_4)
        self.SaveButtonPDZ01.setObjectName(u"SaveButtonPDZ01")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SaveButtonPDZ01.sizePolicy().hasHeightForWidth())
        self.SaveButtonPDZ01.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Variable Display"])
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setItalic(False)
        self.SaveButtonPDZ01.setFont(font7)
        self.SaveButtonPDZ01.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 220, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 185, 127);\n"
"}")
        self.SaveButtonPDZ01.setCheckable(False)
        self.SaveButtonPDZ01.setAutoRepeat(True)
        self.SaveButtonPDZ01.setAutoDefault(False)
        self.SaveButtonPDZ01.setFlat(False)

        self.PlateDetectionFirstZoneLayout.addWidget(self.SaveButtonPDZ01)


        self.PlateDetectionLayout.addLayout(self.PlateDetectionFirstZoneLayout, 2, 1, 1, 1)

        self.PDZ01GraphicalFieldView = QGraphicsView(self.gridLayoutWidget_4)
        self.PDZ01GraphicalFieldView.setObjectName(u"PDZ01GraphicalFieldView")
        self.PDZ01GraphicalFieldView.setFrameShape(QFrame.Box)
        self.PDZ01GraphicalFieldView.setFrameShadow(QFrame.Plain)

        self.PlateDetectionLayout.addWidget(self.PDZ01GraphicalFieldView, 1, 1, 1, 1)

        self.PlateDetectionSecondZoneLayout = QHBoxLayout()
        self.PlateDetectionSecondZoneLayout.setObjectName(u"PlateDetectionSecondZoneLayout")
        self.CountDetectedPD02Label = QLabel(self.gridLayoutWidget_4)
        self.CountDetectedPD02Label.setObjectName(u"CountDetectedPD02Label")
        self.CountDetectedPD02Label.setFont(font6)
        self.CountDetectedPD02Label.setAlignment(Qt.AlignCenter)

        self.PlateDetectionSecondZoneLayout.addWidget(self.CountDetectedPD02Label)

        self.CountDetectedPDZ02LineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.CountDetectedPDZ02LineEdit.setObjectName(u"CountDetectedPDZ02LineEdit")
        sizePolicy.setHeightForWidth(self.CountDetectedPDZ02LineEdit.sizePolicy().hasHeightForWidth())
        self.CountDetectedPDZ02LineEdit.setSizePolicy(sizePolicy)
        self.CountDetectedPDZ02LineEdit.setReadOnly(True)

        self.PlateDetectionSecondZoneLayout.addWidget(self.CountDetectedPDZ02LineEdit)

        self.PredictionPDZ02Label = QLabel(self.gridLayoutWidget_4)
        self.PredictionPDZ02Label.setObjectName(u"PredictionPDZ02Label")
        self.PredictionPDZ02Label.setFont(font6)
        self.PredictionPDZ02Label.setAlignment(Qt.AlignCenter)

        self.PlateDetectionSecondZoneLayout.addWidget(self.PredictionPDZ02Label)

        self.PredictionPDZ02LineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.PredictionPDZ02LineEdit.setObjectName(u"PredictionPDZ02LineEdit")
        sizePolicy.setHeightForWidth(self.PredictionPDZ02LineEdit.sizePolicy().hasHeightForWidth())
        self.PredictionPDZ02LineEdit.setSizePolicy(sizePolicy)
        self.PredictionPDZ02LineEdit.setReadOnly(True)

        self.PlateDetectionSecondZoneLayout.addWidget(self.PredictionPDZ02LineEdit)

        self.SaveButtonPDZ02 = QPushButton(self.gridLayoutWidget_4)
        self.SaveButtonPDZ02.setObjectName(u"SaveButtonPDZ02")
        self.SaveButtonPDZ02.setFont(font7)
        self.SaveButtonPDZ02.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 220, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 185, 127);\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"applications-other"))
        self.SaveButtonPDZ02.setIcon(icon)
        self.SaveButtonPDZ02.setCheckable(False)
        self.SaveButtonPDZ02.setAutoRepeat(True)
        self.SaveButtonPDZ02.setAutoDefault(False)
        self.SaveButtonPDZ02.setFlat(False)

        self.PlateDetectionSecondZoneLayout.addWidget(self.SaveButtonPDZ02)


        self.PlateDetectionLayout.addLayout(self.PlateDetectionSecondZoneLayout, 2, 2, 1, 1)

        self.PlateDetectionOriginalLayout = QHBoxLayout()
        self.PlateDetectionOriginalLayout.setObjectName(u"PlateDetectionOriginalLayout")
        self.CountDetectedPDOLabel = QLabel(self.gridLayoutWidget_4)
        self.CountDetectedPDOLabel.setObjectName(u"CountDetectedPDOLabel")
        self.CountDetectedPDOLabel.setFont(font6)
        self.CountDetectedPDOLabel.setAlignment(Qt.AlignCenter)

        self.PlateDetectionOriginalLayout.addWidget(self.CountDetectedPDOLabel)

        self.CountDetectedPDOLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.CountDetectedPDOLineEdit.setObjectName(u"CountDetectedPDOLineEdit")
        sizePolicy.setHeightForWidth(self.CountDetectedPDOLineEdit.sizePolicy().hasHeightForWidth())
        self.CountDetectedPDOLineEdit.setSizePolicy(sizePolicy)
        self.CountDetectedPDOLineEdit.setReadOnly(True)

        self.PlateDetectionOriginalLayout.addWidget(self.CountDetectedPDOLineEdit)

        self.PredictionPDOLabel = QLabel(self.gridLayoutWidget_4)
        self.PredictionPDOLabel.setObjectName(u"PredictionPDOLabel")
        self.PredictionPDOLabel.setFont(font6)
        self.PredictionPDOLabel.setAlignment(Qt.AlignCenter)

        self.PlateDetectionOriginalLayout.addWidget(self.PredictionPDOLabel)

        self.PredictionPDOLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.PredictionPDOLineEdit.setObjectName(u"PredictionPDOLineEdit")
        sizePolicy.setHeightForWidth(self.PredictionPDOLineEdit.sizePolicy().hasHeightForWidth())
        self.PredictionPDOLineEdit.setSizePolicy(sizePolicy)
        self.PredictionPDOLineEdit.setReadOnly(True)

        self.PlateDetectionOriginalLayout.addWidget(self.PredictionPDOLineEdit)

        self.ShowResultButtonPDO = QPushButton(self.gridLayoutWidget_4)
        self.ShowResultButtonPDO.setObjectName(u"ShowResultButtonPDO")
        sizePolicy.setHeightForWidth(self.ShowResultButtonPDO.sizePolicy().hasHeightForWidth())
        self.ShowResultButtonPDO.setSizePolicy(sizePolicy)
        self.ShowResultButtonPDO.setFont(font7)
        self.ShowResultButtonPDO.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 85, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 15, 185);\n"
"}")

        self.PlateDetectionOriginalLayout.addWidget(self.ShowResultButtonPDO)


        self.PlateDetectionLayout.addLayout(self.PlateDetectionOriginalLayout, 2, 0, 1, 1)

        self.horizontalLayoutWidget_5 = QWidget(self.MainFrame)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(423, 625, 121, 21))
        self.FourProcessingAnalyticalLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.FourProcessingAnalyticalLayout.setObjectName(u"FourProcessingAnalyticalLayout")
        self.FourProcessingAnalyticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonID01 = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonID01.setObjectName(u"ButtonID01")
        font8 = QFont()
        font8.setFamilies([u"Fira Code Medium"])
        font8.setBold(True)
        font8.setItalic(False)
        self.ButtonID01.setFont(font8)
        self.ButtonID01.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	background-color: rgb(85, 85, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"	background-color: rgb(85, 190, 255);\n"
"}")

        self.FourProcessingAnalyticalLayout.addWidget(self.ButtonID01)

        self.ButtonID02 = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonID02.setObjectName(u"ButtonID02")
        self.ButtonID02.setFont(font8)
        self.ButtonID02.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	background-color: rgb(85, 85, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"	background-color: rgb(85, 190, 255);\n"
"}")

        self.FourProcessingAnalyticalLayout.addWidget(self.ButtonID02)

        self.ButtonID03 = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonID03.setObjectName(u"ButtonID03")
        self.ButtonID03.setFont(font8)
        self.ButtonID03.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	background-color: rgb(85, 85, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"	background-color: rgb(85, 190, 255);\n"
"}")

        self.FourProcessingAnalyticalLayout.addWidget(self.ButtonID03)

        self.ButtonID04 = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonID04.setObjectName(u"ButtonID04")
        self.ButtonID04.setFont(font8)
        self.ButtonID04.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	background-color: rgb(85, 85, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: white;\n"
"	background-color: rgb(85, 190, 255);\n"
"}")
        self.ButtonID04.setAutoExclusive(False)
        self.ButtonID04.setFlat(False)

        self.FourProcessingAnalyticalLayout.addWidget(self.ButtonID04)

        self.SliderReviewer = QSlider(self.MainFrame)
        self.SliderReviewer.setObjectName(u"SliderReviewer")
        self.SliderReviewer.setGeometry(QRect(604, 625, 160, 20))
        self.SliderReviewer.setAutoFillBackground(False)
        self.SliderReviewer.setStyleSheet(u"")
        self.SliderReviewer.setOrientation(Qt.Horizontal)
        self.LeftSideSliderNumberDisplayer = QLineEdit(self.MainFrame)
        self.LeftSideSliderNumberDisplayer.setObjectName(u"LeftSideSliderNumberDisplayer")
        self.LeftSideSliderNumberDisplayer.setGeometry(QRect(549, 625, 50, 20))
        self.LeftSideSliderNumberDisplayer.setFont(font5)
        self.LeftSideSliderNumberDisplayer.setFrame(True)
        self.LeftSideSliderNumberDisplayer.setAlignment(Qt.AlignCenter)
        self.LeftSideSliderNumberDisplayer.setReadOnly(True)
        self.RightSideSliderNumberDisplayer = QLineEdit(self.MainFrame)
        self.RightSideSliderNumberDisplayer.setObjectName(u"RightSideSliderNumberDisplayer")
        self.RightSideSliderNumberDisplayer.setGeometry(QRect(768, 625, 50, 20))
        self.RightSideSliderNumberDisplayer.setFont(font5)
        self.RightSideSliderNumberDisplayer.setAlignment(Qt.AlignCenter)
        self.RightSideSliderNumberDisplayer.setReadOnly(True)
        self.ShowResultZone1 = QPushButton(self.MainFrame)
        self.ShowResultZone1.setObjectName(u"ShowResultZone1")
        self.ShowResultZone1.setGeometry(QRect(825, 620, 116, 30))
        sizePolicy.setHeightForWidth(self.ShowResultZone1.sizePolicy().hasHeightForWidth())
        self.ShowResultZone1.setSizePolicy(sizePolicy)
        self.ShowResultZone1.setFont(font7)
        self.ShowResultZone1.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 85, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 15, 185);\n"
"}")
        self.ShowResultZone2 = QPushButton(self.MainFrame)
        self.ShowResultZone2.setObjectName(u"ShowResultZone2")
        self.ShowResultZone2.setGeometry(QRect(945, 620, 116, 30))
        sizePolicy.setHeightForWidth(self.ShowResultZone2.sizePolicy().hasHeightForWidth())
        self.ShowResultZone2.setSizePolicy(sizePolicy)
        self.ShowResultZone2.setFont(font7)
        self.ShowResultZone2.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 85, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 15, 185);\n"
"}")
        self.layoutWidget = QWidget(self.MainFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(422, 405, 397, 46))
        self.FCFV_FirstZoneOperationField = QGridLayout(self.layoutWidget)
        self.FCFV_FirstZoneOperationField.setObjectName(u"FCFV_FirstZoneOperationField")
        self.FCFV_FirstZoneOperationField.setContentsMargins(0, 0, 0, 0)
        self.FCFV_FZOF_LineYAxisOperationSeparator = QFrame(self.layoutWidget)
        self.FCFV_FZOF_LineYAxisOperationSeparator.setObjectName(u"FCFV_FZOF_LineYAxisOperationSeparator")
        self.FCFV_FZOF_LineYAxisOperationSeparator.setFrameShape(QFrame.VLine)
        self.FCFV_FZOF_LineYAxisOperationSeparator.setFrameShadow(QFrame.Sunken)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_LineYAxisOperationSeparator, 0, 1, 2, 1)

        self.FCFV_FZOF_SecondModeRadioButton = QRadioButton(self.layoutWidget)
        self.FCFV_FZOF_SecondModeRadioButton.setObjectName(u"FCFV_FZOF_SecondModeRadioButton")
        self.FCFV_FZOF_SecondModeRadioButton.setFont(font1)
        self.FCFV_FZOF_SecondModeRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(255, 135, 150);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(255, 100, 185);\n"
"}")

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_SecondModeRadioButton, 1, 0, 1, 1)

        self.FCFV_FZOF_FirstModeRadioButton = QRadioButton(self.layoutWidget)
        self.FCFV_FZOF_FirstModeRadioButton.setObjectName(u"FCFV_FZOF_FirstModeRadioButton")
        self.FCFV_FZOF_FirstModeRadioButton.setFont(font1)
        self.FCFV_FZOF_FirstModeRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(255, 185, 115);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(255, 220, 150);\n"
"}")

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_FirstModeRadioButton, 0, 0, 1, 1)

        self.FCFV_FZOF_BetaLabel = QLabel(self.layoutWidget)
        self.FCFV_FZOF_BetaLabel.setObjectName(u"FCFV_FZOF_BetaLabel")
        self.FCFV_FZOF_BetaLabel.setFont(font4)
        self.FCFV_FZOF_BetaLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_BetaLabel, 0, 4, 1, 1)

        self.FCFV_FZOF_RotateLabel = QLabel(self.layoutWidget)
        self.FCFV_FZOF_RotateLabel.setObjectName(u"FCFV_FZOF_RotateLabel")
        self.FCFV_FZOF_RotateLabel.setFont(font4)
        self.FCFV_FZOF_RotateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_RotateLabel, 1, 4, 1, 1)

        self.FCFV_FZOF_AlphaSpinBox = QSpinBox(self.layoutWidget)
        self.FCFV_FZOF_AlphaSpinBox.setObjectName(u"FCFV_FZOF_AlphaSpinBox")
        self.FCFV_FZOF_AlphaSpinBox.setFont(font5)
        self.FCFV_FZOF_AlphaSpinBox.setMaximum(1000)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_AlphaSpinBox, 0, 3, 1, 1)

        self.FCFV_FZOF_ZoomInOutLabel = QLabel(self.layoutWidget)
        self.FCFV_FZOF_ZoomInOutLabel.setObjectName(u"FCFV_FZOF_ZoomInOutLabel")
        self.FCFV_FZOF_ZoomInOutLabel.setFont(font4)
        self.FCFV_FZOF_ZoomInOutLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_ZoomInOutLabel, 1, 2, 1, 1)

        self.FCFV_FZOF_AlphaLabel = QLabel(self.layoutWidget)
        self.FCFV_FZOF_AlphaLabel.setObjectName(u"FCFV_FZOF_AlphaLabel")
        self.FCFV_FZOF_AlphaLabel.setFont(font4)
        self.FCFV_FZOF_AlphaLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_AlphaLabel, 0, 2, 1, 1)

        self.FCFV_FZOF_BetaSpinBox = QSpinBox(self.layoutWidget)
        self.FCFV_FZOF_BetaSpinBox.setObjectName(u"FCFV_FZOF_BetaSpinBox")
        self.FCFV_FZOF_BetaSpinBox.setFont(font5)
        self.FCFV_FZOF_BetaSpinBox.setMaximum(1000)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_BetaSpinBox, 0, 5, 1, 1)

        self.FCFV_FZOF_ZoomInOutSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.FCFV_FZOF_ZoomInOutSpinBox.setObjectName(u"FCFV_FZOF_ZoomInOutSpinBox")
        self.FCFV_FZOF_ZoomInOutSpinBox.setFont(font5)
        self.FCFV_FZOF_ZoomInOutSpinBox.setMaximum(100.000000000000000)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_ZoomInOutSpinBox, 1, 3, 1, 1)

        self.FCFV_FZOF_RotateSpinBox = QSpinBox(self.layoutWidget)
        self.FCFV_FZOF_RotateSpinBox.setObjectName(u"FCFV_FZOF_RotateSpinBox")
        self.FCFV_FZOF_RotateSpinBox.setFont(font5)
        self.FCFV_FZOF_RotateSpinBox.setMaximum(360)

        self.FCFV_FirstZoneOperationField.addWidget(self.FCFV_FZOF_RotateSpinBox, 1, 5, 1, 1)

        self.layoutWidget1 = QWidget(self.MainFrame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(825, 406, 397, 46))
        self.FCFV_SecondZoneOperationField = QGridLayout(self.layoutWidget1)
        self.FCFV_SecondZoneOperationField.setObjectName(u"FCFV_SecondZoneOperationField")
        self.FCFV_SecondZoneOperationField.setContentsMargins(0, 0, 0, 0)
        self.FCFV_SZOF_BetaSpinBox = QSpinBox(self.layoutWidget1)
        self.FCFV_SZOF_BetaSpinBox.setObjectName(u"FCFV_SZOF_BetaSpinBox")
        self.FCFV_SZOF_BetaSpinBox.setFont(font5)
        self.FCFV_SZOF_BetaSpinBox.setMaximum(1000)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_BetaSpinBox, 0, 5, 1, 1)

        self.FCFV_SZOF_ZoomInOutSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.FCFV_SZOF_ZoomInOutSpinBox.setObjectName(u"FCFV_SZOF_ZoomInOutSpinBox")
        self.FCFV_SZOF_ZoomInOutSpinBox.setFont(font5)
        self.FCFV_SZOF_ZoomInOutSpinBox.setMaximum(100.000000000000000)
        self.FCFV_SZOF_ZoomInOutSpinBox.setSingleStep(1.000000000000000)
        self.FCFV_SZOF_ZoomInOutSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.FCFV_SZOF_ZoomInOutSpinBox.setValue(0.000000000000000)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_ZoomInOutSpinBox, 1, 3, 1, 1)

        self.FCFV_SZOF_AlphaSpinBox = QSpinBox(self.layoutWidget1)
        self.FCFV_SZOF_AlphaSpinBox.setObjectName(u"FCFV_SZOF_AlphaSpinBox")
        self.FCFV_SZOF_AlphaSpinBox.setFont(font5)
        self.FCFV_SZOF_AlphaSpinBox.setMaximum(1000)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_AlphaSpinBox, 0, 3, 1, 1)

        self.FCFV_SZOF_FirstModeRadioButton = QRadioButton(self.layoutWidget1)
        self.FCFV_SZOF_FirstModeRadioButton.setObjectName(u"FCFV_SZOF_FirstModeRadioButton")
        self.FCFV_SZOF_FirstModeRadioButton.setFont(font1)
        self.FCFV_SZOF_FirstModeRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(255, 185, 115);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(255, 220, 150);\n"
"}")

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_FirstModeRadioButton, 0, 0, 1, 1)

        self.FCFV_SZOF_ZoomInOutLabel = QLabel(self.layoutWidget1)
        self.FCFV_SZOF_ZoomInOutLabel.setObjectName(u"FCFV_SZOF_ZoomInOutLabel")
        self.FCFV_SZOF_ZoomInOutLabel.setFont(font4)
        self.FCFV_SZOF_ZoomInOutLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_ZoomInOutLabel, 1, 2, 1, 1)

        self.FCFV_SZOF_AlphaLabel = QLabel(self.layoutWidget1)
        self.FCFV_SZOF_AlphaLabel.setObjectName(u"FCFV_SZOF_AlphaLabel")
        self.FCFV_SZOF_AlphaLabel.setFont(font4)
        self.FCFV_SZOF_AlphaLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_AlphaLabel, 0, 2, 1, 1)

        self.FCFV_SZOF_SecondModeRadioButton = QRadioButton(self.layoutWidget1)
        self.FCFV_SZOF_SecondModeRadioButton.setObjectName(u"FCFV_SZOF_SecondModeRadioButton")
        self.FCFV_SZOF_SecondModeRadioButton.setFont(font1)
        self.FCFV_SZOF_SecondModeRadioButton.setStyleSheet(u"QRadioButton {\n"
"	font: bold;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(255, 135, 150);\n"
"}\n"
"\n"
"QRadioButton:pressed {\n"
"	color: rgb(255, 100, 185);\n"
"}")

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_SecondModeRadioButton, 1, 0, 1, 1)

        self.FCFV_SZOF_RotateSpinBox = QSpinBox(self.layoutWidget1)
        self.FCFV_SZOF_RotateSpinBox.setObjectName(u"FCFV_SZOF_RotateSpinBox")
        self.FCFV_SZOF_RotateSpinBox.setFont(font5)
        self.FCFV_SZOF_RotateSpinBox.setMaximum(360)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_RotateSpinBox, 1, 5, 1, 1)

        self.FCFV_SZOF_RotateLabel = QLabel(self.layoutWidget1)
        self.FCFV_SZOF_RotateLabel.setObjectName(u"FCFV_SZOF_RotateLabel")
        self.FCFV_SZOF_RotateLabel.setFont(font4)
        self.FCFV_SZOF_RotateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_RotateLabel, 1, 4, 1, 1)

        self.FCFV_SZOF_LineYAxisOperationSeparator = QFrame(self.layoutWidget1)
        self.FCFV_SZOF_LineYAxisOperationSeparator.setObjectName(u"FCFV_SZOF_LineYAxisOperationSeparator")
        self.FCFV_SZOF_LineYAxisOperationSeparator.setFrameShape(QFrame.VLine)
        self.FCFV_SZOF_LineYAxisOperationSeparator.setFrameShadow(QFrame.Sunken)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_LineYAxisOperationSeparator, 0, 1, 2, 1)

        self.FCFV_SZOF_BetaLabel = QLabel(self.layoutWidget1)
        self.FCFV_SZOF_BetaLabel.setObjectName(u"FCFV_SZOF_BetaLabel")
        self.FCFV_SZOF_BetaLabel.setFont(font4)
        self.FCFV_SZOF_BetaLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FCFV_SecondZoneOperationField.addWidget(self.FCFV_SZOF_BetaLabel, 0, 4, 1, 1)

        self.CreationAndUsagePurposes = QLabel(self.MainFrame)
        self.CreationAndUsagePurposes.setObjectName(u"CreationAndUsagePurposes")
        self.CreationAndUsagePurposes.setGeometry(QRect(820, 20, 400, 15))
        self.CreationAndUsagePurposes.setFont(font4)
        self.CreationAndUsagePurposes.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.OpenSourceReserved = QLabel(self.MainFrame)
        self.OpenSourceReserved.setObjectName(u"OpenSourceReserved")
        self.OpenSourceReserved.setGeometry(QRect(820, 40, 400, 15))
        self.OpenSourceReserved.setFont(font4)
        self.OpenSourceReserved.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.MyGitHubProfile = QLabel(self.MainFrame)
        self.MyGitHubProfile.setObjectName(u"MyGitHubProfile")
        self.MyGitHubProfile.setGeometry(QRect(20, 625, 200, 15))
        self.MyGitHubProfile.setFont(font4)
        self.LastModifiedApplicationDate = QLabel(self.MainFrame)
        self.LastModifiedApplicationDate.setObjectName(u"LastModifiedApplicationDate")
        self.LastModifiedApplicationDate.setGeometry(QRect(20, 640, 200, 15))
        self.LastModifiedApplicationDate.setFont(font4)

        self.retranslateUi(Widget)

        self.ImageProcessingButton.setDefault(False)
        self.VideoProcessingButton.setDefault(False)
        self.StreamingButton.setDefault(False)
        self.RecordingButton.setDefault(False)
        self.SaveParametersButton.setDefault(False)
        self.SaveButtonPDZ01.setDefault(False)
        self.SaveButtonPDZ02.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Fisheye Monitoring System Application", None))
        self.MainApplicationTitle.setText(QCoreApplication.translate("Widget", u"<strong>Fish Eye Monitoring System Application</strong> | <i>Multi-views</i>", None))
#if QT_CONFIG(tooltip)
        self.ImageProcessingButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Monitoring - Image</h2>\n"
"<p>Getting the image by the normal fisheye camera and pr"
                        "ocess the captured (displayed) image afterwards.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Image Processing</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.ImageProcessingButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ImageProcessingButton.setText(QCoreApplication.translate("Widget", u"Image", None))
#if QT_CONFIG(tooltip)
        self.VideoProcessingButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Monitoring - Video</h2>\n"
"<p>Getting the video by the normal fisheye camera and pr"
                        "ocess the captured (displayed) video afterwards.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Video Processing</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.VideoProcessingButton.setText(QCoreApplication.translate("Widget", u"Video", None))
#if QT_CONFIG(tooltip)
        self.StreamingButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Monitoring - Streaming</h2>\n"
"<p>Streaming over the fisheye camera, connected eith"
                        "er by Bluetooth or external cable, then process the streaming video while onboard.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Streaming Processing Onboard</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.StreamingButton.setText(QCoreApplication.translate("Widget", u"Streaming", None))
#if QT_CONFIG(tooltip)
        self.RecordingButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Monitoring - Recording</h2>\n"
"<p>Record using the fisheye camera, connected either"
                        " by Bluetooth or external cable, then process the recorded video afterwards.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Recorded Video Processing</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.RecordingButton.setText(QCoreApplication.translate("Widget", u"Recording", None))
#if QT_CONFIG(tooltip)
        self.SaveParametersButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Monitoring - Save Parameters</h2>\n"
"<p>Use to save some custom existing (or built-"
                        "in) parameters for the fisheye monitoring camera system setup after some configurations to be done before/afterhand.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Saving Existing Parameters</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.SaveParametersButton.setText(QCoreApplication.translate("Widget", u"Save Parameters", None))
        self.NormalFisheyeCameraFieldView_FirstZoneLabel.setText(QCoreApplication.translate("Widget", u"Fisheye Camera Field View <strong>(Zone 1)</strong>", None))
        self.NormalFisheyeCameraFieldView_SecondZoneLabel.setText(QCoreApplication.translate("Widget", u"Fisheye Camera Field View <strong>(Zone 2)</strong>", None))
        self.NormalFisheyeCameraFieldView_OriginalLabel.setText(QCoreApplication.translate("Widget", u"Normal Fisheye Camera Field View <strong>(Original)</strong>", None))
#if QT_CONFIG(tooltip)
        self.FCFV_OOF_RotateLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_OOF_RotateLabel.setText(QCoreApplication.translate("Widget", u"Rotate (degrees)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_OOF_ViewFirstZoneRadioButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Radio Box - Camera Zone 1</h2>\n"
"<p>Process the captured parameters by the fisheye"
                        "'s camera lens into the Camera Zone 1 graphical view.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Camera Zone 1 Processing</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_OOF_ViewFirstZoneRadioButton.setText(QCoreApplication.translate("Widget", u"View (Zone 1)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_OOF_RotateSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_OOF_ViewSecondZoneRadioButton.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Radio Box - Camera Zone 2</h2>\n"
"<p>Process the captured parameters by the fisheye"
                        "'s camera lens into the Camera Zone 2 graphical view.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Camera Zone 2 Processing</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_OOF_ViewSecondZoneRadioButton.setText(QCoreApplication.translate("Widget", u"View (Zone 2)", None))
        self.PlateDetectionFirstZoneLabel.setText(QCoreApplication.translate("Widget", u"Plate Detection <strong>(Zone 1)</strong>", None))
        self.PlateDetectionOriginalLabel.setText(QCoreApplication.translate("Widget", u"Plate Detection <strong>(Original)</strong>", None))
        self.PlateDetectionSecondZoneLabel.setText(QCoreApplication.translate("Widget", u"Plate Detection <strong>(Zone 2)</strong>", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPDZ01Label.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Zone 1)</h2>\n"
"<p>Use for displaying the d"
                        "etected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.CountDetectedPDZ01Label.setText(QCoreApplication.translate("Widget", u"Count Detected:", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPDZ01LineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Zone 1)</h2>\n"
"<p>Use for displaying the d"
                        "etected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.PredictionPDZ02Label_2.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Zone 1)</h2>\n"
"<p>Use for displaying the predic"
                        "ted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.PredictionPDZ02Label_2.setText(QCoreApplication.translate("Widget", u"Prediction:", None))
#if QT_CONFIG(tooltip)
        self.PredictionPDZ01LineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Zone 1)</h2>\n"
"<p>Use for displaying the predic"
                        "ted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.SaveButtonPDZ01.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Save Result (Zone 1)</h2>\n"
"<p>Use for saving the processed resu"
                        "lts based on the count detections and predictions onto some file/data memory for further usages.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Saving Plate Detection Results</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.SaveButtonPDZ01.setText(QCoreApplication.translate("Widget", u"Save", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPD02Label.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Zone 2)</h2>\n"
"<p>Use for displaying the d"
                        "etected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.CountDetectedPD02Label.setText(QCoreApplication.translate("Widget", u"Count Detected:", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPDZ02LineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Zone 2)</h2>\n"
"<p>Use for displaying the d"
                        "etected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.PredictionPDZ02Label.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Zone 2)</h2>\n"
"<p>Use for displaying the predic"
                        "ted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.PredictionPDZ02Label.setText(QCoreApplication.translate("Widget", u"Prediction:", None))
#if QT_CONFIG(tooltip)
        self.PredictionPDZ02LineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Zone 2)</h2>\n"
"<p>Use for displaying the predic"
                        "ted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.SaveButtonPDZ02.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Save Result (Zone 2)</h2>\n"
"<p>Use for saving the processed resu"
                        "lts based on the count detections and predictions onto some file/data memory for further usages.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Saving Plate Detection Results</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.SaveButtonPDZ02.setText(QCoreApplication.translate("Widget", u"Save", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPDOLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Original)</h2>\n"
"<p>Use for displaying the"
                        " detected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.CountDetectedPDOLabel.setText(QCoreApplication.translate("Widget", u"Count Detected:", None))
#if QT_CONFIG(tooltip)
        self.CountDetectedPDOLineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Count Detection (Original)</h2>\n"
"<p>Use for displaying the"
                        " detected count plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Count Detection</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.PredictionPDOLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Original)</h2>\n"
"<p>Use for displaying the pred"
                        "icted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.PredictionPDOLabel.setText(QCoreApplication.translate("Widget", u"Prediction:", None))
#if QT_CONFIG(tooltip)
        self.PredictionPDOLineEdit.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Prediction (Original)</h2>\n"
"<p>Use for displaying the pred"
                        "icted plate based on the modifications in the camera field trick above.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Prediction</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ShowResultButtonPDO.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Result (Original)</h2>\n"
"<p>Use for displaying the given re"
                        "sult based on the count detections and predictions.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Result</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ShowResultButtonPDO.setText(QCoreApplication.translate("Widget", u"Result", None))
#if QT_CONFIG(tooltip)
        self.ButtonID01.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Button ID: 1</h2>\n"
"<p>Button with ID 1 feature may be coming out soon e"
                        "xplanatively.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonID01.setText(QCoreApplication.translate("Widget", u"1", None))
#if QT_CONFIG(tooltip)
        self.ButtonID02.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Button ID: 2</h2>\n"
"<p>Button with ID 2 feature may be coming out soon e"
                        "xplanatively.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonID02.setText(QCoreApplication.translate("Widget", u"2", None))
#if QT_CONFIG(tooltip)
        self.ButtonID03.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Button ID: 3</h2>\n"
"<p>Button with ID 3 feature may be coming out soon e"
                        "xplanatively.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonID03.setText(QCoreApplication.translate("Widget", u"3", None))
#if QT_CONFIG(tooltip)
        self.ButtonID04.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Button ID: 4</h2>\n"
"<p>Button with ID 4 feature may be coming out soon e"
                        "xplanatively.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonID04.setText(QCoreApplication.translate("Widget", u"4", None))
#if QT_CONFIG(tooltip)
        self.SliderReviewer.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Plate Detection Slider (Manual Dragging Values)</h2>\n"
"<p>Acts as a usua"
                        "l slider as always, going from the least minimum value (assuming at 0), up to a certain maximum value as one pinpointed at the right side mini slider value displayer.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.LeftSideSliderNumberDisplayer.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Display Slider Value (Left Side)</h2>\n"
"<p>Mini slider value displayer f"
                        "or showing a current specific value representing the amount of upsteps of value by the slider (possibility going from the least minimum: 0, up to certain maximum value of the slider).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.LeftSideSliderNumberDisplayer.setInputMask("")
        self.LeftSideSliderNumberDisplayer.setText(QCoreApplication.translate("Widget", u"00.00", None))
        self.LeftSideSliderNumberDisplayer.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.RightSideSliderNumberDisplayer.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Unknown - Display Slider Value (Right Side)</h2>\n"
"<p>Mini slider value displayer "
                        "for showing a current specific value representing the amount of upsteps of value by the slider (possibility for the maximum slider value).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Not Implemented Yet</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.RightSideSliderNumberDisplayer.setText(QCoreApplication.translate("Widget", u"00.00", None))
#if QT_CONFIG(tooltip)
        self.ShowResultZone1.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Result (Zone 1)</h2>\n"
"<p>Use for displaying the given resu"
                        "lt based on the count detections and predictions.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Result</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ShowResultZone1.setText(QCoreApplication.translate("Widget", u"Result (Zone 1)", None))
#if QT_CONFIG(tooltip)
        self.ShowResultZone2.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Plate Detection - Show Result (Zone 2)</h2>\n"
"<p>Use for displaying the given resu"
                        "lt based on the count detections and predictions.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Given Plate Detection Result</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.ShowResultZone2.setText(QCoreApplication.translate("Widget", u"Result (Zone 2)", None))
        self.FCFV_FZOF_SecondModeRadioButton.setText(QCoreApplication.translate("Widget", u"Mode 2", None))
        self.FCFV_FZOF_FirstModeRadioButton.setText(QCoreApplication.translate("Widget", u"Mode 1", None))
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_BetaLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b2) Beta Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_FZOF_BetaLabel.setText(QCoreApplication.translate("Widget", u"Beta (\u03b2)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_RotateLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_FZOF_RotateLabel.setText(QCoreApplication.translate("Widget", u"Rotate (degrees)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_AlphaSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b1) Alpha Value</h2>\n"
"<p>Set out the alpha (\u03b1) value within "
                        "the range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_ZoomInOutLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Zoom (IN/OUT) Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 100 (excluding negative numbers and numbers above 100 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-100 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_FZOF_ZoomInOutLabel.setText(QCoreApplication.translate("Widget", u"Zoom (in/out)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_AlphaLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b1) Alpha Value</h2>\n"
"<p>Set out the alpha (\u03b1) value within "
                        "the range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_FZOF_AlphaLabel.setText(QCoreApplication.translate("Widget", u"Alpha (\u03b1)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_BetaSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b2) Beta Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_ZoomInOutSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Zoom (IN/OUT) Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 100 (excluding negative numbers and numbers above 100 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-100 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_FZOF_RotateSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_BetaSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b2) Beta Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_ZoomInOutSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Zoom (IN/OUT) Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 100 (excluding negative numbers and numbers above 100 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-100 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_AlphaSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b1) Alpha Value</h2>\n"
"<p>Set out the alpha (\u03b1) value within "
                        "the range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_SZOF_FirstModeRadioButton.setText(QCoreApplication.translate("Widget", u"Mode 1", None))
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_ZoomInOutLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Zoom (IN/OUT) Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 100 (excluding negative numbers and numbers above 100 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-100 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_SZOF_ZoomInOutLabel.setText(QCoreApplication.translate("Widget", u"Zoom (in/out)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_AlphaLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b1) Alpha Value</h2>\n"
"<p>Set out the alpha (\u03b1) value within "
                        "the range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_SZOF_AlphaLabel.setText(QCoreApplication.translate("Widget", u"Alpha (\u03b1)", None))
        self.FCFV_SZOF_SecondModeRadioButton.setText(QCoreApplication.translate("Widget", u"Mode 2", None))
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_RotateSpinBox.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_RotateLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - Degrees</h2>\n"
"<p>Drag up/down the spin box (or capture exact degrees v"
                        "alue), going from 0 up to 360.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-360 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_SZOF_RotateLabel.setText(QCoreApplication.translate("Widget", u"Rotate (degrees)", None))
#if QT_CONFIG(tooltip)
        self.FCFV_SZOF_BetaLabel.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Spin Box - (\u03b2) Beta Value</h2>\n"
"<p>Set out the beta (\u03b2) value within th"
                        "e range of 0 up to 1,000 (excluding negative numbers and numbers above 1,000 for now).</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">0-1,000 Only</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.FCFV_SZOF_BetaLabel.setText(QCoreApplication.translate("Widget", u"Beta (\u03b2)", None))
        self.CreationAndUsagePurposes.setText(QCoreApplication.translate("Widget", u"<i>Creation and Usage Purposes for: <strong>FTDC Lab Tel-U.</strong></i>", None))
        self.OpenSourceReserved.setText(QCoreApplication.translate("Widget", u"<i>@Open Source Project (Reserved), <strong>January 2024</strong> by: <strong>Immanuel Eben.<strong></i>", None))
        self.MyGitHubProfile.setText(QCoreApplication.translate("Widget", u"<strong>@GitHub: EintsWaveX</strong>", None))
        self.LastModifiedApplicationDate.setText(QCoreApplication.translate("Widget", u"<i>Last Modified: 13th January 2024</i>", None))
    # retranslateUi

