%define unmangled_name proton-vpn-network-manager-openvpn
%define version 0.1.1
%define release 1

Prefix: %{_prefix}

Name: python3-%{unmangled_name}
Version: %{version}
Release: %{release}%{?dist}
Summary: %{unmangled_name} library

Group: ProtonVPN
License: GPLv3
Vendor: Proton Technologies AG <opensource@proton.me>
URL: https://github.com/ProtonVPN/%{unmangled_name}
Source0: %{unmangled_name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{unmangled_name}-%{version}-%{release}-buildroot

BuildRequires: python3-proton-vpn-api-core
BuildRequires: python3-proton-vpn-network-manager >= 0.6.3
BuildRequires: NetworkManager-openvpn
BuildRequires: NetworkManager-openvpn-gnome
BuildRequires: python3-setuptools

Requires: python3-proton-vpn-api-core
Requires: python3-proton-vpn-network-manager >= 0.6.3
Requires: NetworkManager-openvpn
Requires: NetworkManager-openvpn-gnome
Requires: python3-setuptools

%{?python_disable_dependency_generator}

%description
Package %{unmangled_name} library.


%prep
%setup -n %{unmangled_name}-%{version} -n %{unmangled_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%files -f INSTALLED_FILES
%{python3_sitelib}/proton/
%{python3_sitelib}/proton_vpn_network_manager_openvpn-%{version}*.egg-info/
%defattr(-,root,root)

%changelog
* Mon Sep 02 2024 Josep Llaneras <josep.llaneras@proton.ch> 0.1.1
- Deprecate this package

* Thu Jul 11 2024 Josep Llaneras <josep.llaneras@proton.ch> 0.1.0
- Add proton-vpn-api-core depencency

* Wed Apr 10 2024 Josep Llaneras <josep.llaneras@proton.ch> 0.0.7
- Do not override connection id in constructor

* Thu Apr 4 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.0.6
- Add UI friendly protocol name

* Wed Feb 28 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.0.5
- Refactor code

* Wed Jul 05 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.0.4
- Fix entry point in setup.py

* Tue Dec 13 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.0.3
- Fix proton loader ids

* Fri Nov 4 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.0.2
- Set up the VPN connection asynchronously

* Wed Jun 1 2022 Proton Technologies AG <opensource@proton.me> 0.0.1
- First RPM release
