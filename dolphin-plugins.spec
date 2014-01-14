Summary:	Plugins for Dolphin to view various VCS files
Name:		dolphin-plugins
Version:	4.12.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
Conflicts:	kdesdk4-core < 1:4.11.0

%description
Plugins for Dolphin to view various VCS files:
 - git
 - bazaar
 - mercurial (hg)
 - subversion (svn)

%files
%{_kde_libdir}/kde4/fileviewgitplugin.so
%{_kde_libdir}/kde4/fileviewsvnplugin.so
%{_kde_libdir}/kde4/fileviewbazaarplugin.so
%{_kde_libdir}/kde4/fileviewhgplugin.so
%{_kde_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_kde_services}/fileviewgitplugin.desktop
%{_kde_services}/fileviewsvnplugin.desktop
%{_kde_services}/fileviewbazaarplugin.desktop
%{_kde_services}/fileviewhgplugin.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Jan 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
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
