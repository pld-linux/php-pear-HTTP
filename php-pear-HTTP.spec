%define		_class		HTTP
%define		_status		stable
%define		_pearname	HTTP
Summary:	%{_pearname} - miscellaneous HTTP utilities
Summary(pl.UTF-8):	%{_pearname} - różne narzędzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.4.1
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6fe726d7304f81ac1fe866b7725512fa
URL:		http://pear.php.net/package/HTTP/
BuildRequires:	php-pear-PEAR >= 1:1.7.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.6
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-HTTP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa HTTP jest klasą ze statycznymi metodami różnych związanych z
HTTP rzeczy, jak formatowanie daty czy negocjacja języka.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
