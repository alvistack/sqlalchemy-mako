# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-mako
Epoch: 100
Version: 1.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Mako Templates for Python
License: MIT
URL: https://github.com/sqlalchemy/mako/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako’s syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-Mako
Summary: Mako Templates for Python
Requires: python3
Requires: python3-markupsafe >= 0.9.2
Provides: python3-mako = %{epoch}:%{version}-%{release}
Provides: python3dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(mako) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Mako
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako’s syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.

%files -n python%{python3_version_nodots}-Mako
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-Mako
Summary: Mako Templates for Python
Requires: python3
Requires: python3-markupsafe >= 0.9.2
Provides: python3-mako = %{epoch}:%{version}-%{release}
Provides: python3dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(mako) = %{epoch}:%{version}-%{release}

%description -n python3-Mako
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako’s syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.

%files -n python3-Mako
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-mako
Summary: Mako Templates for Python
Requires: python3
Requires: python3-markupsafe >= 0.9.2
Provides: python3-mako = %{epoch}:%{version}-%{release}
Provides: python3dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(mako) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-mako = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(mako) = %{epoch}:%{version}-%{release}

%description -n python3-mako
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako’s syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.

%files -n python3-mako
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
