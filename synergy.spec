Summary: Mouse and keyboard sharing utility
Name: synergy
Version: 1.4.5
Release: 1
License: GPL
Url: http://synergy-foss.org/
Group: Networking/Remote access
Source0: http://synergy.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Source1: synergyc.1.bz2
Source2: synergys.1.bz2
Obsoletes: synergy-plus < %{version}
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxinerama-devel
BuildRequires: libxtst-devel
BuildRequires: cmake
Patch0:	       linkage_syn.patch

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

%prep
%setup -qn synergy-%{version}-Source
%patch0 -p1

%build
%cmake
%make

%install
install -D -m755 bin/synergyc %buildroot%_bindir/synergyc
install -D -m755 bin/synergyc %buildroot%_bindir/synergyc
install -D -m755 bin/integtests %buildroot%_bindir/integtests
install -D -m755 bin/unittests %buildroot%_bindir/unittests
mkdir -p %{buildroot}/%{_mandir}/man1/
bzcat %{SOURCE1} > %{buildroot}%{_mandir}/man1/%{name}c.1
bzcat %{SOURCE2} > %{buildroot}%{_mandir}/man1/%{name}s.1

%files
%defattr(-, root, root,755)
%doc COPYING ChangeLog INSTALL README
%{_bindir}/*
%{_mandir}/man1/*
