
%define		_unix_name	php-booba

#%include	/usr/lib/rpm/macros.php
Summary:	Simple framework for developing web applications
Summary(pl.UTF-8):   Zestaw klas ułatwiających tworzenie aplikacji internetowych w PHP
Name:		php-Booba
Version:	0.8.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/php-booba/%{_unix_name}-%{version}.tar.bz2
# Source0-md5:	af936c95ada9b2433fe0722b0e7d91d0
URL:		http://sourceforge.net/projects/php-booba/
BuildRequires:	docbook-utils
#BuildRequires:	rpm-php-pearprov >= 4.3
Requires:	php(pcre)
Requires:	php(pgsql)
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
php-Booba is a simple framework for developing Web applications. It
contains classes for validating incoming data from forms, a powerful
ticket-based request handling system, and a very fast template system.

%description -l pl.UTF-8
php-Booba jest zestawem klas PHP ułatwiających tworzenie aplikacji
internetowych. Zawiera między innymi klasy wpomagające weryfikację
poprawności danych z wysyłanych formularzy, system obsługi żądań
oparty o mechanizm ticketów oraz bardzo szybki system szablonów.

%package doc
Summary:	Documentation for php-Booba framework
Summary(pl.UTF-8):   Dokumentacja do systemu php-Booba
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for php-Booka framework.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla systemu php-Booba.

%prep
%setup -q -n %{_unix_name}-%{version}

%build
cd doc/pl
docbook2html main.docbook

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_phpsharedir}/%{_unix_name},%{_datadir}/%{_unix_name}}

install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{_unix_name}/template_plugins
install include/template_plugins/*.php $RPM_BUILD_ROOT%{_phpsharedir}/%{_unix_name}/template_plugins

install include/*.php $RPM_BUILD_ROOT%{_phpsharedir}/%{_unix_name}
install templates/simple/* $RPM_BUILD_ROOT%{_datadir}/%{_unix_name}

find doc -name \*.docbook -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_phpsharedir}/%{_unix_name}
%{_datadir}/%{_unix_name}

%files doc
%defattr(644,root,root,755)
%doc doc/*
