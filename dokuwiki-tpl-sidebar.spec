%define		snap	2009-01-26
%define		ver	%(echo %{snap} | tr -d -)
%define		tpl	sidebar
Summary:	Sidebar navigation with DokuWiki
Summary(pl.UTF-8):	Nawigacja po sidebarze przy użyciu DokuWiki
Name:		dokuwiki-tpl-sidebar
Version:	%{ver}
Release:	4
License:	GPL
Group:		Applications/WWW
Source0:	http://dokuwiki.jalakai.co.uk/template-sidebar-rc%{snap}.zip
# Source0-md5:	7a36b63e86d00f72eecae2ba80334fdd
Patch0:		backlink-rightside.patch
Patch1:		more-buttons.patch
Patch2:		acl-check.patch
URL:		http://www.dokuwiki.org/template:sidebar
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20090126
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
Better navigation with DokuWiki. Features a navigation sidebar, a
tagline, highlighting the current page in the sidebar (unique
feature!), using the page heading as link text automatically. Retains
the default DokuWiki look and feel as much as possible.

%description -l pl.UTF-8
Lepsza nawigacja przy użyciu DokuWiki. Opiera się na sidebarze
nawigacyjnym, pasku podświetlającym aktualną stronę na sidebarze (co
jest unikalną cechą!), przy automatycznym użyciu nagłówka strony jako
tekstu odnośnika. Zachowuje domyślny wygląd i zachowanie DokuWiki na
ile to możliwe.

%prep
%setup -q -n %{tpl}
%patch0 -p1
%patch1 -p1
%patch2 -p1

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:

$conf['template']    = '%{tpl}';

If you want a tagline, you can define it as follows:
$conf['tagline']    = 'Your own tagline';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc INSTALL
%{tpldir}
