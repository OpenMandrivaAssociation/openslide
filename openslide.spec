Name:		openslide
Version:	3.2.4
Release:	%mkrel 1
Summary:	C library for reading virtual slides
Group:		System Environment/Libraries
License:	LGPLv2
URL:		http://openslide.org/
Source0:	openslide-3.2.4.tar.gz
BuildRequires:	glib2-devel openjpeg-devel libtiff-devel
BuildRequires:	libjpeg-devel pkgconfig cairo-devel libpng-devel
BuildRoot:	%_tmppath/%{name}-%{version}-buildroot


%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.


%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel libtiff-devel openjpeg-devel libjpeg-devel pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package   	tools
Summary:	Command line tools for %{name}
Group:		Applications/Multimedia

%description	tools
The %{name}-tools package contains command line tools for working
with virtual slides.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README.txt lgpl-2.1.txt TODO.txt LICENSE.txt CHANGELOG.txt
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files tools
%defattr(-,root,root,-)
%{_bindir}/*


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.2.3-3
- rebuild (openjpeg)

* Wed Sep 29 2010 jkeating - 3.2.3-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Adam Goode <adam@spicenitz.org> - 3.2.3-1
- New upstream release, see http://github.com/openslide/openslide/blob/master/CHANGELOG.txt

* Sat Jun 19 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-2
- Restore missing clean section

* Wed Jun 16 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-1
- New upstream release
   + Add openslide-write-png
   + Support for VMU files
   + New error handling system

* Tue Apr 27 2010 Adam Goode <adam@spicenitz.org> - 3.1.1-1
- New upstream release
   + Don't crash or leak memory on some invalid VMS files
   + Ignore extra layers in VMS files

* Thu Apr  1 2010 Adam Goode <adam@spicenitz.org> - 3.1.0-1
- New upstream release
   + Support newer Aperio files (compression 33005)
   + Be more robust in reading raw TIFF tiles
   + Reject invalid TIFF files earlier
   + Fix many memory leaks when probing for TIFF files

* Tue Mar  2 2010 Adam Goode <adam@spicenitz.org> - 3.0.3-1
- New upstream release
   + Fix nasty MIRAX seam problem

* Wed Feb 17 2010 Adam Goode <adam@spicenitz.org> - 3.0.2-1
- New upstream release
   + Allow building on RHEL

* Thu Feb  4 2010 Adam Goode <adam@spicenitz.org> - 3.0.1-1
- New upstream release
   + Fix rendering of the edges of TIFF files
   + Include CHANGELOG.txt

* Mon Feb  1 2010 Adam Goode <adam@spicenitz.org> - 3.0.0-1
- New upstream release
   + License change from GPLv2 to LGPLv2
   + Bug fixes
   + Support more MIRAX files
   + Improve perforamance of MIRAX
   + Add some command-line tools
   + Rework API documentation
   + Add some new properties
   + Remove some unimplemented functions from the header file

* Mon Dec 21 2009 Adam Goode <adam@spicenitz.org> - 2.3.1-1
- New upstream release
   + Support for generic tiled TIFF
   + Bug fixes
   + Try to be less chatty with TIFF output

* Thu Nov 12 2009 Adam Goode <adam@spicenitz.org> - 2.2.1-1
- New upstream release
   + Fix thread safety problems from 2.2.0

* Tue Sep 22 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-3
- Use xz instead of gz

* Mon Sep 21 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-2
- Be more explicit about include directory in files section

* Tue Sep 15 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-1
- New upstream release
   + Thread safety (sometimes lockless)

* Thu Sep 10 2009 Adam Goode <adam@spicenitz.org> - 2.1.0-1
- New upstream release
   + MIRAX support
   + More Aperio support
   + Properties and associated images support
   + Bug fixes

* Wed Feb 25 2009 Adam Goode <adam@spicenitz.org> - 1.1.1-1
- New upstream release
- No more included OpenJPEG
- Much faster rendering and loading

* Tue Dec  9 2008 Adam Goode <adam@spicenitz.org> - 1.0.0-1
- First release
