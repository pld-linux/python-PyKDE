%define		module		PyKDE
%define		vendor_ver	3.11.3
%define		vendor_rel	%{nil}
%define		fn_ver		%{vendor_ver}%{vendor_rel}

Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
# Version:	%{vendor_ver}.%{vendor_rel}
Version:        %{vendor_ver}
#Release:	0.%{vendor_rel}.1
Release:	1
License:	GPL
Group:		Libraries/Python
# Source0:	http://dl.sourceforge.net/sourceforge/pykde/%{module}-%{vendor_ver}.tar.gz
# Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{vendor_ver}rc2.tar.gz
# Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{version}.tar.gz
Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{fn_ver}.tar.gz
# Source0-md5:	7e0b2df3d5f9718833238501c3a21e96
# Source0-size:	1254776
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	perl-base
BuildRequires:	python-devel 
BuildRequires:	python-PyQt-devel >= 3.11
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= %{vendor_ver}
%pyrequires_eq	python
Requires:	OpenGL
Requires:	python-PyQt >= %{vendor_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sipfilesdir           %{_datadir}/sip

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

# fix copy-pasto from PyQt
# (-d/-v args were not used, pykdemoddir/pykdesipdir couldn't be overridden)
%{__perl} -pi -e 's/opt_pyqtmoddir/opt_pykdemoddir/;s/opt_pyqtsipdir/opt_pykdesipdir/' \
	configure.py

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
%{py_sitedir}/*.py[co]
%{py_sitedir}/lib*.so*
#%%attr(755,root,root)
