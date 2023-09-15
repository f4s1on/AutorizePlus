#!/usr/bin/env python
# -*- coding: utf-8 -*-

from javax.swing import JLabel
from javax.swing import JComboBox
from javax.swing import JTextArea
from javax.swing import JScrollPane
from javax.swing import DefaultListModel
from javax.swing import JList
from javax.swing import JPanel
from javax.swing import JButton

from java.awt import Color
from javax.swing.border import LineBorder

import re


class EncryptDecrypt():
    def __init__(self, extender):
        self._extender = extender

    def draw(self):
        """ init the Encrypt/Decrypt tab
        """
        # todo add an option to ignore large requests
        padding = 5
        labelWidth = 140
        labelHeight = 30
        editHeight = 35
        editWidth = 300
        buttonWidth = 120
        buttonHeight = 30
        column1X = 10
        column2X = column1X + labelWidth + padding
        column3X = column2X + editWidth + padding
        EncMods = ["AES/ECB/NOPADDING", "AES/CBC/PKCS5Padding","AES/CBC/PKCS7Padding", "AES/CFB/PKCS5Padding",
                   "AES/CFB/PKCS7Padding","DES/ECB/NOPADDING","DES/CBC/PKCS5Padding","DES/CBC/PKCS7Padding",
                   "DES/CFB/PKCS5Padding","DES/CFB/PKCS7Padding","DESede/ECB/NOPADDING","DESede/CBC/PKCS5Padding",
                   "DESede/CBC/PKCS7Padding", "DESede/CFB/PKCS5Padding","DESede/CFB/PKCS7Padding"]
        row1Y = 10
        row2Y = row1Y + labelHeight + padding
        row3Y = row2Y + editHeight + padding
        row4Y = row3Y + editHeight + padding
        row5Y = row4Y + editHeight + padding
        row6Y = row5Y + editHeight + padding
        row7Y = row6Y + editHeight + padding
        row8Y = row7Y + editHeight + padding
        row9Y = row8Y + labelHeight + padding
        row10Y = row9Y + buttonHeight + padding

        DETypeLabel = JLabel("Type:")
        DETypeLabel.setBounds(column1X, row1Y, labelWidth, labelHeight)

        Secret1 = JLabel("Secret1:")
        Secret1.setBounds(column1X, row2Y, labelWidth, labelHeight)

        IV1 = JLabel("IV1:")
        IV1.setBounds(column1X, row3Y, labelWidth, labelHeight)

        Secret2 = JLabel("Secret2:")
        Secret2.setBounds(column1X, row4Y, labelWidth, labelHeight)

        IV2 = JLabel("IV2:")
        IV2.setBounds(column1X, row5Y, labelWidth, labelHeight)

        request = JLabel("request(regex):")
        request.setBounds(column1X, row6Y, labelWidth, labelHeight)

        response = JLabel("response(regex):")
        response.setBounds(column1X, row7Y, labelWidth, labelHeight)

        DELabelList = JLabel("Filter List:")
        DELabelList.setBounds(column1X, row9Y, labelWidth, labelHeight)

        self._extender.DEType = JComboBox(EncMods)
        self._extender.DEType.setBounds(column2X, row1Y, editWidth, labelHeight)

        self._extender.Secret1Text = JTextArea("", 5, 30)
        scrollSecret1Text = JScrollPane(self._extender.Secret1Text)
        scrollSecret1Text.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollSecret1Text.setBounds(column2X, row2Y, editWidth, editHeight)

        self._extender.IV1Text = JTextArea("", 5, 30)
        scrollIV1Text = JScrollPane(self._extender.IV1Text)
        scrollIV1Text.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollIV1Text.setBounds(column2X, row3Y, editWidth, editHeight)

        self._extender.Secret2Text = JTextArea("", 5, 30)
        scrollSecret2Text = JScrollPane(self._extender.Secret2Text)
        scrollSecret2Text.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollSecret2Text.setBounds(column2X, row4Y, editWidth, editHeight)

        self._extender.IV2Text = JTextArea("", 5, 30)
        scrollIV2Text = JScrollPane(self._extender.IV2Text)
        scrollIV2Text.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollIV2Text.setBounds(column2X, row5Y, editWidth, editHeight)

        self._extender.requestText = JTextArea('{\"data\":\"(.*)\"}', 5, 30)
        scrollrequestText = JScrollPane(self._extender.requestText)
        scrollrequestText.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollrequestText.setBounds(column2X, row6Y, editWidth, editHeight)

        self._extender.responseText = JTextArea('^\"(.*)\"$', 5, 30)
        scrollresponseText = JScrollPane(self._extender.responseText)
        scrollresponseText.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollresponseText.setBounds(column2X, row7Y, editWidth, editHeight)

        # i couldn't figure out how to have a model that contained anythin other than a string
        # so i'll use 2 models, one with the data and one for the JList
        self._extender.badProgrammerDEModel = {}
        self._extender.DEModel = DefaultListModel()
        self._extender.DEList = JList(self._extender.DEModel)

        scrollDEList = JScrollPane(self._extender.DEList)
        scrollDEList.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED)
        scrollDEList.setBounds(column2X, row9Y, editWidth, editHeight)
        scrollDEList.setBorder(LineBorder(Color.BLACK))

        self._extender.DEAdd = JButton("Add filter", actionPerformed=self.addDEFilter)
        self._extender.DEAdd.setBounds(column2X, row8Y, buttonWidth, buttonHeight)
        self._extender.DEDel = JButton("Remove filter", actionPerformed=self.delDEFilter)
        self._extender.DEDel.setBounds(column3X, row9Y, buttonWidth, buttonHeight)
        self._extender.DEMod = JButton("Modify filter", actionPerformed=self.modDEFilter)
        self._extender.DEMod.setBounds(column3X, row9Y + buttonHeight + padding, buttonWidth, buttonHeight)

        self._extender.DEFeedback = JLabel("")
        self._extender.DEFeedback.setBounds(column1X, row10Y, column3X + buttonWidth, labelHeight)

        self._extender.DEPnl = JPanel()
        self._extender.DEPnl.setLayout(None)
        self._extender.DEPnl.setBounds(0, 0, 1000, 1000)
        self._extender.DEPnl.add(DETypeLabel)
        self._extender.DEPnl.add(self._extender.DEType)
        self._extender.DEPnl.add(Secret1)
        self._extender.DEPnl.add(Secret2)
        self._extender.DEPnl.add(scrollSecret1Text)
        self._extender.DEPnl.add(scrollSecret2Text)
        self._extender.DEPnl.add(IV1)
        self._extender.DEPnl.add(IV2)
        self._extender.DEPnl.add(scrollIV1Text)
        self._extender.DEPnl.add(scrollIV2Text)
        self._extender.DEPnl.add(request)
        self._extender.DEPnl.add(response)
        self._extender.DEPnl.add(scrollrequestText)
        self._extender.DEPnl.add(scrollresponseText)
        self._extender.DEPnl.add(self._extender.DEAdd)
        self._extender.DEPnl.add(DELabelList)
        self._extender.DEPnl.add(scrollDEList)
        self._extender.DEPnl.add(self._extender.DEDel)
        self._extender.DEPnl.add(self._extender.DEMod)
        self._extender.DEPnl.add(self._extender.DEFeedback)

    def addDEFilter(self, event):
        typeName = self._extender.DEType.getSelectedItem()
        secret1 = self._extender.Secret1Text.getText()
        secret2 = self._extender.Secret2Text.getText()
        IV1 = self._extender.IV1Text.getText()
        IV2 = self._extender.IV2Text.getText()
        request = self._extender.requestText.getText()
        response = self._extender.responseText.getText()

        method = typeName
        if method in self._extender.badProgrammerDEModel:
            self._extender.DEFeedback.setText("Encrypt/Decrypt already exists")
            return

        self._extender.badProgrammerDEModel[method] = {"secret1": secret1, "secret2": secret2,
                                                       "IV1": IV1, "IV2": IV2, "type": typeName,
                                                       "request": request, "response": response}
        self._extender.DEModel.addElement(method)
        self._extender.Secret1Text.setText("")
        self._extender.Secret2Text.setText("")
        self._extender.IV1Text.setText("")
        self._extender.IV2Text.setText("")
        self._extender.requestText.setText("")
        self._extender.responseText.setText("")
        self._extender.DEFeedback.setText("")

    def delDEFilter(self, event):
        index = self._extender.DEList.getSelectedIndex()
        if not index == -1:
            key = self._extender.DEList.getSelectedValue()
            del self._extender.badProgrammerDEModel[key]
            self._extender.DEList.getModel().remove(index)

    def modDEFilter(self, event):
        index = self._extender.DEList.getSelectedIndex()
        if not index == -1:
            key = self._extender.DEList.getSelectedValue()
            self._extender.DEType.getModel().setSelectedItem(self._extender.badProgrammerDEModel[key]["type"])
            self._extender.Secret1Text.setText(self._extender.badProgrammerDEModel[key]["secret1"])
            self._extender.Secret2Text.setText(self._extender.badProgrammerDEModel[key]["secret2"])
            self._extender.IV1Text.setText(self._extender.badProgrammerDEModel[key]["IV1"])
            self._extender.IV2Text.setText(self._extender.badProgrammerDEModel[key]["IV2"])
            self._extender.requestText.setText(self._extender.badProgrammerDEModel[key]["request"])
            self._extender.responseText.setText(self._extender.badProgrammerDEModel[key]["response"])
            self.delDEFilter(event)
