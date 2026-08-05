import math
angle_degrees=30
hypotenuse=10.0
radians=angle_degrees*math.pi/180
height=hypotenuse*math.sin(radians)
print(f'角度{angle_degrees}度，斜邊長{hypotenuse}，高度{height:.2f}')

tan_value=1.0
rad_result=math.atan(tan_value)
deg_result=rad_result*180/math.pi
print(f'反正切值{tan_value}，弧度{rad_result:.2f}，角度{deg_result:.2f}')
