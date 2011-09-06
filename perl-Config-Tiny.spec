Name:           perl-Config-Tiny
Version:        2.12
Release:        7.1%{?dist}
Summary:        Perl module for reading and writing .ini style configuration files

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Config-Tiny/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Config-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::MinimumVersion)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Config::Tiny is a Perl module designed for reading and writing .ini
style configuration files. It is designed for simplicity and ease of
use, and thus only supports the most basic operations.


%prep
%setup -q -n Config-Tiny-%{version}
chmod a-x Changes lib/Config/Tiny.pm


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test AUTOMATED_TESTING=1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Config/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.12-7.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-5
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-4
- Rebuild for perl 5.10 (again), first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-3
- rebuild normally, second pass

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-2.1
- rebuild with TMV, tests disabled for first pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.12-2
- Rebuild for new perl

* Thu Dec 13 2007 Ralf Corsépius <rc040203@freenet.de> - 2.12-1
- Update to 2.12.

* Mon Oct  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.10-1
- Updated to 2.10.

* Sun Jul 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.08-1
- Updated to 2.08.

* Wed May 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.07-1
- Updated to 2.07.

* Sat Apr 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.06-1
- Updated to 2.06.

* Mon Mar  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.05-1
- Updated to 2.05.

* Sat Feb 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.04-2
- Rebuild for FC5 (perl 5.8.8).

* Sat Jan 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.04-1
- Updated to 2.04.

* Fri Dec 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.03-1
- Updated to 2.03.

* Mon Jun 27 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.02-1
- Updated to 2.02.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.01-2
- rebuilt

* Thu Mar 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.01-1
- Updated to 2.01.

* Sun Jul 25 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.00-0.fdr.1
- Updated to 2.00.

* Sat Jul 10 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.9-0.fdr.1
- Updated to 1.9.

* Fri Jul  2 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.8-0.fdr.1
- Updated to 1.8.

* Tue Jun 29 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.7-0.fdr.1
- Updated to 1.7.

* Sat Jun  5 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.6-0.fdr.3
- Changed URL to canonical location (bug 1140).
- Added build req perl >= 1:5.6.1 and perl(Test::More) (bug 1140).
- Added missing req perl(:MODULE_COMPAT_...) (bug 1140).
- Updated to match most recent perl spec template (bug 1140).
- Removed unneeded optimization settings and find *.bs (bug 1140).

* Thu Mar 18 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.6-0.fdr.2
- Reduced directory ownership bloat.

* Thu Mar 11 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.6-0.fdr.1
- Updated to 1.6.

* Wed Jan  7 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:1.5-0.fdr.1
- Updated to 1.5.

* Sat Dec 13 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:1.3-0.fdr.1
- Initial RPM release.

