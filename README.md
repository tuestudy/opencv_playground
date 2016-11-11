# OpenCV Playground

TSG - OpenCV 스터디 놀이터

## Installation

### Mac OSX

#### 필요 소프트웨어

  * homebrew
  * Python 3

#### 설치

1. opencv3 설치

	```
	brew install homebrew/science/opencv3 --with-python3
	brew link --force opencv3
	```

	or

	```
	brew install homebrew/science/opencv3
	brew install webp
	brew link --force opencv3
	```

2. Python site-packages에 opencv3 경로 추가

	* `brew info opencv3` 해서 보면 끝부분에 관련 내용이 있음

	```
	echo /usr/local/opt/opencv3/lib/python3.5/site-packages >> /usr/local/lib/python3.5/site-packages/opencv3.pth
	```

	  * virtualenvwrapper를 사용하는 경우, 사용하는 virtualenv의 site-packages에 위 내용을 적용해야 함

3. (필요한 경우) numpy 설치: `pip install numpy`

	* numpy 가 설치 되지 않은 경우 아래 에러 발생

	```
	>>> import cv2
	ImportError: numpy.core.multiarray failed to import
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ImportError: numpy.core.multiarray failed to import
	```

#### 설치확인

```
Python 3.5.2 (default, Sep 28 2016, 18:08:09)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> print(cv2.__version__)
3.1.0
```
