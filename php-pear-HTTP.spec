%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_pearname	%{_class}
Summary:	%{_class} - Miscellaneous HTTP utilities
Summary(pl):	%{_class} - R�ne narz�dzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

%description -l pl
Klasa HTTP jest klas� ze statycznymi metodami r�nych zwi�zanych z
HTTP rzeczy, jak formatowanie daty czy negocjacja j�zyka.

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
%{php_pear_dir}/*.php
