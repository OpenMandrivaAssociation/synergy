Summary: Mouse and keyboard sharing utility
Name: synerg
Version: 1.3.6
Release: %mkrel 1
License: GPL
Url: http://synergy-foss.org/
Group: Networking/Remote access
Source: http://synergy.googlecode.com/files/synergy-%{version}-Source.tar.gz
Source1: synergyc.1.bz2
Source2: synergys.1.bz2
Obsoletes: synergy-plus < %{version}
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxinerama-devel
BuildRequires: libxtst-devel
BuildRequires: cmake

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

%prep
%setup -qn synergy-%{version}-Source

%build
%cmake
%make

%install
rm -Rf $RPM_BUILD_ROOT
install -D -m755 build/synergyc %buildroot%_bindir/synergyc
install -D -m755 build/synergys %buildroot%_bindir/synergys
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}c.1
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}s.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root,755)
%doc COPYING ChangeLog INSTALL README examples/synergy.conf 
%{_bindir}/synergyc
%{_bindir}/synergys
%{_mandir}/man1/*
