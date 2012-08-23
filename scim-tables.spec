%define nam             scim-tables
%define ver             0.4.3
%define rel             1

%define scim_version	0.99.7

Summary:	Data files for SCIM Generic Table input method module
Name:		%{nam}
Version:	%{ver}
Release:	%{rel}
License:	GPL
Group:		System Environment/Libraries
URL:		http://www.turbolinux.com.cn/~suzhe/scim
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Source0:	%{name}-%{version}.tar.gz
#NoSource:	0

PreReq:		/sbin/ldconfig, /bin/sh, /usr/bin/scim-make-table
BuildRequires:	scim >= %{scim_version}

%description
This package includes many data files for SCIM Generic Table input method module.

The data files are came from unicon and xcin.

%package zh
Summary:	Data files for Chinese
Group:		System Environment/Libraries
Requires:	scim >= %{scim_version}

%description zh
This package includes table IM data files for Chinese.

The data files are came from unicon and xcin.

%package ja
Summary:	Data files for Japanese
Group:		System Environment/Libraries
Requires:	scim >= %{scim_version}

%description ja
This package includes table IM data files for Japanese.

The data files are came from unicon.

%package ko
Summary:	Data files for Korean
Group:		System Environment/Libraries
Requires:	scim >= %{scim_version}

%description ko
This package includes table IM data files for Korean.

The data files are came from unicon.

%package additional
Summary:	Data files for additional languages.
Group:		System Environment/Libraries
Requires:	scim >= %{scim_version}

%description additional
This package includes table IM data files for additional languages,
such as Russian etc..

#--------------------------------------------------

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-%{version}

%build
%configure

make 

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install 

%clean
rm -rf ${RPM_BUILD_ROOT}

%post

%postun

%files zh
%defattr(-, root, root)
%doc zh/README-Erbi.txt zh/README-CangJie.txt
/usr/share/scim/tables/Array30.bin
/usr/share/scim/tables/CangJie.bin
/usr/share/scim/tables/Cantonese.bin
/usr/share/scim/tables/Dayi3.bin
/usr/share/scim/tables/Erbi.bin
/usr/share/scim/tables/Erbi-QS.bin
/usr/share/scim/tables/EZ.bin
/usr/share/scim/tables/Jyutping.bin
/usr/share/scim/tables/Simplex.bin
/usr/share/scim/tables/Wubi.bin
/usr/share/scim/tables/Ziranma.bin
/usr/share/scim/tables/ZhuYin.bin
/usr/share/scim/icons/Array30.png
/usr/share/scim/icons/CangJie.png
/usr/share/scim/icons/Cantonese.png
/usr/share/scim/icons/Dayi.png
/usr/share/scim/icons/Erbi.png
/usr/share/scim/icons/Erbi-QS.png
/usr/share/scim/icons/EZ.png
/usr/share/scim/icons/Jyutping.png
/usr/share/scim/icons/Simplex.png
/usr/share/scim/icons/Wubi.png
/usr/share/scim/icons/Ziranma.png
/usr/share/scim/icons/ZhuYin.png

%files ja
%defattr(-, root, root)
%doc ja/kanjidic_licence.html ja/kanjidic_doc.html
/usr/share/scim/tables/HIRAGANA.bin
/usr/share/scim/tables/KATAKANA.bin
/usr/share/scim/tables/Nippon.bin
/usr/share/scim/icons/HIRAGANA.png
/usr/share/scim/icons/KATAKANA.png
/usr/share/scim/icons/Nippon.png

%files ko
%defattr(-, root, root)
/usr/share/scim/tables/Hangul.bin
/usr/share/scim/tables/Hanja.bin
/usr/share/scim/icons/Hangul.png
/usr/share/scim/icons/Hanja.png

%files additional
%defattr(-, root, root)
/usr/share/scim/tables/Amharic.bin
/usr/share/scim/tables/Yawerty.bin
/usr/share/scim/icons/Amharic.png
/usr/share/scim/icons/Yawerty.png

#--------------------------------------------------

%changelog
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
