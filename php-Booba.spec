
%define		_unix_name	php-booba

%include	/usr/lib/rpm/macros.php
Summary:	Simple framework for developing web applications
Summary(pl):	Zestaw klas ułatwiających tworzenie aplikacji internetowych w PHP
Name:		php-Booba
Version:	0.2.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# dl.sf.net seems to be down...
Source0:	http://osdn.dl.sourceforge.net/php-booba/%{_unix_name}-%{version}.tar.bz2
# Source0-md5:	82e3aa8886ba570b128e0741edd89bf1
URL:		http://sourceforge.net/projects/php-booba/
BuildRequires:	rpm-php-pearprov >= 4.3
Requires:	php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
php-Booba is a simple framework for developing Web applications. It
contains classes for validating incoming data from forms, a powerful
ticket-based request handling system, and a very fast template system.

%description -l pl
php-Booba jest zestawem klas PHP ułatwiających tworzenie aplikacji
internetowych. Zawiera między innymi klasy wpomagające weryfikację
poprawności danych z wysyłanych formularzy, system obsługi żądań
oparty o mechanizm ticketów oraz bardzo szybki system szablonów.

%prep
%setup -q -n %{_unix_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir}/%{_unix_name},%{_datadir}/%{_unix_name}}

install include/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_unix_name}
install templates/simple/* $RPM_BUILD_ROOT%{_datadir}/%{_unix_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{php_pear_dir}/%{_unix_name}
%{_datadir}/%{_unix_name}
