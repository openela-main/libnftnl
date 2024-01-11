%define rpmversion 1.1.5
%define specrelease 5

Name:           libnftnl
Version:        %{rpmversion}
Release:        %{specrelease}%{?dist}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl
License:        GPLv2+
URL:            http://netfilter.org/projects/libnftnl/
Source0:        http://ftp.netfilter.org/pub/libnftnl/libnftnl-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libmnl-devel
Patch0:             0001-tests-flowtable-Don-t-check-NFTNL_FLOWTABLE_SIZE.patch
Patch1:             0002-flowtable-Fix-memleak-in-error-path-of-nftnl_flowtab.patch
Patch2:             0003-chain-Fix-memleak-in-error-path-of-nftnl_chain_parse.patch
Patch3:             0004-flowtable-Correctly-check-realloc-call.patch
Patch4:             0005-chain-Correctly-check-realloc-call.patch
Patch5:             0006-include-resync-nf_tables.h-cache-copy.patch
Patch6:             0007-set-Add-support-for-NFTA_SET_DESC_CONCAT-attributes.patch
Patch7:             0008-set_elem-Introduce-support-for-NFTNL_SET_ELEM_KEY_EN.patch
Patch8:             0009-src-Fix-for-reading-garbage-in-nftnl_chain-getters.patch
Patch9:             0010-set_elem-missing-set-and-build-for-NFTNL_SET_ELEM_EX.patch
Patch10:            0011-expr-dynset-release-stateful-expression-from-.free-p.patch
Patch11:            0012-set-expose-nftnl_set_elem_nlmsg_build.patch

%description
A library for low-level interaction with nftables Netlink's API over libmnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
# This is what autogen.sh (only in git repo) does - without it, patches changing
# Makefile.am cause the build system to regenerate Makefile.in and trying to use
# automake-1.14 for that which is not available in RHEL.
autoreconf -fi
rm -rf autom4te*.cache

%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
* Fri Jan 21 2022 Phil Sutter <psutter@redhat.com> [1.1.5-5.el8]
- set: expose nftnl_set_elem_nlmsg_build() (Phil Sutter) [2040754]
- expr: dynset: release stateful expression from .free path (Phil Sutter) [2040478]
- set_elem: missing set and build for NFTNL_SET_ELEM_EXPR (Phil Sutter) [2040478]

* Wed Feb 19 2020 Phil Sutter <psutter@redhat.com> [1.1.5-4.el8]
- src: Fix for reading garbage in nftnl_chain getters (Phil Sutter) [1758673]

* Fri Feb 14 2020 Phil Sutter <psutter@redhat.com> [1.1.5-3.el8]
- set_elem: Introduce support for NFTNL_SET_ELEM_KEY_END (Phil Sutter) [1795223]
- set: Add support for NFTA_SET_DESC_CONCAT attributes (Phil Sutter) [1795223]
- include: resync nf_tables.h cache copy (Phil Sutter) [1795223]

* Fri Dec 06 2019 Phil Sutter <psutter@redhat.com> [1.1.5-2.el8]
- chain: Correctly check realloc() call (Phil Sutter) [1778952]
- flowtable: Correctly check realloc() call (Phil Sutter) [1778952]
- chain: Fix memleak in error path of nftnl_chain_parse_devs() (Phil Sutter) [1778952]
- flowtable: Fix memleak in error path of nftnl_flowtable_parse_devs() (Phil Sutter) [1778952]

* Mon Dec 02 2019 Phil Sutter <psutter@redhat.com> [1.1.5-1.el8]
- Rebase onto upstream version 1.1.5 (Phil Sutter) [1717129]

* Thu Oct 24 2019 Phil Sutter <psutter@redhat.com> [1.1.4-3.el8]
- set: Export nftnl_set_list_lookup_byname() (Phil Sutter) [1762563]

* Thu Oct 17 2019 Phil Sutter <psutter@redhat.com> [1.1.4-2.el8]
- obj/ct_timeout: Fix NFTA_CT_TIMEOUT_DATA parser (Phil Sutter) [1758673]
- set_elem: Validate nftnl_set_elem_set() parameters (Phil Sutter) [1758673]
- obj/ct_timeout: Avoid array overrun in timeout_parse_attr_data() (Phil Sutter) [1758673]
- set: Don't bypass checks in nftnl_set_set_u{32,64}() (Phil Sutter) [1758673]
- obj/tunnel: Fix for undefined behaviour (Phil Sutter) [1758673]
- set_elem: Fix return code of nftnl_set_elem_set() (Phil Sutter) [1758673]
- obj: ct_timeout: Check return code of mnl_attr_parse_nested() (Phil Sutter) [1758673]

* Fri Oct 04 2019 Phil Sutter <psutter@redhat.com> [1.1.4-1.el8]
- Rebase to upstream version 1.1.4 (Phil Sutter) [1717129]

* Thu Jan 31 2019 Phil Sutter <psutter@redhat.com> [1.1.1-4.el8]
- src: rule: Support NFTA_RULE_POSITION_ID attribute (Phil Sutter) [1670565]

* Tue Jan 29 2019 Phil Sutter <psutter@redhat.com> [1.1.1-3.el8]
- src: chain: Fix nftnl_chain_rule_insert_at() (Phil Sutter) [1666495]
- src: chain: Add missing nftnl_chain_rule_del() (Phil Sutter) [1666495]
- flowtable: Fix for reading garbage (Phil Sutter) [1661327]
- flowtable: Fix memleak in nftnl_flowtable_parse_devs() (Phil Sutter) [1661327]
- flowtable: Fix use after free in two spots (Phil Sutter) [1661327]
- flowtable: Add missing break (Phil Sutter) [1661327]
- object: Avoid obj_ops array overrun (Phil Sutter) [1661327]

* Mon Dec 17 2018 Phil Sutter <psutter@redhat.com> [1.1.1-2.el8]
- chain: Hash chain list by name (Phil Sutter) [1658533]
- chain: Add lookup functions for chain list and rules in chain (Phil Sutter) [1658533]
- chain: Support per chain rules list (Phil Sutter) [1658533]
- src: remove nftnl_rule_cmp() and nftnl_expr_cmp() (Phil Sutter) [1658533]

* Thu Jul 12 2018 Phil Sutter <psutter@redhat.com> [1.1.1-1.el8]
- Rebase onto upstream version 1.1.1
- Sync spec file with RHEL7
- Disable JSON parsing, deprecated by upstream
- Make use of builtin testsuite

* Sat Jun 23 2018 Phil Sutter - 1.0.9-3
- Drop leftover mxml dependency [1594917]

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.9-1
- Update to 1.0.9. Fixes bug #1531004

* Sat Oct 21 2017 Kevin Fenzi <kevin@scrye.com> - 1.0.8-4
- Update to 1.0.8. Fixes bug #1504350

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.7-1
- Update to 1.0.7. Fixes bug #1406201

* Wed Jun 01 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.6-1
- Update to 1.0.6. Fixes bug #1341384

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Kevin Fenzi <kevin@scrye.com> 1.0.5-1
- Update to 1.0.5. Fixes bug #1263684

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 1.0.3-1
- Update to final 1.0.3

* Wed Sep 03 2014 Kevin Fenzi <kevin@scrye.com> 1.0.3-0.1.20140903git
- Update to 20140903 git snapshot

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Kevin Fenzi <kevin@scrye.com> 1.0.2-1
- Update to 1.0.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Kevin Fenzi <kevin@scrye.com> 1.0.1-1.
- Update to 1.0.1

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 1.0.0-1.20140330git
- Update to 20140330 snapshot
- Sync version to be a post 1.0.0 snapshot

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.10.20140326git
- Update to 20140326 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.9.20140307git
- Update to 20140307 snapshot

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.8.20140125git
- Update to 20140125

* Thu Jan 23 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140122git
- Add obsoletes/provides to devel subpackage as well. 

* Wed Jan 22 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140122git
- Renamed libnftnl
- Update to 20140122 snapshot.

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140118git
- Update to 20140118 snapshot.

* Sat Jan 11 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140111git
- Update to 20140111 snapshot. 
- Enable xml (some tests stll fail, but it otherwise builds ok)

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 0-0.3.20131202git
- Update to 20131202 snapshot, switch to upstream snapshot repo instead of git checkouts. 

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2
- Fixes from review. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
