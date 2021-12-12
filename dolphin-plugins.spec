%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plugins for Dolphin to view various VCS files
Name:		dolphin-plugins
Version:	21.12.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(DolphinVcs)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
Conflicts:	kdesdk4-core < 1:4.11.0
Requires:	dolphin >= 1:15.12.0

%description
This package contains various plugins for dolphin.

%files -f all.lang
%{_qt5_plugindir}/dolphin/vcs/*.so
%{_qt5_plugindir}/kf5/kfileitemaction/mountisoaction.so
%{_kde5_datadir}/config.kcfg/*.kcfg
%{_datadir}/metainfo/org.kde.dolphin-plugins.metainfo.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang all --all-name --with-html
