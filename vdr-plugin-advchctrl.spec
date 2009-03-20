
%define plugin	advchctrl
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define rel	17

Summary:	VDR plugin: Advanced Channel Control
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Advchctrl-plugin
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		advchctrl-0.0.5-1.3.38.diff
Patch2:		advchctrl-0.0.5-warnings.diff
Patch3:		advchctrl-0.0.5-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


