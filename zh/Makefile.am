## Makefile.am -- Process this file with automake to produce Makefile.in
## Copyright (C) 2002 James Su
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2, or (at your option)
## any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

scim_tables_source = \
		Array30.txt.in		\
		CangJie.txt.in		\
		Cantonese.txt.in	\
		Dayi3.txt.in		\
		Erbi.txt.in		\
		Erbi-QS.txt.in          \
		EZ.txt.in		\
		Jyutping.txt.in		\
		Simplex.txt.in		\
		Wubi.txt.in		\
		Ziranma.txt.in		\
		ZhuYin.txt.in

scim_tables = \
		Array30.txt		\
		CangJie.txt		\
		Cantonese.txt		\
		Dayi3.txt		\
		Erbi.txt		\
		Erbi-QS.txt             \
		EZ.txt			\
		Jyutping.txt		\
		Simplex.txt		\
		Wubi.txt		\
		Ziranma.txt		\
		ZhuYin.txt

scim_tables_bindir = $(SCIM_TABLEDIR)
scim_tables_bin_DATA = \
		Array30.bin	\
		CangJie.bin	\
		Cantonese.bin	\
		Dayi3.bin	\
		Erbi.bin	\
		Erbi-QS.bin     \
		EZ.bin		\
		Jyutping.bin	\
		Simplex.bin	\
		Wubi.bin	\
		Ziranma.bin	\
		ZhuYin.bin


EXTRA_DIST = $(scim_tables_source) README-Erbi.txt README-CangJie.txt

CLEANFILES = $(scim_tables_bin_DATA) *.bak

DISTCLEANFILES = $(scim_tables)

.txt.bin:
	$(SCIM_MAKE_TABLE) $< -b -o $@

