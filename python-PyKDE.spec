
%include	/usr/lib/rpm/macros.python
%define		module	PyKDE
%define vendor_ver 3.11
%define vendor_rel alpha4
%define fn_ver %{vendor_ver}-%{vendor_rel}

Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
# Version:        %{vendor_ver}.%{vendor_rel}
Version:        %{vendor_ver}
Release:	0.%{vendor_rel}.1
License:	GPL
Group:		Libraries/Python
# Source0:	http://dl.sourceforge.net/sourceforge/pykde/%{module}-%{vendor_ver}.tar.gz
# Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{vendor_ver}rc2.tar.gz
# Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{version}.tar.gz
Source0:	http://beauty.ant.gliwice.pl/bugs/%{module}-%{fn_ver}.tar.gz
# Source0-md5:	eb2312e1c6d68f90cb127b2d4c9879c3

URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	python-devel 
BuildRequires:	python-static
BuildRequires:	python-PyQt-devel >= 3.11
BuildRequires:	rpm-pythonprov
BuildRequires:	sip = %{vendor_ver}
%pyrequires_eq	python
Requires:	OpenGL
Requires:	python-PyQt = %{vendor_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define          _sipdir         /usr/share/sip

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
%setup -q -n %{module}-%{fn_ver}
#%%patch0 -p1

%build
KDEDIR=%{_prefix}
python configure.py \
        -d %{py_sitedir} \
	-v %{_sipdir} \
	-c -j 3 # 
        # -t %{py_libdir}/config \

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%{py_sitedir}/lib*.so*
