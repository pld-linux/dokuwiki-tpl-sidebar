%define		_snap	2007-03-12
%define		_ver	%(echo %{_snap} | tr -d -)
Summary:	Sidebar navigation with DokuWiki
Name:		dokuwiki-tpl-sidebar
Version:	%{_ver}
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.jandecaluwe.com/testwiki/lib/exe/fetch.php/navigation:sidebar-%{_snap}.tar.gz
# Source0-md5:	297db12e6a4fd2a745f4eb20ced0b09b
URL:		http://www.jandecaluwe.com/testwiki/doku.php/navigation:intro
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_tpldir		%{_dokudir}/lib/tpl/%{_tpl}
%define		_tpl		sidebar

%description
Better navigation with DokuWiki. Features a navigation sidebar, a
tagline, highlighting the current page in the sidebar (unique
feature!), using the page heading as link text automatically. Retains
the default dokuwiki look and feel as much as possible.

%prep
%setup -q -n %{_tpl}

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file: 
$conf['template']    = 'sidebar';

If you want a tagline, you can define it as follows: 
$conf['tagline']    = 'Your own tagline';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_tpldir}
cp -a . $RPM_BUILD_ROOT%{_tpldir}
rm -f $RPM_BUILD_ROOT%{_tpldir}/INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%{_tpldir}
