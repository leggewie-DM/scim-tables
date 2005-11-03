%define nam             scim-tables
%define ver             0.5.4
%define skim            1
%define rel             1

%define scim_version	1.4.0

%define build_scim_setup	1

Summary:	SCIM Generic Table IMEngine and its data files.
Name:		%{nam}
Version:	%{ver}
Release:	%{rel}
License:	GPL
Group:		System Environment/Libraries
URL:		http://sourceforge.net/projects/scim
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Source0:	%{name}-%{version}.tar.gz

PreReq:		/sbin/ldconfig, /bin/sh

Requires:	scim >= %{scim_version}
BuildRequires:	scim-devel >= %{scim_version}

Requires:	gtk2 >= 2.0.0
BuildRequires:	gtk2-devel >= 2.0.0

%if %{skim}
BuildRequires:	skim-devel >= 1.2.0
%endif

%description
This package includes Generic Table IMEngine for SCIM and many data files for it.

%if %{skim}
%package skim
Summary:        Skim support for Generic Table
Group:          System/I18n
Requires:	%{name} = %{version}
Requires:	skim >= 1.2.0

%description skim
This package includes Skim support for Generic Table IMEngine.
%endif

%package zh
Summary:	Data files for Chinese
Group:		System Environment/Libraries
Requires:	scim-tables >= %{ver}

%description zh
This package includes table IM data files for Chinese.

%package ja
Summary:	Data files for Japanese
Group:		System Environment/Libraries
Requires:	scim-tables >= %{ver}

%description ja
This package includes table IM data files for Japanese.

%package ko
Summary:	Data files for Korean
Group:		System Environment/Libraries
Requires:	scim-tables >= %{ver}

%description ko
This package includes table IM data files for Korean.

%package additional
Summary:	Data files for additional languages.
Group:		System Environment/Libraries
Requires:	scim-tables >= %{ver}

%description additional
This package includes table IM data files for additional languages,
such as Russian etc..

#--------------------------------------------------

%changelog
* Wed Jan 5 2005 James Su <suzhe@tsinghua.org.cn>
- Added Generic Table IMEngine module into this package.

* Sun Jun 20 2004 James Su <suzhe@tsinghua.org.cn>
- Added Amharic table.

* Mon Apr 05 2004 James Su <suzhe@tsinghua.org.cn>
- Updated Nippon table.
- Added Yawerty table for Russian.

* Fri Nov 28 2003 James Su <suzhe@turbolinux.com.cn>
- upgraded CangJie.txt.in, added README-CangJie.txt

* Tue Sep 02 2003 James Su <suzhe@turbolinux.com.cn>
- updated table format according to SCIM 0.8.0
- added icon files.

* Wed Feb 26 2003 James Su <suzhe@turbolinux.com.cn>
- updated table format according to SCIM 0.3.1.

* Mon Nov 04 2002 James Su <suzhe@turbolinux.com.cn>
- Initial release.
#--------------------------------------------------

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}

make 

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}/%{_libdir}/scim-1.0/*/*.{a,la}

%if %{skim}
rm -f $RPM_BUILD_ROOT//opt/kde3/lib/kde*/*.{a,la}
%endif

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%{_bindir}/scim-make-table
/usr/lib/scim-1.0/IMEngine/table.so
/usr/share/scim/icons/table.png
%if %{build_scim_setup}
/usr/lib/scim-1.0/SetupUI/table-imengine-setup.so
%endif
%{_datadir}/locale/*/LC_MESSAGES/scim-tables.mo

%files zh
%defattr(-, root, root)
%doc tables/zh/README-Erbi.txt tables/zh/README-CangJie.txt
/usr/share/scim/tables/Array30.bin
/usr/share/scim/tables/CangJie.bin
/usr/share/scim/tables/CangJie3.bin
/usr/share/scim/tables/Cantonese.bin
/usr/share/scim/tables/CantonHK.bin
/usr/share/scim/tables/Dayi3.bin
/usr/share/scim/tables/Erbi.bin
/usr/share/scim/tables/Erbi-QS.bin
/usr/share/scim/tables/EZ.bin
/usr/share/scim/tables/Jyutping.bin
/usr/share/scim/tables/Quick.bin
/usr/share/scim/tables/Simplex.bin
/usr/share/scim/tables/Stroke5.bin
/usr/share/scim/tables/Wu.bin
/usr/share/scim/tables/Wubi.bin
/usr/share/scim/tables/Ziranma.bin
/usr/share/scim/tables/ZhuYin.bin
/usr/share/scim/icons/Array30.png
/usr/share/scim/icons/CangJie.png
/usr/share/scim/icons/CangJie3.png
/usr/share/scim/icons/Cantonese.png
/usr/share/scim/icons/CantonHK.png
/usr/share/scim/icons/Dayi.png
/usr/share/scim/icons/Erbi.png
/usr/share/scim/icons/Erbi-QS.png
/usr/share/scim/icons/EZ.png
/usr/share/scim/icons/Jyutping.png
/usr/share/scim/icons/Quick.png
/usr/share/scim/icons/Simplex.png
/usr/share/scim/icons/Stroke5.png
/usr/share/scim/icons/Wu.png
/usr/share/scim/icons/Wubi.png
/usr/share/scim/icons/Ziranma.png
/usr/share/scim/icons/ZhuYin.png

%files ja
%defattr(-, root, root)
%doc tables/ja/kanjidic_licence.html tables/ja/kanjidic_doc.html tables/ja/kanjidic-permission-to-use-for-scim
/usr/share/scim/tables/HIRAGANA.bin
/usr/share/scim/tables/KATAKANA.bin
/usr/share/scim/tables/Nippon.bin
/usr/share/scim/icons/HIRAGANA.png
/usr/share/scim/icons/KATAKANA.png
/usr/share/scim/icons/Nippon.png

%files ko
%defattr(-, root, root)
/usr/share/scim/tables/Hangul.bin
/usr/share/scim/tables/HangulRomaja.bin
/usr/share/scim/tables/Hanja.bin
/usr/share/scim/icons/Hangul.png
/usr/share/scim/icons/Hanja.png

%files additional
%defattr(-, root, root)
/usr/share/scim/tables/Amharic.bin
/usr/share/scim/tables/Arabic.bin
/usr/share/scim/tables/Bengali-inscript.bin
/usr/share/scim/tables/Bengali-probhat.bin
/usr/share/scim/tables/Gujarati-inscript.bin
/usr/share/scim/tables/Gujarati-phonetic.bin
/usr/share/scim/tables/Hindi-inscript.bin
/usr/share/scim/tables/Hindi-phonetic.bin
/usr/share/scim/tables/IPA-X-SAMPA.bin
/usr/share/scim/tables/Kannada-inscript.bin
/usr/share/scim/tables/Kannada-kgp.bin
/usr/share/scim/tables/LaTeX.bin
/usr/share/scim/tables/Malayalam-inscript.bin
/usr/share/scim/tables/Nepali_Rom.bin
/usr/share/scim/tables/Nepali_Trad.bin
/usr/share/scim/tables/Punjabi-inscript.bin
/usr/share/scim/tables/Punjabi-jhelum.bin
/usr/share/scim/tables/Punjabi-phonetic.bin
/usr/share/scim/tables/Tamil-inscript.bin
/usr/share/scim/tables/Tamil-phonetic.bin
/usr/share/scim/tables/Telugu-inscript.bin
/usr/share/scim/tables/Thai.bin
/usr/share/scim/tables/Viqr.bin
/usr/share/scim/tables/Yawerty.bin

/usr/share/scim/icons/Amharic.png
/usr/share/scim/icons/Arabic.png
/usr/share/scim/icons/Bengali-inscript.png
/usr/share/scim/icons/Bengali-probhat.png
/usr/share/scim/icons/Gujarati-inscript.png
/usr/share/scim/icons/Gujarati-phonetic.png
/usr/share/scim/icons/Hindi-inscript.png
/usr/share/scim/icons/Hindi-phonetic.png
/usr/share/scim/icons/IPA-X-SAMPA.png
/usr/share/scim/icons/Kannada-inscript.png
/usr/share/scim/icons/Kannada-kgp.png
/usr/share/scim/icons/LaTeX.png
/usr/share/scim/icons/Malayalam-inscript.png
/usr/share/scim/icons/Nepali.png
/usr/share/scim/icons/Punjabi-inscript.png
/usr/share/scim/icons/Punjabi-jhelum.png
/usr/share/scim/icons/Punjabi-phonetic.png
/usr/share/scim/icons/Tamil-inscript.png
/usr/share/scim/icons/Tamil-phonetic.png
/usr/share/scim/icons/Telugu-inscript.png
/usr/share/scim/icons/Thai.png
/usr/share/scim/icons/Viqr.png
/usr/share/scim/icons/Yawerty.png


%if %{skim}
%files skim
%defattr(-, root, root)
/opt/kde3/lib/kde*/*.so
/opt/kde3/share/apps/skim/pics/scim-tables.png
/opt/kde3/share/config.kcfg/generictable.kcfg
/opt/kde3/share/locale/*/LC_MESSAGES/skim-scim-tables.mo
/opt/kde3/share/services/skimconfiguredialog/skimplugin_scim_table_config.desktop
%endif
