Summary:	Helpful utilities for use with tla
Summary(pl):	Pomocne narzêdzia do u¿ywania z tla
Name:		tla-tools
# version - patch number from tla archive
Version:	0.0.81
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	%{name}--devo.tar.gz
# Source0-md5:	50124e0443c87b47a9ea5d9174dccdfe
URL:		http://wiki.gnuarch.org/moin.cgi/tla_2dtools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tla-tools is a package of helpful commands to use with the tla
program.

%description -l pl
tla-tools to pakiet pomocnych narzêdzi do u¿ywania z programem tla.

%prep
%setup -q -n %{name}--devo

%build
./configure \
	--prefix=%{__prefix} \
	--bindir=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
