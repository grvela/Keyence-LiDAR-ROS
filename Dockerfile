FROM ros:humble-ros-core-jammy

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    python3 \
    python3-pip \
    python3-colcon-common-extensions \
    python3-colcon-mixin \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

RUN colcon mixin add default \
      https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml && \
    colcon mixin update && \
    colcon metadata add default \
      https://raw.githubusercontent.com/colcon/colcon-metadata-repository/master/index.yaml && \
    colcon metadata update

RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-humble-ros-base=0.10.0-1* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/laser-keyence

COPY ./requirements.txt /home/laser-keyence

RUN pip3 install -r requirements.txt