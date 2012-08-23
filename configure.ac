# Process this file with autoconf to produce a configure script.
AC_INIT(scim-tables, 0.4.3, suzhe@turbolinux.com.cn)
AC_CONFIG_SRCDIR([README])

SCIM_VERSION=0.99.7

AC_SUBST(SCIM_VERSION)

# Init automake stuff
AM_INIT_AUTOMAKE

PKG_CHECK_MODULES(SCIM,[scim >= $SCIM_VERSION])

# Checks for programs.
AC_PATH_PROG(SCIM_MAKE_TABLE, scim-make-table, no)

if test "x$SCIM_MAKE_TABLE" = "xno"; then
  AC_MSG_ERROR(Could not find a scim-make-table in your PATH)
fi

SCIM_ICONDIR=`$PKG_CONFIG --variable=icondir scim`
SCIM_TABLEDIR=`$PKG_CONFIG --variable=tabledir scim`

if test "x$SCIM_ICONDIR" = "x"; then
  SCIM_ICONDIR=/usr/share/scim/icons
fi

if test "x$SCIM_TABLEDIR" = "x"; then
  SCIM_TABLEDIR=/usr/share/scim/tables
fi

AC_SUBST(ac_aux_dir)
AC_SUBST(SCIM_MAKE_TABLE)
AC_SUBST(SCIM_ICONDIR)
AC_SUBST(SCIM_TABLEDIR)

AC_CONFIG_FILES([Makefile
		 zh/Makefile
		 zh/Array30.txt
		 zh/CangJie.txt
		 zh/Cantonese.txt
		 zh/Dayi3.txt
		 zh/Erbi.txt
		 zh/Erbi-QS.txt
		 zh/EZ.txt
		 zh/Jyutping.txt
		 zh/Simplex.txt
		 zh/Wubi.txt
		 zh/Ziranma.txt
		 zh/ZhuYin.txt
		 ja/Makefile
		 ja/HIRAGANA.txt
		 ja/KATAKANA.txt
		 ja/Nippon.txt
		 ko/Makefile
		 ko/Hangul.txt
		 ko/Hanja.txt
		 additional/Makefile
		 additional/Yawerty.txt
		 additional/Amharic.txt
		 icons/Makefile
		 scim-tables.spec])
AC_OUTPUT
