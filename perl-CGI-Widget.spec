#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Widget
Summary:	CGI::Widget - base class for CGI::Widget::
Summary(pl.UTF-8):	CGI::Widget - klasa bazowa dla CGI::Widget::
Name:		perl-CGI-Widget
Version:	0.15
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70a57a75c17696fe57590efbaab787f8
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-CGI
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CGI::Widget module's purpose is to allow authors of CGI or other
dynamically generated HTML documents an easy way to create common,
and possibly complex, page elements.

%description -l pl.UTF-8
Zadaniem CGI::Widget jest udostępnienie autorom skryptów CGI (lub
korzystającym z innych technik dynamicznego tworzenia dokumentów HTML)
prostego sposobu na tworzenie wspólnych i możliwie złożonych elementów
stron.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
