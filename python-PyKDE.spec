%include	/usr/lib/rpm/macros.python
%define		module	PyKDE
%define fnver 3.5-2
#%%define         snap 20030413    
Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
#Version:	3.5.0.snap%{snap}
Version:	3.5
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:        http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{fnver}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	python-devel >= 2.2.2
# BuildRequires:	kde-devel >= 3.1.1
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 3.5.0.snap20030405
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	kdelibs-devel >= 3.1.1a
%requires_eq	sip
%pyrequires_eq	python
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
TODO

%description -l pl
TODO

%prep
%setup -q -n %{module}-%{fnver}

%build
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir}}
python build.py \
        -c -q %{_prefix} -i %{_includedir}/qt -l qt-mt \
        -d %{py_sitedir} \
     -t %{_includedir} 

        # -d $RPM_BUILD_ROOT%{py_sitedir} \

%install

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so*
