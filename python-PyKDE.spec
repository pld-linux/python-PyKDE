%define		module		PyKDE
Summary:	Python bindings for KDE
Summary(pl.UTF-8):	Dowiązania do KDE dla Pythona
Name:		python-%{module}
Version:	3.16.1
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/Downloads/PyKDE3/%{module}-%{version}.tar.bz2
# Source0-md5:	986e67ced4753cac5a4b7be8031ad64e
Patch0:		%{name}-make_install.patch
Patch1:		%{name}-py2.5.patch
Patch2:		%{name}-sip.patch
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdebase-common-filemanagement
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	python-PyQt-devel >= 3.17
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 2:4.4.1
%pyrequires_eq	python-libs
Requires:	OpenGL
Requires:	python-PyQt >= 3.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir		%{_datadir}/sip

%description
PyKDE is a set of Python bindings for the KDE desktop environment. The
bindings are implemented as a set of Python modules: dcop, kdecore,
kdesu, kdefx (KDE 3.0 and later), kdeui, kio, kfile, kparts, khtml,
kjs, kspell and kdeprint (KDE 2.2.0 and later). The modules correspond
to libraries in the kdelibs package. PyKDE supports nearly all classes
and methods in these libraries.

%description -l pl.UTF-8
PyKDE jest zbiorem dowiązań do KDE dla języka Python. Dowiązania są
zaimplementowane jako zbiór modułów Pythona: dcop, kdecore, kdesu,
kdefix (KDE 3.0 i późniejsze), kdeui, kio, kfile, kparts, khtml, kjs,
kspell i kdeprint (KDE 2.2.0 i późniejsze). Moduły odpowiadają
bibliotekom w pakiecie kdelibs. PyKDE wspiera prawie wszystkie klasy i
metody w wymienionych bibliotekach.

%package devel
Summary:	Files needed to build other bindings based on KDE
Summary(pl.UTF-8):	Pliki potrzebne do budowania innych dowiązań bazowanych na KDE
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the KDE classes.

%description devel -l pl.UTF-8
Pliki potrzebne do budowania innych dowiązań do klas C++
dziedziczących z dowolnej klasy KDE.

%prep
%setup -q -n PyKDE-%{version}
#% patch0 -p1
#%patch1 -p1

%{__sed} -i -e '1s,#!.*/bin/env python,#!%{__python},' contrib/kdepyuic

%build
python configure.py \
	-c -j 10 \
	-d %{py_sitedir} \
	-n %{_libdir} \
	-v %{_sipfilesdir} \
	-k %{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# FIXME: shouldn't this library be packaged?
ln -sf kde3/libkonsolepart.so $RPM_BUILD_ROOT%{_libdir}/libkonsolepart.so

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install contrib/kdepyuic $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/*
%attr(755,root,root) %{_bindir}/kdepyuic
