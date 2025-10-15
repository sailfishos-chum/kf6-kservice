%global  kf_version 6.7.0

Name:    kf6-kservice
Summary: Query information about installed applications
Version: 6.18.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: %{name}-%{version}.tar.bz2

# upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: kf6-extra-cmake-modules >= %{kf_version}

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kservice6 --all-name

%files -f kservice6.lang
%license LICENSES/*
%{_kf6_bindir}/kbuildsycoca6
%{_kf6_libdir}/libKF6Service.so.*
%{_kf6_datadir}/qlogging-categories6/kservice.categories
%{_kf6_datadir}/qlogging-categories6/kservice.renamecategories

%files devel
%{_kf6_includedir}/KService
%{_kf6_libdir}/cmake/KF6Service
%{_kf6_libdir}/libKF6Service.so
