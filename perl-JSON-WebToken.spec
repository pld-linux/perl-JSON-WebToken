#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	JSON
%define		pnam	WebToken
%include	/usr/lib/rpm/macros.perl
Summary:	JSON::WebToken - JSON Web Token (JWT) implementation
Name:		perl-JSON-WebToken
Version:	0.10
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a68a0e415493495c5d3c516d854de047
URL:		https://metacpan.org/release/JSON-WebToken/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl(Test::Mock::Guard) >= 0.07
BuildRequires:	perl-Test-Requires >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON::WebToken is JSON Web Token (JWT) implementation for Perl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/JSON/*.pm
%{perl_vendorlib}/JSON/WebToken
%{_mandir}/man3/*
