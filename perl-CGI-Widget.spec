#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Widget
Summary:	CGI::Widget - Base class for CGI::Widget::
Summary(pl):	CGI::Widget - klasa bazowa dla CGI::Widget::
Name:		perl-CGI-Widget
Version:	0.15
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CGI::Widget module's purpose is to allow authors of CGI or other
dynamically generated HTML documents an easy way to create common,
and possibly complex, page elements.

%description -l pl
Zadaniem CGI::Widget jest udostêpnienie autorom skryptów CGI (lub
korzystaj±cym z innych technik dynamicznego tworzenia dokumentów HTML)
prostego sposobu na tworzenie wspólnych i mo¿liwie z³o¿onych elementów
stron.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
