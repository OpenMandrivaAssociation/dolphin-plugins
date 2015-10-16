%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plugins for Dolphin to view various VCS files
Name:		dolphin-plugins
Version:	15.08.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	kde-baseapps-devel
BuildRequires:	cmake(DolphinVcs)
BuildRequires:	cmake(KF5KDELibs4Support)

Conflicts:	kdesdk4-core < 1:4.11.0

%description
Plugins for Dolphin to view various VCS files:
 - bazaar
 - dropbox
 - git
 - mercurial (hg)
 - subversion (svn)

%files
%{_qt5_plugindir}/fileviewbazaarplugin.so
%{_qt5_plugindir}/fileviewdropboxplugin.so
%{_qt5_plugindir}/fileviewgitplugin.so
%{_qt5_plugindir}/fileviewsvnplugin.so
%{_kde5_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kde5_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kde5_services}/fileviewbazaarplugin.desktop
%{_kde5_services}/fileviewdropboxplugin.desktop
%{_kde5_services}/fileviewgitplugin.desktop
%{_kde5_services}/fileviewsvnplugin.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
