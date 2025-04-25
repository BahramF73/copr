%define soname libfprint-tod-goodix-53xc

Name:           libfprint-2-tod1-goodix
Version:        0.0.6
Release:        %autorelease
Summary:        Goodix driver module for libfprint-2 Touch OEM Driver for XPS 13 9310 and G3 15 3590
License:        NonFree
Group:          Hardware/Mobile
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-goodix/+git/libfprint-2-tod1-goodix
BuildRequires:  git
BuildRequires:  pkgconfig(udev)
Requires:       libfprint-tod
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v27C6p538Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p533Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p530Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p5840d*dc*dsc*dp*ic*isc*ip*)

%description
This is user space driver for Goodix finger print module. Proprietary driver for the fingerprint reader on the Dell XPS 13 9310 and Dell G3 15 3590 - direct from Dell's Ubuntu repo. It should work for 27c6:538c, 27c6:533c, 27c6:530c, 27c6:5840.

%global debug_package %{nil}

%prep
git clone %{url}
cd libfprint-2-tod1-goodix

%build

%install
cd libfprint-2-tod1-goodix
install -dm 0755 %{buildroot}/%{_udevrulesdir}
install -dm 0755 %{buildroot}/%{_libdir}/libfprint-2/tod-1
install -m 0644 lib/udev/rules.d/60-%{name}.rules %{buildroot}/%{_udevrulesdir}/60-%{name}.rules
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/%{soname}-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/%{soname}-%{version}.so

%files
%{_udevrulesdir}/60-%{name}.rules
%{_libdir}/libfprint-2/tod-1/%{soname}-%{version}.so

%changelog
%autochangelog
