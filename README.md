---
# 2023_1_2
---
* 우분트 설치(20.04ver) Vmware 안에 설치.
    * image 주소 : https://releases.ubuntu.com/focal/ 데스크탑 버전 설치

* ROS2 설치:
    * foxy : sudo apt install ros-foxy-desktop ros-foxy-rmw-fastrtps* ros-foxy-rmw-cyclonedds*
* testpub testsub 으로 ROS2 정상작동 확인.

* vsc  설치:
    *  ubuntu 에서 한글 사용을 위해 .deb 파일을 받아 설치 : sudo dpkg -i code_1.74.2-1671533413_amd64.deb

* turtlesim_node 실행 후 teleop 으로 움직임 확인.

* turtlesim_node 실행 후 rqt 의 node graph, message publisher 으로 움직임 확인.

* ROS2 파이썬 패키지 만들기:
    * 파이썬 패키지 : ros2 pkg create --build-type ament_python (패키지이름)

---
# 2023_1_3
---
* pub,sub 노드 생성:
    * setup.py에서 pub, sub에 대한 엔트리 타임 설정.
    * pub, sub 파이썬 코드 작성.(m_pubsub(mpub.py, msub.py))
    * 노드 생성.(cd ~/robot_ws && colcon build --symlink-install)

* 생성한 pub, sub 노드 실행:
    * 터미널 창에서 실행 : ros2 run m_pubsub mp, ros2 run m_pubsub ms
    * rqt node graph로 정상동작 확인.

* SaaS(Software as a Service) 개념 및 google slide 사용법 숙지.

* turtlesim 거북이 제어:
    * pub(turtle_move) 을 생성하여 Twist 타입의 데이터를 보내 turtlesim 으로 받아 거북이 움직임을 제어.
    * 거북이의 수를 추가, 색을 변경하여 2마리 이상의 거북이 움직임 제어.
        * 거북이 추가 : ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 7.0, theta: 1.5, name: "turtle2"}"
        * 거북이 색 변경 : ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 100, g: 50, b: 200, width : 5}"
        * 삼각함수를 거북이 제어에 사용.

* Python opencv 설치 : python3 -m pip install opencv-python
    * 반전, 회전, 색상 변환 기본 동작 시험.

---
# 2023_1_4
---
* 인터페이스
    * 인터페이스 패키지 만들기 : ros2 pkg create --build-type ament_cmake test_interface
        * 인터페이스 자료형 : Intfloat.msg(in64 num, float64 sum)
    * topic, service, action 으로 구분
    * opt/ros/foxy/share/std_msg/mgs/(파일명) : 지금까지 기본적으로 사용한 Twist, String 등의 위치
    * interface, node 를 하나의 패키지로 만들면 안됨. -> 패키지를 따로 만들어야 함.
    * calss 와 같이 대문자로 시작해야 함.
    * 사전 작업
    1. msg 파일 생성 후 만들고자 하는 msg파일 생성(Intfloat.msg)
    2. CMakeLists.txt 파일 아래와 같이 코드 수정.
    <pre>
    <code>
    # find dependencies
    find_package(ament_cmake REQUIRED)
    find_package(geometry_msgs REQUIRED)
    find_package(rosidl_default_generators REQUIRED)
    # uncomment the following section in order to fill in
    # further dependencies manually.
    # find_package(<dependency> REQUIRED)

    rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/Intfloat.msg"
    "srv/AddThreeInts.srv"
    "srv/MinusThreeInts.srv"
    DEPENDENCIES geometry_msgs
    )
    </code>
    </pre>
    3. package.xml 파일에 아래와 코드를 수정.

        <buildtool_depend>ament_cmake</buildtool_depend>
        <buildtool_depend>rosidl_default_generators</buildtool_depend>
        <exec_depend>rosidl_default_runtime</exec_depend>
        <member_of_group>rosidl_interface_packages</member_of_group>

* 서비스 패키지 만들기 : ros2 pkg create --build-type ament_python test_num
    * server, client 노드 실행 :
        * setup.py에서 service, client 에 대한 엔트리 타임 설정.
        * server, client 파이썬 코드 작성.
            * test_num(test_service_client.py, test_service_client_minus.py, test_service_ser1.py)
        * 터미널 창에서 정상동작(3개의 숫자 더하기, 3개의 숫자 빼기) 확인.

* 액션(피보나치 수열)
    * test_interface 패키지에 action 폴더 생성 후 Fibonacci.action 파일 생성 및 인터페이스 설정.
    * server, client 노드 실행 :
        * setup.py에서 service, client 에 대한 엔트리 타임 설정.
        * server, client 파이썬 코드 작성.
            * test_num(fibonacci_action_server.py, fibonacci_action_client.py)
    *  터미널 창에서 정상동작(피보나치 수열) 확인.

---
# 2023_1_5
---
* 파라미터
    * turtlesim 을 이용한 파라미터 기본 사용 법 숙지.
        * ros2 param list : 파라미터 리스트 확인
        * ros2 param describe /turtlesim background_g : 파라미터 정보 확인
        * ros2 param set /turtlesim background_g 255 : 파라미터 값 변경
        * ros2 param dump /turtlesim : 파라미터 저장
        * ros2 run turtlesim turtlesim_node --ros-args --params-file ./turtlesim.yaml : 저장된 파라미터를 사용하여 turtlesim 구동

    * 파라미터 패키지 만들기 : ros2 pkg create --build-type ament_python test_para
    * setup.py에서 엔트리 타임 설정(tp).
    * 파라미터 에서 터미널 텍스트 출력 확인. (test_py_para.py) -> ros run test_para tp

* launch
    * test_para 패키지 사용.
    * 3개의 노드를 사용하여 turtlesim 3개 구동.(turtlesim_mimic_launch.py) -> /robot_ws/src/test_para/launch$ ros2 launch turtlesim_mimic_alunch.py

* turtle bot3(burger)
    * pc 와 turtle bot3 wifi 연결.
        * 라즈베리파이에 50-clound-init.yaml 파일 생성.
            <pre>
            <code>
            # This file is generated from information provided by the datasource.  Changes
            # to it will not persist across an instance reboot.  To disable cloud-init's
            # network configuration capabilities, write a file
            # /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
            # network: {config: disabled}
            network:
            version: 2
            renderer: networkd
            ethernets:
                eth0:
                dhcp4: true
                dhcp6: true
                optional: true
            wifis:
                wlan0:
                dhcp4: true
                dhcp6: true
                access-points:
                    turtle:
                    password: turtlebot3
            </code>
            </pre>
        * ifconfig : 현재 ip 확인.
        * sudo apt install nmap : nmap 설치.
        * nmap -sn 192.168.0.0/24 : 현재 할당되어 있는 ip 확인.
        * ssh ubuntu@192.168.0.6(터틀봇ip) : 터틀 봇과 pc 연결.

    * turtle bot 3 관련 패키지 다운로드 : https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

* turtle bot 3 키보드 제어.
    * turtle bot 연결.
        * sudo nano ~/.bashrc -> export TURTLEBOT3_MODEL=burger 추가.
        * ros2 launch turtlebot3_bringup robot.launch.py
    * 제어 pc.
        * .bashrc 파일-> export TURTLEBOT3_MODEL=burger 추가.
        * ros2 run turtlebot3_teleop teleop_keyboard
    * turtle bot 3를 pc 에서 키보드 제어 확인.

---
# 2023_1_5
---
* pc 에서 turtle bot 3 라파로 접근
    * 노틸러스 사용
    * other locations -> connection to server -> sftp://192.168.0.6(turtlebot의ip)

* pc와 turtle bot 3 통신 중 사용되는 topic
    * battary state : 베터리 잔량.
    * cmd vel : 터틀 봇 움직임.
    * joint : 바퀴의 각도 확인.
    * odm : 시작 위치로 부터 얼마나 떨어져 있는지 확인.
    * scan : 레이저 센서로 각도에서 오는 값을 읽어서 거리 측정 가능.
    * tf : 3차원 공간에서 x,y,z 값, 지면으로 부터 얼마나 떨어져 있는지 측정 가능.

* 패키지에서 노드로 터틀봇 제어.
    * 제어 pc
        * 패키지 생성: ros2 pkg create --build-type ament_python tb3_move
        * node 코드 작성(tb3_basic_move.py) : linear.x, angular.z 값으로 움직임 제어(topic : vmd_vel).
        * setup.py에서 node 에 대한 엔트리 타임 설정(tb3m).
        * 터미널 창 : ros2 run tb3_move tb3m
        * 멈추고 싶은 경우 : ros2 run turtlebot3_teleop teleop_keyboard
    * turtle bot 3
        * ros2 launch turtlebot3_bringup robot.launch.py

* turtle bot 3 카메라 설정
    *  문제 해결 중

* slam 설정
    * https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node

* navigation 설정
    * https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#run-navigation-nodes

---
# 2023_1_9
---
* simulation
    * gazebo : https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation
    * slam : https://emanual.robotis.com/docs/en/platform/turtlebot3/slam_simulation/
    * navigation : https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/   
        -> gazebo 를 사용하여 가상의 맵을 형성   
        -> slam 을 사용하여 맵의 지도를 작성 및 저장   
        -> navigation 을 이용하여 동작 확인.

* 프로젝트 아이디어 회의
    * google slide : https://docs.google.com/presentation/d/1_tC2GGcQ1quFyGeajHxiugFS1wR6vpighWsBEbJgPas/edit?usp=sharing
    * github : https://github.com/SSI0816/project-jj

* turtle bot 3 카메라 설정
    * 기존의 turtle bot의 sd 카드를 교체.
    * git clone https://github.com/christianrauch/raspicam2_node.git
    * sudo apt autoremove --purge libgles2-mesa-dev mesa-common-dev 충돌하는 비디오제거
    * sudo add-apt-repository ppa:ubuntu-pi-flavour-makers/ppa 파이캠 필요한 라이브러리
    * sudo apt install libraspberrypi-bin libraspberrypi-dev 파이캠 필요한 라이브러리   
        -> 에러 발생 : sudo apt-get update, sudo apt-get upgrade 실행   
        -> 에러 수정.

---
# 2023_1_10
---        
* turtle bot 3 카메라 설정
    * turtle bot 기체 변경.
    * sudo usermod -a -G video ubuntu 카메라 유저권한 접근성 등록.
    * sudo apt-get install v4l-utils
    * v4l2-ctl --list-devices 카메라 잡히는지 확인.
    * df -h #Find your device numbert 디바이스 확인.
    * wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20160527_all.deb -P /tmp 라스피컨피그 설치
    * sudo apt-get install libnewt0.52 whiptail parted triggerhappy lua5.1 alsa-utils -y 라스피컨피크 설치
    * sudo apt-get install -fy
    * sudo dpkg -i /tmp/raspi-config_20160527_all.deb
    * /boot/firmware/config.txt 파일 맨 밑에 추가
        <pre>
        <code>
        start_x=1   
		gpu_mem=128
        </code>
        </pre>
    * rqt 로 확인시 bgr8 변환 과정에서 에러 발생   
        ->  sudo apt install ros-foxy-image-transport*   
        -> 애러 수정.
    * rqt 로 정상 동작 확인.

* GPIO
    * sudo apt-get install python-dev
    * sudo apt-get install python-rpi.gpio
    * led, 서보모터(SG90), 부저를 아두이노에 장착하여 동작 확인.
