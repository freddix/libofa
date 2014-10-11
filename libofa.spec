Summary:	Open Fingerprint Architecture - identyfying a piece of music with just sound
Name:		libofa
Version:	0.9.3
Release:	14
License:	GPL v2 or Adaptive Public License
Group:		Libraries
Source0:	http://musicip-libofa.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	51507d2c4b432bd2755f48d58471696e
Patch0:		%{name}-link.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-gcc43.patch
URL:		http://www.musicdns.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	fftw3-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MusicDNS and the Open Fingerprint Architecture provide a system for
identifying a piece of music with nothing more than the sound of the
piece itself.

%package devel
Summary:	Header files for libofa library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	expat-devel
Requires:	fftw3-devel
Requires:	libstdc++-devel

%description devel
Header files for libofa library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%{__sed} -i -e 's| examples||g' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %ghost %{_libdir}/libofa.so.?
%attr(755,root,root) %{_libdir}/libofa.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libofa.so
%{_includedir}/ofa1
%{_pkgconfigdir}/libofa.pc

