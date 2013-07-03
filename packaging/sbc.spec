Name:    sbc	
Version: 1.1
Release: 1%{?dist}
Summary: Bluetooth SBC Utilities
Group:   Development/Libraries
License: GPLv2
URL:     http://www.bluez.org
Source0: http://www.kernel.org/pub/linux/bluetooth/sbc-1.1.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(sndfile)

%description
Bluetooth SBC utilities

%package devel
Summary:    Bluetooth SBC development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
This package contains Bluetooth SBC development files

%prep
%setup -q

%build
%configure --enable-shared --disable-static --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/sbcinfo
%{_bindir}/sbcdec
%{_bindir}/sbcenc
%{_libdir}/libsbc.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/sbc/*
%{_libdir}/libsbc.so
%{_libdir}/pkgconfig/sbc.pc
