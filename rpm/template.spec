Name:           ros-indigo-handle-detector
Version:        1.1.0
Release:        5%{?dist}
Summary:        ROS handle_detector package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/handle_detector
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pcl-conversions
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-visualization-msgs
BuildRequires:  lapack-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-visualization-msgs

%description
ROS package to detect handles.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jun 16 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-5
- Autogenerated by Bloom

* Thu Jun 11 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-4
- Autogenerated by Bloom

* Mon May 18 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-3
- Autogenerated by Bloom

* Sat May 16 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-2
- Autogenerated by Bloom

* Thu May 14 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-1
- Autogenerated by Bloom

* Thu Apr 23 2015 Andreas ten Pas <atp@ccs.neu.edu> - 1.1.0-0
- Autogenerated by Bloom

