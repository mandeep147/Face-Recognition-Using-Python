# Face-Recognition-Using-Python  
A face detection app: responds with name of person depending on the trained database  

Preffered OS: Ubuntu 14.04 (or higher)  


**Requirements:**  
Python  
OpenCV 
Framework: Flask   

**Installing Python and OpenCV**    
1.	Update apt-get manager and upgrade pre-installed packages (if any) using  
	a.	sudo apt-get update  
	b.	sudo apt-get upgrade  
  
2.	 Installing development tools  
	sudo apt-get install build-essential cmake git pkg-config  
	cmake package : to configure our build   
  
3.	Installing Image I/O packages needs to be loaded by OpenCV from disk  
    sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev  
   
4.	Installing GTK development library, which highgui module of OpenCV depends on to display images on Screen:   
	sudo apt-get install libgtk2.0-dev  
   
5.	Packages for processing video-streams and accessing individual frames  
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  
  
6.	Libraries to optimize routines inside OpenCV  
	sudo apt-get install libatlas-base-dev gfortran  
   
7.	Install “pip” – python package manager  
	a.	wget https://bootstrap.pypa.io/get-pip.py   
	b.	sudo python get-pip.py  
  
8.	Install virtualenv and virtualenvwrapper – to create separate Python Environments for each project (not mandatory but recommended)  
	a.	 sudo pip install virtualenv virtualenvwrapper  
	b.	 sudo rm -rf ~/.cache/pip  
	c.	Update ~./bashrc file  
	d.	Reload the contents of bashrc file  
		source ~/.bashrc  
	e.	Make Virtual environment  
		mkvirtualenv cv  
  
9.	Install Python 2.7 and numpy   	
	a.	 sudo apt-get install python2.7-dev  
	b.	 pip install numpy  
   
10.	Install OpenCV and supporting modules   
	cd ~  
	git clone https://github.com/Itseez/opencv.git	   
	cd opencv  
	git checkout 3.0.0  
  
	cd ~  
	git clone https://github.com/Itseez/opencv_contrib.git	   
	cd opencv_contrib  
	git checkout 3.0.0  
  
	Setup the build :   
	cd ~/opencv  
	mkdir build  
   
	cd build  
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
		-D CMAKE_INSTALL_PREFIX=/usr/local \
		-D INSTALL_C_EXAMPLES=ON \
		-D INSTALL_PYTHON_EXAMPLES=ON \
		-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
		-D BUILD_EXAMPLES=ON ..  
  
	Compile OpenCV   
	make -j4  
   
	Install OpenCV (if compied without error)  
		sudo make install  
		sudo ldconfig  
   
11.	Linking OpenCV with virtual environment “cv”  
	cd ~/.virtualenvs/cv/lib/python2.7/site-packages/  
	ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so  
  
V.	Install framework and set up database required for accessing application  
	1.	pip install flask  
	2.	Set up the database  
		sudo apt-get install mysql-server  
	3. Connect to mysql by username specified while installing it  
		mysql -u <username> -p  
  
	a.	Create database   
		CREATE DATABASE detect;  
	b.	Create table  
		CREATE TABLE detect.userDetails (
		  id BIGINT NULL AUTO_INCREMENT,
		  firstName VARCHAR(45) NULL,
		  lastName VARCHAR(45) NULL,
			PRIMARY KEY (id));  
	4.	Connecting MySQL with Flask   
		pip install flask-mysql  
**Modify the username and password in app.py   

**Exceuting the Application:**    
1. Clone the repository or download the zip  
2. Navigate to the folder  
3. Make sure you are in root directory of project  
4. Run the server using  
		workon cv (cv is name of virtual environment, you created while setting up the environment)
		python runserver.py  
5. To run the demo, go to localhost:3000 on the browser  
6. The app should be running  
