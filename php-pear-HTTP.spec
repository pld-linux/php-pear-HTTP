%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_pearname	%{_class}
Summary:	%{_class} - Miscellaneous HTTP utilities
Summary(pl):	%{_class} - Ró¿ne narzêdzie do HTTP
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

%description -l pl
Klasa HTTP jest klas± ze statycznymi metodami ró¿nych zwi±zanych z
HTTP rzeczy, jak formatowanie daty czy negocjacja jêzyka.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
