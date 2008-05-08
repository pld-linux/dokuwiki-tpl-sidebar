%define		_snap	2007-03-12
%define		_ver	%(echo %{_snap} | tr -d -)
%define		_tpl	sidebar
Summary:	Sidebar navigation with DokuWiki
Summary(pl.UTF-8):	Nawigacja po sidebarze przy użyciu DokuWiki
Name:		dokuwiki-tpl-sidebar
Version:	%{_ver}
Release:	1
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

%description
Better navigation with DokuWiki. Features a navigation sidebar, a
tagline, highlighting the current page in the sidebar (unique
feature!), using the page heading as link text automatically. Retains
the default DokuWiki look and feel as much as possible.

%description -l pl.UTF-8
Lepsza nawigacja przy użyciu DokuWiki. Opiera się na sidebarze
nawigacyjnym, pasku podświetlającym aktualną stronę na sidebarze
(co jest unikalną cechą!), przy automatycznym użyciu nagłówka strony
jako tekstu odnośnika. Zachowuje domyślny wygląd i zachowanie DokuWiki
na ile to możliwe.

%prep
%setup -q -n %{_tpl}

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template']    = '%{_tpl}';

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
