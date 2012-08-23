#include <kdialog.h>
#include <klocale.h>
/****************************************************************************
** Form implementation generated from reading ui file './generictableui.ui'
**
** Created by User Interface Compiler
**
** WARNING! All changes made in this file will be lost!
****************************************************************************/

#include "generictableui.h"

#include <qvariant.h>
#include <qpushbutton.h>
#include <qtabwidget.h>
#include <qcheckbox.h>
#include <qlabel.h>
#include <klineedit.h>
#include <qlayout.h>
#include <qtooltip.h>
#include <qwhatsthis.h>
#include "klineedit.h"
#include "skimkeygrabber.h"

/*
 *  Constructs a GenericTableSettingsUI as a child of 'parent', with the
 *  name 'name' and widget flags set to 'f'.
 */
GenericTableSettingsUI::GenericTableSettingsUI( QWidget* parent, const char* name, WFlags fl )
    : QWidget( parent, name, fl )
{
    if ( !name )
	setName( "GenericTableSettings" );
    GenericTableSettingsLayout = new QVBoxLayout( this, 0, 0, "GenericTableSettingsLayout"); 

    tabWidget2 = new QTabWidget( this, "tabWidget2" );

    tab = new QWidget( tabWidget2, "tab" );
    tabLayout = new QVBoxLayout( tab, 11, 6, "tabLayout"); 

    layout1 = new QVBoxLayout( 0, 0, 6, "layout1"); 

    kcfg__IMEngine_Table_ShowPrompt = new QCheckBox( tab, "kcfg__IMEngine_Table_ShowPrompt" );
    layout1->addWidget( kcfg__IMEngine_Table_ShowPrompt );

    kcfg__IMEngine_Table_ShowKeyHint = new QCheckBox( tab, "kcfg__IMEngine_Table_ShowKeyHint" );
    layout1->addWidget( kcfg__IMEngine_Table_ShowKeyHint );

    kcfg__IMEngine_Table_UserTableBinary = new QCheckBox( tab, "kcfg__IMEngine_Table_UserTableBinary" );
    layout1->addWidget( kcfg__IMEngine_Table_UserTableBinary );

    kcfg__IMEngine_Table_UserPhraseFirst = new QCheckBox( tab, "kcfg__IMEngine_Table_UserPhraseFirst" );
    layout1->addWidget( kcfg__IMEngine_Table_UserPhraseFirst );

    kcfg__IMEngine_Table_LongPhraseFirst = new QCheckBox( tab, "kcfg__IMEngine_Table_LongPhraseFirst" );
    layout1->addWidget( kcfg__IMEngine_Table_LongPhraseFirst );
    tabLayout->addLayout( layout1 );
    spacer2 = new QSpacerItem( 20, 41, QSizePolicy::Minimum, QSizePolicy::Expanding );
    tabLayout->addItem( spacer2 );
    tabWidget2->insertTab( tab, QString::fromLatin1("") );

    TabPage = new QWidget( tabWidget2, "TabPage" );
    TabPageLayout = new QGridLayout( TabPage, 1, 1, 11, 6, "TabPageLayout"); 

    textLabel1_2 = new QLabel( TabPage, "textLabel1_2" );

    TabPageLayout->addWidget( textLabel1_2, 1, 0 );

    textLabel1_3 = new QLabel( TabPage, "textLabel1_3" );

    TabPageLayout->addWidget( textLabel1_3, 2, 0 );

    textLabel1 = new QLabel( TabPage, "textLabel1" );

    TabPageLayout->addWidget( textLabel1, 0, 0 );

    puncButton = new SkimEditShortcutButton( TabPage, "puncButton" );

    TabPageLayout->addWidget( puncButton, 0, 2 );

    kcfg__IMEngine_Table_FullWidthPunctKey = new KLineEdit( TabPage, "kcfg__IMEngine_Table_FullWidthPunctKey" );

    TabPageLayout->addWidget( kcfg__IMEngine_Table_FullWidthPunctKey, 0, 1 );

    letterButton = new SkimEditShortcutButton( TabPage, "letterButton" );

    TabPageLayout->addWidget( letterButton, 1, 2 );

    kcfg__IMEngine_Table_FullWidthLetterKey = new KLineEdit( TabPage, "kcfg__IMEngine_Table_FullWidthLetterKey" );

    TabPageLayout->addWidget( kcfg__IMEngine_Table_FullWidthLetterKey, 1, 1 );

    modeButton = new SkimEditShortcutButton( TabPage, "modeButton" );

    TabPageLayout->addWidget( modeButton, 2, 2 );

    kcfg__IMEngine_Table_ModeSwitchKey = new KLineEdit( TabPage, "kcfg__IMEngine_Table_ModeSwitchKey" );

    TabPageLayout->addWidget( kcfg__IMEngine_Table_ModeSwitchKey, 2, 1 );

    addButton = new SkimEditShortcutButton( TabPage, "addButton" );

    TabPageLayout->addWidget( addButton, 4, 2 );

    kcfg__IMEngine_Table_AddPhraseKey = new KLineEdit( TabPage, "kcfg__IMEngine_Table_AddPhraseKey" );

    TabPageLayout->addWidget( kcfg__IMEngine_Table_AddPhraseKey, 4, 1 );

    deleteButton = new SkimEditShortcutButton( TabPage, "deleteButton" );

    TabPageLayout->addWidget( deleteButton, 5, 2 );

    kcfg__IMEngine_Table_DeletePhraseKey = new KLineEdit( TabPage, "kcfg__IMEngine_Table_DeletePhraseKey" );

    TabPageLayout->addWidget( kcfg__IMEngine_Table_DeletePhraseKey, 5, 1 );

    textLabel1_4_2 = new QLabel( TabPage, "textLabel1_4_2" );

    TabPageLayout->addWidget( textLabel1_4_2, 4, 0 );

    textLabel1_4_2_2 = new QLabel( TabPage, "textLabel1_4_2_2" );

    TabPageLayout->addWidget( textLabel1_4_2_2, 5, 0 );
    spacer5 = new QSpacerItem( 20, 31, QSizePolicy::Minimum, QSizePolicy::Expanding );
    TabPageLayout->addItem( spacer5, 7, 1 );
    tabWidget2->insertTab( TabPage, QString::fromLatin1("") );
    GenericTableSettingsLayout->addWidget( tabWidget2 );
    languageChange();
    resize( QSize(433, 305).expandedTo(minimumSizeHint()) );
    clearWState( WState_Polished );

    // signals and slots connections
    connect( kcfg__IMEngine_Table_AddPhraseKey, SIGNAL( textChanged(const QString&) ), addButton, SLOT( setShortcuts(const QString&) ) );
    connect( addButton, SIGNAL( setEditorText(const QString&) ), kcfg__IMEngine_Table_AddPhraseKey, SLOT( setText(const QString&) ) );
    connect( kcfg__IMEngine_Table_DeletePhraseKey, SIGNAL( textChanged(const QString&) ), deleteButton, SLOT( setShortcuts(const QString&) ) );
    connect( deleteButton, SIGNAL( setEditorText(const QString&) ), kcfg__IMEngine_Table_DeletePhraseKey, SLOT( setText(const QString&) ) );
    connect( kcfg__IMEngine_Table_FullWidthLetterKey, SIGNAL( textChanged(const QString&) ), letterButton, SLOT( setShortcuts(const QString&) ) );
    connect( letterButton, SIGNAL( setEditorText(const QString&) ), kcfg__IMEngine_Table_FullWidthLetterKey, SLOT( setText(const QString&) ) );
    connect( kcfg__IMEngine_Table_FullWidthPunctKey, SIGNAL( textChanged(const QString&) ), puncButton, SLOT( setShortcuts(const QString&) ) );
    connect( puncButton, SIGNAL( setEditorText(const QString&) ), kcfg__IMEngine_Table_FullWidthPunctKey, SLOT( setText(const QString&) ) );
    connect( kcfg__IMEngine_Table_ModeSwitchKey, SIGNAL( textChanged(const QString&) ), modeButton, SLOT( setShortcuts(const QString&) ) );
    connect( modeButton, SIGNAL( setEditorText(const QString&) ), kcfg__IMEngine_Table_ModeSwitchKey, SLOT( setText(const QString&) ) );

    // buddies
    textLabel1_2->setBuddy( kcfg__IMEngine_Table_FullWidthLetterKey );
    textLabel1_3->setBuddy( kcfg__IMEngine_Table_ModeSwitchKey );
    textLabel1->setBuddy( kcfg__IMEngine_Table_FullWidthPunctKey );
    textLabel1_4_2->setBuddy( kcfg__IMEngine_Table_AddPhraseKey );
    textLabel1_4_2_2->setBuddy( kcfg__IMEngine_Table_DeletePhraseKey );
}

/*
 *  Destroys the object and frees any allocated resources
 */
GenericTableSettingsUI::~GenericTableSettingsUI()
{
    // no need to delete child widgets, Qt does it all for us
}

/*
 *  Sets the strings of the subwidgets using the current
 *  language.
 */
void GenericTableSettingsUI::languageChange()
{
    setCaption( tr2i18n( "Generic Table" ) );
    kcfg__IMEngine_Table_ShowPrompt->setText( tr2i18n( "Show &prompt" ) );
    kcfg__IMEngine_Table_ShowKeyHint->setText( tr2i18n( "Show key &hint" ) );
    kcfg__IMEngine_Table_UserTableBinary->setText( tr2i18n( "Save &user table in binary format" ) );
    kcfg__IMEngine_Table_UserPhraseFirst->setText( tr2i18n( "Show the u&ser defined phrases first" ) );
    kcfg__IMEngine_Table_LongPhraseFirst->setText( tr2i18n( "Show &longer phrases first" ) );
    tabWidget2->changeTab( tab, tr2i18n( "General" ) );
    textLabel1_2->setText( tr2i18n( "Full width &letter" ) );
    textLabel1_3->setText( tr2i18n( "&Mode switch" ) );
    textLabel1->setText( tr2i18n( "Full width &punctuation" ) );
    textLabel1_4_2->setText( tr2i18n( "&Add phrase" ) );
    textLabel1_4_2_2->setText( tr2i18n( "&Delete phrase" ) );
    tabWidget2->changeTab( TabPage, tr2i18n( "Keyboard" ) );
}

#include "generictableui.moc"
