%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Miscellaneous HTTP utilities
Summary(pl):	%{_pearname} - Ró¿ne narzêdzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	4d385175bcc29b200ca03f4c56d014d8
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

This class has in PEAR status: %{_status}.

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
