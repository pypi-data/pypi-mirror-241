#!/opt/ias/env/bin/python

import cv2
import numpy as np


def main() -> None:
    file = '/home/jiang/ws/trash/sewage/s1/1/10-40-29.003.jpg'
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)  # 阈值处理

    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.destroyWindow('binary')
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 查找轮廓
    print(len(contours))

    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area < 1000:
            continue
        print('area:', area)
        cnt = contours[i]
        approx1 = cv2.approxPolyDP(cnt, 13, True)  # 拟合精确度
        print('approx1:', approx1.shape, type(approx1), approx1.dtype)
        approx2 = approx1.reshape(-1, 2)
        print('approx2:', approx2.shape, type(approx2), approx2.dtype)
        for p in approx2:
            print(p)
        img = cv2.polylines(img, [approx1], True, (255, 0, 255), 2)

    cv2.imshow('approxPolyDP1', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
