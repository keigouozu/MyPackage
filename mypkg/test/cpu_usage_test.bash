#!/bin/bash
# SPDX-FileCopyrightText: 2024 Keigo Uozu
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run mypkg cpu_usage > /tmp/cpu_usage.log 2>&1 

if grep -q "Current cpu usage" /tmp/cpu_usage.log; then
    echo "Test passed"
    exit 0
else
    echo "Test failed"
    exit 1
fi
