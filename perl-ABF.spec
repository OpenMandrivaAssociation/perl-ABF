%define upstream_name	    ABF
%define upstream_version    0.01
%define git		    20130102

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%{?git:0.%git.}3
Summary:	Perl implementation of ABF API
License:	GPLv3+
Group:		Development/Other
URL:		https://github.com/mikhirev/ABF
Source0:	%{upstream_name}-%{git}.tar.xz
BuildRequires:	perl-devel
# (tpg) for checks
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
This package provides perl classes for interaction with ABF.

%prep
%setup -q -n %{upstream_name}-%{git}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README.md
%{perl_vendorlib}/ABF*
%{_mandir}/man3/*
