Summary: Mouse and keyboard sharing utility
Name: synergy
Version: 1.4.10
Release: 2
License: GPLv2
Url: http://synergy-foss.org/
Group: Networking/Remote access
Source0: http://synergy.googlecode.com/files/synergy-%{version}-Source.tar.gz
Source1: synergyc.1.bz2
Source2: synergys.1.bz2
Obsoletes: synergy-plus < %{version}
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xi)
BuildRequires: cmake
BuildRequires: gcc-c++, gcc, gcc-cpp

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

%prep
%setup -qn synergy-%{version}-Source
find . -perm 0600 -exec chmod 0644 {} \;

%build
export CC=gcc
export CXX=g++
export LDFLAGS="$LDFLAGS -lm -lpthread"
%cmake
%make

%install
install -D -p -m 0755 bin/synergyc %{buildroot}%{_bindir}/synergyc
install -D -p -m 0755 bin/synergys %{buildroot}%{_bindir}/synergys
install -D -p -m 0644 doc/synergyc.man %{buildroot}%{_mandir}/man8/synergyc.8
install -D -p -m 0644 doc/synergys.man %{buildroot}%{_mandir}/man8/synergys.8

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%doc COPYING README doc/synergy.conf.example*
%{_bindir}/synergyc
%{_bindir}/synergys
%{_mandir}/man8/synergyc.8*
%{_mandir}/man8/synergys.8*
