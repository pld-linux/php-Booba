
%define		_unix_name	php-booba

%include	/usr/lib/rpm/macros.php
Summary:	Simple framework for developing web applications
Summary(pl):	Zestaw klas u�atwiaj�cych tworzenie aplikacji internetowych w PHP
Name:		php-Booba
Version:	0.3.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# dl.sf.net seems to be down...
Source0:	http://osdn.dl.sourceforge.net/php-booba/%{_unix_name}-%{version}.tar.bz2
# Source0-md5:	6b2da92f303915b64652947baa772093
URL:		http://sourceforge.net/projects/php-booba/
BuildRequires:	rpm-php-pearprov >= 4.3
Requires:	php
Requires:	php-pcre
Requires:	php-pgsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
php-Booba is a simple framework for developing Web applications. It
contains classes for validating incoming data from forms, a powerful
ticket-based request handling system, and a very fast template system.

%description -l pl
php-Booba jest zestawem klas PHP u�atwiaj�cych tworzenie aplikacji
internetowych. Zawiera mi�dzy innymi klasy wpomagaj�ce weryfikacj�
poprawno�ci danych z wysy�anych formularzy, system obs�ugi ��da�
oparty o mechanizm ticket�w oraz bardzo szybki system szablon�w.

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
