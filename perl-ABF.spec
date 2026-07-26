%define upstream_name	    ABF
%define git		    20130102

Name:		perl-%{upstream_name}
Version:	0.01
Release:	%{?git:0.%git.}4
Summary:	Perl implementation of ABF API
License:	GPLv3+
Group:		Development/Other
URL:		https://github.com/mikhirev/ABF
Source0:	%{upstream_name}-%{git}.tar.xz
BuildRequires:	make
BuildRequires:	perl-devel
# (tpg) for checks
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(JSON)
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
