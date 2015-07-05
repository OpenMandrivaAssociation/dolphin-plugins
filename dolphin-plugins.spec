%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plugins for Dolphin to view various VCS files
Name:		dolphin-plugins
Version:	15.04.3
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	kde-baseapps-devel
Conflicts:	kdesdk4-core < 1:4.11.0

%description
Plugins for Dolphin to view various VCS files:
 - bazaar
 - dropbox
 - git
 - mercurial (hg)
 - subversion (svn)

%files
%{_kde_libdir}/kde4/fileviewbazaarplugin.so
%{_kde_libdir}/kde4/fileviewdropboxplugin.so
%{_kde_libdir}/kde4/fileviewgitplugin.so
%{_kde_libdir}/kde4/fileviewhgplugin.so
%{_kde_libdir}/kde4/fileviewsvnplugin.so
%{_kde_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_kde_services}/fileviewbazaarplugin.desktop
%{_kde_services}/fileviewdropboxplugin.desktop
%{_kde_services}/fileviewgitplugin.desktop
%{_kde_services}/fileviewhgplugin.desktop
%{_kde_services}/fileviewsvnplugin.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:14.12.0-1
- New version 14.12.0

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2
- Update files (new plugin for dropbox)

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
