%define		module		PyKDE
%define		snap		20051013

Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
Version:	4.0.0
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/PyKDE-snapshot%{snap}.tar.gz
# Source0-md5:	2e9d02b0b42b2892e5cf925d1ef7b6f6
Patch0:		%{name}-debian-4.patch
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	python-devel
BuildRequires:	python-PyQt-devel >= 3.13-2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
Requires:	OpenGL
Requires:	python-PyQt >= 3.13
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

%prep
%setup -q -n PyKDE-snapshot%{snap}

%build
python configure.py \
	-d %{py_sitedir} \
	-n %{_libdir} \
	-v %{_sipfilesdir} \
	-c -j 3

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fPIC -pipe -w -D_REENTRANT" \
	LINK="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py[co]
%{py_sitedir}/*.so
%{_datadir}/sip/*
