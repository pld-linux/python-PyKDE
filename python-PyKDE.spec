# TODO: Check if it builds on NEST/AC (blindly merged from RA)
# - Fix check of libpython.a - We don't need it in PLD

%include	/usr/lib/rpm/macros.python
%define		module	PyKDE
%define vendor_ver 3.8
%define vendor_rel 0
#%%define fn_ver %{vendor_ver}.%{vendor_rel}

Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
Version:        %{vendor_ver}.%{vendor_rel}
Release:	0.1
License:	GPL
Group:		Libraries/Python
# Source0:	http://dl.sourceforge.net/sourceforge/pykde/%{module}-%{vendor_ver}.tar.gz
# Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{vendor_ver}rc2.tar.gz
Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{version}.tar.gz
# Source0-md5:	c917602653ff79b318734d51aa875fb5
Patch0:         %{name}-p2.3-PyQT3.8fix.patch
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdelibs-devel >= 3.1.1a
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	python-PyQt-devel >= 3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= %{vendor_ver}
%pyrequires_eq	python
Requires:	OpenGL
Requires:	python-PyQt >= %{vendor_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define          _sipfilesdir         /usr/share/sip

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
%setup -q -n %{module}-%{version}

%build
KDEDIR=%{_prefix}
python build.py \
        -q %{_prefix} \
        -k %{_prefix} \
        -i %{_includedir}/qt \
        -d $RPM_BUILD_ROOT%{py_sitedir} \
        -t %{py_libdir} \
        -s %{py_sitedir} \
	-c- # NOTE c+ makes compilation 5 times faster and eats more memmory than my 256/256 MB Xed machine has :/
            #      Also it may couse failure of linking of huge object files on some archs.
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir}}
%{__make} install
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%{py_sitedir}/lib*.so*
