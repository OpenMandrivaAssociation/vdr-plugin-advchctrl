%define plugin	advchctrl

Summary:	VDR plugin: Advanced Channel Control
Name:		vdr-plugin-%plugin
Version:	0.0.5
Release:	22
Group:		Video
License:	GPL
URL:		https://www.vdr-wiki.de/wiki/index.php/Advchctrl-plugin
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		advchctrl-0.0.5-1.3.38.diff
Patch2:		advchctrl-0.0.5-warnings.diff
Patch3:		advchctrl-0.0.5-i18n-1.6.patch
Patch4:		advchctrl-0.0.5-gcc44.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The idea for this plugin was born by the boring different
audio volume level on some transponders. In the parameters
of the plugin you can set the default volume.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .1338
%patch2 -p1 -b .warnings
%patch3 -p1
%patch4 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-19mdv2010.0
+ Revision: 401089
- actually rebuild for new VDR
- rebuild for new VDR
- fix build with gcc4.4 (gcc44.patch)

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-17mdv2009.1
+ Revision: 359272
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-16mdv2009.0
+ Revision: 197889
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-15mdv2009.0
+ Revision: 197621
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-14mdv2008.1
+ Revision: 145000
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-13mdv2008.1
+ Revision: 144964
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-12mdv2008.1
+ Revision: 103050
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-11mdv2008.0
+ Revision: 49959
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-10mdv2008.0
+ Revision: 42046
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-9mdv2008.0
+ Revision: 22680
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-8mdv2007.0
+ Revision: 90877
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-7mdv2007.1
+ Revision: 73934
- rebuild for new vdr
- Import vdr-plugin-advchctrl

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2007.0
- rebuild for new vdr

* Sat Jun 10 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2007.0
- initial Mandriva release

