/****************************************************************************
** Form interface generated from reading ui file './generictableui.ui'
**
** Created by: The User Interface Compiler ($Id: qt/main.cpp   3.3.8   edited Jan 11 14:47 $)
**
** WARNING! All changes made in this file will be lost!
****************************************************************************/

#ifndef GENERICTABLESETTINGS_H
#define GENERICTABLESETTINGS_H

#include <qvariant.h>
#include <qpixmap.h>
#include <qwidget.h>

class QVBoxLayout;
class QHBoxLayout;
class QGridLayout;
class QSpacerItem;
class SkimEditShortcutButton;
class QTabWidget;
class QCheckBox;
class QLabel;
class KLineEdit;

class GenericTableSettingsUI : public QWidget
{
    Q_OBJECT

public:
    GenericTableSettingsUI( QWidget* parent = 0, const char* name = 0, WFlags fl = 0 );
    ~GenericTableSettingsUI();

    QTabWidget* tabWidget2;
    QWidget* tab;
    QCheckBox* kcfg__IMEngine_Table_ShowPrompt;
    QCheckBox* kcfg__IMEngine_Table_ShowKeyHint;
    QCheckBox* kcfg__IMEngine_Table_UserTableBinary;
    QCheckBox* kcfg__IMEngine_Table_UserPhraseFirst;
    QCheckBox* kcfg__IMEngine_Table_LongPhraseFirst;
    QWidget* TabPage;
    QLabel* textLabel1_2;
    QLabel* textLabel1_3;
    QLabel* textLabel1;
    SkimEditShortcutButton* puncButton;
    KLineEdit* kcfg__IMEngine_Table_FullWidthPunctKey;
    SkimEditShortcutButton* letterButton;
    KLineEdit* kcfg__IMEngine_Table_FullWidthLetterKey;
    SkimEditShortcutButton* modeButton;
    KLineEdit* kcfg__IMEngine_Table_ModeSwitchKey;
    SkimEditShortcutButton* addButton;
    KLineEdit* kcfg__IMEngine_Table_AddPhraseKey;
    SkimEditShortcutButton* deleteButton;
    KLineEdit* kcfg__IMEngine_Table_DeletePhraseKey;
    QLabel* textLabel1_4_2;
    QLabel* textLabel1_4_2_2;

protected:
    QVBoxLayout* GenericTableSettingsLayout;
    QVBoxLayout* tabLayout;
    QSpacerItem* spacer2;
    QVBoxLayout* layout1;
    QGridLayout* TabPageLayout;
    QSpacerItem* spacer5;

protected slots:
    virtual void languageChange();

private:
    QPixmap image0;

};

#endif // GENERICTABLESETTINGS_H
