%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Miscellaneous HTTP utilities
Summary(pl):	%{_pearname} - Ró¿ne narzêdzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.3.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d223e8065322a9678051183f1b42ad00
URL:		http://pear.php.net/package/HTTP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
