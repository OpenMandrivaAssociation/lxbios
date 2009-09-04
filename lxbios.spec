Summary:	An utility to read/write LinuxBIOS parameters
Name:		lxbios
Version:	2.0.1
Release:	%mkrel 5
License:	GPL
Group:		System/Base
Url:		http://lxbios.sourceforge.net
Source0:	http://downloads.sourceforge.net/lxbios/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
At boot time, LinuxBIOS places a table (known as the LinuxBIOS table) in low
physical memory.  The contents of this table are preserved even after
LinuxBIOS transfers control to the kernel and the kernel initializes itself.
The LinuxBIOS table contains various system information such as the type of
mainboard in use.  It also specifies locations in the CMOS (nonvolatile RAM)
where the LinuxBIOS parameters are stored.

WARNING:
This tool is useful only for LinuxBIOS capable hardware.
Please visit http://www.linuxbios.org for more informations.
 
%prep
%setup -q

%build
perl -pi -e "s/CFLAGS =.*/CFLAGS = %{optflags}/" Makefile
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install %{name} %{buildroot}%{_bindir}
install lxbios.1.gz %{buildroot}%{_mandir}/man1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README DISCLAIMER COPYING ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*


