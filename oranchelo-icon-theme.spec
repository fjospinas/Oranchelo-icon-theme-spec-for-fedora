# Oranchelo Icon Theme SPEC file to build RPM package

# Build instructions for v0.7.5.9:
# rpmbuild -bb oranchelo-icon-theme.spec --define "pkg_version 0.7.5.9"

%define install_dir %{_datadir}/icons
%define themes_base_name Oranchelo

Name:           oranchelo-icon-theme
Version:        %{pkg_version}
Release:        1
Summary:        Oranchelo is a flat-design icon theme for XFCE4

License:        GPLv3
URL:            https://github.com/OrancheloTeam/%{name}
Source0:        https://github.com/OrancheloTeam/%{name}/archive/v%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
Oranchelo is a flat-design icon theme for XFCE4 based on Super Flat Remix and
inspired by "Corny icons" by Patryk Goworowski.

%prep
%autosetup

%build
find -type f -executable -exec chmod -x {} \;

%install
mkdir -p %{buildroot}%{install_dir}
cp -r %{themes_base_name}* %{buildroot}%{install_dir}

%files
%license LICENSE
%doc README.md
%{install_dir}/%{themes_base_name}*

%post
/bin/touch --no-create {install_dir}/%{themes_base_name}* &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create {install_dir}/%{themes_base_name}* &>/dev/null
  if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    /usr/bin/gtk-update-icon-cache {install_dir}/%{themes_base_name}* &>/dev/null || :
  fi
fi

%changelog
* Wed Feb 21 2018 Adolfo Silerio <zayronxio@gmail.com> - 0.7.5.9-1
- Franz
- Kicad
- Vmplayer
- Slack
- Smartgit
- Qalculator
- Grsync
- Bijiben
- Vivaldi
- Skype
