#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Plugins for Dolphin to view various VCS files
Name:		plasma6-dolphin-plugins
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/dolphin-plugins/-/archive/%{gitbranch}/dolphin-plugins-%{gitbranchd}.tar.bz2#/dolphin-plugins-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/dolphin-plugins-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(DolphinVcs) >= 6.0.0
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Network)
Requires:	plasma6-dolphin

%description
This package contains various plugins for dolphin.

%files -f all.lang
%{_qtdir}/plugins/dolphin/vcs/*.so
%{_qtdir}/plugins/kf6/kfileitemaction/mountisoaction.so
%{_qtdir}/plugins/kf6/kfileitemaction/makefileactions.so
%{_datadir}/qlogging-categories6/dolphingit.categories
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/metainfo/org.kde.dolphin-plugins.metainfo.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n dolphin-plugins-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja \
	-DBUILD_WITH_QT6:BOOL=ON

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang all --all-name --with-html
