%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Miscellaneous HTTP utilities
Summary(pl):	%{_pearname} - R�ne narz�dzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3420e720e0c5c401c0e732443dc6832d
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa HTTP jest klas� ze statycznymi metodami r�nych zwi�zanych z
HTTP rzeczy, jak formatowanie daty czy negocjacja j�zyka.

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
