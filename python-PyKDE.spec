#TODO:
# - fix building

%include	/usr/lib/rpm/macros.python
%define		module	PyKDE
%define vendor_ver 3.5
%define vendor_rel 2
%define fn_ver %{vendor_ver}-%{vendor_rel}

#%%define         snap 20030413
Summary:	Python bindings for KDE
Summary(pl):	Dowi±zania do KDE dla Pythona
Name:		python-%{module}
#Version:	3.5.0.snap%{snap}
Version:	%{vendor_ver}.%{vendor_rel}
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.river-bank.demon.co.uk/download/PyKDE2/%{module}-%{fn_ver}.tar.gz
Patch0: 	%{name}-remove_modules_from_sipnames.patch
URL:		http://www.riverbankcomputing.co.uk/pykde/index.php
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	python-PyQt-devel >= 3.5.0.snap20030405
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	kdelibs-devel >= 3.1.1a
%pyrequires_eq	python
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6
%define          _sipfilesdir         /usr/share/sip

%description
TODO

%description -l pl
TODO

%prep
%setup -q -n %{module}-%{fn_ver}
%patch0 -p1

%build
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir}}
cp  %{py_sitedir}/libqtcmodule.so $RPM_BUILD_ROOT%{py_sitedir}/
# /tmp/python-PyKDE-3.5.2-root-matkor/usr/lib/python2.2/site-packages/libqtcmodule.so

python build.py \
        -c -q %{_prefix} -i %{_includedir}/qt -l qt-mt \
        -d $RPM_BUILD_ROOT%{py_sitedir} \
        -t %{_includedir}

        # -d %{py_sitedir} \

%install

rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so*
