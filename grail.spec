#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Gesture Recognition And Instantiation Library
Name:		grail
Version:	3.1.0
Release:	1
License:	GPL v3 / LGPL v3
Group:		X11/Libraries
Source0:	https://launchpad.net/grail/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	2ac56af5f6f466b433c99ca12f34c34f
URL:		https://launchpad.net/grail
BuildRequires:	evemu-devel
BuildRequires:	frame-devel >= 2.5.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6.0
BuildRequires:	xorg-proto-inputproto-devel >= 2.2.0
BuildRequires:	xorg-xserver-server-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grail consists of an interface and tools for handling gesture
recognition and gesture instantiation.

When a multitouch gesture is performed on a device, the recognizer
emits one or several possible gestures. Once the context of the
gesture is known, i.e., in what window the touches land and what
gestures the clients of that window listen to, the instantiator
delivers the matching set of gestures.

The library handles tentative getures, i.e., buffering of events for
several alternative gestures until a match is confirmed.

%package tools
Summary:	Test tools for grail library
Summary(pl.UTF-8):	Testowe narzędzia biblioteki grail
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Test tools for grail library.

%description tools -l pl.UTF-8
Testowe narzędzia biblioteki grail.

%package devel
Summary:	Header files for grail library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki grail
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	frame-devel

%description devel
Header files for grail library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki grail.

%package static
Summary:	Static grail library
Summary(pl.UTF-8):	Statyczna biblioteka grail
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static grail library.

%description static -l pl.UTF-8
Statyczna biblioteka grail.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libgrail.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrail.so.6

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/grail-test-3-1
%attr(755,root,root) %{_bindir}/grail-test-atomic
%attr(755,root,root) %{_bindir}/grail-test-edge
%attr(755,root,root) %{_bindir}/grail-test-propagation
%{_mandir}/man1/grail-test-3-1.1*
%{_mandir}/man1/grail-test-atomic.1*
%{_mandir}/man1/grail-test-edge.1*
%{_mandir}/man1/grail-test-propagation.1*


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrail.so
%{_includedir}/oif/*
%{_pkgconfigdir}/grail.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgrail.a
%endif
