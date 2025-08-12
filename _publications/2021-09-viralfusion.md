---
title: "Viral-fusion: A visual-inertial-ranging-lidar sensor fusion approach"
collection: publications
permalink: /publication/2021-07-viral
excerpt: 'We propose a comprehensive optimization-based estimator for the 15-D state of an unmanned aerial vehicle (UAV), fusing data from an extensive set of sensors: inertial measurement unit (IMU), ultrawideband (UWB) ranging sensors, and multiple onboard visual-inertial and lidar odometry subsystems.'
date: 2021-07-30
venue: 'IEEE Transactions on Robotics'
paperurl: 'https://ieeexplore.ieee.org/document/9502143'
authors: 'Nguyen, T.M., **Cao, M.**, Yuan, S., Lyu, Y., Nguyen, T.H. and Xie, L.'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---

In recent years, onboard self-localization (OSL) methods based on cameras or lidar have achieved many significant progresses. However, some issues such as estimation drift and robustness in low-texture environment still remain inherent challenges for OSL methods. On the other hand, infrastructure-based methods can generally overcome these issues, but at the expense of some installation cost. This poses an interesting problem of how to effectively combine these methods, so as to achieve localization with long-term consistency as well as flexibility compared to any single method. To this end, we propose a comprehensive optimization-based estimator for the 15-D state of an unmanned aerial vehicle (UAV), fusing data from an extensive set of sensors: inertial measurement unit (IMU), ultrawideband (UWB) ranging sensors, and multiple onboard visual-inertial and lidar odometry subsystems. In essence, a sliding window is used to formulate a sequence of robot poses, where relative rotational and translational constraints between these poses are observed in the IMU preintegration and OSL observations, while orientation and position are coupled in the body-offset UWB range observations. An optimization-based approach is developed to estimate the trajectory of the robot in this sliding window. We evaluate the performance of the proposed scheme in multiple scenarios, including experiments on public datasets, high-fidelity graphical-physical simulation, and field-collected data from UAV flight tests. The result demonstrates that our integrated localization method can effectively resolve the drift issue, while incurring minimal installation requirements.

<!-- <img style="float: center;" src="/images/rss2.gif"> -->



<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->