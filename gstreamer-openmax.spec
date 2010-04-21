#
%include	/usr/lib/rpm/macros.gstreamer
#
Summary:	GStreamer plug-in that allows communication with OpenMAX IL components
Summary(pl.UTF-8):	Wtyczka GStreamera pozwalająca na komunikację z komponentami OpenMAX IL
Name:		gstreamer-openmax
Version:	0.10.0.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# when becomes stable
#Source0:	http://gstreamer.freedesktop.org/src/gst-openmax/gst-openmax-%{version}.tar.bz2
Source0:	http://gstreamer.freedesktop.org/src/gst-openmax/pre/gst-openmax-%{version}.tar.bz2
# Source0-md5:	a48b336e62694c9d58fc828eb51dbb09
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gstreamer-devel >= 0.10.22
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gstreamer >= 0.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GstOpenMAX is a GStreamer plug-in that allows communication with
OpenMAX IL components.

OpenMAX IL is an industry standard that provides an abstraction layer
for computer graphics, video, and sound routines.

%description -l pl.UTF-8
GstOpenMAX to wtyczka GStreamera pozwalająca na komunikację z
komponentami OpenMAX IL.

OpenMAX IL to standard przemysłowy zapewniający warstwę abstrakcji dla
funkcji grafiki komputerowej, obrazu i dźwięku komp.

%prep
%setup -q -n gst-openmax-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstomx.so
