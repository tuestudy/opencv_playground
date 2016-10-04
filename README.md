# OpenCV Playground

TSG - OpenCV 스터디 놀이터

## Installation

### Mac OSX

#### 필요 소프트웨어

  * homebrew
  * Python 3

#### 설치

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

#### 설치확인

```
Python 3.5.2 (default, Sep 28 2016, 18:08:09) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> print(cv2.__version__)
3.1.0
```
