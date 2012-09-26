%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		openslide
Version:	3.3.0
Release:	1
Summary:	C library and command line tools for reading virtual slides
Group:		Graphics
License:	LGPLv2
URL:		http://openslide.org/
Source0:	https://github.com/downloads/openslide/%{name}/%{name}-%{version}.tar.xz
Patch0:		openslide-3.3.0-rosa-find_openjpeg.patch
BuildRequires:	glib2-devel openjpeg-devel tiff-devel
BuildRequires:	jpeg-devel pkgconfig cairo-devel png-devel
Obsoletes:	openslide-tools < 3.3.0
Provides:	openslide-tools = %{EVRD}


%description
Command line tools for working with virtual slides.


%package	-n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
%rename		openslide-devel

%description	-n %{develname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package   	-n %{libname}
Summary:	C library for reading virtual slides
Group:		System/Libraries
Obsoletes:	openslide < 3.3.0

%description	-n %{libname}
The OpenSlide library allows programs to access virtual slide files regardless
of the underlying image format.

%prep
%setup -q
%patch0 -p1
autoreconf


%build
%configure --disable-static
%make


%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README.txt lgpl-2.1.txt TODO.txt LICENSE.txt CHANGELOG.txt
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}-*


%files -n %{libname}
%{_libdir}/*.so.*


%files -n %{develname}
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
