%define		module		PyKDE
Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
Version:	3.16.0
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.com/Downloads/PyKDE3/%{module}-%{version}.tar.gz
# Source0-md5:	92fa0f7d6063dc2aad97d5302975ca76
Patch0:		%{name}-make_install.patch
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

%description -l pl
PyKDE jest zbiorem dowi±zañ do KDE dla jêzyka Python. Dowi±zania s±
zaimplementowane jako zbiór modu³ów Pythona: dcop, kdecore, kdesu,
kdefix (KDE 3.0 i pó¼niejsze), kdeui, kio, kfile, kparts, khtml, kjs,
kspell i kdeprint (KDE 2.2.0 i pó¼niejsze). Modu³y odpowiadaj±
bibliotekom w pakiecie kdelibs. PyKDE wspiera prawie wszystkie klasy i
metody w wymienionych bibliotekach.

%package devel
Summary:	Files needed to build other bindings based on KDE
Summary(pl):	Pliki potrzebne do budowania innych dowi±zañ bazowanych na KDE
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-sip-devel

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the KDE classes.

%description devel -l pl
Pliki potrzebne do budowania innych dowi±zañ do klas C++
dziedzicz±cych z dowolnej klasy KDE.

%prep
%setup -q -n PyKDE-%{version}
%patch0 -p1

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
ln -sf kde3/libkonsolepart.so $RPM_BUILD_ROOT%{_libdir}/libkonsolepart.so

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

install contrib/kdepyuic $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/kdepyuic
%{py_sitedir}/*.py[co]
%{py_sitedir}/*.so

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/*
%attr(755,root,root) %{_bindir}/kdepyuic
