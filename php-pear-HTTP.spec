%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - miscellaneous HTTP utilities
Summary(pl):	%{_pearname} - ró¿ne narzêdzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.3.6
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b166af8069febd24699df675cf0d5b0f
URL:		http://pear.php.net/package/HTTP/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0.6
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-PEAR
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa HTTP jest klas± ze statycznymi metodami ró¿nych zwi±zanych z
HTTP rzeczy, jak formatowanie daty czy negocjacja jêzyka.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

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
