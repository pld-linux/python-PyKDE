# TODO:
# - Make build install process more PLD conforming.

%include	/usr/lib/rpm/macros.python
%define		module	PyKDE
%define vendor_ver 3.7
%define vendor_rel 2
%define fn_ver %{vendor_ver}-%{vendor_rel}

Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
Version:	%{vendor_ver}.%{vendor_rel}
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/sourceforge/pykde/%{module}-%{vendor_ver}-%{vendor_rel}.tar.gz
# Source0-md5:	7252731d6933ddc89ba579738bd903aa
Patch0:         %{name}-setShared_args_num.patch
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	kdelibs-devel >= 3.1.1a
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	python-PyQt-devel >= 3.7
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= %{vendor_ver}
%pyrequires_eq	python
Requires:	OpenGL
Requires:	python-PyQt >= 3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6
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
kspell, i kdeprint (KDE 2.2.0 i pó¼niejsze). Modu³y odpowiadaj±
bibliotekom w pakiecie kdelibs. PyKDE wspiera prawie wszystkie klasy i
metody w wymienionych bibliotekach.

%prep
%setup -q -n %{module}-%{fn_ver}
%patch0 -p1

%build
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir}}

cp  %{py_sitedir}/libqtcmodule.so $RPM_BUILD_ROOT%{py_sitedir}/

DESTDIR=$RPM_BUILD_ROOT 
python build.py \
        -q %{_prefix} -i %{_includedir}/qt -l qt-mt \
        -d $RPM_BUILD_ROOT%{py_sitedir} \
        -t %{_includedir} \
	-c+ # makes compilation 5 times faster and eats more memmory than my 256/256 MB Xed machine has :/

%install
rm -rf $RPM_BUILD_ROOT
export LIBRARY_PATH=$RPM_BUILD_ROOT/%{py_sitedir}

%{__make} install

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%{py_sitedir}/lib*.so*
