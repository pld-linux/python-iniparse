Summary:	Python Module for Accessing and Modifying Configuration Data in INI files
Name:		python-iniparse
Version:	0.4
Release:	2
Group:		Development/Libraries
Source0:	http://iniparse.googlecode.com/files/iniparse-%{version}.tar.gz
# Source0-md5:	5e573e9e9733d97623881ce9bbe5eca6
License:	MIT
URL:		http://code.google.com/p/iniparse/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iniparse is an INI parser for Python which is API compatible with the
standard library's ConfigParser, preserves structure of INI files
(order of sections & options, indentation, comments, and blank lines
are preserved when data is updated), and is more convenient to use.

%prep
%setup -q -n iniparse-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{_docdir}/iniparse-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{py_sitescriptdir}/iniparse
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/iniparse-*.egg-info
%endif
