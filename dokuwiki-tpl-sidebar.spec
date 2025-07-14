%define		tpl	sidebar
Summary:	Sidebar navigation with DokuWiki
Summary(pl.UTF-8):	Nawigacja po sidebarze przy użyciu DokuWiki
Name:		dokuwiki-tpl-sidebar
Version:	20111110
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://dokuwiki.jalakai.co.uk/template-sidebar-rc2009-01-26.zip
# Source0-md5:	7a36b63e86d00f72eecae2ba80334fdd
Patch0:		backlink-rightside.patch
Patch1:		more-buttons.patch
Patch2:		acl-check.patch
Patch3:		%{name}-20101007.patch
Patch4:		dw-20101007.patch
Patch5:		%{name}-20110525.patch
Patch6:		%{name}-20111110.patch
URL:		http://www.dokuwiki.org/template:sidebar
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
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
%patch -P3 -p4
%patch -P4 -p1
%patch -P5 -p6
%patch -P6 -p4
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

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

while read file; do
	ln -sf ../../default/$file $RPM_BUILD_ROOT%{tpldir}/$file
done <<EOF
images/UWEB.png
images/apple-touch-icon.png
images/button-cc.gif
images/button-rss.png
images/link_icon.gif
images/mail_icon.gif
images/resizecol.png
images/tocdot2.gif
images/windows.gif
images/button-pld.png
EOF

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
