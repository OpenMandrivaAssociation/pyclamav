Summary:	A Python interface to libclamav
Name:		pyclamav
Version:	0.4.0
Release:	%mkrel 3
License:	GPL
Group:		System/Libraries
URL:		http://xael.org/norman/python/pyclamav/index.html
Source0:	http://xael.org/norman/python/pyclamav/%{name}-%{version}.tar.bz2
BuildRequires:  clamav-devel >= 0.90
BuildRequires:	python-devel
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Python interface to libclamav.

%prep
%setup -q

%build
env CFLAGS="%{optflags}" python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python -- setup.py install \
	--root=%{buildroot} \
	--optimize=2

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README.txt CHANGELOG example.py
%attr(755,root,root) %{_libdir}/python2.5/site-packages/%{name}.so
%{_libdir}/python2.5/site-packages/%{name}*.egg-info


