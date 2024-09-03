%define libnftnl_rpmversion 1.2.6
%define libnftnl_specrelease 4

Name:           libnftnl
Version:        %{libnftnl_rpmversion}
Release:        %{libnftnl_specrelease}%{?dist}%{?buildid}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl
License:        GPLv2+
URL:            https://netfilter.org/projects/libnftnl/
Source0:        %{url}/files/%{name}-%{version}.tar.xz

Patch1:             0001-set-Do-not-leave-free-d-expr_list-elements-in-place.patch
Patch2:             0002-expr-fix-buffer-overflows-in-data-value-setters.patch
Patch3:             0003-set-buffer-overflow-in-NFTNL_SET_DESC_CONCAT-setter.patch
Patch4:             0004-set_elem-use-nftnl_data_cpy-in-NFTNL_SET_ELEM_-KEY-K.patch
Patch5:             0005-obj-ct_timeout-setter-checks-for-timeout-array-bound.patch
Patch6:             0006-udata-incorrect-userdata-buffer-size-validation.patch
Patch7:             0007-expr-Repurpose-struct-expr_ops-max_attr-field.patch
Patch8:             0008-expr-Call-expr_ops-set-with-legal-types-only.patch
Patch9:             0009-include-Sync-nf_log.h-with-kernel-headers.patch
Patch10:            0010-expr-Introduce-struct-expr_ops-attr_policy.patch
Patch11:            0011-expr-Enforce-attr_policy-compliance-in-nftnl_expr_se.patch
Patch12:            0012-chain-Validate-NFTNL_CHAIN_USE-too.patch
Patch13:            0013-table-Validate-NFTNL_TABLE_USE-too.patch
Patch14:            0014-flowtable-Validate-NFTNL_FLOWTABLE_SIZE-too.patch
Patch15:            0015-obj-Validate-NFTNL_OBJ_TYPE-too.patch
Patch16:            0016-set-Validate-NFTNL_SET_ID-too.patch
Patch17:            0017-table-Validate-NFTNL_TABLE_OWNER-too.patch
Patch18:            0018-obj-Do-not-call-nftnl_obj_set_data-with-zero-data_le.patch
Patch19:            0019-obj-synproxy-Use-memcpy-to-handle-potentially-unalig.patch
Patch20:            0020-utils-Fix-for-wrong-variable-use-in-nftnl_assert_val.patch
Patch21:            0021-object-getters-take-const-struct.patch
Patch22:            0022-obj-Return-value-on-setters.patch
Patch23:            0023-obj-Repurpose-struct-obj_ops-max_attr-field.patch
Patch24:            0024-obj-Call-obj_ops-set-with-legal-attributes-only.patch
Patch25:            0025-obj-Introduce-struct-obj_ops-attr_policy.patch
Patch26:            0026-obj-Enforce-attr_policy-compliance-in-nftnl_obj_set_.patch
Patch27:            0027-utils-Introduce-and-use-nftnl_set_str_attr.patch
Patch28:            0028-obj-Respect-data_len-when-setting-attributes.patch
Patch29:            0029-expr-Respect-data_len-when-setting-attributes.patch
Patch30:            0030-tests-Fix-objref-test-case.patch

BuildRequires:  libmnl-devel
BuildRequires:  gcc
BuildRequires:  make
#BuildRequires:  autoconf
#BuildRequires:  automake

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
#autoreconf -fi
#rm -rf autom4te*.cache

%configure --disable-static --disable-silent-rules
%make_build

%check
%make_build check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
* Thu May 09 2024 Phil Sutter <psutter@redhat.com> [1.2.6-4.el9]
- Bump release for side-tag build with fixed libmnl (Phil Sutter) [RHEL-28515]

* Wed May 08 2024 Phil Sutter <psutter@redhat.com> [1.2.6-3.el9]
- tests: Fix objref test case (Phil Sutter) [RHEL-28515]
- expr: Respect data_len when setting attributes (Phil Sutter) [RHEL-28515]
- obj: Respect data_len when setting attributes (Phil Sutter) [RHEL-28515]
- utils: Introduce and use nftnl_set_str_attr() (Phil Sutter) [RHEL-28515]
- obj: Enforce attr_policy compliance in nftnl_obj_set_data() (Phil Sutter) [RHEL-28515]
- obj: Introduce struct obj_ops::attr_policy (Phil Sutter) [RHEL-28515]
- obj: Call obj_ops::set with legal attributes only (Phil Sutter) [RHEL-28515]
- obj: Repurpose struct obj_ops::max_attr field (Phil Sutter) [RHEL-28515]
- obj: Return value on setters (Phil Sutter) [RHEL-28515]
- object: getters take const struct (Phil Sutter) [RHEL-28515]
- utils: Fix for wrong variable use in nftnl_assert_validate() (Phil Sutter) [RHEL-28515]
- obj: synproxy: Use memcpy() to handle potentially unaligned data (Phil Sutter) [RHEL-28515]
- obj: Do not call nftnl_obj_set_data() with zero data_len (Phil Sutter) [RHEL-28515]
- table: Validate NFTNL_TABLE_OWNER, too (Phil Sutter) [RHEL-28515]
- set: Validate NFTNL_SET_ID, too (Phil Sutter) [RHEL-28515]
- obj: Validate NFTNL_OBJ_TYPE, too (Phil Sutter) [RHEL-28515]
- flowtable: Validate NFTNL_FLOWTABLE_SIZE, too (Phil Sutter) [RHEL-28515]
- table: Validate NFTNL_TABLE_USE, too (Phil Sutter) [RHEL-28515]
- chain: Validate NFTNL_CHAIN_USE, too (Phil Sutter) [RHEL-28515]
- expr: Enforce attr_policy compliance in nftnl_expr_set() (Phil Sutter) [RHEL-28515]
- expr: Introduce struct expr_ops::attr_policy (Phil Sutter) [RHEL-28515]
- include: Sync nf_log.h with kernel headers (Phil Sutter) [RHEL-28515]
- expr: Call expr_ops::set with legal types only (Phil Sutter) [RHEL-28515]
- expr: Repurpose struct expr_ops::max_attr field (Phil Sutter) [RHEL-28515]
- udata: incorrect userdata buffer size validation (Phil Sutter) [RHEL-28515]
- obj: ct_timeout: setter checks for timeout array boundaries (Phil Sutter) [RHEL-28515]
- set_elem: use nftnl_data_cpy() in NFTNL_SET_ELEM_{KEY,KEY_END,DATA} (Phil Sutter) [RHEL-28515]
- set: buffer overflow in NFTNL_SET_DESC_CONCAT setter (Phil Sutter) [RHEL-28515]
- expr: fix buffer overflows in data value setters (Phil Sutter) [RHEL-28515]

* Fri Oct 27 2023 Phil Sutter <psutter@redhat.com> [1.2.6-2.el9]
- spec: Avoid variable name clash, add missing dist tag (Phil Sutter) [RHEL-14149]

* Thu Oct 26 2023 Phil Sutter <psutter@redhat.com> [1.2.6-1.el9]
- set: Do not leave free'd expr_list elements in place (Phil Sutter) [RHEL-14149]
- Rebase onto version 1.2.6 (Phil Sutter) [RHEL-14149]

* Tue Jun 07 2022 Phil Sutter <psutter@redhat.com> - 1.2.2-1
- New version 1.2.2

* Wed May 18 2022 Phil Sutter <psutter@redhat.com> - 1.2.1-1
- Fix debug printing for tcp option reset expression
- new version 1.2.1

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.9-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.9-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.1.9-1
- Update to 1.1.9. Fixes rhbz#1916855

* Sat Oct 31 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.8-1
- Update to 1.1.8. Fixes bug #1891597

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.1.7-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Fri Jun 05 2020 Phil Sutter <psutter@redhat.com> - 1.1.7-1
- Rebase onto upstream version 1.1.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Phil Sutter <psutter@redhat.com> - 1.1.5-1
- Update to 1.1.5. Fixes bug #1778850

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 1.1.4-1
- Update to 1.1.4. Fixes bug #1743175

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.1.3-1
- Update to 1.1.3. Fixes bug #1714231

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.1.1-5
- Fix FTBFS bug #1604620

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Phil Sutter <psutter@redhat.com> - 1.1.1-3
- Disable running tests/test-script.sh again, it breaks builds on big endian.

* Thu Jun 14 2018 Phil Sutter <psutter@redhat.com> - 1.1.1-2
- Drop leftover mxml dependency. Fixes bug #1594107
- Enable running tests/test-scrip.sh again when checking.

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 1.1.1-1
- Update to 1.1.1. Fixes bug #1589403

* Fri May 04 2018 Kevin Fenzi <kevin@scrye.com> - 1.1.0-1
- Update to 1.1.0. Fixes bug #1574094

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
